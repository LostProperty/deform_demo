import colander
import deform

from .models import (
    DBSession,
    Recipe as RecipeModel,
    Ingredient as IngredientModel,
)

# TODO: move to a utils file
class SqlAlchemyModelMixin(object):

    def save_to_model(self, appstruct, item=False):
        """
        Save the appstruct data to the DB
        """
        # Save the main model
        if item == False:
            item = self.Meta.model()

        item.set_values(appstruct)
        DBSession.add(item)
        DBSession.flush()

        # Save the related models
        relations = self.Meta.relations
        for relation_name, relation_model in relations.items():
            related_items = appstruct.pop(relation_name)
            self.update_related_items(item, related_items, relation_model)

    def update_related_items(self, item, new_related_items, related_model):
        """
        Save related model fields to the DB
        """
        # Delete all rows here
        model_field = getattr(related_model, self.Meta.model_id)
        related_items = DBSession.query(related_model).filter(model_field == item.id)
        for related_item in related_items:
            DBSession.delete(related_item)
        # Add new rows
        for new_related_item in new_related_items:
            related_model_instance = related_model()
            new_related_item[self.Meta.model_id] = item.id
            related_model_instance.set_values(new_related_item)
            DBSession.merge(related_model_instance)

    def populate_form(self, item):
        """
        Get the DB item data into a format for populating the form
        """
        item_dict = item.__dict__
        relations = self.Meta.relations
        for relation_name, relation_model in relations.items():
            item_dict[relation_name] = self.get_related_items_for_form(item, relation_name)
        return item_dict

    def get_related_items_for_form(self, item, name):
        """
        Get the related objects in the right format to populate the form
        """
        related_list = []
        for related_item in getattr(item, name):
            related_list.append(related_item.__dict__)
        return related_list


class Ingredient(colander.MappingSchema, SqlAlchemyModelMixin):
    # TODO: make a drop-down (can we have in-line add)
    # TODO: can we display in-line?
    name = colander.SchemaNode(colander.String())
    quantity = colander.SchemaNode(colander.String())


class Ingredients(colander.SequenceSchema):
    ingredient = Ingredient()


class Recipe(colander.MappingSchema, SqlAlchemyModelMixin):
    name = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(
        colander.String(),
        missing='',
        widget=deform.widget.TextAreaWidget(
            rows=10,
            cols=60,
            css_class=''
        ),
        description='Description of the Recipe',
    )
    # TODO: add some custom validators
    ingredients = Ingredients()

    class Meta:
        model = RecipeModel
        model_id = 'recipe_id'
        # NOTE: the dictionary key must match the MappingSchema attribute
        relations = {'ingredients': IngredientModel}
        #relationships['instructions'] = InstructionModel

import colander
import deform

from .models import (
    Recipe as RecipeModel,
    Ingredient as IngredientModel,
)

class Ingredient(colander.MappingSchema):
    # TODO: make a drop-down (can we have in-line add)
    # TODO: can we display in-line?
    name = colander.SchemaNode(colander.String())
    quantity = colander.SchemaNode(colander.String())


class Ingredients(colander.SequenceSchema):
    ingredient = Ingredient()


class Recipe(colander.MappingSchema):
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
        # NOTE: the dictionary key must match the MappingSchema attribute
        relations = {'ingredients': IngredientModel}
        #relationships['instructions'] = InstructionModel

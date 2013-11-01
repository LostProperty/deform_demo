import colander
import deform

from .models import (
    Recipe,
    Ingredient,
)

class Ingredient(colander.MappingSchema):
    # TODO: make a drop-down (can we have in-line add)
    # TODO: can we display in-line?
    name = colander.SchemaNode(colander.String())
    quantity = colander.SchemaNode(colander.String())

    class Meta:
        model = Ingredient


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
        model = Recipe
        #fields = ['title', 'forenames', 'surname', 'email']

# TODO: add recipe ingredients

from pyramid.view import view_config

import deform
from deform import Form

from .models import (
    DBSession,
    Recipe,
    Ingredient,
)

from .schemas import (
    Recipe
)


@view_config(route_name='home', renderer='templates/form.pt')
def form(request):
    schema = Recipe()
    form = Form(schema, buttons=('submit',))

    if request.POST:
        try:
            appstruct = form.validate(request.POST.items())
            #serialized = schema.serialize(app_struct)
            set_values(schema, appstruct)

            # TODO: redirect to list of items here (base template to be used)
            # To do add flash
            render_form = form.render()

        #TODO: can we also catch sqlalchemy.exc.IntegrityError and show to the user
        except deform.ValidationFailure as e:
            render_form = e.render()
    else:
        render_form = form.render()

    return {"form": render_form}


def set_values(schema, appstruct):
    # TODO: should we move this function to be a method on the schema (added with a mixin)
    model = schema.Meta.model
    item = model()

    for key, value in appstruct.items():
        # TODO: can we switch the block and lose the line below?
        try:
            setattr(item, key, value)
        except: # TypeError
            pass
    DBSession.add(item)
    DBSession.flush()

    # set the related fields
    relations = schema.Meta.relations
    for relation_name, relation_model in relations.items():
        related_items = appstruct.pop(relation_name)
        save_related_items(related_items, item, relation_model)


def save_related_items(related_items, item, model):
    """
    Save the data for the related models.
    """
    for related_item in related_items:
        # Note this is still recipe specific, but better than before
        related_item['recipe_id'] = item.id
        model_instance = model()
        model_instance.set_values(related_item)
        DBSession.add(model_instance)

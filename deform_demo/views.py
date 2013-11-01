from pyramid.view import view_config

import deform
from deform import Form

from .models import (
    DBSession,
    #Recipe,
    #Ingredient,
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
            #TODO: do we need the schema here too (for relationship mapping)?
            item = set_values(schema, appstruct)
            DBSession.add(item)
            # TODO: redirect to list of items here (base template to be used)
            # To do add flash
            render_form = form.render()

        #TODO: can we also catch sqlalchemy.exc.IntegrityError and show to the user
        except deform.ValidationFailure as e:
            render_form = e.render()
    else:
        render_form = form.render() #recipe_dict)

    return {"form": render_form}


def set_values(schema, appstruct):
    import pdb; pdb.set_trace()
    # do we have the schema name in the app struct? I'd prefer to work with the schema and it's data
    model = schema.Meta.model
    item = model()
    # get model attributes
    # loop the appstruct and set these
    # get the models relationships
    # loop for their existence in the appstruct and set these
    # save_related_items
    for key, value in appstruct.items():
        setattr(item, key, value)
        # if isinstance(value, list):
        #     import pdb; pdb.set_trace()
        #     #for key, value in appstruct.items():
        # else:
        #     setattr(item, key, value)
    return item

# def save_related_items(self, related_items, item, model):
#     """
#     Save the data for the related models. Could we move this code to the model?
#     """
#     for related_item in related_items:
#         # Note this is still recipe specific, but better than before
#         related_item['recipe_id'] = item.id
#         model_instance = model()
#         model_instance.set_values(related_item)
#         DBSession.add(model_instance)

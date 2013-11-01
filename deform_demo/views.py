from pyramid.view import view_config

import deform
from deform import Form

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
            schema.save_to_model(appstruct)
            request.session.flash('Item has been saved.')
            # TODO: redirect to list of items here (base template to be used)
            render_form = form.render()

        #TODO: can we also catch sqlalchemy.exc.IntegrityError and show to the user
        except deform.ValidationFailure as e:
            render_form = e.render()
    else:
        render_form = form.render()

    return {"form": render_form}

import deform
from deform import Form

from pyramid.view import view_config

from .schemas import (
    Recipe
)
from .models import DBSession, Recipe as RecipeModel


@view_config(route_name='list', renderer='templates/list.jinja2')
def list(request):
    items = DBSession.query(RecipeModel)
    return {'items': items}


@view_config(route_name='add', renderer='templates/form.jinja2')
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
        # Or should all SQL errors be covered by Colander validation?
        except deform.ValidationFailure as e:
            render_form = e.render()
    else:
        render_form = form.render()

    return {"form": render_form}

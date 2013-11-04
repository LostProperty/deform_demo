import deform
from deform import Form

from pyramid.httpexceptions import HTTPFound

from .schemas import (
    Recipe
)
from .models import DBSession, Recipe as RecipeModel


def list(request):
    items = DBSession.query(RecipeModel)
    return {'items': items}


def form(request):
    schema = Recipe()
    form = Form(schema, buttons=('submit',))
    edit_id = request.matchdict.get('id', False)
    edit_item = False
    if edit_id:
        edit_item = DBSession.query(RecipeModel).filter_by(id=edit_id).one()

    if request.POST:
        try:
            appstruct = form.validate(request.POST.items())
            schema.save_to_model(appstruct, edit_item)
            request.session.flash('Item has been saved.')
            return HTTPFound(request.route_url('list'))

        #TODO: can we also catch sqlalchemy.exc.IntegrityError and show to the user
        # Or should all SQL errors be covered by Colander validation?
        except deform.ValidationFailure as e:
            render_form = e.render()
    else:
        if edit_item:
            render_form = form.render(schema.populate_form(edit_item))
        else:
            render_form = form.render()

    return {'form': render_form}


def delete(request):
    id = int(request.POST.get('item_id'))
    item = DBSession.query(RecipeModel).filter_by(id=id).one()
    DBSession.delete(item)
    return HTTPFound(request.route_url('list'))

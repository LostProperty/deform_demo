from pyramid.response import Response
from pyramid.view import view_config

import colander
import deform
from sqlalchemy.exc import DBAPIError
from deform import Form

from .models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'deform_demo'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_deform_demo_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

# TODO: move schema to it's own file
class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    value = colander.SchemaNode(
        colander.String(),
        missing='',
        widget=deform.widget.TextAreaWidget(
            rows=10,
            cols=60,
            css_class=''
        ),
        description='Description of the Recipe',
    )
    rank = colander.SchemaNode(colander.Int(),
                      validator=colander.Range(0, 9))

# TODO: move forms stuff to it's own view file
@view_config(route_name='form', renderer='templates/form.pt')
def form(request):
    schema = Person()
    form = Form(schema, buttons=('submit',))

    if request.POST:
        try:
            appstruct = form.validate(request.POST.items())
            #serialized = schema.serialize(app_struct)
            item = MyModel()
            #TODO: do we need the schema here too (for relationship mapping)?
            item = set_values(item, appstruct)
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


def set_values(item, appstruct):
    for key, value in appstruct.items():
        setattr(item, key, value)
    return item

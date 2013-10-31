import colander
import deform
from deform import Form
from pyramid.view import view_config

class Person(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    description = colander.SchemaNode(
        colander.String(),
        missing='',
        widget=deform.widget.TextAreaWidget(
            rows=10,
            cols=60,
            css_class=''
        ),
        description='Description of the Recipe'
    )

class ProjectorViews(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer="templates/site_view.pt")
    def site_view(self):
        schema = Person()
        myform = Form(schema, buttons=('submit',))

        # TODO: check for post, save to the DB
        return {"form": myform.render()}

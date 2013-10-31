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
        #return {"form": myform.render()}
        return {"form": self.render_form(myform)}

    def render_form(self, form, appstruct=colander.null, submitted='submit',
                    success=None, readonly=False, is_i18n=False):

        captured = None

        if submitted in self.request.POST:
            # the request represents a form submission
            try:
                # try to validate the submitted values
                controls = self.request.POST.items()
                captured = form.validate(controls)
                if success:
                    response = success()
                    if response is not None:
                        return response
                html = form.render(captured)
            except deform.ValidationFailure as e:
                # the submitted values could not be validated
                html = e.render()

        else:
            # the request requires a simple form rendering
            html = form.render(appstruct, readonly=readonly)

        # if self.request.is_xhr:
        #     return Response(html)

        #code, start, end = self.get_code(2)
        #locale_name = get_locale_name(self.request)

        reqts = form.get_widget_resources()

        # captured = highlight(pprint.pformat(captured, width=1),
        #                      PythonLexer(),
        #                      formatter)

        # values passed to template for rendering
        return {
            'form':html,
            #'captured': captured,
            #'code': code,
            #'start':start,
            #'end':end,
            #'is_i18n':is_i18n,
            #'locale': locale_name,
            #'demos':self.get_demos(),
            #'title':self.get_title(),
            'css_links':reqts['css'],
            'js_links':reqts['js'],
            }

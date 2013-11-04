from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from sqlalchemy import engine_from_config
import pyramid_jinja2

from .models import (
    DBSession,
    Base,
)


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include(pyramid_jinja2)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('deform_static', 'deform:static')
    session_factory = UnencryptedCookieSessionFactoryConfig('Ye7eevoht7faht ')
    config.set_session_factory(session_factory)

    # TODO: break out these routes and views to a seperate file
    config.add_route('list', '/',)
    config.add_route('add', '/add')
    config.add_route('edit', '/edit/{id:\d+}')
    config.add_route('delete', '/delete')

    config.add_view('.views.list', route_name='list', renderer='templates/list.jinja2')
    config.add_view('.views.form', route_name='add', renderer='templates/form.jinja2')
    config.add_view('.views.form', route_name='edit', renderer='templates/form.jinja2')
    config.add_view('.views.delete', route_name='delete')

    config.scan()
    return config.make_wsgi_app()

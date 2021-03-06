from pyramid.config import Configurator
from pyramid_zodbconn import get_connection


def root_factory(request):
    conn = get_connection(request)
    return conn.root()['app_root']


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=root_factory, settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # adding traversal back in
    config.scan()
    return config.make_wsgi_app()

from pyramid.config import Configurator
from pyramid_zodbconn import get_connection
from .models import appmaker


def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=root_factory, settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    # omitting traversal for now; using URL dispatch instead
    # config.scan()
    config.add_route('Genesis 1:1', '/gen1:1')
    config.add_view('.views.view_passage', route_name='Genesis 1:1',
                    renderer='templates/view.pt')
    return config.make_wsgi_app()


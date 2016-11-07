from docutils.core import publish_parts
import re

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from .models import Face, PassageArtifacts


@view_config(context='.models.Face', renderer='templates/faceofthedeep.pt')
def my_view(context, request):
    return HTTPFound(location=request.resource_url(context, 'Face'))


@view_config(context=PassageArtifacts, renderer='templates/view.pt')
def view_passage(context, request):
    # face = context.__parent__
    passage = context  # obviously unnecessary, but leaving it for the moment for conceptual reasons

    elements = []
    for text, type_ in passage.text_type_data:
        if type_ == 'image':
            element = ('<img class="artifact" src="{url}" height="100" '
                       'width="100" style="position:absolute;">'
                       .format(url=text)) 
        else:
            # assuming type_ == 'text'
            element = ('<p class="artifact" style="position:absolute;"'
                       '>{text}</p>'.format(text=text))
        elements.append(element)
    formatted_elems = '\n'.join(elements)

    return dict(passage=passage,
                elements=formatted_elems,
                request=request)

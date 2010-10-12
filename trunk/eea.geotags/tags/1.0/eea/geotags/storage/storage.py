""" Basic geotags storage
"""
try:
    from zope.annotation.interfaces import IAnnotations
except ImportError:
    #BBB Plone 2.5
    from zope.app.annotation.interfaces import IAnnotations

import logging
from persistent.dict import PersistentDict
from zope.interface import implements
from zope.component import queryAdapter
from eea.geotags.config import ANNO_TAGS
from interfaces import IGeoTags
logger = logging.getLogger('eea.geotags.storage')

class GeoTags(object):
    """ Geo tags storage
    """
    implements(IGeoTags)

    def __init__(self, context):
        self.context = context

    def tags():

        def get(self):
            anno = queryAdapter(self.context, IAnnotations)
            if not anno:
                logger.exception('%s is not Annotable', self.context.absolute_url())
                return {}
            return dict(anno.get(ANNO_TAGS, {}))

        def set(self, value):
            anno = queryAdapter(self.context, IAnnotations)
            if not anno:
                logger.exception('%s is not Annotable', self.context.absolute_url())
                return
            anno[ANNO_TAGS] = PersistentDict(value)

        return property(get, set)

    tags = tags()

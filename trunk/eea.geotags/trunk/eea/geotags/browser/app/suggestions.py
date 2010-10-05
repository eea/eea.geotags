import logging
import simplejson
from zope.component import queryAdapter
from Products.Five.browser import BrowserView

from eea.geotags.interfaces import IDiscoverGeoTags

logger = logging.getLogger('@@eea.geotags.suggestions')
LOOKIN = ('title', 'description')

class View(BrowserView):
    """ Suggest geotags for context
    """
    _discover = None

    @property
    def discover(self):
        if not self._discover:
            self._discover = queryAdapter(self.context, IDiscoverGeoTags)
        return self._discover

    def __call__(self, lookin=LOOKIN, **kwargs):
        entities = []
        for metadata in lookin:
            entities.extend(self.discover(metadata))

        return simplejson.dumps({
            'suggestions': entities
        })

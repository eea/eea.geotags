""" Interfaces
"""

from zope import schema
from zope.interface import Interface

from eea.geotags.config import _


class IGeotagsSettings(Interface):
    """ Geotags settings
    """

    maps_api_key = schema.TextLine(
        title=_(u"Google Maps API key"),
        description=_(
            u'This will be used to render the Google Maps widget'
            u'for eea.geotags enabled location fields.'
            u'You can get one from https://developers.google.com/maps/'
            u'documentation/javascript/get-api-key'
        ),
        required=False,
        default=u''
    )

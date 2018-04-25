""" Interfaces
"""

from plone.registry import field
from zope.interface import Interface

from eea.geotags.config import _


class IGeotagsSettings(Interface):
    """ Geotags settings
    """

    maps_api_key = field.TextLine(
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

    geonames_key = field.TextLine(
        title=_(u"Geonames key"),
        description=_(u'http://www.geonames.org/'),
        required=False,
        default=u''
    )


class IGeoVocabularies(Interface):
    geotags = field.Dict(
        title=_(u'Geotags tree'),
        key_type=field.TextLine(),
        value_type=field.Dict(
            key_type=field.TextLine(),
            value_type=field.TextLine()
        ),
    )

    biotags = field.Dict(
        title=_(u'Biogeographical regions'),
        key_type=field.TextLine(),
        value_type=field.Dict(
            key_type=field.TextLine(),
            value_type=field.TextLine()
        ),
    )
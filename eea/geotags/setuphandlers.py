""" Setuphandlers
"""
import logging
import zope.deprecation

logger = logging.getLogger('eea.geotags.setuphandlers')


def setupGeonames(_):
    """ portal_properties.geographical_properties has been moved to
        plone.app.registry and is available in
        eea.geolocation.interfaces.IGeolocationClientSettings
    """
    pass


zope.deprecation.deprecated(
    setupGeonames,
    ('eea.geotags.setuphandlers.setupGeonames is no longer needed.'
     + setupGeonames.__doc__)
)


def importVocabularies(_):
    """ Vocabularies have been migrated to eea.geolocation
    """
    pass


zope.deprecation.deprecated(
    importVocabularies,
    ('eea.geotags.setuphandlers.importVocabularies is no longer needed.'
     + importVocabularies.__doc__)
)


def importVarious(context):
    """ Import various
    """
    if context.readDataFile('eea.geotags.txt') is None:
        return

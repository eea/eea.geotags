""" Setuphandlers
"""
import logging
import zope.deprecation

from Products.CMFCore.utils import getToolByName
from Products.ATVocabularyManager.utils.vocabs import createHierarchicalVocabs

from eea.geotags.vocabularies.data.groups import VOC
from eea.geotags.vocabularies.data.biogroups import VOC as BIOVOC

logger = logging.getLogger('eea.geotags.setuphandlers')


def setupGeonames(_):
    """ portal_properties.geographical_properties has been moved to
        plone.app.registry and is available in
        eea.geotags.controlpanel.interfaces.IGeotagsSettings
    """
    pass


zope.deprecation.deprecated(
    setupGeonames,
    ('eea.geotags.setuphandlers.setupGeonames is no longer needed.'
     + setupGeonames.__doc__)
)


def importVocabularies(context):
    """ Import groups vocabulary
    """
    site = context.getSite()
    atvm = getToolByName(site, 'portal_vocabularies', None)

    createHierarchicalVocabs(atvm, VOC)
    logger.info("Added 'Geotags Tree' vocabulary")

    createHierarchicalVocabs(atvm, BIOVOC)
    logger.info('Added "Biogeographical regions" vocabulary')


def importVarious(context):
    """ Import various
    """
    if context.readDataFile('eea.geotags.txt') is None:
        return

    importVocabularies(context)

""" Setuphandlers
"""
import logging
from Products.CMFCore.utils import getToolByName
from eea.geotags.vocabularies.data.groups import VOC
from eea.geotags.vocabularies.data.biogroups import VOC as BIOVOC
from Products.ATVocabularyManager.utils.vocabs import createHierarchicalVocabs

logger = logging.getLogger('eea.geotags.setuphandlers')

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

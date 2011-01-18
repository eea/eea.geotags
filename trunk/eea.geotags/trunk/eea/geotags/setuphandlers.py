import logging
from Products.CMFCore.utils import getToolByName
from eea.geotags.vocabularies.data.groups import VOC
from eea.geotags.vocabularies.data.biogroups import VOC as BIOVOC
from Products.ATVocabularyManager.utils.vocabs import createHierarchicalVocabs

logger = logging.getLogger('eea.geotags')

def importVocabularies(site):
    """ Import groups vocabulary
    """
    # AT Vocabulary Manager
    qtool = getToolByName(site, 'portal_quickinstaller')
    installed = [package['id'] for package in qtool.listInstalledProducts()]
    if not set(['Products.ATVocabularyManager',
                'ATVocabularyManager']).intersection(installed):
        qtool.installProduct('Products.ATVocabularyManager')

    atvm = getToolByName(site, 'portal_vocabularies', None)
    createHierarchicalVocabs(atvm, VOC)
    createHierarchicalVocabs(atvm, BIOVOC)

def importVarious(self):
    if self.readDataFile('eea.geotags.txt') is None:
        return

    site = self.getSite()

    setup_tool = getToolByName(site, 'portal_setup')

    # Alchemy
    setup_tool.setImportContext('profile-eea.alchemy:default')
    setup_tool.runAllImportSteps()

    # jQuery Splitter
    setup_tool.setImportContext('profile-eea.jquery:13-splitter')
    setup_tool.runAllImportSteps()

    # plone 2/3 compatibility (SKINS DIR)
    setup_tool.setImportContext('profile-eea.geotags:02-skins')
    setup_tool.runAllImportSteps()
    setup_tool.setImportContext('profile-eea.geotags:01-default')

    # Import vocabularies
    importVocabularies(site)


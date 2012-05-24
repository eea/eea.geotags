""" Layout upgrades
"""
import logging
from Products.CMFCore.utils import getToolByName
from eea.geotags.interfaces import IGeoTaggable, IGeoTags, IGeoTagged
from zope.component.interface import interfaceToName
from zope.interface import alsoProvides
import transaction
logger = logging.getLogger("eea.geotags.upgrades")

def set_geotags_interface(context):
    """  Set IGeoTagged interface to objects that have geotags set
    """
    ctool = getToolByName(context, 'portal_catalog')
    iface = interfaceToName(context, IGeoTaggable)
    brains = ctool(object_provides=iface, show_inactive=True, Language='all')
    count = 0
    for brain in brains:
        doc = brain.getObject()
        tags = IGeoTags(doc).tags
        if tags:
            alsoProvides(doc, IGeoTagged)
            doc.reindexObject()
            count += 1
            if count % 10 == 0:
                logger.info("Committing geotags interface migration transaction")
                transaction.commit()

    logger.info("DONE adding IGeoTagged to objects with geotags")

# -*- coding: utf-8 -*-
""" Add missing ascii chars
"""

import json
import logging
import transaction
from Products.CMFCore.utils import getToolByName
from eea.geotags.interfaces import IGeoTaggable
from eea.geotags.storage.storage import GeoTags


logger = logging.getLogger(__name__)


def missing_ascii(context):
    portal_catalog = getToolByName(context, 'portal_catalog')
    brains = portal_catalog(object_provides=IGeoTaggable.__identifier__, Language='all')

    mapping = {
        "Trkiye" :"Türkiye"
    }


    logger.info("Going through %s brains" % len(brains))
    count = 0
    for brain in brains:
        for key, value in mapping.items():
            if brain.location not in [(), "", []]:
                new_location = []
                location = brain.location
                changed = False

                for loc in location:
                    if key in loc:
                        loc = loc.replace(key, value)
                        changed = True

                    new_location.append(loc)

                brain.location = tuple(new_location)
                if changed:
                    obj = brain.getObject()

                    new_location[0] = new_location[0].decode('utf-8')
                    obj.location = tuple(new_location)

                    portal_catalog.reindexObject(obj, idxs=['location'], update_metadata=1)

            if isinstance(brain.geotags, str) or isinstance(brain.geotags, unicode):
                if brain.geotags != "":
                    geo = json.loads(brain.geotags)

                    if key in geo['features'][-1]['properties']['name'] or \
                       key in geo['features'][-1]['properties']['description'] or \
                       key in geo['features'][-1]['properties']['title']:
                        obj = brain.getObject()
                        storage = GeoTags(obj)

                        tags = storage._get_tags()

                        tags['features'][-1]['properties']['name'] = tags['features'][-1]['properties']['name'].encode('utf-8').replace(key, value).decode('utf-8')
                        tags['features'][-1]['properties']['title'] = tags['features'][-1]['properties']['title'].encode('utf-8').replace(key, value).decode('utf-8')
                        tags['features'][-1]['properties']['description'] = tags['features'][-1]['properties']['description'].encode('utf-8').replace(key, value).decode('utf-8')

                        storage._set_tags(tags)

                        portal_catalog.reindexObject(obj, idxs=['geotags'], update_metadata=1)
                        transaction.commit()

        count += 1
        if count % 1000 == 0:
            logger.info("Passed through %s brains" % count)
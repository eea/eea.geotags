# -*- coding: utf-8 -*-
""" Add missing ascii chars
"""

import json
import logging
from Products.CMFCore.utils import getToolByName
from eea.geotags.interfaces import IGeoTaggable


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

                for loc in location:
                    if key in loc:
                        loc = loc.replace(key, value)

                    new_location.append(loc)

                brain.location = tuple(new_location)

            if isinstance(brain.geotags, str) or isinstance(brain.geotags, unicode):
                if brain.geotags != "":
                    geo = json.loads(brain.geotags)
                    print geo

                    if key in geo['features'][-1]['properties']['name']:
                        # first we encode the geo
                        new_geo = geo['features'][-1]['properties']['name'].encode("latin-1", "ignore")
                        
                        # then we replace
                        new_geo = new_geo.replace(key, value)
                        
                        # then we decode back to unicode
                        new_geo = new_geo.decode("latin-1")
    
                        # finally set the new geo value
                        geo['features'][-1]['properties']['name'] = new_geo

                    if key in geo['features'][-1]['properties']['description']:
                        # first we encode the geo
                        new_geo = geo['features'][-1]['properties']['description'].encode("latin-1", "ignore")
                        
                        # then we replace
                        new_geo = new_geo.replace(key, value)
                        
                        # then we decode back to unicode
                        new_geo = new_geo.decode("latin-1")
    
                        # finally set the new geo value
                        geo['features'][-1]['properties']['description'] = new_geo

                    if key in geo['features'][-1]['properties']['title']:
                        # first we encode the geo
                        new_geo = geo['features'][-1]['properties']['title'].encode("latin-1", "ignore")
                        
                        # then we replace
                        new_geo = new_geo.replace(key, value)
                        
                        # then we decode back to unicode
                        new_geo = new_geo.decode("latin-1")
    
                        # finally set the new geo value
                        geo['features'][-1]['properties']['title'] = new_geo

                    brain.geotags = json.dumps(geo)

        count += 1
        if count % 1000 == 0:
            logger.info("Passed through %s brains" % count)
"""  Map view
"""
from Products.Five.browser import BrowserView
import json
import urllib
from Products.CMFCore.utils import getToolByName


class MapView(BrowserView):
    """ Map View faceted navigation logic
    """

    def map_points(self, brains):
        """ Return geotags information found on brains
        """
        res = []

        props = getToolByName(self.context, 'portal_properties').site_properties
        for brain in brains:
            if brain.geotags:
                # we only need the features items
                feature = json.loads(brain.geotags).get('features')
                location = feature[0]['properties']['description']
                feature[0]['properties']['description'] = urllib.quote(
                                    location.encode('utf-8'))
                feature[0].update({"itemDescription":
                                    urllib.quote(brain.Description)})
                feature[0].update({"itemUrl": brain.getURL()})
                feature[0].update({"itemTitle":
                                    urllib.quote(brain.Title)})
                start_date = brain.start.strftime(props.localLongTimeFormat)
                end_date = brain.end.strftime(props.localLongTimeFormat)
                feature[0].update({"itemDate": '%s to %s' % (start_date, end_date)})
                feature = json.dumps(feature)
                # hack as we only need the objects within the list
                res.append(feature[1: -1])

        return res

"""  Map view
"""
from Products.Five.browser import BrowserView
import json
import urllib


class MapView(BrowserView):
    """ Map View faceted navigation logic
    """

    def map_points(self, brains):
        """ Return geotags information found on brains
        """
        res = []

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
                feature = json.dumps(feature)
                # hack as we only need the objects within the list
                res.append(feature[1: -1])

        return res

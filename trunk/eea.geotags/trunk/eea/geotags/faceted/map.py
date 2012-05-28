"""  Map view
"""
from Products.Five.browser import BrowserView


class MapView(BrowserView):
    """ Map View faceted navigation logic
    """

    def map_points(self, brains):
        """ Return geotags information found on brains
        """
        res = []
        for brain in brains:
            if brain.geotags:
                res.append(brain.geotags)
        return res

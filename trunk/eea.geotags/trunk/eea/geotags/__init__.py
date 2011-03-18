""" EEA Geotags
"""
try:
    import zope.annotation
    zope.annotation
except ImportError:
    #BBB Plone 2.5
    from eea.geotags import plone25
    plone25

from  eea.geotags import field
from eea.geotags import widget
field, widget
from eea.geotags import content

def initialize(context):
    """ Zope 2 """
    content.initialize(context)

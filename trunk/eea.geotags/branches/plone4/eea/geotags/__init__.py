""" EEA Geotags package
"""
from  eea.geotags import field
from eea.geotags import widget
from eea.geotags import content

field, widget

def initialize(context):
    """ Zope 2 initialize
    """
    content.initialize(context)

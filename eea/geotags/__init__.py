""" EEA Geotags
"""
try:
    import zope.annotation
except ImportError:
    #BBB Plone 2.5
    import plone25

import field
import widget
import content

def initialize(context):
    """ Zope 2 """
    content.initialize(context)

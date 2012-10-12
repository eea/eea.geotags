""" RDF Marshaller module for geotags """

from eea.geotags.field.location import GeotagsFieldMixin
from eea.geotags.interfaces import IGeoTags
from eea.rdfmarshaller.archetypes.fields import ATField2Surf
from eea.rdfmarshaller.archetypes.interfaces import IATField2Surf
from eea.rdfmarshaller.interfaces import ISurfSession
from zope.component import adapts, getAdapter
from zope.interface import implements, Interface

import surf

class GeotagsField2Surf(ATField2Surf):
    """Adapter to express geotags field with RDF using Surf."""
    implements(IATField2Surf)
    adapts(GeotagsFieldMixin, Interface, ISurfSession)

    def value(self):
        """ Value of geotags field """
                
        # create a GeoPoint Class
        GeoPoint = self.session.get_class(surf.ns.GEO.Point)
        GeoLat = self.session.get_class(surf.ns.GEO.Lat)
        GeoLong = self.session.get_class(surf.ns.GEO.Long)
        
        value = self.field.getAccessor(self.context)()
        
        geo = getAdapter(self.context, IGeoTags)

        output = []
        i = 0
        for point in geo.getPoints():
            rdfp = self.session.get_resource("geotag%s" % i, GeoPoint)
            rdfp[surf.ns.GEO['lat']] = GeoLat(point[0])
            rdfp[surf.ns.GEO['long']] = GeoLong(point[1])
            rdfp[surf.ns.RDFS['label']] = 'Rome'

            rdfp.update()
            output.append(rdfp)

            i += 1

        #this is like example 2 in #3425
        #output.append((rdfp, None, surf.ns.GEO))   

        return output

"""desired output is:
<document:Document 
rdf:about="http://www.eea.europa.eu/data-and-maps/daviz/learn-more/prepare-data">
...
<dct:spatial>
    <geo:Point>
     <rdfs:label>Rome</rdfs:label>
     <geo:lat>41.901514</geo:lat>
     <geo:long>12.460774</geo:long>
    </geo:Point>
 </dct:spatial>
<dct:spatial>
    <geo:Point>
     <rdfs:label>Bucharest</rdfs:label>
     <geo:lat>44.437711</geo:lat>
     <geo:long>26.097367</geo:long>
    </geo:Point>
 </dct:spatial>
...
</document:Document>
"""

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

    prefix = "dcterms"
    name = "spatial"

    def value(self):
        """desired RDF output is like:
        
        <document:Document 
        rdf:about="
        http://www.eea.europa.eu/data-and-maps/daviz/learn-more/prepare-data">
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
        <dct:spatial rdf:resource="http://sws.geonames.org/2985244/">
        ...
        </document:Document>
        
        """
        # create a GeoPoint Class
        GeoPoint = self.session.get_class(surf.ns.GEO.Point)
        
        geo = getAdapter(self.context, IGeoTags)

        output = []
        i = 0

        for feature in geo.getFeatures():
            rdfp = self.session.get_resource("#geotag%s" % i, GeoPoint)
            
            label = feature['properties']['title']
            rdfp[surf.ns.RDFS['label']] = label
            
            latitude = feature['properties']['center'][0]
            rdfp[surf.ns.GEO['lat']] = latitude

            longitude = feature['properties']['center'][1]
            rdfp[surf.ns.GEO['long']] = longitude
            
            if feature['properties']['other'].has_key('geonameId'):
                geonameId = feature['properties']['other']['geonameId']
                                        
            rdfp.update()
            output.append(rdfp)

            i += 1

        #this is like example 2 in #3425
        #output.append((rdfp, None, surf.ns.GEO))   

        return output


jQuery(document).ready(function(){
    var djConfig = { parseOnLoad: true },
        url = "http://serverapi.arcgisonline.com/jsapi/arcgis/?v=2.7",
        map;

    if(jQuery('#faceted-form').length) {
        jQuery(Faceted.Events).one('FACETED-AJAX-QUERY-SUCCESS', function(){
             if (jQuery("#map_points").length) {
                map = jQuery('#eeaEsriMap');
                map.insertAfter("#plone-document-byline");
                jQuery.getScript(url, function () {
                    dojo.ready(function () {
                        map.EEAGeotagsView();
                    });
                });
                jQuery(Faceted.Events).bind('FACETED-AJAX-QUERY-SUCCESS', function(){
                    EEAGeotags.View.prototype.drawPoints(jQuery('.eea-location-links'));
                });
            }
        });
    }
    else {
        if (jQuery("#map_points").length) {
            map = jQuery("#eeaEsriMap");
            jQuery.getScript(url, function () {
                dojo.ready(function () {
                    map.EEAGeotagsView();
                });
            });
        }
    }
});

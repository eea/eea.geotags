jQuery(document).ready(function(){
    var djConfig = { parseOnLoad: true },
        url = "http://serverapi.arcgisonline.com/jsapi/arcgis/?v=2.7";
    if(jQuery('#faceted-form').length) {
        jQuery(Faceted.Events).one('FACETED-AJAX-QUERY-SUCCESS', function(){
             var map = jQuery("#eeaEsriMap");
             if (map.length) {
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
        var map = jQuery("#eeaEsriMap");
        if (map.length) {
            jQuery.getScript(url, function () {
                dojo.ready(function () {
                    jQuery('#eeaEsriMap').EEAGeotagsView();
                });
            });
        }
    }
});

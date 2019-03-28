//<![CDATA[

var map;
var layer_mapnik;
var layer_tah;
var layer_markers;

function drawmap() {
    // Popup und Popuptext mit evtl. Grafik
    var popuptext="<font color=\"black\"><b>Urlaubswichtelbude</b></font>";
    
    var gps_json = (function() {
            var json = null;
            $.ajax({
                'async': false,
                'global': false,
                'url': "/json/values.json",
                'dataType': "json",
                'success': function (data) {
                    json = data;
                }
            });
            return json;
        })();
    newPositionLat = gps_json.lat;
    newPositionLon = gps_json.lon;
    if ( newPositionLat != null ) {
        coords_date = String(gps_json.datum);
        var day = coords_date.substr(6, 2);
        var month = coords_date.substr(4, 2);
        var year = coords_date.substr(0, 4);
        var hour = coords_date.substr(8, 2);
        var minute = coords_date.substr(10, 2);
        var second = coords_date.substr(12, 2);
        coords_date = day + '.' + month + '.' + year + ' ' + hour +':' + minute + ':' + second;
        coords_source = 'gps json';
    }else {
        newPositionLat  =   '52.0';
        newPositionLon  =   '8.0';
        coords_source = 'fake';
        coords_date = 'none';
    }
    
    OpenLayers.Lang.setCode('de');
    
    // Position und Zoomstufe der Karte
    var lon = 8.0;
    var lat = 52.0;
    var zoom = 13;

    map = new OpenLayers.Map('map', {
        projection: new OpenLayers.Projection("EPSG:900913"),
        displayProjection: new OpenLayers.Projection("EPSG:4326"),
        controls: [
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.LayerSwitcher(),
            new OpenLayers.Control.PanZoomBar()],
        maxExtent:
            new OpenLayers.Bounds(-20037508.34,-20037508.34,
                                    20037508.34, 20037508.34),
        numZoomLevels: 10,
        maxResolution: 156543,
        units: 'meters'
    });

    layer_mapnik = new OpenLayers.Layer.OSM.Mapnik("Mapnik");
    layer_markers = new OpenLayers.Layer.Markers("Address", { projection: new OpenLayers.Projection("EPSG:4326"), 
    	                                          visibility: true, displayInLayerSwitcher: false });

    map.addLayers([layer_mapnik, layer_markers]);
    jumpTo(newPositionLon, newPositionLat, zoom);
 
    // Position des Markers
    addMarker(layer_markers, newPositionLon, newPositionLat, popuptext);

}

//]]>
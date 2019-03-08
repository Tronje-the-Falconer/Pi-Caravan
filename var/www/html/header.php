<!DOCTYPE html>
<html>
   <head>
        <title>Pi-Caravan</title>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta http-equiv="content-script-type" content="text/javascript" />
        <meta http-equiv="content-style-type" content="text/css" />
        <meta http-equiv="content-language" content="de" />
        <meta name="author" content="Jan Ole Kording" />
        <script src="js/ajax.js"></script>
        <script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
        <script src="js/weather.js"></script>
        <script src='js/Chart.js'></script>
        <script src='js/moment.min.js'></script>
        <link rel="stylesheet" type="text/css" href="/css/map.css"></link>
        <!--[if IE]>
        <link rel="stylesheet" type="text/css" href="/css/ie_map.css"></link>
        <![endif]-->
        <script type="text/javascript" src="/js/OpenLayers.js"></script>
        <script type="text/javascript" src="/js/OpenStreetMap.js"></script>
        <script type="text/javascript" src="/js/map.js"></script>
        <script type="text/javascript" src="/js/osm.js"></script>
         
        <!-- <script type="text/javascript">
        //<![CDATA[

        var map;
        var layer_mapnik;
        var layer_tah;
        var layer_markers;

        function drawmap() {
            // Popup und Popuptext mit evtl. Grafik
            var popuptext="<font color=\"black\"><b>Thomas Heiles<br>Stra&szlig;e 123<br>54290 Trier</b></font>";

            OpenLayers.Lang.setCode('de');
            
            // Position und Zoomstufe der Karte
            var lon = 6.641389;
            var lat = 49.756667;
            var zoom = 7;

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
                numZoomLevels: 18,
                maxResolution: 156543,
                units: 'meters'
            });

            layer_mapnik = new OpenLayers.Layer.OSM.Mapnik("Mapnik");
            layer_markers = new OpenLayers.Layer.Markers("Address", { projection: new OpenLayers.Projection("EPSG:4326"), 
                                                          visibility: true, displayInLayerSwitcher: false });

            map.addLayers([layer_mapnik, layer_markers]);
            jumpTo(lon, lat, zoom);
         
            // Position des Markers
            addMarker(layer_markers, 6.641389, 49.756667, popuptext);

        }

        //]]>
            </script> -->
  </head>
  <body onload="drawmap();">

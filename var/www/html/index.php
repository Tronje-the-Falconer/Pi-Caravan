<?php
    include 'header.php';                                       // template-head
    include 'modules/radio.php';                                // radio-functions
?>
<div style="position: relative;">
    <h1 class="art-postheader">Pi Caravan</h1>
    <hr>
</div>
<div id="Radio" style="position: relative;">
    <h2 class="art-postheader">Radio</h2>
    <form method="post">
        <table style="width: 20%;">
                   <tr>
                <td><button class="art-button" name="radio_on" value="radio_on">Radio on</button></td>
                <td><button class="art-button" name="radio_reset">Radio on and reset</button></td>
                <td><button class="art-button" name="radio_off">Radio off</button></td>
            </tr>
            <tr>
                <td><button class="art-button" name="radio_volume_down">Volume down</button></td>
                <td><button class="art-button" name="radio_volume_up">Volume up</button></td>
                <td></td>
            </tr>
            <tr>
                <td><button class="art-button" name="radio_seek_down">seek down</button></td>
                <td><button class="art-button" name="radio_seek_up">seek up</button></td>
                <td></td>
            </tr>
            <tr>
                <td>Tune Frequency:</td>
                <td><input name="radio_frequency" type="number" maxlength="5" min="87.5" max="108" step="0.01" onchange="(function(el){el.value=parseFloat(el.value).toFixed(2);})(this)" placeholder="105,50"></td>
                <td><button class="art-button" name="radio_tune">Tune</button></td>
            </tr>
        </table>
    </form>
    <hr>
</div>
<div id="Temperatur" style="position: relative;">
    <h2 class="art-postheader">Temperatur</h2>
    <table style="width: 20%;">
        <tr>
            <td>Außentemperatur: </td>
            <td><div id="temp_outside"></div></td>
            <td> °C</td>
        </tr>
        <tr>
            <td>Innentemperatur: </td>
            <td><div id="temp_inside"></div></td>
            <td> °C</td>
        </tr>
        <tr>
            <td>Kühlschrank innen: </td>
            <td><div id="fridge"></div></td>
            <td> °C</td>
        </tr>
        <tr>
            <td>Kühlschrank Abluft: </td>
            <td><div id="fridge_exhaust"></div></td>
            <td> °C</td>
        </tr>
        <tr>
            <td>Gyroskop: </td>
            <td><div id="gyro_temp"></div></td>
            <td> °C</td>
        </tr>
        <tr>
            <td>Kühlschrank Abluft Lüfter </td>
            <td>AN/AUS</td>
        </tr>
    </table>
    <hr>
</div>
<div id="Gyroskop" style="height:400px;"">
    <h2 class="art-postheader">Gyroskop</h2>
    <div>
        <table>
            <tr>
                <td>x (left, left_big): </td>
                <td><div id="gyro_x"></div></td>
                <td> °</td>
            </tr>
            <tr>
                <td>y (top,top_big): </td>
                <td><div id="gyro_y"></div></td>
                <td> °</td>
            </tr>
            <tr>
                <td>z: </td>
                <td><div id="gyro_z"></div></td>
                <td> °</td>
            </tr>
        </table>
    </div>

    <div id="Libellen" style="position: relative;">
        <div style="position: absolute;">
                <div id="glas_green" style="align: middle; left:1px; top:1px; z-index:1; position:absolute;" ><img  height="250" width="250" src="pictures/glas_green.gif"></div>
                <div id="blase_2" style="align: middle; z-index:2; position:absolute;"><img height="50" width="50" src="pictures/blase.gif"></div>
                <div id="fadenkreuz2" style="align: middle; left:1px; top:1px; z-index:3; position:absolute;" ><img height="250" width="250" src="pictures/fadenkreuz_schwarz.gif"></div>
        </div>
        <div style="position: absolute; float: left; margin-left: 255px;">
                <div id="glas_white" style="align: middle; left:1px; top:1px; z-index:1; position:absolute;" ><img height="250" width="250" src="pictures/glas.gif"></div>
                <div id="blase" style="align: middle; z-index:2; position:absolute;"><img height="50" width="50" src="pictures/blase.gif"></div>
                <div id="fadenkreuz" style="align: middle; left:1px; top:1px; z-index:3; position:absolute;" ><img height="250" width="250" src="pictures/fadenkreuz.gif"></div>
        </div>
     </div>
    <hr>
</div>
<div id="Füllstände" style="position: relative; margin-top: 255px;">
    <h2 class="art-postheader">Füllstände Wasser / Abwasser</h2>

    <hr>
</div>
<div id="GPS" style="position: relative;">
    <h2 class="art-postheader">GPS</h2>
    <div style="position: relative;">
        <div id="header" style="position: absolute;">
            <div id="osm"style="position: absolute;">© <a href="http://www.openstreetmap.org">OpenStreetMap</a>
             und <a href="http://www.openstreetmap.org/copyright">Mitwirkende</a>,
             <a href="http://creativecommons.org/licenses/by-sa/2.0/deed.de">CC-BY-SA</a>
            </div>
        </div>
        <div id="map" style="width:600px; height:600px;">
        </div>
    </div>
    <hr>
</div>
<div id="Strom" style="position: relative;">
    <h2 class="art-postheader">Batterieüberwachung</h2>
    <hr>
</div>
<div id="Windmesser" style="position: relative;">
    <h2 class="art-postheader">Windmesser</h2>
    <table>
        <tr>
            <td>Windspeed: </td>
            <td><div id="windspeed"></div></td>
            <td>m/s</td>
        </tr>
        <tr>
            <td>Windaverage: </td>
            <td><div id="windaverage"></div></td>
            <td>m/s</td>
        </tr>
        <tr>
            <td><div id="windaverage_description"></div></td>
        </tr>
    </table>
    <hr>
</div>
<div id="Wetter" style="position: relative;">
    <h2 class="art-postheader">aktuelles Wetter</h2>
    <div id="coords"></div>
    <div id="weatherBg">
        <div id="weather"><p></p></div>
    </div>
    <div id="weather_uviBg">
        <h3 class="art-postheader">aktuelle UV-Belastung (12:00 Uhr)</h3>
        <div id="weather_uvi"><p></p></div>
    </div>
    <h2 class="art-postheader">Wetter Vorhersage</h2>
    <canvas id="weather_forecast_chart"></canvas>
    <div id="weather_forecast"><p></p></div>
    <h3 class="art-postheader">UV-Belastung (12:00 Uhr)</h3>
    <div id="weather_uvi_forecast"><p></p></div>
</div>

<?php
    include 'footer.php';
?>


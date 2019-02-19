<?php
    include 'header.php';                                       // template-head
    include 'modules/radio.php';                                // radio-functions
?>
<h1 class="art-postheader">Pi Caravan</h1>
<hr>
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
        <td>Kühlschrank Abluft Lüfter </td>
        <td>AN/AUS</td>
    </tr>
</table>
<hr>
<h2 class="art-postheader">Gyroskop</h2>
<table>
    <tr>
        <td>x: </td>
        <td><div id="gyro_x"></div></td>
        <td> °</td>
    </tr>
    <tr>
        <td>y: </td>
        <td><div id="gyro_y"></div></td>
        <td> °</td>
    </tr>
    <tr>
        <td>z: </td>
        <td><div id="gyro_z"></div></td>
        <td> °</td>
    </tr>
</table>
<hr>
<h2 class="art-postheader">Füllstände Wasser / Abwasser</h2>
<hr>
<h2 class="art-postheader">Wetter</h2>
<div id="weather"><p></p></div>
<div id="weatherBg">Farbe</div>
<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script type="text/javascript">
// ABFRAGE VON GEOLOCATION
if (navigator.geolocation) {
    jQuery('div#weather').html('<p>Geolocation funktioniert :) </p>');
 
    function position(currentPosition) {
        var coords      =   currentPosition.coords;
        var lat         =   coords.latitude;
        var lng         =   coords.longitude;
 
        weatherApi(lat, lng);
    };
} else {
    jQuery('div#weather').html('<p>Geolocation funktioniert nicht :( </p>');
 
    var lat         =   '52.52';
    var lng         =   '13.39';
 
    weatherApi(lat, lng);
}
 
navigator.geolocation.getCurrentPosition(position);
     
// FUNCTION
function weatherApi (newPositionLat = null , newPositionLng = null ) {
    // AUSLESEN VON LAT UND LNG
    if ( newPositionLat == null && newPositionLng == null  ) {
        var newPositionLat  =   '52.5200066';
        var newPositionLng  =   '13.404954';    
    }
                     
    // API URL
    var apiUrl              =   'https://api.openweathermap.org/data/2.5/weather?lat=' + newPositionLat + '&lon=' + newPositionLng + '&units=metric&APPID=b0d9b80c7b930202dc653cf8dc846c47';
 
    // WETTER API
    jQuery.ajax ({
        url: apiUrl,
        type: 'GET',
        dataType: 'jsonp',
        success: function(data) {
            // KOORDINATEN
            var coordLat            =   data.coord.lat;
            var coordLng            =   data.coord.lon;
             
            // WETTER
            var weatherId           =   data.weather[0].id;
            var weatherMain         =   data.weather[0].main;
            var weatherDesc         =   data.weather[0].description;
            var weatherIcon         =   '<img src="https://openweathermap.org/img/w/' + data.weather[0].icon + '.png">';
            var weatherBg           =   data.weather[0].icon;
             
            // EXAKT
             
            if ( weatherBg == 800  ) {  
                // klares wetter
                jQuery('div#weatherBg').css('background-color', 'yellow');
            } else if ( weatherBg == 951  ) {   
                // ruhe
                jQuery('div#weatherBg').css('background-color', 'blue');
            } else if ( weatherBg == 952  ) {   
                // leichte-briese
                jQuery('div#weatherBg').css('background-color', 'AliceBlue ');
            } else if ( weatherBg == 954  ) {   
                // maessige-briese
                jQuery('div#weatherBg').css('background-color', 'AntiqueWhite ');
            } else if ( weatherBg == 955  ) {   
                // frische-briese
                jQuery('div#weatherBg').css('background-color', 'Aqua');
            } else if ( weatherBg == 956  ) {   
                // starke-briese
                jQuery('div#weatherBg').css('background-color', 'Aquamarine ');
            } else if ( weatherBg == 957  ) {   
                // starker-wind
                jQuery('div#weatherBg').css('background-color', 'Azure');
            } else if ( weatherBg == 958  ) {   
                // sturm
                jQuery('div#weatherBg').css('background-color', 'BlueViolet');
            } else if ( weatherBg == 959  ) {   
                // starker-sturm
                jQuery('div#weatherBg').css('background-color', 'Brown');
            } else if ( weatherBg == 959  ) {   
                // starker-sturm
                jQuery('div#weatherBg').css('background-color', 'BurlyWood');
            } else if ( weatherBg == 960  ) {   
                // sturm
                jQuery('div#weatherBg').css('background-color', 'CadetBlue');
            } else if ( weatherBg == 961  ) {   
                // heftiger-sturm
                jQuery('div#weatherBg').css('background-color', 'Chartreuse');
            } else if ( weatherBg == 962  ) {   
                // hurrikan
                jQuery('div#weatherBg').css('background-color', 'Coral');
            } 
             
            // RANGE 
             
            else if ( weatherBg >= 900 && weatherBg <= 950  ) {   
                // extrem
                jQuery('div#weatherBg').css('background-color', 'DarkBlue');                            
            } else if ( weatherBg >= 801 && weatherBg <= 899 ) {  
                // wolkig
                jQuery('div#weatherBg').css('background-color', 'DarkGrey');                            
            } else if ( weatherBg >= 701 && weatherBg <= 799  ) { 
                // atmosphäre
                jQuery('div#weatherBg').css('background-color', 'DarkTurquoise');                       
            } else if ( weatherBg >= 600 && weatherBg <= 700 ) {  
                // schnee
                jQuery('div#weatherBg').css('background-color', 'GhostWhite');                          
            } else if ( weatherBg >= 500 && weatherBg <= 599  ) { 
                // regen
                jQuery('div#weatherBg').css('background-color', 'LightSteelBlue');                          
            } else if ( weatherBg >= 300 && weatherBg <= 499  ) { 
                // nieselregen
                jQuery('div#weatherBg').css('background-color', 'LightSkyBlue');                            
            } else if ( weatherBg >= 200 && weatherBg <= 299 ) {  
                // gewitter
                jQuery('div#weatherBg').css('background-color', 'MidnightBlue');
            }
             
            // BASE
            var baseData            =   data.base;
             
            // TEMP
            var mainTemp            =   data.main.temp;
            var mainPressure        =   data.main.pressure;
            var mainHumidity        =   data.main.humidity;
            var mainTempMin         =   data.main.temp_min;
            var mainTempMax         =   data.main.temp_max;
             
            // VISIBILITY
            var visibility          =   data.visibility;
             
            // WIND
            var windSpeed           =   data.wind.speed;
            var windDeg             =   data.wind.deg;
             
            // CLOUDS
            var clouds              =   data.clouds.all;
             
            // DT
            var dt                  =   data.dt;
             
            // SYS
            var sysType             =   data.sys.type;
            var sysId               =   data.sys.id;
            var sysMessage          =   data.sys.message;
            var sysCountry          =   data.sys.country;
            var sysSunrise          =   data.sys.sunrise;
            var sysSunset           =   data.sys.sunset;
             
            // ID
            var id                  =   data.id;
             
            // NAME
            var name                =   data.name;
             
            // COD
            var cod                 =   data.cod;
             
            var coor                =   '<h2>Koordinaten</h2><ul><li><strong>Lat:</strong> ' + coordLat + '</li><li><strong>Lng:</strong> ' + coordLng + '</li></ul>';
            var weather             =   '<h2>Wetter</h2><ul><li><strong>ID:</strong> ' + weatherId + '</li><li><strong>Main:</strong> ' + weatherMain + '</li><li><strong>Desc:</strong> ' + weatherDesc + '</li><li><strong>icon:</strong> ' + weatherIcon + '</li></ul>';
            var base                =   '<h2>Base</h2><ul><li><strong>Base:</strong> ' + baseData + '</li></ul>';
            var temperatur          =   '<h2>Temperatur</h2><ul><li><strong>Main Temp:</strong> ' + mainTemp + '</li><li><strong>Druck:</strong> ' + mainPressure + '</li><li><strong>Feuchtigkeit:</strong> ' + mainHumidity + '</li><li><strong>min. Temp.:</strong> ' + mainTempMin + '</li><li><strong>Max. Temp.:</strong> ' + mainTempMax + '</li></ul>';
            var visibility          =   '<h2>Sichtweite</h2><ul><li><strong>Sichtweite:</strong> ' + visibility + '</li></ul>';
            var wind                =   '<h2>Wind</h2><ul><li><strong>Wind Speed:</strong> ' + windSpeed + '</li><li><strong>Wind Deg:</strong> ' + windDeg + '</li></ul>';
            var clouds              =   '<h2>Wolken</h2><ul><li><strong>Wolken:</strong> ' + clouds + '</li></ul>';
            var dt                  =   '<h2>DT</h2><ul><li><strong>Dt:</strong> ' + dt + '</li></ul>';
            var system              =   '<h2>Base</h2><ul><li><strong>Typ:</strong> ' + sysType + '</li><li><strong>ID:</strong> ' + sysId + '</li><li><strong>Message:</strong> ' + sysMessage + '</li><li><strong>Land:</strong> ' + sysCountry + '</li><li><strong>Sunrise:</strong> ' + sysSunrise + '</li><li><strong>Sunset:</strong> ' + sysSunset + '</li></ul>';
            var id                  =   '<h2>ID</h2><ul><li><strong>ID:</strong> ' + id + '</li></ul>';
            var name                =   '<h2>Name</h2><ul><li><strong>Name:</strong> ' + name + '</li></ul>';
            var cod                 =   '<h2>Cod</h2><ul><li><strong>Cod:</strong> ' + cod + '</li></ul>';
             
            // OUTPUT
            jQuery('div#weather').html( coor + weather + base + temperatur + visibility + wind + clouds + dt + system + id + name + cod );
            console.log(data);
        }
    });
}
</script>


<hr>
<h2 class="art-postheader">GPS</h2>
<hr>
<h2 class="art-postheader">Batterieüberwachung</h2>
<hr>
<h2 class="art-postheader">Windmesser</h2>
<?php
    include 'footer.php';
?>


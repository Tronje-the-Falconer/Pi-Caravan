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
<h2 class="art-postheader">aktuelles Wetter</h2>
<div id="weatherBg">
    <div id="weather"><p></p></div>
</div>
<div id="weather_uviBg">
    <h2 class="art-postheader">UV-Belastung</h2>
    <div id="weather_uvi"><p></p></div>
</div>
<h2 class="art-postheader">Vorhersage</h2>
<h2 class="art-postheader">Wetter</h2>
<div id="weather_forecast"><p></p></div>
<h2 class="art-postheader">UV-Belastung</h2>
<div id="weather_uvi_forecast"><p></p></div>

<script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script type="text/javascript">
    // ABFRAGE VON GEOLOCATION
    if (navigator.geolocation) {
        jQuery('div#weather').html('<p>Geolocation funktioniert :) </p>');
     
        function position(currentPosition) {
            var coords      =   currentPosition.coords;
            var lat         =   coords.latitude;
            var lon         =   coords.longitude;
     
            weatherApi(lat, lon);
        };
    } else {
        jQuery('div#weather').html('<p>Geolocation funktioniert nicht :( </p>');
     
        var lat         =   '52.52';
        var lon         =   '13.39';
     
        weatherApi(lat, lon);
    }
     
    navigator.geolocation.getCurrentPosition(position);
         
    // FUNCTION
    function weatherApi (newPositionLat = null , newPositionLon = null ) {
        // AUSLESEN VON LAT UND lon
        if ( newPositionLat == null && newPositionLon == null  ) {
            var newPositionLat  =   '52.028437';
            var newPositionLon  =   '8.919562';        
        }
                         
        // API URL
        var apiUrl_weather               =   'https://api.openweathermap.org/data/2.5/weather?lat=' + newPositionLat + '&lon=' + newPositionLon + '&units=metric&lang=de&APPID=b0d9b80c7b930202dc653cf8dc846c47';
        var apiUrl_weather_forecast      =   'https://api.openweathermap.org/data/2.5/forecast?lat=' + newPositionLat + '&lon=' + newPositionLon + '&units=metric&lang=de&APPID=b0d9b80c7b930202dc653cf8dc846c47';
        var apiUrl_weather_uvi           =   'https://api.openweathermap.org/data/2.5/uvi?lat=' + newPositionLat + '&lon=' + newPositionLon + '&APPID=b0d9b80c7b930202dc653cf8dc846c47';
        var apiUrl_weather_uvi_forecast  =   'https://api.openweathermap.org/data/2.5/uvi/forecast?lat=' + newPositionLat + '&lon=' + newPositionLon + '&APPID=b0d9b80c7b930202dc653cf8dc846c47';
        
        
        // WETTER AKTUELL API
        jQuery.ajax ({
            url: apiUrl_weather,
            type: 'GET',
            dataType: 'jsonp',
            success: function(data) {
                function timeConverter(UNIX_timestamp, Format){
                    var a = new Date(UNIX_timestamp * 1000);
                    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
                    var year = a.getFullYear();
                    var month = months[a.getMonth()];
                    var date = a.getDate();
                    var hour = a.getHours();
                    var min = a.getMinutes();
                    var sec = a.getSeconds();
                    if ( Format == 'date'  ) {
                        var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
                        return time;
                    }else{
                        var time = hour + ':' + min + ':' + sec ;
                        return time;
                    }
                }
                // KOORDINATEN
                var coordLat            =   data.coord.lat;
                var coordLon            =   data.coord.lon;
                 
                // WETTER
                var weatherId           =   data.weather[0].id; // Weather condition id
                var weatherMain         =   data.weather[0].main; // Group of weather parameters (Rain, Snow, Extreme etc.)
                var weatherDescription  =   data.weather[0].description; // Weather condition within the group
                var weatherIcon         =   '<img src="https://openweathermap.org/img/w/' + data.weather[0].icon + '.png">'; // Weather icon id
                var weatherBg           =   data.weather[0].icon; // Weather icon id
                 
                // BASE
                var baseData            =   data.base; // Internal parameter
                 
                // TEMP
                var mainTemp            =   data.main.temp; // Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
                var mainPressure        =   data.main.pressure; // Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
                var mainHumidity        =   data.main.humidity; // Humidity, %
                var mainTempMin         =   data.main.temp_min; // Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
                var mainTempMax         =   data.main.temp_max; // Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
                var mainSeaLvl          =   data.main.sea_level; //  Atmospheric pressure on the sea level, hPa
                var mainGrndLvl         =   data.main.grnd_level; // Atmospheric pressure on the ground level, hPa
                 
                // VISIBILITY
                var visibility          =   data.visibility; // Visibility, meter
                 
                // WIND
                var windSpeed           =   data.wind.speed; // Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
                var windDeg             =   data.wind.deg; // Wind direction, degrees (meteorological)
                 
                // CLOUDS
                var clouds              =   data.clouds.all; // Cloudiness, %
                
                // RAIN
                //var rain1h              =   data.rain.1h; // Rain volume for the last 1 hour, mm
                //var rain3hrain          =   data.rain.3h; // Rain volume for the last 3 hours, mm
                
                //SNOW
                //var snow1hsnow          =   data.snow.1h; // Snow volume for the last 1 hour, mm
                //var snow3hsnow          =   data.snow.3h; // Snow volume for the last 3 hours, mm
                
                // DT
                var dt_unix               =   data.dt; // Time of data calculation, unix, UTC
                var dt                    =   timeConverter(dt_unix, 'date');
                 
                // SYS
                var sysType             =   data.sys.type; // Internal parameter
                var sysId               =   data.sys.id; // Internal parameter
                var sysMessage          =   data.sys.message; // Internal parameter
                var sysCountry          =   data.sys.country; // Country code (GB, JP etc.)
                var sysSunrise_unix     =   data.sys.sunrise; // Sunrise time, unix, UTC
                var sysSunrise          =   timeConverter(sysSunrise_unix);
                var sysSunset_unix      =   data.sys.sunset; // Sunset time, unix, UTC
                var sysSunset           =   timeConverter(sysSunset_unix);
                
                // ID
                var id                  =   data.id; // City ID
                 
                // NAME
                var name                =   data.name; // City name
                 
                // COD
                var cod                 =   data.cod; // Internal parameter
                
                // LAST UPDATE
                //var lastupdate          =   data.lastupdate.value; // Last time when data was updated
                 
                var coor                =   '<h4>Koordinaten</h4><ul><li><strong>Lat:</strong> ' + coordLat + '</li><li><strong>Lon:</strong> ' + coordLon + '</li></ul>';
                var weather             =   '<h4>Wetter</h4><ul><li><strong>Main:</strong> ' + weatherMain + '</li><li><strong>Desc:</strong> ' + weatherDescription + '</li><li><strong>icon:</strong> ' + weatherIcon + '</li></ul>';
                var base                =   '<h4>Base</h4><ul><li><strong>Base:</strong> ' + baseData + '</li></ul>';
                var temperatur          =   '<h4>Temperatur</h4><ul><li><strong>Temp:</strong> ' + mainTemp + ' &deg;C</li><li><strong>min. Temp.:</strong> ' + mainTempMin + ' &deg;C</li><li><strong>max. Temp.:</strong> ' + mainTempMax + ' &deg;C</li><li><strong>Druck:</strong> ' + mainPressure + ' hPa</li><li><strong>Feuchtigkeit:</strong> ' + mainHumidity + ' %</li></ul>';
                var visibility          =   '<h4>Sichtweite</h4><ul><li><strong>Sichtweite:</strong> ' + visibility + ' Meter</li></ul>';
                var wind                =   '<h4>Wind</h4><ul><li><strong>Wind Geschwindigkeit:</strong> ' + windSpeed + ' m/s</li><li><strong>Wind Richtung:</strong> ' + windDeg + ' &deg;</li></ul>';
                var clouds              =   '<h4>Wolken</h4><ul><li><strong>Wolken:</strong> ' + clouds + ' %</li></ul>';
                var dt                  =   '<h4>Daten von</h4><ul><li><strong>Dt:</strong> ' + dt + '</li></ul>';
                var system              =   '<h4>Base</h4><ul><li><strong>Land:</strong> ' + sysCountry + '</li><li><strong>Sonnenaufgang:</strong> ' + sysSunrise + ' Uhr</li><li><strong>Sonnenuntergang:</strong> ' + sysSunset + ' Uhr</li></ul>';
                var id                  =   '<h4>ID</h4><ul><li><strong>ID:</strong> ' + id + '</li></ul>';
                var name                =   '<h4>Name</h4><ul><li><strong>Name:</strong> ' + name + '</li></ul>';
                var cod                 =   '<h4>Cod</h4><ul><li><strong>Cod:</strong> ' + cod + '</li></ul>';
                
                
                // EXAKT
                 
                if ( weatherId == 800  ) {  
                    // klares wetter
                    jQuery('div#weatherBg').css('background-color', 'yellow');
                } else if ( weatherId == 951  ) {   
                    // ruhe
                    jQuery('div#weatherBg').css('background-color', 'blue');
                } else if ( weatherId == 952  ) {   
                    // leichte-briese
                    jQuery('div#weatherBg').css('background-color', 'AliceBlue ');
                } else if ( weatherId == 954  ) {   
                    // maessige-briese
                    jQuery('div#weatherBg').css('background-color', 'AntiqueWhite ');
                } else if ( weatherId == 955  ) {   
                    // frische-briese
                    jQuery('div#weatherBg').css('background-color', 'Aqua');
                } else if ( weatherId == 956  ) {   
                    // starke-briese
                    jQuery('div#weatherBg').css('background-color', 'Aquamarine ');
                } else if ( weatherId == 957  ) {   
                    // starker-wind
                    jQuery('div#weatherBg').css('background-color', 'Azure');
                } else if ( weatherId == 958  ) {   
                    // sturm
                    jQuery('div#weatherBg').css('background-color', 'BlueViolet');
                } else if ( weatherId == 959  ) {   
                    // starker-sturm
                    jQuery('div#weatherBg').css('background-color', 'Brown');
                } else if ( weatherId == 959  ) {   
                    // starker-sturm
                    jQuery('div#weatherBg').css('background-color', 'BurlyWood');
                } else if ( weatherId == 960  ) {   
                    // sturm
                    jQuery('div#weatherBg').css('background-color', 'CadetBlue');
                } else if ( weatherId == 961  ) {   
                    // heftiger-sturm
                    jQuery('div#weatherBg').css('background-color', 'Chartreuse');
                } else if ( weatherId == 962  ) {   
                    // hurrikan
                    jQuery('div#weatherBg').css('background-color', 'Coral');
                } 
                 
                // RANGE 
                 
                else if ( weatherId >= 900 && weatherId <= 950  ) {   
                    // extrem
                    jQuery('div#weatherBg').css('background-color', 'DarkBlue');                            
                } else if ( weatherId >= 801 && weatherId <= 899 ) {  
                    // wolkig
                    jQuery('div#weatherBg').css('background-color', 'DarkGrey');                            
                } else if ( weatherId >= 701 && weatherId <= 799  ) { 
                    // atmosphäre
                    jQuery('div#weatherBg').css('background-color', 'DarkTurquoise');                       
                } else if ( weatherId >= 600 && weatherId <= 700 ) {  
                    // schnee
                    jQuery('div#weatherBg').css('background-color', 'GhostWhite');                          
                } else if ( weatherId >= 500 && weatherId <= 599  ) { 
                    // regen
                    jQuery('div#weatherBg').css('background-color', 'LightSteelBlue');                          
                } else if ( weatherId >= 300 && weatherId <= 499  ) { 
                    // nieselregen
                    jQuery('div#weatherBg').css('background-color', 'LightSkyBlue');                            
                } else if ( weatherId >= 200 && weatherId <= 299 ) {  
                    // gewitter
                    jQuery('div#weatherBg').css('background-color', 'MidnightBlue');
                }
                
                // OUTPUT
                jQuery('div#weather').html( name + coor + weather + temperatur + visibility + wind + clouds + dt + system );
                //console.log(data);
            }
        });
        
        //UV AKTUELL API
        jQuery.ajax ({
            url: apiUrl_weather_uvi,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                function timeConverter(UNIX_timestamp, Format){
                    var a = new Date(UNIX_timestamp * 1000);
                    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
                    var year = a.getFullYear();
                    var month = months[a.getMonth()];
                    var date = a.getDate();
                    var hour = a.getHours();
                    var min = a.getMinutes();
                    var sec = a.getSeconds();
                    if ( Format == 'date'  ) {
                        var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
                        return time;
                    }else{
                        var time = hour + ':' + min + ':' + sec ;
                        return time;
                    }
                }
                // KOORDINATEN
                var coordLat            =   data.lat; // latitude for returned data
                var coordLon            =   data.lon; // longitude for returned data 
                
                var date_iso            = data.date_iso; //date and time corresponding to returned date 
                var date_orig           = data.date; // ISO 8601 timestamp
                var date                = timeConverter(date_orig, 'date');
                var value               = data.value;

                var coor                =   '<h4>Koordinaten</h4><ul><li><strong>Lat:</strong> ' + coordLat + '</li><li><strong>Lon:</strong> ' + coordLon + '</li></ul>';
                var uv                  =   '<h4>UV-Data</h4><ul><li><strong>ISO:</strong> ' + date_iso + '</li><li><strong>Date:</strong> ' + date + '</li><li><strong>value:</strong> ' + value + '</li></ul>';
                
                
                //Hintergrund einfärben
                if ( value < 2.9  ) {  
                    // Risk of harm from unprotected sun exposure, for the average adult "Low"
                    jQuery('div#weather_uviBg').css('background-color', 'green');  //A UV Index reading of 0 to 2 means low danger from the sun's UV rays for the average person. Wear sunglasses on bright days. If you burn easily, cover up and use broad spectrum SPF 30+ sunscreen. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                } else if ( value >= 3.0 && value <= 5.9  ) {   
                    // Risk of harm from unprotected sun exposure, for the average adult "Moderate"
                    jQuery('div#weather_uviBg').css('background-color', 'yellow'); // A UV Index reading of 3 to 5 means moderate risk of harm from unprotected sun exposure. Stay in shade near midday when the sun is strongest. If outdoors, wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                } else if ( value >= 6.0 && value <= 7.9  ) {   
                    // Risk of harm from unprotected sun exposure, for the average adult "High"
                    jQuery('div#weather_uviBg').css('background-color', 'orange'); //A UV Index reading of 6 to 7 means high risk of harm from unprotected sun exposure. Protection against skin and eye damage is needed. Reduce time in the sun between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                } else if ( value >= 8.0 && value <= 10.9  ) {   
                    // Risk of harm from unprotected sun exposure, for the average adult "Very high"
                    jQuery('div#weather_uviBg').css('background-color', 'red');// A UV Index reading of 8 to 10 means very high risk of harm from unprotected sun exposure. Take extra precautions because unprotected skin and eyes will be damaged and can burn quickly. Minimize sun exposure between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                } else if ( value > 11.0  ) {   
                    // Risk of harm from unprotected sun exposure, for the average adult "Extreme"
                    jQuery('div#weather_uviBg').css('background-color', 'violett'); // A UV Index reading of 11 or more means extreme risk of harm from unprotected sun exposure. Take all precautions because unprotected skin and eyes can burn in minutes. Try to avoid sun exposure between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                }
                
                
                
                // OUTPUT
                jQuery('div#weather_uvi').html(coor + uv);
                //console.log(data);
            }
        });
        //Wetter Vorhersage API alle 3 Stunden (8 Pro Tag), 5 Tage
        jQuery.ajax ({
            url: apiUrl_weather_forecast,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                function timeConverter(UNIX_timestamp, Format){
                    var a = new Date(UNIX_timestamp * 1000);
                    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
                    var year = a.getFullYear();
                    var month = months[a.getMonth()];
                    var date = a.getDate();
                    var hour = a.getHours();
                    var min = a.getMinutes();
                    var sec = a.getSeconds();
                    if ( Format == 'date'  ) {
                        var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
                        return time;
                    }else{
                        var time = hour + ':' + min + ':' + sec ;
                        return time;
                    }
                }
                // DATA
                var weather_forecast_data_objekt = data;

                var weather_forecast_day_1_1 = weather_forecast_data_objekt.list[0];
                var weather_forecast_day_1_2 = weather_forecast_data_objekt.list[1];
                var weather_forecast_day_1_3 = weather_forecast_data_objekt.list[2];
                var weather_forecast_day_1_4 = weather_forecast_data_objekt.list[3];
                var weather_forecast_day_1_5 = weather_forecast_data_objekt.list[4];
                var weather_forecast_day_1_6 = weather_forecast_data_objekt.list[5];
                var weather_forecast_day_1_7 = weather_forecast_data_objekt.list[6];
                var weather_forecast_day_1_8 = weather_forecast_data_objekt.list[7];
                var weather_forecast_day_2_1 = weather_forecast_data_objekt.list[8];
                var weather_forecast_day_2_2 = weather_forecast_data_objekt.list[9];
                var weather_forecast_day_2_3 = weather_forecast_data_objekt.list[10];
                var weather_forecast_day_2_4 = weather_forecast_data_objekt.list[11];
                var weather_forecast_day_2_5 = weather_forecast_data_objekt.list[12];
                var weather_forecast_day_2_6 = weather_forecast_data_objekt.list[13];
                var weather_forecast_day_2_7 = weather_forecast_data_objekt.list[14];
                var weather_forecast_day_2_8 = weather_forecast_data_objekt.list[15];
                var weather_forecast_day_3_1 = weather_forecast_data_objekt.list[16];
                var weather_forecast_day_3_2 = weather_forecast_data_objekt.list[17];
                var weather_forecast_day_3_3 = weather_forecast_data_objekt.list[18];
                var weather_forecast_day_3_4 = weather_forecast_data_objekt.list[19];
                var weather_forecast_day_3_5 = weather_forecast_data_objekt.list[20];
                var weather_forecast_day_3_6 = weather_forecast_data_objekt.list[21];
                var weather_forecast_day_3_7 = weather_forecast_data_objekt.list[22];
                var weather_forecast_day_3_8 = weather_forecast_data_objekt.list[23];
                var weather_forecast_day_4_1 = weather_forecast_data_objekt.list[24];
                var weather_forecast_day_4_2 = weather_forecast_data_objekt.list[25];
                var weather_forecast_day_4_3 = weather_forecast_data_objekt.list[26];
                var weather_forecast_day_4_4 = weather_forecast_data_objekt.list[27];
                var weather_forecast_day_4_5 = weather_forecast_data_objekt.list[28];
                var weather_forecast_day_4_6 = weather_forecast_data_objekt.list[29];
                var weather_forecast_day_4_7 = weather_forecast_data_objekt.list[30];
                var weather_forecast_day_4_8 = weather_forecast_data_objekt.list[32];
                var weather_forecast_day_5_1 = weather_forecast_data_objekt.list[32];
                var weather_forecast_day_5_2 = weather_forecast_data_objekt.list[33];
                var weather_forecast_day_5_3 = weather_forecast_data_objekt.list[34];
                var weather_forecast_day_5_4 = weather_forecast_data_objekt.list[35];
                var weather_forecast_day_5_5 = weather_forecast_data_objekt.list[36];
                var weather_forecast_day_5_6 = weather_forecast_data_objekt.list[37];
                var weather_forecast_day_5_7 = weather_forecast_data_objekt.list[38];
                var weather_forecast_day_5_8 = weather_forecast_data_objekt.list[39];
                
                
                var weatherMain_day_1_1         =   weather_forecast_day_1_1.weather[0].main; // Group of weather parameters (Rain, Snow, Extreme etc.)
                var weatherDescription_day_1_1  =   weather_forecast_day_1_1.weather[0].description; // Weather condition within the group
                var weatherIcon_day_1_1         =   '<img src="https://openweathermap.org/img/w/' + weather_forecast_day_1_1.weather[0].icon + '.png">'; // Weather icon id
                var weatherBg_day_1_1           =   weather_forecast_day_1_1.weather[0].icon; // Weather icon id
                
                
                var weather             =   '<h4>Wetter</h4><ul><li><strong>Main:</strong> ' + weatherMain_day_1_1 + '</li><li><strong>Desc:</strong> ' + weatherDescription_day_1_1 + '</li><li><strong>icon:</strong> ' + weatherIcon_day_1_1 + '</li></ul>';
                
                // OUTPUT
                jQuery('div#weather_forecast').html( weather );
                //console.log(weather_forecast_data_objekt.list[0]);
                
            }
        });
        //UV Vorhersage API
        jQuery.ajax ({
            url: apiUrl_weather_uvi_forecast,
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                function timeConverter(UNIX_timestamp, Format){
                    var a = new Date(UNIX_timestamp * 1000);
                    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
                    var year = a.getFullYear();
                    var month = months[a.getMonth()];
                    var date = a.getDate();
                    var hour = a.getHours();
                    var min = a.getMinutes();
                    var sec = a.getSeconds();
                    if ( Format == 'date'  ) {
                        var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
                        return time;
                    }else{
                        var time = hour + ':' + min + ':' + sec ;
                        return time;
                    }
                }
                // DATA
                var uvi_forecast_data_objekts = data;
                
                var uvi_forecast_data_1 = uvi_forecast_data_objekts[0];
                var uvi_forecast_data_2 = uvi_forecast_data_objekts[1];
                var uvi_forecast_data_3 = uvi_forecast_data_objekts[2];
                var uvi_forecast_data_4 = uvi_forecast_data_objekts[3];
                var uvi_forecast_data_5 = uvi_forecast_data_objekts[4];
                var uvi_forecast_data_6 = uvi_forecast_data_objekts[5];
                var uvi_forecast_data_7 = uvi_forecast_data_objekts[6];
                var uvi_forecast_data_8 = uvi_forecast_data_objekts[7];
                
                
                var uvi_forecast_date_iso_1            = uvi_forecast_data_1.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_1           = uvi_forecast_data_1.date; // ISO 8601 timestamp
                var uvi_forecast_date_1                = timeConverter(uvi_forecast_date_orig_1, 'date');
                var uvi_forecast_value_1               = uvi_forecast_data_1.value;
                
                var uvi_forecast_date_iso_2            = uvi_forecast_data_2.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_2           = uvi_forecast_data_2.date; // ISO 8602 timestamp
                var uvi_forecast_date_2                = timeConverter(uvi_forecast_date_orig_2, 'date');
                var uvi_forecast_value_2               = uvi_forecast_data_2.value;
                
                var uvi_forecast_date_iso_3            = uvi_forecast_data_3.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_3           = uvi_forecast_data_3.date; // ISO 8603 timestamp
                var uvi_forecast_date_3                = timeConverter(uvi_forecast_date_orig_3, 'date');
                var uvi_forecast_value_3               = uvi_forecast_data_3.value;
                
                var uvi_forecast_date_iso_4            = uvi_forecast_data_4.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_4           = uvi_forecast_data_4.date; // ISO 8604 timestamp
                var uvi_forecast_date_4                = timeConverter(uvi_forecast_date_orig_4, 'date');
                var uvi_forecast_value_4               = uvi_forecast_data_4.value;
                
                var uvi_forecast_date_iso_5            = uvi_forecast_data_5.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_5           = uvi_forecast_data_5.date; // ISO 8605 timestamp
                var uvi_forecast_date_5                = timeConverter(uvi_forecast_date_orig_5, 'date');
                var uvi_forecast_value_5               = uvi_forecast_data_5.value;
                
                var uvi_forecast_date_iso_6            = uvi_forecast_data_6.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_6           = uvi_forecast_data_6.date; // ISO 8606 timestamp
                var uvi_forecast_date_6                = timeConverter(uvi_forecast_date_orig_6, 'date');
                var uvi_forecast_value_6               = uvi_forecast_data_6.value;
                
                var uvi_forecast_date_iso_7            = uvi_forecast_data_7.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_7           = uvi_forecast_data_7.date; // ISO 8607 timestamp
                var uvi_forecast_date_7                = timeConverter(uvi_forecast_date_orig_7, 'date');
                var uvi_forecast_value_7               = uvi_forecast_data_7.value;
                
                var uvi_forecast_date_iso_8            = uvi_forecast_data_8.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig_8           = uvi_forecast_data_8.date; // ISO 8608 timestamp
                var uvi_forecast_date_8                = timeConverter(uvi_forecast_date_orig_8, 'date');
                var uvi_forecast_value_8               = uvi_forecast_data_8.value;
                
                var uvi_forecast         =   '<div id="uvi_forecast_1" ><h4>' + uvi_forecast_date_1 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_1 + '</li></ul></div><div id="uvi_forecast_2" ><h4>' + uvi_forecast_date_2 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_2 + '</li></ul></div><div id="uvi_forecast_3" ><h4>' + uvi_forecast_date_3 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_3 + '</li></ul></div><div id="uvi_forecast_4" ><h4>' + uvi_forecast_date_4 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_4 + '</li></ul></div><div id="uvi_forecast_5" ><h4>' + uvi_forecast_date_5 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_5 + '</li></ul></div><div id="uvi_forecast_6" ><h4>' + uvi_forecast_date_6 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_6 + '</li></ul></div><div id="uvi_forecast_7" ><h4>' + uvi_forecast_date_7 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_7 + '</li></ul></div><div id="uvi_forecast_8" ><h4>' + uvi_forecast_date_8 + '</h4><ul><li><strong>value:</strong> ' + uvi_forecast_value_8 + '</li></ul><h4></div>';

                
                
                // OUTPUT
                jQuery('div#weather_uvi_forecast').html(uvi_forecast);
                
                
                // colourise
                var uvi_forecast_values = [uvi_forecast_value_1, uvi_forecast_value_2, uvi_forecast_value_3, uvi_forecast_value_4, uvi_forecast_value_5, uvi_forecast_value_6, uvi_forecast_value_7, uvi_forecast_value_8]
                var uvi_forecast_count = 1
                for (uvi_forecast_value of uvi_forecast_values){
                    if ( uvi_forecast_value < 2.9  ) {  
                        // Risk of harm from unprotected sun exposure, for the average adult "Low"
                        var uvi_forecast_bgcolor =  'green';  //A UV Index reading of 0 to 2 means low danger from the sun's UV rays for the average person. Wear sunglasses on bright days. If you burn easily, cover up and use broad spectrum SPF 30+ sunscreen. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                    } else if ( uvi_forecast_value >= 3.0 && uvi_forecast_value <= 5.9  ) {   
                        // Risk of harm from unprotected sun exposure, for the average adult "Moderate"
                        var uvi_forecast_bgcolor = 'yellow'; // A UV Index reading of 3 to 5 means moderate risk of harm from unprotected sun exposure. Stay in shade near midday when the sun is strongest. If outdoors, wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                    } else if ( uvi_forecast_value >= 6.0 && uvi_forecast_value <= 7.9  ) {   
                        // Risk of harm from unprotected sun exposure, for the average adult "High"
                        var uvi_forecast_bgcolor = 'orange'; //A UV Index reading of 6 to 7 means high risk of harm from unprotected sun exposure. Protection against skin and eye damage is needed. Reduce time in the sun between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                    } else if ( uvi_forecast_value >= 8.0 && uvi_forecast_value <= 10.9  ) {   
                        // Risk of harm from unprotected sun exposure, for the average adult "Very high"
                        var uvi_forecast_bgcolor = 'red';// A UV Index reading of 8 to 10 means very high risk of harm from unprotected sun exposure. Take extra precautions because unprotected skin and eyes will be damaged and can burn quickly. Minimize sun exposure between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                    } else if ( uvi_forecast_value > 11.0  ) {   
                        // Risk of harm from unprotected sun exposure, for the average adult "Extreme"
                        var uvi_forecast_bgcolor = 'violett'; // A UV Index reading of 11 or more means extreme risk of harm from unprotected sun exposure. Take all precautions because unprotected skin and eyes can burn in minutes. Try to avoid sun exposure between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                    }
                    
                    var weatherforecast_div_id = 'div#uvi_forecast_' + uvi_forecast_count.toString()
                    jQuery(weatherforecast_div_id).css('background-color', uvi_forecast_bgcolor);
                    uvi_forecast_count = uvi_forecast_count + 1
                    
                }
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


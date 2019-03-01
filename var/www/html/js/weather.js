// ABFRAGE VON GEOLOCATION
if (navigator.geolocation) {
    //jQuery('div#weather').html('<p>Geolocation funktioniert :) </p>');
 
    function position(currentPosition) {
        var coords      =   currentPosition.coords;
        var lat         =   coords.latitude;
        var lon         =   coords.longitude;
        weatherApi(lat, lon);
    };
} else {
    //jQuery('div#weather').html('<p>Geolocation funktioniert nicht :( </p>');
        var lat         =   null;
        var lon         =   null;
        weatherApi(lat, lon);
}

navigator.geolocation.getCurrentPosition(position);

// FUNCTION
function weatherApi (newPositionLat = null , newPositionLon = null ) {
    var coords_source = 'geolocation';
    // AUSLESEN VON LAT UND lon
    var gps_json = (function() {
            var json = null;
            $.ajax({
                'async': false,
                'global': false,
                'url': "/gps_location.json",
                'dataType': "json",
                'success': function (data) {
                    json = data;
                }
            });
            return json;
        })();
        
    if ( gps_json != null ) {
        newPositionLat = gps_json.lat;
        newPositionLon = gps_json.lon;
        coords_source = 'gps json';
    }else if (newPositionLat == null && newPositionLon == null) {
        newPositionLat  =   '52.0';
        newPositionLon  =   '8.0';
        coords_source = 'fake';
    }
    
    jQuery('div#coords').html( 'Koordinatenherkunft: ' + coords_source);
    var openweatherorgapi = gps_json.api;
    // API URL
    var apiUrl_weather               =   'https://api.openweathermap.org/data/2.5/weather?lat=' + newPositionLat + '&lon=' + newPositionLon + '&units=metric&lang=de&APPID=' + openweatherorgapi;
    var apiUrl_weather_forecast      =   'https://api.openweathermap.org/data/2.5/forecast?lat=' + newPositionLat + '&lon=' + newPositionLon + '&units=metric&lang=de&APPID=' + openweatherorgapi;
    var apiUrl_weather_uvi           =   'https://api.openweathermap.org/data/2.5/uvi?lat=' + newPositionLat + '&lon=' + newPositionLon + '&APPID=' + openweatherorgapi;
    var apiUrl_weather_uvi_forecast  =   'https://api.openweathermap.org/data/2.5/uvi/forecast?lat=' + newPositionLat + '&lon=' + newPositionLon + '&APPID=' + openweatherorgapi;
    
    
    // WETTER AKTUELL API
    jQuery.ajax ({
        url: apiUrl_weather,
        type: 'GET',
        dataType: 'jsonp',
        success: function(data) {
            function timeConverter(UNIX_timestamp, Format){
                var a = new Date(UNIX_timestamp * 1000);
                if ( Format == 'date'  ) {
                    var options = { weegday: 'long', year: 'numeric', day: '2-digit', month: '2-digit', hour: '2-digit',minute: '2-digit', weekday: 'long' };
                }else if (Format == 'time'){
                    var options = { hour: '2-digit',minute: '2-digit' };
                }else{
                    var options = { hour: '2-digit',minute: '2-digit' };
                }
                var time = a.toLocaleDateString("de-DE", options);
                return time;
            }
            // KOORDINATEN
            var coordLat            =   data.coord.lat;
            var coordLon            =   data.coord.lon;
             
            // WETTER
            var weatherId           =   data.weather[0].id; // Weather condition id
            var weatherMain         =   data.weather[0].main; // Group of weather parameters (Rain, Snow, Extreme etc.)
            var weatherDescription  =   data.weather[0].description; // Weather condition within the group
            var weatherIcon         =   '<img src="https://openweathermap.org/img/w/' + data.weather[0].icon + '.png">'; // Weather icon id
            // var weatherBg           =   data.weather[0].icon; // Weather icon id
             
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
            
            var dt                  =   '<strong>Daten aus ' + name + ' vom ' + dt +'</strong><br>'; 
            var coor                =   '<strong>Koordinaten </strong<strong>Lat: </strong> ' + coordLat + ' <strong>Lon: </strong> ' + coordLon + '<br>';
            var weather             =   '<strong>Wetter</strong><br>  ' + weatherMain + '<br>  ' + weatherIcon + '<br>' + weatherDescription + '<br>'  ;
            var temperatur          =   '<strong>Temperatur</strong><br><strong>  Temp:</strong> ' + mainTemp + ' &deg;C<br><strong>  min. Temp.:</strong> ' + mainTempMin + ' &deg;C<br><strong>  max. Temp.:</strong> ' + mainTempMax + ' &deg;C<br><br><strong>Druck:</strong> ' + mainPressure + ' hPa<br><strong>Feuchtigkeit:</strong> ' + mainHumidity + ' %<br>';
            var visibility          =   '<strong>Sichtweite </strong>' + visibility + ' Meter<br>';
            var wind                =   '<strong>Wind</strong><strong>Geschwindigkeit: </strong>' + windSpeed + ' m/s<br><strong>Richtung: </strong>' + windDeg + ' &deg;<br>';
            var clouds              =   '<strong>Wolken: </strong>' + clouds + ' %<br>';
            var system              =   '<strong>Sonnenaufgang:</strong> ' + sysSunrise + ' Uhr<br><strong>Sonnenuntergang:</strong> ' + sysSunset + ' Uhr<br>';
            
            var weatherdiv = dt + coor + weather + temperatur + visibility + wind + clouds + system ;
            
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
            jQuery('div#weather').html( weatherdiv);
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
                if ( Format == 'date'  ) {
                    var options = { weekday: 'short' };
                }else if (Format == 'time'){
                    var options = { hour: '2-digit',minute: '2-digit' };
                }else{
                    var options = { hour: '2-digit',minute: '2-digit' };
                }
                var time = a.toLocaleDateString("de-DE", options);
                return time;
            }
            // KOORDINATEN
            var coordLat            =   data.lat; // latitude for returned data
            var coordLon            =   data.lon; // longitude for returned data 
            
            var date_iso            = data.date_iso; //date and time corresponding to returned date 
            var date_orig           = data.date; // ISO 8601 timestamp
            var date                = timeConverter(date_orig, 'date');
            var value               = data.value;
            
            var protection
            //Hintergrund einfärben
            if ( value < 2.9  ) {  
                // Risk of harm from unprotected sun exposure, for the average adult "Low"
                jQuery('div#weather_uviBg').css('background-color', 'green');  //A UV Index reading of 0 to 2 means low danger from the sun's UV rays for the average person. Wear sunglasses on bright days. If you burn easily, cover up and use broad spectrum SPF 30+ sunscreen. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                protection = "Kein Schutz erforderlich. <br><br> Ein UV-Index von 0 bis 2 bedeutet für die durchschnittliche Person eine geringe Gefahr durch die UV-Strahlen der Sonne. Tragen Sie an hellen Tagen eine Sonnenbrille. Wenn Sie leicht brennen, decken Sie den Sonnenschutz mit Sonnenschutzfaktor SPF 30+ ab. Helle Oberflächen wie Sand, Wasser und Schnee erhöhen die UV-Belastung.";
            } else if ( value >= 3.0 && value <= 5.9  ) {   
                // Risk of harm from unprotected sun exposure, for the average adult "Moderate"
                jQuery('div#weather_uviBg').css('background-color', 'yellow'); // A UV Index reading of 3 to 5 means moderate risk of harm from unprotected sun exposure. Stay in shade near midday when the sun is strongest. If outdoors, wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                protection = "Schutz erforderlich: Hut, T-Shirt, Sonnenbrille, Sonnencreme <br><br> Ein UV-Index von 3 bis 5 bedeutet ein mäßiges Risiko, durch ungeschützte Sonneneinstrahlung Schaden zu nehmen. Bleiben Sie kurz vor Mittag im Schatten, wenn die Sonne am stärksten ist. Wenn Sie sich im Freien aufhalten, tragen Sie Sonnenschutzkleidung, einen Hut mit breiter Krempe und eine Sonnenbrille mit UV-Schutz. Tragen Sie großzügig alle 2 Stunden Sonnencreme mit breitem Spektrum mit Sonnenschutzfaktor 30+ auf, auch an bewölkten Tagen und nach dem Schwimmen oder Schwitzen. Helle Oberflächen wie Sand, Wasser und Schnee erhöhen die UV-Belastung.";
            } else if ( value >= 6.0 && value <= 7.9  ) {   
                // Risk of harm from unprotected sun exposure, for the average adult "High"
                jQuery('div#weather_uviBg').css('background-color', 'orange'); //A UV Index reading of 6 to 7 means high risk of harm from unprotected sun exposure. Protection against skin and eye damage is needed. Reduce time in the sun between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                protection = "Schutz erforderlich: Hut, T-Shirt, Sonnenbrille, Sonnencreme. <br> Die Weltgesundheitsorganisation empfiehlt, mittags den Schatten zu suchen. <br><br> Ein UV-Index von 6 bis 7 bedeutet ein hohes Risiko, durch ungeschützte Sonneneinstrahlung Schaden zu nehmen. Schutz vor Haut- und Augenschäden ist erforderlich. Reduzieren Sie die Zeit in der Sonne zwischen 10 und 16 Uhr. Wenn Sie sich im Freien aufhalten, suchen Sie Schatten, und tragen Sie Sonnenschutzkleidung, einen Hut mit breiter Krempe und eine Sonnenbrille mit UV-Schutz. Tragen Sie großzügig alle 2 Stunden Sonnencreme mit breitem Spektrum mit Sonnenschutzfaktor 30+ auf, auch an bewölkten Tagen und nach dem Schwimmen oder Schwitzen. Helle Oberflächen wie Sand, Wasser und Schnee erhöhen die UV-Belastung.";
            } else if ( value >= 8.0 && value <= 10.9  ) {   
                // Risk of harm from unprotected sun exposure, for the average adult "Very high"
                jQuery('div#weather_uviBg').css('background-color', 'red');// A UV Index reading of 8 to 10 means very high risk of harm from unprotected sun exposure. Take extra precautions because unprotected skin and eyes will be damaged and can burn quickly. Minimize sun exposure between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                protection = "zusätzlicher Schutz erforderlich: Aufenthalt im Freien möglichst vermeiden. <br> Die Weltgesundheitsorganisation empfiehlt, den Aufenthalt im Freien zwischen 11 und 15 Uhr zu vermeiden; auch im Schatten gehören ein sonnendichtes Oberteil, lange Hosen, Sonnencreme, Sonnenbrille und ein breitkrempiger Hut zum sonnengerechten Verhalten. <br><br> Ein UV-Index von 8 bis 10 bedeutet ein sehr hohes Risiko, durch ungeschützte Sonneneinstrahlung Schaden zu nehmen. Treffen Sie zusätzliche Vorsichtsmaßnahmen, da ungeschützte Haut und Augen beschädigt werden und schnell verbrennen können. Minimieren Sie die Sonneneinstrahlung zwischen 10 und 4 Uhr. Wenn Sie sich im Freien aufhalten, suchen Sie Schatten, und tragen Sie Sonnenschutzkleidung, einen Hut mit breiter Krempe und eine Sonnenbrille mit UV-Schutz. Tragen Sie großzügig alle 2 Stunden Sonnencreme mit breitem Spektrum mit Sonnenschutzfaktor 30+ auf, auch an bewölkten Tagen und nach dem Schwimmen oder Schwitzen. Helle Oberflächen wie Sand, Wasser und Schnee erhöhen die UV-Belastung.";
            } else if ( value > 11.0  ) {   
                // Risk of harm from unprotected sun exposure, for the average adult "Extreme"
                jQuery('div#weather_uviBg').css('background-color', 'violett'); // A UV Index reading of 11 or more means extreme risk of harm from unprotected sun exposure. Take all precautions because unprotected skin and eyes can burn in minutes. Try to avoid sun exposure between 10 a.m. and 4 p.m. If outdoors, seek shade and wear sun protective clothing, a wide-brimmed hat, and UV-blocking sunglasses. Generously apply broad spectrum SPF 30+ sunscreen every 2 hours, even on cloudy days, and after swimming or sweating. Bright surfaces, such as sand, water and snow, will increase UV exposure.
                protection = "zusätzlicher Schutz erforderlich: Aufenthalt im Freien möglichst vermeiden <br> Die Weltgesundheitsorganisation rät, zwischen 11 und 15 Uhr im Schutz eines Hauses zu bleiben und auch außerhalb dieser Zeit unbedingt Schatten zu suchen. Auch im Schatten gelten ein sonnendichtes Oberteil, lange Hosen, Sonnencreme, Sonnenbrille und ein breitkrempiger Hut als unerlässlich. <br><br> Ein UV-Index von 11 oder mehr bedeutet ein extremes Risiko, durch ungeschützte Sonneneinstrahlung Schaden zu nehmen. Treffen Sie alle Vorsichtsmaßnahmen, da ungeschützte Haut und Augen in wenigen Minuten brennen können. Vermeiden Sie Sonneneinstrahlung zwischen 10 und 4 Uhr. Wenn Sie sich im Freien aufhalten, suchen Sie Schatten, und tragen Sie Sonnenschutzkleidung, einen Hut mit breiter Krempe und eine Sonnenbrille mit UV-Schutz. Tragen Sie großzügig alle 2 Stunden Sonnencreme mit breitem Spektrum mit Sonnenschutzfaktor 30+ auf, auch an bewölkten Tagen und nach dem Schwimmen oder Schwitzen. Helle Oberflächen wie Sand, Wasser und Schnee erhöhen die UV-Belastung.";
            }
            
            //var coor                =   '<h4>Koordinaten</h4><ul><li><strong>Lat:</strong> ' + coordLat + '</li><li><strong>Lon:</strong> ' + coordLon + '</li></ul>';
            var uv                  =   'UV-Index: <strong>' + value + '</strong><br><br>' + protection;
            
            // OUTPUT
            jQuery('div#weather_uvi').html(uv);
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
                if ( Format == 'date'  ) {
                    var options = { hour: '2-digit',minute: '2-digit', weekday: 'short' };
                }else if (Format == 'time'){
                    var options = { hour: '2-digit',minute: '2-digit' };
                }else{
                    var options = { hour: '2-digit',minute: '2-digit' };
                }
                var time = a.toLocaleDateString("de-DE", options);
                return time;
            }
            // DATA
            var weather_forecast_data_objekts = data.list;
            //console.log(weather_forecast_data_objekts);
            
            
            var weather_forecast = '';
            var weather_forecast_timestamps = [];
            var weather_forecast_temperatures = [];
            var weather_forecast_icons = [];
            var weather_forecast_descriptions = [];
            
            var weather_forecast_data_objekts_Length = weather_forecast_data_objekts.length;
            //console.log(weather_forecast_data_objekts_Length);
            
            for (var i = 0; i < weather_forecast_data_objekts_Length; i++) {
                var weather_forecast_data_objekt_counter = i + 1;
                var weather_forecast_data_objekt = weather_forecast_data_objekts[i];
                
                //
                var forecast_weatherMain         =   weather_forecast_data_objekt.weather[0].main; // Group of weather parameters (Rain, Snow, Extreme etc.)
                var forecast_weatherDescription  =   weather_forecast_data_objekt.weather[0].description; // Weather condition within the group
                var forecast_weatherIcon_path   =  'https://openweathermap.org/img/w/' + weather_forecast_data_objekt.weather[0].icon + '.png';
                var forecast_image = new Image();
                    forecast_image.src = forecast_weatherIcon_path;
                var forecast_weatherIcon         =   '<img src="' + forecast_weatherIcon_path + '">'; // Weather icon id
                var forecast_weatherBg           =   weather_forecast_data_objekt.weather[0].icon; // Weather icon id
                var forecast_mainTemp            =   weather_forecast_data_objekt.main.temp; // Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
                
                //
                var forecast_mainPressure        =   weather_forecast_data_objekt.main.pressure; // Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
                var forecast_mainHumidity        =   weather_forecast_data_objekt.main.humidity; // Humidity, %
                var forecast_mainTempMin         =   weather_forecast_data_objekt.main.temp_min; // Minimum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
                var forecast_mainTempMax         =   weather_forecast_data_objekt.main.temp_max; // Maximum temperature at the moment. This is deviation from current temp that is possible for large cities and megalopolises geographically expanded (use these parameter optionally). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
                var forecast_mainSeaLvl          =   weather_forecast_data_objekt.main.sea_level; //  Atmospheric pressure on the sea level, hPa
                var forecast_mainGrndLvl         =   weather_forecast_data_objekt.main.grnd_level; // Atmospheric pressure on the ground level, hPa
                 
                // VISIBILITY
                var forecast_visibility          =   weather_forecast_data_objekt.visibility; // Visibility, meter
                 
                // WIND
                var forecast_windSpeed           =   weather_forecast_data_objekt.wind.speed; // Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
                var forecast_windDeg             =   weather_forecast_data_objekt.wind.deg; // Wind direction, degrees (meteorological)
                 
                // CLOUDS
                var forecast_clouds              =   weather_forecast_data_objekt.clouds.all; // Cloudiness, %
                
                // DT
                var forecast_dt_unix               =   weather_forecast_data_objekt.dt; // Time of data calculation, unix, UTC
                var forecast_dt                    =   timeConverter(forecast_dt_unix, 'date');
                 
                // SYS
                var forecast_sysType             =   weather_forecast_data_objekt.sys.type; // Internal parameter
                var forecast_sysId               =   weather_forecast_data_objekt.sys.id; // Internal parameter
                var forecast_sysMessage          =   weather_forecast_data_objekt.sys.message; // Internal parameter
                var forecast_sysCountry          =   weather_forecast_data_objekt.sys.country; // Country code (GB, JP etc.)
                var forecast_sysSunrise_unix     =   weather_forecast_data_objekt.sys.sunrise; // Sunrise time, unix, UTC
                var forecast_sysSunrise          =   timeConverter(forecast_sysSunrise_unix, 'time');
                var forecast_sysSunset_unix      =   weather_forecast_data_objekt.sys.sunset; // Sunset time, unix, UTC
                var forecast_sysSunset           =   timeConverter(forecast_sysSunset_unix, 'time');
                
                //weather_forcast_div = '<ul><li><strong>Day:</strong> ' + forecast_dt + '</li><li><strong>Main:</strong> ' + forecast_weatherMain + '</li><li><strong>Desc:</strong> ' + forecast_weatherDescription + '</li><li><strong>icon:</strong> ' + forecast_weatherIcon + '</li></ul>';
                //weather_forecast = weather_forecast + weather_forcast_div;
                
                
                // diagrammwerte
                weather_forecast_timestamps.push(forecast_dt);
                weather_forecast_temperatures.push(forecast_mainTemp);
                weather_forecast_icons.push(forecast_image);
                weather_forecast_descriptions.push(forecast_weatherDescription);

                weather_forecast_data_objekt_counter = weather_forecast_data_objekt_counter + 1;
            }
            
            //console.log(weather_forecast_timestamps);
            //console.log(weather_forecast_temperatures);
            //console.log(weather_forecast_icons);
            
            //var weather = '<ul><li><strong>Main:</strong> ' + weatherMain_day_1_1 + '</li><li><strong>Desc:</strong> ' + weatherDescription_day_1_1 + '</li><li><strong>icon:</strong> ' + weatherIcon_day_1_1 + '</li></ul>';
            
            // OUTPUT
            // jQuery('div#weather_forecast').html( weather_forecast );
            //console.log(weather_forecast);
            
            // WETTERDIAGRAMM
            var weather_forecast_chart = document.getElementById("weather_forecast_chart");
            var config_weather_forecast_chart = {
                type: 'line',
                data: {
                    labels: weather_forecast_timestamps,
                    datasets: [{
                        label: 'Temperatur',
                        data: weather_forecast_temperatures,
                        backgroundColor: '#C03738',
                        borderColor: '#C03738',
                        borderWidth: 2,
                        pointRadius: 2,
                        pointStyle: weather_forecast_icons,
                        cubicInterpolationMode: 'monotone',
                        fill: false
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: 'Wetter Vorhersage',
                        fontSize: 24,
                        display: false
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                        callbacks: {
                            label: function(tooltipItem, data) {
                                yvalue = Number(tooltipItem.yLabel).toFixed(1);
                                label_desc = weather_forecast_descriptions[tooltipItem.index];
                                label = yvalue.toString() + ' ' + label_desc;
                                return label;
                            }
                        }
                    },
                    scales: {
                        yAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: 'Temperatur',
                            //    fontSize: 20,
                                fontColor: '#000000'
                            },
                            id: 'temperature',
                            type: 'linear',
                            position: 'left',

                        }]
                    }
                }
            };
            window.onload = function() {
                window.weather_forecast_chart = new Chart(weather_forecast_chart, config_weather_forecast_chart);
            };
            
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
                if ( Format == 'date'  ) {
                    var options = { weekday: 'short', month: '2-digit', day: '2-digit'};
                }else if (Format == 'time'){
                    var options = { hour: '2-digit',minute: '2-digit' };
                }else{
                    var options = { hour: '2-digit',minute: '2-digit' };
                }
                var time = a.toLocaleDateString("de-DE", options);
                return time;
            }
            // DATA
            var uvi_forecast_data_objekts = data;
            
            var uvi_forecast = '<table><tr>';
            var uvi_forecast_data_objekts_Length = uvi_forecast_data_objekts.length;
            for (var i = 0; i < uvi_forecast_data_objekts_Length; i++) {
                var uvi_forecast_data_objekt_counter = i + 1;
                var uvi_forecast_data_objekt = uvi_forecast_data_objekts[i];
                var uvi_forecast_date_iso = uvi_forecast_data_objekt.date_iso; //date and time corresponding to returned date 
                var uvi_forecast_date_orig  = uvi_forecast_data_objekt.date; // ISO 8601 timestamp
                var uvi_forecast_date = timeConverter(uvi_forecast_date_orig , 'date');
                var uvi_forecast_value = uvi_forecast_data_objekt.value;
                
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
                
                //uvi_forcast_div = '<div style = "background-color: ' + uvi_forecast_bgcolor + ' " id="uvi_forecast_' + uvi_forecast_data_objekt_counter.toString() + '" ><h4>' + uvi_forecast_date + '</h4>UV-Index:<strong> ' + uvi_forecast_value + '</strong></div>';
                uvi_forcast_div = '<td align="center", style = "background-color: ' + uvi_forecast_bgcolor + ' " id="uvi_forecast_' + uvi_forecast_data_objekt_counter.toString() + '" ><h4>' + uvi_forecast_date + ' </h4><strong>' + uvi_forecast_value + '</strong></td>';
                uvi_forecast = uvi_forecast + uvi_forcast_div;

                uvi_forecast_data_objekt_counter = uvi_forecast_data_objekt_counter + 1;
            }

            // OUTPUT
            jQuery('div#weather_uvi_forecast').html(uvi_forecast);
        }
    });
}
var xmlHttpObject = false;
if (typeof XMLHttpRequest != 'undefined') {
    xmlHttpObject = new XMLHttpRequest();
}
if (!xmlHttpObject) {
    try {
        xmlHttpObject = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
        try {
            xmlHttpObject = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {
            xmlHttpObject = null;
        }
    }
}

function loadContent() {
    
    xmlHttpObject.open('get','/json/values.json');
    xmlHttpObject.onreadystatechange = handleContent;
    xmlHttpObject.send(null);
    return false;
}

function handleContent() {
    if (xmlHttpObject.readyState == 4 && xmlHttpObject.status == 200) {
        myObj = JSON.parse(xmlHttpObject.responseText);
        
        var testmodus = myObj.testmodus;
        
        var temp_outside = myObj.temperature_outside;
        var temp_inside = myObj.temperature_inside;
        var fridge = myObj.temperature_fridge;
        var freezer = myObj.temperature_freezer;
        var fridge_exhaust = myObj.temperature_fridge_exhaust;
        var exhaust_fan = myObj.fridge_exhaust_fan;
        var temp_truma = myObj.temperature_truma;
        var temp_trumavent = myObj.temperature_trumavent;
        
        var humidity_outside = myObj.humidity_outside;
        var humidity_inside = myObj.humidity_inside;
        
        var windspeed = myObj.windspeed;
        var windaverage = myObj.windaverage;
        var windchill =  myObj.windchill;
        var str_windaverage_description = "";
        
        var batteriespannung = myObj.batteriespannung;
        var batteriefuellstand = myObj.batteriefuellstand;
        var solarerzeugung = myObj.solarerzeugung;
        var systemverbrauch = myObj.systemverbrauch;
        var netzbezug = myObj.netzbezug;
        
        var frischwasser = myObj.frischwasserstand;
        var abwasser = myObj.abwasserstand;
        var toilette = myObj.toilettenstand;
       
        var gyro_x = myObj.gyroskop_x;
        var gyro_y = myObj.gyroskop_y;
        var gyro_z = myObj.gyroskop_z;
        var gyro_temp = myObj.gyroskop_temp;
        
        var str_windchill_txt = null;
        
        var str_windspeed = '-';
        if (windspeed === null){
            str_windspeed = '-';
        }
        else{
            str_windspeed = windspeed.toFixed(1);
            if ((windaverage+3.6) < 4.8){
                str_windchill_txt = "Windchill bei unter < 4.8km/h nicht exakt definiert.";
            }
        }
        var str_windaverage = '-';
        if (windaverage === null){
            str_windaverage = '-';
        }
        else{
            str_windaverage = windaverage.toFixed(1);
            if ((windaverage+3.6) < 4.8){
                str_windchill_txt = "Windchill bei unter < 4.8km/h nicht exakt definiert.";
            }
        }
        var str_windchill = '-';
        if (windchill === null){
            str_windchill = '-';
        }
        else{
            str_windchill = windchill.toFixed(1);
        }
        var str_batteriespannung = '-';
        if (batteriespannung === null){
            str_batteriespannung = '-';
        }
        else{
            str_batteriespannung = batteriespannung.toFixed(1);
        }
        var str_batteriefuellstand = '-';
        if (batteriefuellstand === null){
            str_batteriefuellstand = '-';
        }
        else{
            str_batteriefuellstand = batteriefuellstand.toFixed(1);
        }
        var str_solarerzeugung = '-';
        if (solarerzeugung === null){
            str_solarerzeugung = '-';
        }
        else{
            str_solarerzeugung = solarerzeugung.toFixed(1);
        }
        var str_systemverbrauch = '-';
        if (systemverbrauch === null){
            str_systemverbrauch = '-';
        }
        else{
            str_systemverbrauch = systemverbrauch.toFixed(1);
        }
        var str_netzbezug = '-';
        if (netzbezug === null){
            str_netzbezug = '-';
        }
        else{
            str_netzbezug = netzbezug.toFixed(1);
        }
        var str_frischwasser = '-';
        if (frischwasser === null){
            str_frischwasser = '-';
        }
        else{
            str_frischwasser = frischwasser.toFixed(1);
        }
        var str_abwasser = '-';
        if (abwasser === null){
            str_abwasser = '-';
        }
        else{
            str_abwasser = abwasser.toFixed(1);
        }
        var str_toilette = '-';
        if (toilette === null){
            str_toilette = '-';
        }
        else{
            str_toilette = toilette.toFixed(1);
        }
        var str_temp_outside = '-';
        if (temp_outside === null){
            str_temp_outside = '-';
        }
        else{
            str_temp_outside = temp_outside.toFixed(1);
        }
        var str_temp_inside = '-';
        if (temp_inside === null){
            str_temp_inside = '-';
        }
        else{
            str_temp_inside = temp_inside.toFixed(1);
        }
        var str_fridge = '-';
        if (fridge === null){
            str_fridge = '-';
        }
        else{
            str_fridge = fridge.toFixed(1);
        }
        var str_freezer = '-';
        if (freezer === null){
            str_freezer = '-';
        }
        else{
            str_freezer = freezer.toFixed(1);
        }
        var str_fridge_exhaust = '-';
        if (fridge_exhaust === null){
            str_fridge_exhaust = '-';
        }
        else{
            str_fridge_exhaust = fridge_exhaust.toFixed(1);
        }
        
        var str_temp_truma = '-';
        if (temp_truma === null){
            str_temp_truma = '-';
        }
        else{
            str_temp_truma = temp_truma.toFixed(1);
        }
        var str_temp_truma_vent = '-';
        if (temp_trumavent === null){
            str_temp_truma_vent = '-';
        }
        else{
            str_temp_truma_vent = temp_trumavent.toFixed(1);
        }
        var str_humidity_inside = '-';
        if (humidity_inside === null){
            str_humidity_inside = '-';
        }
        else{
            str_humidity_inside = humidity_inside.toFixed(1);
        }
        var str_humidity_outside = '-';
        if (humidity_outside === null){
            str_humidity_outside = '-';
        }
        else{
            str_humidity_outside = humidity_outside.toFixed(1);
        }
        
        
        if (gyro_x !== null && gyro_y !== null && gyro_z !== null && gyro_temp !== null){
            var str_gyro_x = gyro_x.toFixed(1);
            var str_gyro_y = gyro_y.toFixed(1);
            var str_gyro_z = gyro_z.toFixed(1);
            var str_gyro_temp = gyro_temp.toFixed(1);
            var rotate_x ='rotate('+ str_gyro_x +'deg)';
            var rotate_y ='rotate('+ str_gyro_y +'deg)';
            // fuer 3grad Libelle
            var top_math = 100 + (gyro_y*-25);
            var left_math = 100 + (gyro_x*25);
            var top_str = top_math.toString() + "px";
            var left_str = left_math.toString() + "px";
            //fuer allgemeine Libelle
            var top_math_big = 100 + (gyro_y*-3.5);
            var left_math_big = 100 + (gyro_x*3.5);
            var top_str_big = top_math_big.toString() + "px";
            var left_str_big = left_math_big.toString() + "px";
            
            
            if (gyro_x >= 4){
                left_str = '225px';
            }
            if (gyro_y >= 4){
                top_str = '225px';
            }
            if (gyro_x <= -4){
                left_str = '-25px';
            }
            if (gyro_y <= -4){
                top_str = '-25px';
            }
            str_gyro_x = str_gyro_x + '   ' + left_str + '   ' + left_str_big;
            str_gyro_y = str_gyro_y + '   ' + top_str+ '   ' + top_str_big;
        }
        else{
            str_gyro_x = '-';
            str_gyro_y = '-';
            str_gyro_z = '-';
            str_gyro_temp = '-';
        }
        
        
        if (windaverage < 0){
            str_windaverage_description = "kein Wind";
            jQuery('div#windaverage_description').css('background-color', '#FFFFFF');
        }
        else if (windaverage >=0.6 &&  windaverage <=1.7){
            str_windaverage_description = "Leiser Zug | 0,6 bis 1,7 m/s | 1,9 bis 6,4	km/h | 1-3 kn | 1 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#ECECFF');
        }
        else if (windaverage >=1.8 &&  windaverage <=3.3){
            str_windaverage_description = "Flaue Briese | 1,8 bis 3,3	m/s | 6,5 bis 12,0 km/h | 4-6 kn | 2 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#D9D9FF');
        }
        else if (windaverage >=3.4 &&  windaverage <=5.4){
            str_windaverage_description = "Leichte Briese | 3,4 bis 5,4 m/s | 12,1 bis 19,4 km/h | 7-10 kn | 3 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#C5C5FF');
        }
        else if (windaverage >=5.5 &&  windaverage <=7.9){
            str_windaverage_description = "Frische Briese | 5,5 bis 7,9	m/s | 19,5 bis 28,7 km/h | 11-15 kn | 4 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#B0B0FF');
        }
        else if (windaverage >=8 &&  windaverage <=11){
            str_windaverage_description = "Steife Briese | 8,0 bis 11,0 m/s | 28,8 bis 39,8 km/h | 16-21 kn | 5 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#9B9BFF');
        }
        else if (windaverage >=11.1 &&  windaverage <=14.1){
            str_windaverage_description = "Harter Wind | 11,1 bis 14,1 m/s | 39,9 bis 50,9 km/h | 22-27 kn | 6 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#8383FF');
        }
        else if (windaverage >=14.2 &&  windaverage <=17.2){
            str_windaverage_description = "Stürmischer Wind | 14,2 bis 17,2 m/s | 51,0 bis 62,0 km/h | 28-33 kn | 7 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#6868FF');
        }
        else if (windaverage >=17.3 &&  windaverage <=20.8){
            str_windaverage_description = "Sturm | 17,3 bis 20,8 m/s | 62,1 bis 75,0 km/h | 34-40 kn | 8 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#4747FF');
        }
        else if (windaverage >=20.9 &&  windaverage <=24.4){
            str_windaverage_description = "Starker Sturm | 20,9 bis 24,4 m/s | 75,1 bis 87,9 km/h | 41-47 kn | 9 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#0000FF');
        }
        else if (windaverage >=24.5 &&  windaverage <=28.5){
            str_windaverage_description = "Schwerer Sturm | 24,5 bis 28,5 m/s | 88 bis 102 km/h | 48-55 kn | 10 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#0000BB');
        }
        else if (windaverage >=28.6 &&  windaverage <=32.6){
            str_windaverage_description = "Orkanartiger Sturm | 28,6 bis 32,6 m/s | 102,9 bis 117,6 km/h | 56-63 kn | 11 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#000077');
        }
        else if (windaverage >32.6 && windaverage < 900){
            str_windaverage_description = "Orkan | > 32,6 m/s | >117,7 km/h | >63 kn | 12 Beaufort";
            jQuery('div#windaverage_description').css('background-color', '#000000');
        }
        else if (windaverage == 999){
            str_windaverage_description = "Noch keine 10 min für Durchschnittsgeschwindigkeit gemessen";
        }
        var str_exhaust_fan = '-';
        if (exhaust_fan === true){
             str_exhaust_fan = 'An';
        }
        else if (exhaust_fan === false){
             str_exhaust_fan = 'Aus';
        }
        else{
             str_exhaust_fan = '-';
        }
        
        if (testmodus == true){
            jQuery('div#testmodus').css('background-color', '#FF0000');
            str_testmodus = '!!!Testmode!!!';
        }
        else{
            str_testmodus = '';
        }
       
        //------------------------Setzen der Werte auf der Webseite
        
        document.getElementById('testmodus').innerHTML = str_testmodus;
        document.getElementById('temp_outside').innerHTML = str_temp_outside;
        document.getElementById('temp_inside').innerHTML = str_temp_inside;
        document.getElementById('fridge').innerHTML = str_fridge;
        document.getElementById('freezer').innerHTML = str_freezer;
        document.getElementById('fridge_exhaust').innerHTML = str_fridge_exhaust;
        document.getElementById('fan').innerHTML = str_exhaust_fan;
        document.getElementById('truma').innerHTML = str_temp_truma;
        document.getElementById('trumavent').innerHTML = str_temp_truma_vent;
        
        document.getElementById('humidity_inside').innerHTML = str_humidity_inside;
        document.getElementById('humidity_outside').innerHTML = str_humidity_outside;
        
        document.getElementById('windspeed').innerHTML = str_windspeed;
        document.getElementById('windaverage').innerHTML = str_windaverage;
        document.getElementById('windaverage_description').innerHTML = str_windaverage_description;
        document.getElementById('windchill').innerHTML = str_windchill;
        if (str_windchill_txt !== null){
            document.getElementById('windchill_txt').innerHTML = str_windchill_txt;
        }
        else{
            document.getElementById('windchill_txt').innerHTML = '';
        }
        
        document.getElementById('gyro_x').innerHTML = str_gyro_x;
        document.getElementById('gyro_y').innerHTML = str_gyro_y;
        document.getElementById('gyro_z').innerHTML = str_gyro_z;
        document.getElementById('gyro_temp').innerHTML = str_gyro_temp;
        
        
        document.getElementById('batteriespannung').innerHTML = str_batteriespannung;
        document.getElementById('batteriefuellstand').innerHTML = str_batteriefuellstand;
        document.getElementById('solarerzeugung').innerHTML = str_solarerzeugung;
        document.getElementById('systemverbrauch').innerHTML = str_systemverbrauch;
        document.getElementById('netzbezug').innerHTML = str_netzbezug;
        
        document.getElementById('frischwasser').innerHTML = str_frischwasser;
        document.getElementById('abwasser').innerHTML = str_abwasser;
        document.getElementById('toilette').innerHTML = str_toilette;
        
        //document.getElementById("image_side").style.transform = rotate_x;
        //document.getElementById("image_rear").style.transform = rotate_y;
        document.getElementById("blase").style.left = left_str;
        document.getElementById("blase").style.top = top_str;
        
        document.getElementById("blase_2").style.left = left_str_big;
        document.getElementById("blase_2").style.top = top_str_big;
    }
}

    var myVar = setInterval(myTimer, 3000);

    function myTimer() {
        var d = new Date();
        loadContent();
    }
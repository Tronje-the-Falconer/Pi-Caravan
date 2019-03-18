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

        var str_temp_outside = myObj.temperature_outside.toFixed(1);
        var str_temp_inside = myObj.temperature_inside.toFixed(1);
        var str_fridge = myObj.temperature_fridge.toFixed(1);
        var str_fridge_exhaust = myObj.temperature_fridge_exhaust.toFixed(1);
       
        var windspeed = myObj.windspeed
        var windaverage = myObj.windaverage
        var str_windspeed = windspeed.toFixed(1);
        var str_windaverage = windaverage.toFixed(1);
        
        var gyro_x = myObj.gyroskop_x;
        var gyro_y = myObj.gyroskop_y;
        var gyro_z = myObj.gyroskop_z;
        var gyro_temp = myObj.gyroskop_temp;
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
        
        var str_windaverage_description = "";
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
        else if (windaverage = 999){
            str_windaverage_description = "Noch keine 10 min für Durchschnittsgeschwindigkeit gemessen";
        }
        
        //------------------------Setzen der Werte auf der Webseite
        
        document.getElementById('temp_outside').innerHTML = str_temp_outside;
        document.getElementById('temp_inside').innerHTML = str_temp_inside;
        document.getElementById('fridge').innerHTML = str_fridge;
        document.getElementById('fridge_exhaust').innerHTML = str_fridge_exhaust;
        
        document.getElementById('windspeed').innerHTML = str_windspeed;
        document.getElementById('windaverage').innerHTML = str_windaverage;
        document.getElementById('windaverage_description').innerHTML = str_windaverage_description;
        
        document.getElementById('gyro_x').innerHTML = str_gyro_x;
        document.getElementById('gyro_y').innerHTML = str_gyro_y;
        document.getElementById('gyro_z').innerHTML = str_gyro_z;
        document.getElementById('gyro_temp').innerHTML = str_gyro_temp;
        
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
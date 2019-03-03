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
    xmlHttpObject.open('get','values.json');
    xmlHttpObject.onreadystatechange = handleContent;
    xmlHttpObject.send(null);
    // xmlHttpObject.open('get','config/scales.json');
    // xmlHttpObject.onreadystatechange = handleContentScales;
    // xmlHttpObject.send(null);
    return false;
}

function handleContent() {
    if (xmlHttpObject.readyState == 4 && xmlHttpObject.status == 200) {
        myObj = JSON.parse(xmlHttpObject.responseText);

        var str_temp_outside = myObj.temperature_outside.toFixed(1);
        var str_temp_inside = myObj.temperature_inside.toFixed(1);
        var str_fridge = myObj.temperature_fridge.toFixed(1);
        var str_fridge_exhaust = myObj.temperature_fridge_exhaust.toFixed(1);
        var gyro_x = myObj.gyroskop_x;
        var gyro_y = myObj.gyroskop_y;
        var gyro_z = myObj.gyroskop_z;
        var str_gyro_x = gyro_x.toFixed(1);
        var str_gyro_y = gyro_y.toFixed(1);
        var str_gyro_z = gyro_z.toFixed(1);
        var rotate_x ='rotate('+ str_gyro_x +'deg)';
        var rotate_y ='rotate('+ str_gyro_y +'deg)';
        var top_math = 100 + (gyro_y*25);
        var left_math = 100 + (gyro_x*25);
        var top_str = top_math.toString() + "px";
        var left_str = left_math.toString() + "px";
        
        
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
        str_gyro_x = str_gyro_x + '   ' + left_str;
        str_gyro_y = str_gyro_y + '   ' + top_str;
        //------------------------Setzen der Temperatur-Werte auf der Webseite
        
        document.getElementById('temp_outside').innerHTML = str_temp_outside;
        document.getElementById('temp_inside').innerHTML = str_temp_inside;
        document.getElementById('fridge').innerHTML = str_fridge;
        document.getElementById('fridge_exhaust').innerHTML = str_fridge_exhaust;
        document.getElementById('gyro_x').innerHTML = str_gyro_x;
        document.getElementById('gyro_y').innerHTML = str_gyro_y;
        document.getElementById('gyro_z').innerHTML = str_gyro_z;
        
        //document.getElementById("image_side").style.transform = rotate_x;
        //document.getElementById("image_rear").style.transform = rotate_y;
        document.getElementById("blase").style.left = left_str;
        document.getElementById("blase").style.top = top_str;
    }
}

    var myVar = setInterval(myTimer, 3000);

    function myTimer() {
        var d = new Date();
        loadContent();
    }
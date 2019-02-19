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
        var str_gyro_x = myObj.gyroskop_x.toFixed(1);
        var str_gyro_y = myObj.gyroskop_y.toFixed(1);
        var str_gyro_z = myObj.gyroskop_z.toFixed(1);

        //------------------------Setzen der Temperatur-Werte auf der Webseite
        
        document.getElementById('temp_outside').innerHTML = str_temp_outside;
        document.getElementById('temp_inside').innerHTML = str_temp_inside;
        document.getElementById('fridge').innerHTML = str_fridge;
        document.getElementById('fridge_exhaust').innerHTML = str_fridge_exhaust;
        document.getElementById('gyro_x').innerHTML = str_gyro_x;
        document.getElementById('gyro_y').innerHTML = str_gyro_y;
        document.getElementById('gyro_z').innerHTML = str_gyro_z;
    }
}

    var myVar = setInterval(myTimer, 3000);

    function myTimer() {
        var d = new Date();
        loadContent();
    }
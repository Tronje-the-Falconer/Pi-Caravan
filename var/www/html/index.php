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
<?php
    include 'footer.php';
?>


<?php
    include 'header.php';                                       // template-head
    include 'modules/radio.php';                                // radio-functions
?>
<h1 class="art-postheader">Pi Caravan</h1>
<h2 class="art-postheader">Radio</h2>
<form  method="post">
    <table style="width: 100%;">
               <tr>
            <td><button class="art-button" name="radio_on">Radio on</button></td>
            <td><button class="art-button" name="radio_off">Radio off</button></td>
            <td></td>
        </tr>
        <tr>
            <td><button class="art-button" name="radio_volume_up">Volume up</button></td>
            <td><button class="art-button" name="radio_volume_down">Volume down</button></td>
            <td></td>
        </tr>
        <tr>
            <td><button class="art-button" name="radio_seek_up">seek up</button></td>
            <td><button class="art-button" name="radio_seek_down">seek down</button></td>
            <td></td>
        </tr>
        <tr>
            <td><button class="art-button" name="radio_tune">Tune</button></td>
            <td>Tune Frequency:</td>
            <td><input name="radio_frequency" type="number" maxlength="5" min="87.5" max="108" step="0.01" onchange="(function(el){el.value=parseFloat(el.value).toFixed(2);})(this)" placeholder="105,50"></td>
        </tr>
    </table>
</form>
<?php
    include 'footer.php';
?>


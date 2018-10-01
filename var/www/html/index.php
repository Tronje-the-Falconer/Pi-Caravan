<?php
    include 'header.php';                                       // Template-Kopf und Navigation
?>
<h1 class="art-postheader">Pi Caravan</h1>
<h2 class="art-postheader">Radio</h2>
<form  method="post">
    <table style="width: 100%;">
        <tr>
            <td><button class="art-button" name="radio_on">Radio on</button></td>
            <td><button class="art-button" name="radio_off">Radio off</button></td>
        </tr>
        <tr>
            <td><button class="art-button" name="radio_volume_up">Volume up</button></td>
            <td><button class="art-button" name="radio_volume_down">Volume down</button></td>
        </tr>
        <tr>
            <td><button class="art-button" name="radio_seek_up">seek up</button></td>
            <td><button class="art-button" name="radio_seek_down">seek down</button></td>
            
        </tr>
        <tr>
            <td><button class="art-button" name="radio_tune">Tune</button> Tune Frequency:</td>
            <td><input type="text" name="radio_frequency"></td>
        </tr>
        
    </table>
</form>
<?php
    include 'footer.php';
?>


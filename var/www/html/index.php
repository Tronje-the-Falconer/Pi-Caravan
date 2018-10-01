<?php
    include 'header.php';                                       // Template-Kopf und Navigation
?>
<h1 class="art-postheader">Pi Caravan</h1>
<h2 class="art-postheader">Radio</h2>
<form  method="post">
    <table style="width: 100%;">
        <tr>
            <td><button class="art-button" name="Radio on">Radio on</button></td>
            <td><button class="art-button" name="Radio off">Radio off</button></td>
        </tr>
        <tr>
            <td><button class="art-button" name="Radio Volume up">Volume up</button></td>
            <td><button class="art-button" name="Radio Volume down">Volume down</button></td>
        </tr>
        <tr>
            <td><button class="art-button" name="Radio Seek Up">seek up</button></td>
            <td><button class="art-button" name="Radio Seek Down">seek down</button></td>
            
        </tr>
        <tr>
            <td><button class="art-button" name="Radio Tune">Tune</button> Tune Frequency:</td>
            <td><input type="text" name="Radio Frequency"></td>
        </tr>
        
    </table>
</form>
<?php
    include 'footer.php';
?>


<?php
    #
    if (isset($_POST['radio_on'])){
        shell_exec('sudo /var/sudowebscript.sh radiostartstop up');
    }
    if (isset($_POST['radio_off'])){
        shell_exec('sudo /var/sudowebscript.sh radiostartstop down');
    }
    if (isset($_POST['radio_reset'])){
        shell_exec('sudo /var/sudowebscript.sh radioreset');
    }
    if (isset($_POST['radio_volume_up'])){
        shell_exec('sudo /var/sudowebscript.sh radiovolume 10'); # Hardcoded! berechnen!
    }
    if (isset($_POST['radio_volume_down'])){
        shell_exec('sudo /var/sudowebscript.sh radiovolume 2'); # Hardcoded! berechnen!
    }
    if (isset($_POST['radio_seek_up'])){
        shell_exec('sudo /var/sudowebscript.sh radioseek up');
    }
    if (isset($_POST['radio_seek_down'])){
        shell_exec('sudo /var/sudowebscript.sh radioseek down');
    }
    $radiotune = 'sudo /var/sudowebscript.sh radiotunefreq ' . $_POST['radio_frequency'];
    if (isset($_POST['radio_tune'])){
        shell_exec($radiotune);
    }
?>

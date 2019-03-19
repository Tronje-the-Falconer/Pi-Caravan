#!/usr/bin/python
# coding=utf-8
# pi_caravan_paths.py
#------------------------------------------------------------
"""
    paths for pi-caravan
    
    setting up paths for pi-caravan
"""

def set_paths():
    """
    setting paths
    """
    
    global logfile_txt_file
    global pi_caravan_log_file
    global sqlite3_file
    global onewire_path
    global values_json_file

    logfile_txt_file = '/var/www/html/logs/logfile.txt'
    pi_caravan_log_file = '/var/www/html/logs/pi-caravan.log'
    sqlite3_file = '/var/www/html/database/pi-ager.sqlite3'
    onewire_path = '/sys/bus/w1/devices'
    values_json_file = '/var/www/html/json/values.json'


def get_path(filename):
    """
    getting path for files
    """
    global logfile_txt_file
    global pi_caravan_log_file
    global sqlite3_file
    global onewire_path
    global values_json_file
    set_paths()
    if filename == 'values_json_file':
        return values_json_file
    elif filename == 'logfile_txt_file':
        return logfile_txt_file
    elif filename == 'pi_caravan_log_file':
        return pi_caravan_log_file
    elif filename == 'sqlite3_file':
        return sqlite3_file
    elif filename == 'onewire_path':
        return onewire_path
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
    global web_json_file

    logfile_txt_file = '/var/www/html/logs/logfile.txt'
    pi_caravan_log_file = '/var/www/html/logs/pi-caravan.log'
    sqlite3_file = '/var/www/html/database/pi-ager.sqlite3'
    onewire_path = '/sys/bus/w1/devices'
    web_json_file = '/var/www/html/values.json'

def get_path_logfile_txt_file():
    """
    getting path for website logfile
    """
    global logfile_txt_file
    set_paths()
    return logfile_txt_file
    
def get_pi_caravan_log_file_path():
    """
    getting path for logfile
    """
    global pi_caravan_log_file
    set_paths()
    return pi_caravan_log_file

def get_path_sqlite3_file():
    """
    getting path for sqlite file
    """
    global sqlite3_file
    set_paths()
    return sqlite3_file

def get_path_onewire():
    """
    getting path for onewiresensors 
    """
    global onewire_path
    set_paths()
    return onewire_path
    
def get_path_web_json_file():
    """
    getting path for web_json_file
    """
    global web_json_file
    set_paths()
    return web_json_file

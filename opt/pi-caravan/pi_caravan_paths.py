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

    logfile_txt_file = '/var/www/logs/logfile.txt'
    pi_caravan_log_file = '/var/www/logs/pi-caravan.log'
    sqlite3_file = '/var/www/config/pi-ager.sqlite3'
    onewire_path = '/sys/bus/w1/devices'

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
    getting path for website logfile
    """
    global onewire_path
    set_paths()
    return onewire_path

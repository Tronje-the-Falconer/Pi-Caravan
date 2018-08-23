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

    logfile_txt_file = '/var/www/logs/logfile.txt'
    pi_caravan_log_file = '/var/www/logs/pi-caravan.log'

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

#!/usr/bin/python
# coding=utf-8
# pi_caravan_logging.py
#------------------------------------------------------------
"""
    logging for pi-caravan
    
    creating loggers for the pi-caravan modules
"""
import logging
from logging import handlers
import pi_caravan_paths
import pi_caravan_database_get_logging_value
import pathlib
import os, stat

def get_logginglevel(loglevelstring):
    """
    setting loglevels
    """
    global logger
    
    if loglevelstring == 10:
        loglevel = logging.DEBUG
    elif loglevelstring == 20:
        loglevel = logging.INFO
    elif loglevelstring == 30:
        loglevel = logging.WARNING
    elif loglevelstring == 40:
        loglevel = logging.ERROR
    elif loglevelstring == 50:
        loglevel = logging.CRITICAL
    
    return loglevel
    
def check_website_logfile():
    """
    checking and setting permission for the website logfile 
    """
    global logger
    filepath = pi_caravan_paths.get_path_logfile_txt_file()
    website_logfile = pathlib.Path(filepath)
    filepermission = oct(os.stat(pi_caravan_paths.logfile_txt_file)[stat.ST_MODE])[-3:]
    if not website_logfile.is_file():
        new_website_logfile = open(pi_caravan_paths.get_path_logfile_txt_file(), "wb")
        new_website_logfile.close()
        #os.chmod(pi_caravan_paths.get_path_logfile_txt_file(), stat.S_IWOTH|stat.S_IWGRP|stat.S_IWUSR|stat.S_IROTH|stat.S_IRGRP|stat.S_IRUSR)
    if (filepermission != '666'):
        os.chmod(pi_caravan_paths.get_path_logfile_txt_file(), stat.S_IWOTH|stat.S_IWGRP|stat.S_IWUSR|stat.S_IROTH|stat.S_IRGRP|stat.S_IRUSR)

def create_logger(pythonfile):
    """
    creating loggers
    """
    check_website_logfile()
    loglevel_file_value = pi_caravan_database_get_logging_value.get_logging_value('loglevel_file')
    loglevel_console_value = pi_caravan_database_get_logging_value.get_logging_value('loglevel_console')
    
    # Logger fuer website
    website_log_rotatingfilehandler = logging.handlers.RotatingFileHandler(pi_caravan_paths.get_path_logfile_txt_file(), mode='a', maxBytes=1048576, backupCount=36, encoding=None, delay=False)
    website_log_rotatingfilehandler.setLevel(logging.INFO)
    website_log_rotatingfilehandler_formatter = logging.Formatter('%(asctime)s %(message)s', '%y-%m-%d %H:%M:%S')
    website_log_rotatingfilehandler.setFormatter(website_log_rotatingfilehandler_formatter)

    # Logger fuer pi-caravan debugging
    pi_caravan_log_rotatingfilehandler = logging.handlers.RotatingFileHandler(pi_caravan_paths.get_pi_caravan_log_file_path(), mode='a', maxBytes=2097152, backupCount=20, encoding=None, delay=False)
    pi_caravan_log_rotatingfilehandler.setLevel(get_logginglevel(loglevel_file_value))
    pi_caravan_log_rotatingfilehandler_formatter = logging.Formatter('%(asctime)s %(name)-27s %(levelname)-8s %(message)s', '%m-%d %H:%M:%S')
    pi_caravan_log_rotatingfilehandler.setFormatter(pi_caravan_log_rotatingfilehandler_formatter)

    # Logger fuer die Console
    console_streamhandler = logging.StreamHandler()
    console_streamhandler.setLevel(get_logginglevel(loglevel_console_value))
    console_streamhandler_formatter = logging.Formatter(' %(levelname)-10s: %(name)-8s %(message)s')
    console_streamhandler.setFormatter(console_streamhandler_formatter)
    
    logger = logging.getLogger(pythonfile)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(website_log_rotatingfilehandler)
    logger.addHandler(pi_caravan_log_rotatingfilehandler)
    logger.addHandler(console_streamhandler)
    
    return logger
        
logger = create_logger(__name__)
logger.debug('logging initialised')

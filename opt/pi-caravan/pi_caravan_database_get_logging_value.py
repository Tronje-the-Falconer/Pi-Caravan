#!/usr/bin/python
# coding=utf-8
# pi_caravan_database_get_logging_value.py
#------------------------------------------------------------
"""
    logger for database module
    
    special module for getting loglevel in databasemodule 
"""
import sqlite3
import pi_caravan_names
import pi_caravan_paths

def get_logging_value(destination):
    """
    get loglevel
    """
    rows = None
    connection = sqlite3.connect(pi_caravan_paths.sqlite3_file)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    try:
        command = 'SELECT ' + pi_caravan_names.value_field + ' FROM ' + pi_caravan_names.debug_table + ' WHERE ' + pi_caravan_names.key_field + ' = "' + destination + '"'
        cursor.execute(command)
        connection.commit()
        
        row = cursor.fetchone()
        
        connection.close()
        logging_value = row[pi_caravan_names.value_field]
    except:
        logging_value = 10
    finally:
        return logging_value

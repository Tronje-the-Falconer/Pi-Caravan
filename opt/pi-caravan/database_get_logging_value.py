#!/usr/bin/python
# coding=utf-8
# database_get_logging_value.py
#------------------------------------------------------------
"""
    logger for database module
    
    special module for getting loglevel in databasemodule 
"""
import sqlite3
import names
import paths

def get_logging_value(destination):
    """
    get loglevel
    """
    rows = None
    connection = sqlite3.connect(paths.get_path('sqlite3_file'))
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    try:
        command = 'SELECT ' + names.value_field + ' FROM ' + names.debug_table + ' WHERE ' + names.key_field + ' = "' + destination + '"'
        cursor.execute(command)
        connection.commit()
        
        row = cursor.fetchone()
        
        connection.close()
        logging_value = row[names.value_field]
    except:
        logging_value = 10
    finally:
        return logging_value

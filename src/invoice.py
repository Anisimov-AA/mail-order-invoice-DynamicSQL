import pymysql # to connect to MySQL database
import json # to read/write JSON files
import os # to work with files, folders

def load_db_config():
    """Load database connection settings from config file"""
    config_path = 'config/db_config.json'
    with open(config_path, 'r') as f:
        return json.load(f)
        
def load_sql_query(filename):
    """Load SQL query from sql/ folder"""
    query_path = os.path.join('sql', filename)
    with open(query_path, 'r') as f:
        return f.read()
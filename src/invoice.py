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
            
def get_db_connection():
    """Create and return database connection"""
    try:
        config = load_db_config()
        return pymysql.connect(**config)
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return None
        
if __name__ == '__main__':
    # 1. Test configuration loading
    print("Testing configuration loading...")
    config = load_db_config()
    print(f" Database config loaded: {config['database']}@{config['host']}")
    
    query = load_sql_query('get_invoice_by_order.sql')
    print(f" SQL query loaded ({len(query)} characters)")
    
    # 2. Test database connection
    print("\nTesting database connection...")
    conn = get_db_connection()
    if conn:
        print(" Database connected successfully")
        conn.close()
        print(" Connection closed")
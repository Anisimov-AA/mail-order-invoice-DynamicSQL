import pymysql # to connect to MySQL database
import json # to read/write JSON files
import os # to work with files, folders

def load_db_config():
    """Load database connection settings from config file"""
    config_path = 'config/db_config.json'
    with open(config_path, 'r') as f:       # 1. open the file
        return json.load(f)                 # 2. load JSON, convert to dictionary & return the dictionary
        
def load_sql_query(filename):
    """Load SQL query from sql/ folder"""
    query_path = os.path.join('sql', filename)
    with open(query_path, 'r') as f:        # 1. open the file
        return f.read()                     # 2. read all text & return the text 
            
def get_db_connection():
    """Create and return database connection"""
    try:
        config = load_db_config()               # 1. load config
        return pymysql.connect(**config)    # 2. connect & return connection
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return None
        
def get_invoice_data(order_num):
    """
    Fetch invoice data for given order number using Dynamic SQL
    
    Args:
        order_num (int): Order number to look up
    
    Returns:
        list: List of tuples containing invoice data, or None if error
    """
    
    connection = None
    try: 
        connection = get_db_connection()                    # 1. connect to database
        query = load_sql_query('get_invoice_by_order.sql')  # 2. load the SQL query
        cursor = connection.cursor()                        # 3. create cursor
        cursor.execute(query, (order_num,))                 # 4. execute query (Dynamic SQL)
        results = cursor.fetchall()                         # 5. get all results
        cursor.close()                                      # 6. close cursor
        return results                                      # 7. return the results
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally: # always close connection
        if connection: 
            connection.close() 
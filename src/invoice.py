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

def display_invoice(results):
    """Display formatted invoice from query results"""
    
    # check if we have results
    if not results or len(results) == 0:
        print("No order found with that number")
        return
    
    # extract header info from first row
    first_row = results[0]
    order_num = first_row[0]
    customer_name = first_row[1]
    customer_num = first_row[2]
    zip_code = first_row[3]
    city = first_row[4]
    taken_by = first_row[5]
    received_on = first_row[6]
    shipped_on = first_row[7]
    
    # print invoice header
    print("\n" + "=" * 28 + " INVOICE " + "=" * 29)
    print(f"Order Number: {order_num}")
    print(f"Customer Name: {customer_name}")
    print(f"Customer No: {customer_num}")
    print(f"ZIP Code: {zip_code} ({city if city else 'N/A'})")
    print(f"Taken By: {taken_by}")
    print(f"Received on: {received_on}")
    print(f"Shipped on: {shipped_on if shipped_on else 'Not yet shipped'}")
    
    # print order details section
    print("-" * 26 + " Order Details " + "-" * 25)
    print(f"{'Part No':<10} {'Part Name':<30} {'Qty':<6} {'Price':<10} {'Total':<10}")
    print("-" * 66)
    
    # print each line item and calculate total
    total_amount = 0
    for row in results:
        part_num = row[8]
        part_name = row[9]
        quantity = row[10]
        price = float(row[11])
        line_total = float(row[12])
        
        print(f"{part_num:<10} {part_name:<30} {quantity:<6} ${price:<9.2f} ${line_total:<9.2f}")
        total_amount += line_total
    
    # print footer with total
    print("=" * 66)
    print(f"TOTAL AMOUNT: ${total_amount:.2f}")
    print("=" * 66 + "\n")
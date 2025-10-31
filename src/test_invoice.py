from invoice import load_db_config, load_sql_query, get_db_connection, get_invoice_data

def test_config():
    """Test configuration loading"""
    config = load_db_config()
    print(f"Database config loaded: {config['database']}@{config['host']}")

def test_sql_loading():
    """Test SQL query loading"""
    query = load_sql_query('get_invoice_by_order.sql')
    print(f"SQL query loaded ({len(query)} characters)")

def test_connection():
    """Test database connection"""
    conn = get_db_connection()
    if conn:
        print("Database connected successfully")
        conn.close()

def test_invoice_data():
    """Test invoice data retrieval"""
    data = get_invoice_data(1020)
    if data:
        print(f"Found {len(data)} line items for order 1020:")
        
        for i in range(len(data)):
            print(data[i])

if __name__ == '__main__':
    # test_config()
    # test_sql_loading()
    # test_connection()
    test_invoice_data()
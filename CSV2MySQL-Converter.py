import pandas as pd
import mysql.connector
import os
from mysql.connector import Error, pooling
import time

# List of CSV files and their corresponding table names
csv_files = [
    ('customers.csv', 'customers'),
    ('orders.csv', 'orders'),
    ('sellers.csv', 'sellers'),
    ('products.csv', 'products'),
    ('geolocation.csv', 'geolocation'),
    ('payments.csv', 'payments'),
    ('order_items.csv', 'order_items')
]

# Folder containing the CSV files
folder_path = 'C:/Users/priya/Data_set/e-Commerce (Target) Sales Dataset'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Priyanshu009',
    'database': 'eCommerceWScude'
}

def get_sql_type(dtype):
    """Returns the SQL type corresponding to the pandas dtype."""
    if pd.api.types.is_integer_dtype(dtype):
        return 'INT'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    else:
        return 'TEXT'

def create_table_if_not_exists(cursor, table_name, df):
    """Creates a table if it does not exist."""
    columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])
    create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})'
    cursor.execute(create_table_query)

def process_csv_file(file_path, table_name, cursor):
    """Processes a single CSV file and imports it into the specified MySQL table."""
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Replace NaN with None to handle SQL NULL
        df = df.where(pd.notnull(df), None)

        # Clean column names
        df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]

        # Create table if it does not exist
        create_table_if_not_exists(cursor, table_name, df)

        # Optimize data insertion
        insert_query = f"INSERT INTO `{table_name}` ({', '.join(['`' + col + '`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(df.columns))})"
        data = [tuple(None if pd.isna(x) else x for x in row) for _, row in df.iterrows()]

        # Insert data in chunks to avoid packet size issues
        chunk_size = 1000
        for i in range(0, len(data), chunk_size):
            cursor.executemany(insert_query, data[i:i + chunk_size])
            print(f"Data from {file_path} inserted into table {table_name}, batch {i // chunk_size + 1}")

    except Error as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """Main function to connect to the database and process all CSV files."""
    start_time = time.time()  # Start time measurement

    try:
        # Setup database connection pooling
        pool = pooling.MySQLConnectionPool(pool_name="mypool",
                                           pool_size=5,
                                           **db_config)

        # Obtain a connection from the pool
        conn = pool.get_connection()
        cursor = conn.cursor()

        for csv_file, table_name in csv_files:
            file_path = os.path.join(folder_path, csv_file)
            process_csv_file(file_path, table_name, cursor)

        # Commit the transaction
        conn.commit()
        print("All files successfully added to SQL")

    except Error as e:
        print(f"Database error: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed")

    end_time = time.time()  # End time measurement
    duration = end_time - start_time
    print(f"Total execution time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()

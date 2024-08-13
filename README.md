# CSV to MySQL Data Importer

## Introduction

Welcome to the **CSV to MySQL Data Importer** project! This Python script simplifies the process of importing CSV data into a MySQL database. Whether you're migrating data for analytics, integration, or any other purpose, this tool provides a streamlined and efficient solution.

## Features

- **Dynamic Table Creation**: Automatically generates tables based on CSV file headers.
- **Efficient Data Insertion**: Uses chunked inserts to handle large datasets with optimal performance.
- **Connection Pooling**: Manages database connections effectively to enhance performance.
- **Robust Error Handling**: Provides clear error messages and handles common issues.
- **Performance Metrics**: Tracks and reports script execution time.

![App Screenshot](https://github.com/priyanshurathod009/CSV2MySQL-Converter/blob/main/Image/images01.jpeg.jpg?raw=true)

## Getting Started

Follow these instructions to set up and use the CSV to MySQL Data Importer.

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
- **MySQL Server**: Download and install from [mysql.com](https://dev.mysql.com/downloads/).
- **Python Packages**: Install required packages using pip.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/priyanshurathod009/CSV2MySQL-Converter.git
   cd csv-to-mysql-importer
   ```

2. **Install Dependencies**

   ```bash
   pip install pandas mysql-connector-python
   ```

3. **Configure MySQL**

   - Create a MySQL database (e.g., `StockPricePrediction`).
   - Update the database credentials in the script (`import_script.py`).

### Configuration

1. **Set the Folder Path**

   Place your CSV files in the designated folder or update the `folder_path` in the script:

   ```python
   folder_path = 'C:/Users/priya/StockPricePrediction'
   ```

2. **Update Database Credentials**

   Modify the `db_config` dictionary in `import_script.py` with your MySQL credentials:

   ```python
   db_config = {
       'host': 'localhost',
       'user': 'root',
       'password': 'yourpassword',
       'database': 'StockPricePrediction'
   }
   ```

## Usage

To execute the script and start importing data, run:

```bash
python import_script.py
```

The script will process each CSV file, create necessary tables, and insert data into the MySQL database.

## Performance Optimization

- **Chunk Size**: Data is processed in chunks of `5000` rows to enhance performance and manage large datasets.
- **Execution Time**: The script is optimized to complete execution in under 50 seconds for typical datasets.

## Troubleshooting

- **Error: Got a packet bigger than 'max_allowed_packet' bytes**
  - Adjust the `max_allowed_packet` setting in your MySQL configuration and restart the server.

- **Error: Lost connection to MySQL server during query**
  - Verify server stability and resource allocation. Ensure proper connection settings.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact:

For inquiries or further information, please contact

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/priyanshu-rathod/)

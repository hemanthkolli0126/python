import os
import pyodbc
import datetime
from google.cloud import bigquery
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_data_from_sql_server(server, database, username, password):
    """Fetches data for the current day from SQL Server."""
    try:
        connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        today = datetime.date.today().strftime('%Y-%m-%d')
        sql_query = "SELECT * FROM Attendance WHERE DATE >= ? AND DATE <= ?"
        cursor.execute(sql_query, (today, today))
        rows = cursor.fetchall()
        column_names = [d[0] for d in cursor.description]
        rows = [[str(value) if isinstance(value, datetime.datetime) else value for value in row] for row in rows]
        connection.close()
        logger.info("SQL Server connection closed.")
        return rows, column_names
    except pyodbc.Error as e:
        logger.error(f"Error fetching data from SQL Server: {str(e)}")
        return None, None

def transfer_data_to_bigquery(rows, column_names, project_id, dataset_id, table_id):
    """Transfers data to BigQuery."""
    try:
        client = bigquery.Client()
        table_id = f"{project_id}.{dataset_id}.{table_id}"
        table = client.get_table(table_id)
        if table is None:
            schema = create_bigquery_schema()
            table_ref = bigquery.Table(table_id, schema=schema)
            table = client.create_table(table_ref)
            logger.info("Table created:", table.table_id)
        else:
            schema = table.schema
        rows_dict = []
        for row in rows:
            cleaned_row = [int(value) if isinstance(value, bool) else value for value in row]
            rows_dict.append({column_names[i]: cleaned_row[i] for i in range(len(column_names))})
        errors = client.insert_rows_json(table, rows_dict)
        if errors:
            for error in errors:
                index = error["index"]
                logger.error(f"Error inserting row at index {index}: {error['errors']}")
        else:
            logger.info("Data inserted successfully.")
    except Exception as e:
        logger.error(f"Error transferring data to BigQuery: {str(e)}")

def create_bigquery_schema():
    schema = [
        bigquery.SchemaField("E M P C O D E", "STRING"),
        bigquery.SchemaField("N A M E", "STRING"),
        bigquery.SchemaField("S E X", "STRING"),
        bigquery.SchemaField("L E F T D A T E", "DATE"),
        bigquery.SchemaField("C O M M U N I T Y C O D E", "STRING"),
        bigquery.SchemaField("C O M M U N I T Y", "STRING"),
        bigquery.SchemaField("S I T E C O D E", "STRING"),
        bigquery.SchemaField("S I T E", "STRING"),
        bigquery.SchemaField("E S T A B L I S H M E N T C O D E", "STRING"),
        bigquery.SchemaField("E S T A B L I S H M E N T", "STRING"),
        bigquery.SchemaField("C O N T C O D E", "STRING"),
        bigquery.SchemaField("C O N T N A M E", "STRING"),
        bigquery.SchemaField("W O R K _ O R D E R _ N O", "STRING"),
        bigquery.SchemaField("D I V I S I O N C O D E", "STRING"),
        bigquery.SchemaField("D I V I S I O N", "STRING"),
        bigquery.SchemaField("U N I T C O D E", "STRING"),
        bigquery.SchemaField("U N I T", "STRING"),
        bigquery.SchemaField("D E P T C O D E", "STRING"),
        bigquery.SchemaField("D E P A R T M E N T", "STRING"),
        bigquery.SchemaField("C A T C O D E", "STRING"),
        bigquery.SchemaField("C A T E G O R Y", "STRING"),
        bigquery.SchemaField("D E S G C O D E", "STRING"),
        bigquery.SchemaField("D E S I G N A T I O N", "STRING"),
        bigquery.SchemaField("G R A D E C O D E", "STRING"),
        bigquery.SchemaField("G R A D E", "STRING"),
        bigquery.SchemaField("D A T E", "DATE"),
        bigquery.SchemaField("S H I F T C O D E", "STRING"),
        bigquery.SchemaField("I N _ T I M E", "STRING"),
        bigquery.SchemaField("L A T E", "STRING"),
        bigquery.SchemaField("E A R L Y _ C O M E", "STRING"),
        bigquery.SchemaField("O U T _ T I M E 1", "STRING"),
        bigquery.SchemaField("W O R K H R S _ 1", "INTEGER"),
        bigquery.SchemaField("I N _ T I M E 2", "STRING"),
        bigquery.SchemaField("O U T _ T I M E 2", "STRING"),
        bigquery.SchemaField("W O R K H R S _ 2", "INTEGER"),
        bigquery.SchemaField("I N _ T I M E 3", "STRING"),
        bigquery.SchemaField("O U T _ T I M E 3", "STRING"),
        bigquery.SchemaField("W O R K H R S _ 3", "INTEGER"),
        bigquery.SchemaField("I N _ T I M E 4", "STRING"),
        bigquery.SchemaField("O U T _ T I M E 4", "STRING"),
        bigquery.SchemaField("W O R K H R S _ 4", "INTEGER"),
        bigquery.SchemaField("I N _ T I M E 5", "STRING"),
        bigquery.SchemaField("O U T _ T I M E 5", "STRING"),
        bigquery.SchemaField("W O R K H R S _ 5", "INTEGER"),
        bigquery.SchemaField("O U T _ T I M E", "STRING"),
        bigquery.SchemaField("E A R L Y", "STRING"),
        bigquery.SchemaField("W O R K H R S", "INTEGER"),
        bigquery.SchemaField("F I N A L _ W O R K H R S", "INTEGER"),
        bigquery.SchemaField("E X T R A _ T I M E", "INTEGER"),
        bigquery.SchemaField("O V E R _ T I M E", "INTEGER"),
        bigquery.SchemaField("L E A V E", "STRING"),
        bigquery.SchemaField("H A L F _ D A Y", "STRING"),
        bigquery.SchemaField("H A L F _ 1 _ 2", "STRING"),
        bigquery.SchemaField("S T A T U S", "STRING"),
        bigquery.SchemaField("R E M A R K", "STRING"),
        bigquery.SchemaField("R U L E _ A P P L I E D", "STRING"),
        bigquery.SchemaField("W O H L", "STRING"),
        bigquery.SchemaField("P U N C H _ C O U N T E R", "INTEGER"),
        bigquery.SchemaField("I N _ O U T _ C O U N T E R", "INTEGER"),
        bigquery.SchemaField("L A S T _ P U N C H _ S T A T U S", "STRING"),
    ]
    return schema

if __name__ == "__main__":
    server = ""
    database = ""
    username = ""
    password = ""
    project_id = os.environ.get("GCLOUD_PROJECT")
    dataset_id = ''
    table_id = ''
    data, column_names = fetch_data_from_sql_server(server, database, username, password)
    if data and column_names:
        transfer_data_to_bigquery(data, column_names, project_id, dataset_id, table_id)
    else:
        logger.error("No data fetched from SQL Server. Exiting script.")
    logger.info("Script execution completed.")
    

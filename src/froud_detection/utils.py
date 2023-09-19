import os 
import sys
from src.froud_detection.exception import CustomException
from src.froud_detection.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pyodbc


load_dotenv()

server = os.getenv("SERVER")
database = os.getenv("DATABASE")
table_name = os.getenv("TABLE_NAME")


def read_sql_data():
    logging.info("reading sql database started")
    try:
        mydb=conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes')

        logging.info("Connection Established",mydb)
        df=pd.read_sql_query(f"Select * from concrete_data",mydb)
        print(df.head())

        return df




    except Exception as ex:
        raise CustomException(ex)
import os

from dotenv import load_dotenv

load_dotenv('.env')

DATABASE_CREDENTIALS = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME')
}

HOSTNAME = os.getenv('HOSTNAME')

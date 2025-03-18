import os
import json
from dotenv import load_dotenv

current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, 'authorization.json')

with open(config_path, 'r') as file:
    config = json.load(file)

empty_email = config['empty_email']
digits_email = config['digits_email']
digits_email_with_at = config['digits_email_with_at']
digits_email_with_at_com = config['digits_email_with_at_com']
partly_right_email = config['partly_right_email']
empty_password = config['empty_password']
special_symbols_password = config['special_symbols_password']
digits_password = config['digits_password']



load_dotenv()

valid_email = os.getenv("VALID_EMAIL")
valid_password = os.getenv("VALID_PASSWORD")

if not valid_email or not valid_password:
    raise ValueError("Переменные окружения VALID_EMAIL и VALID_PASSWORD не заданы!")
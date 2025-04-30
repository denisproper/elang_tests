from faker import Faker
from env.authorization.json_read import *
from dotenv import load_dotenv


fake = Faker()


load_dotenv()

valid_email = os.getenv("VALID_EMAIL")
valid_password = os.getenv("VALID_PASSWORD")

class AuthorizationData:

    @staticmethod
    def get_valid_email_and_password_data():
        return [valid_email, valid_password]

    @staticmethod
    def get_valid_email_and_wrong_password_data():
        return [valid_email, digits_password]

    @staticmethod
    def get_email_and_short_password_data():
        return [
            (valid_email, special_symbols_password),
            (digits_email, special_symbols_password),
            (digits_email_with_at_com, special_symbols_password),
            (partly_right_email, special_symbols_password),
            (digits_email_with_at, special_symbols_password)
    ]

    @staticmethod
    def get_invalid_email_format_data():
        return [
            (digits_email, digits_password),
            (digits_email, valid_password),
            (digits_email_with_at, digits_password),
            (digits_email_with_at, valid_password)
        ]

    @staticmethod
    def get_data_for_account_not_found_message():
        return [
            (digits_email_with_at_com, valid_password),
            (digits_email_with_at_com, digits_password),
            (partly_right_email, digits_password),
            (partly_right_email, valid_password)
    ]

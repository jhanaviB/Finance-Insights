from plaid.model.products import Products
from dotenv import load_dotenv

import datetime
import os
import time
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.api import plaid_api
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from dotenv import load_dotenv

load_dotenv()

def main(return_json=True, start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.date.today() - datetime.timedelta(days=365)
    if end_date is None:
        end_date = datetime.date.today()
        
    access_token = os.getenv("ACCESS_TOKEN")
    if not access_token:
        raise Exception("ACCESS_TOKEN not set in environment variables.")

    configuration = Configuration(
        host="https://production.plaid.com",
        api_key={
            "clientId": os.getenv("PLAID_CLIENT_ID"),
            "secret": os.getenv("PLAID_SECRET"),
            "user": {
                "client_user_id": "test",
                "phone_number": "+1 732 5226768"
                },
            "client_name": "Personal Finance App",
            "products": ["transactions"],
            "transactions": {
            "days_requested": 730
            },
            "country_codes": ["US"],
            "language": "en"
        }
  
    )
    api_client = ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    request = TransactionsGetRequest(
        access_token=access_token,
        start_date=start_date,
        end_date=end_date,
        options=TransactionsGetRequestOptions(count=365, offset=0)
    )
    time.sleep(2)
    response = client.transactions_get(request)
    transactions = response.transactions

    return [
        {
            "date": t.date,
            "amount": t.amount,
            "name": t.name,
            "category": getattr(getattr(t, "personal_finance_category", None), "primary", None),
            "merchant_name": getattr(t, "merchant_name", None)
        }
        for t in transactions
    ]

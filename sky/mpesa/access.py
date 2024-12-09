import requests
from .credentials import CONSUMER_SECRET, CONSUMER_KEY
import base64
import datetime
import logging


request_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"


def fetch_access_token(url: str, consumer_key: str, consumer_secret: str):
    # convert the keys
    key = f"{consumer_key}:{consumer_secret}".encode('utf-8')

    # convert to the key to base 64 string
    encoded_string = base64.b64encode(key)

    # Convert back to a string from binary string
    key_string = encoded_string.decode("utf-8")

    # Define the headers
    headers = {
        'Authorization': f'Basic {key_string}'
    }

    try:
        # Make the request to the daraja api
        response: object = requests.get(request_url, headers=headers)

        # extract the data 
        data: dict = response.json()
            
    except Exception as e:
        logging.error(e)
        access_token: str = data.get("access_token")
        logging.debug(access_token)

    return access_token


def start_payment():
    """Initiates payment to the client"""

    url: str = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    short_code: int = 174379
    current_time: str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    pass_key: str = fetch_access_token()

    password: str = base64.b64encode(f"{short_code}+{pass_key}+{current_time}".encode('utf-8')).decode('utf-8')

    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {fetch_access_token()}"
    }

    request_body: dict = {
        "BusinessShortCode": 174379,    
        "Password": password,    
        "Timestamp":f"{current_time}",    
        "TransactionType": "CustomerPayBillOnline",    
        "Amount": 1,    
        "PartyA": 254703830062,    
        "PartyB": 174379,    
        "PhoneNumber":254703830062,    
        "CallBackURL": "https://mydomain.com/pat",    
        "AccountReference":"Test",    
        "TransactionDesc":"Test"
        }
    
    try:
        response = requests.post(url, headers=headers, data=request_body)

        data = response.json()

        logging.debug(data)

    except Exception as error:
        logging.error(error)



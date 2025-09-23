from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

load_dotenv("backend/.env")

PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create_link_token")
async def create_link_token(request: Request):
    try:
        if request.headers.get("content-type") == "application/json":
            body = await request.json()
        else:
            body = {}
    except:
        body = {}
    
    url = f"https://production.plaid.com/link/token/create"
    print("CLIENT_ID:", PLAID_CLIENT_ID)
    print("SECRET:", PLAID_SECRET)
    
    payload = {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "user": {"client_user_id": body.get("client_user_id", "default-user")},
        "client_name": body.get("client_name", "Transaction Insights"),
        "products": body.get("products", ["transactions"]),
        "country_codes": body.get("country_codes", ["US"]),
        "language": body.get("language", "en")
    }
    response = requests.post(url, json=payload)
    print(response.json())
    return response.json()

@app.post("/exchange_public_token")
async def exchange_public_token(request: Request):
    data = await request.json()
    public_token = data.get("public_token")
    url = f"https://production.plaid.com/item/public_token/exchange"
    payload = {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "public_token": public_token
    }
    response = requests.post(url, json=payload)
    return response.json()

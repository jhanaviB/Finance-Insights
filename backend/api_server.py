from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.GetData import main as get_transactions
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.mount("/.well-known", StaticFiles(directory="../.well-known"), name="well-known")

@app.get("/transactions")
def transactions(year: int = Query(None)):
        if year:
            start_date = f"{year}-01-01"
            end_date=f"{year}-12-31"
            return get_transactions(start_date = start_date,end_date=end_date)
        else:
              return get_transactions()

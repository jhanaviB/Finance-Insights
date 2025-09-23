#!/bin/bash

echo "Starting Transaction Insights servers..."

echo "Starting Plaid Link server on port 8000..."
uvicorn api_server_link:app --host 0.0.0.0 --port 8000 &
LINK_PID=$!

echo "Starting Transaction API server on port 8080..."
uvicorn backend.api_server:app --host 0.0.0.0 --port 8080 &
API_PID=$!

echo "Servers started!"
echo "- Plaid Link: http://localhost:8000"
echo "- Transaction API: http://localhost:8080/transactions"
echo "- Open plaid_link.html in your browser to connect your bank account"
echo ""
echo "Press Ctrl+C to stop all servers"

trap "echo 'Stopping servers...'; kill $LINK_PID $API_PID; exit" INT
wait
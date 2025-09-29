# Transaction Insights 💰

>  **Work In Progress** - Currently supports Venmo transactions only

An AI-powered financial transaction analysis platform that connects to your bank accounts via Plaid and provides intelligent spending insights through a REST API.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-latest-green.svg)](https://fastapi.tiangolo.com)
[![Plaid](https://img.shields.io/badge/Plaid-API-orange.svg)](https://plaid.com)
[![Status](https://img.shields.io/badge/Status-WIP-yellow.svg)]()

## 🚧 Current Status

**This project is actively under development**

 **What's Working**:
- Plaid integration with Venmo accounts
- Basic transaction data retrieval from Venmo
- RESTful API endpoints
- AI plugin discovery mechanism

 **Limitations**:
- OAuth production access required for other accounts
- Single account connection
- Basic transaction display only

## Features (Current)

- **🤖 AI Plugin Ready**: MCP-compatible API for AI assistants
- **📈 Basic Filtering**: Year-based transaction filtering
- **🔒 Secure**: Production-ready Plaid integration

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Bank Integration**: Plaid API
- **Frontend**: HTML/JavaScript (basic)
- **Environment**: Python virtual environment
- **Server**: Uvicorn ASGI

## Quick Start

### Prerequisites
- Python 3.8+
- Plaid Developer Account (Sandbox mode)
- **Active Venmo account** for testing

### 1. Setup
```bash
git clone https://github.com/jhanaviB/vigilant-parakeet.git
cd vigilant-parakeet
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install fastapi uvicorn plaid-python python-dotenv requests
```

### 2. Environment Configuration
Create `backend/.env`:
```env
PLAID_CLIENT_ID=your_plaid_client_id
PLAID_SECRET=your_plaid_sandbox_secret
ACCESS_TOKEN=your_venmo_access_token
```

### 3. Start Development Servers
```bash
# Start both servers
chmod +x start_servers.sh
./start_servers.sh

# Or manually:
uvicorn api_server_link:app --host 0.0.0.0 --port 8000 &
uvicorn backend.api_server:app --host 0.0.0.0 --port 8080 &
```

### 4. Connect Your Venmo Account
1. Open `plaid_link.html` in browser
2. Click "Open Plaid Link"
3. **Select Venmo** from the institution list
4. Enter your Venmo credentials
5. Access token auto-saves to `.env`

### 5. View Your Venmo Data
- **All transactions**: `http://localhost:8080/transactions`
- **Specific year**: `http://localhost:8080/transactions?year=2024`
- **Plugin info**: `http://localhost:8080/.well-known/ai-plugin.json`

## 🔌 API Endpoints

### Transaction API (Port 8080)
```
GET /transactions              # All Venmo transactions
GET /transactions?year=2024    # Venmo transactions for specific year
```

### Plaid Link API (Port 8000)
```
POST /create_link_token        # Create Plaid Link token
POST /exchange_public_token    # Exchange token for Venmo access
```

## 🤖 AI Integration

Works as an MCP-compatible resource:

**Example AI queries**:
- *"Show me my Venmo spending from last month"*
- *"What did I pay for on Venmo yesterday?"*
- *"Analyze my Venmo payment patterns"*


## 📝 License

MIT License - see [LICENSE](LICENSE) file

## Contact

- **GitHub**: [@jhanaviB](https://github.com/jhanaviB)
- **Email**: jhanavibehl@gmail.com




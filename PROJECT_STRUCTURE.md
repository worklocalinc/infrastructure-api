# Project Structure Documentation

This document outlines the complete structure of the Infrastructure Management API.

## Directory Structure

```
infrastructure-api/
├── main.py                    # Main FastAPI application
├── unified_router.py          # Unified operations across all services
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker container configuration
├── docker-compose.yml         # Docker Compose setup
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
├── LICENSE                   # MIT License
├── README.md                 # Project documentation
│
├── cloudflare/               # CloudFlare DNS management
│   ├── __init__.py
│   └── cloudflare_router.py  # CloudFlare API endpoints
│
├── google-cloud/             # Google Cloud Platform management
│   ├── __init__.py
│   └── google_cloud_router.py # GCP API endpoints
│
├── namesilo/                 # Namesilo domain management
│   ├── __init__.py
│   └── namesilo_router.py    # Namesilo API endpoints
│
├── godaddy/                  # GoDaddy domain management
│   ├── __init__.py
│   └── godaddy_router.py     # GoDaddy API endpoints
│
├── github/                   # GitHub integration
│   ├── __init__.py
│   └── github_router.py      # GitHub API endpoints
│
├── common/                   # Shared utilities
│   ├── __init__.py
│   ├── auth.py              # API key authentication
│   └── models.py            # Pydantic models
│
└── openwebui/               # OpenWebUI integration
    └── openwebui_tools.py   # Helper functions for AI agents
```

## Module Descriptions

### Main Application (`main.py`)
- FastAPI application setup
- CORS configuration
- Route registration
- Health check endpoints

### Unified Router (`unified_router.py`)
- Cross-service operations
- Domain search across all providers
- Quick DNS updates
- Service status checks

### Service Modules

#### CloudFlare (`cloudflare/`)
- Zone management
- DNS record CRUD operations
- Quick DNS updates

#### Google Cloud (`google-cloud/`)
- GCloud command execution
- Compute instance management
- Storage bucket operations
- Snapshot creation

#### Namesilo (`namesilo/`)
- Domain listing
- DNS record management
- Domain information retrieval

#### GoDaddy (`godaddy/`)
- Domain management
- DNS record operations
- Bulk DNS updates

#### GitHub (`github/`)
- Repository management
- Issue and PR creation
- Branch operations
- File content management

### Common Utilities (`common/`)
- **auth.py**: Bearer token authentication
- **models.py**: Shared Pydantic models for requests/responses

### OpenWebUI Integration (`openwebui/`)
- Python client for AI agents
- Simplified API wrappers
- Tool definitions for OpenWebUI

## API Authentication

All endpoints require Bearer token authentication:
```
Authorization: Bearer YOUR_API_KEY
```

API keys are configured in the environment variable `API_KEYS` as a comma-separated list.

## Environment Variables

See `.env.example` for all required configuration variables:
- Service API credentials (CloudFlare, Namesilo, GoDaddy, GitHub)
- Google Cloud configuration
- API security keys
- Server configuration

## Deployment

The API is designed to run on:
- Local development (Python/uvicorn)
- Docker containers
- Google Cloud Run
- Any ASGI-compatible server

## Live Instance

The production API is available at:
- Base URL: https://tools.worklocal.studio/
- Documentation: https://tools.worklocal.studio/docs
- Health Check: https://tools.worklocal.studio/health

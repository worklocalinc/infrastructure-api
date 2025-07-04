# main.py - Main Infrastructure Management API Server
import os
import sys
from pathlib import Path

# Add subdirectories to Python path
current_dir = Path(__file__).parent
sys.path.extend([
    str(current_dir / "cloudflare"),
    str(current_dir / "google-cloud"),
    str(current_dir / "namesilo"),
    str(current_dir / "godaddy"),
    str(current_dir / "common"),
])

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Import routers from each service
from cloudflare_router import router as cloudflare_router
from google_cloud_router import router as gcp_router
from namesilo_router import router as namesilo_router
from godaddy_router import router as godaddy_router
from unified_router import router as unified_router

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Infrastructure Management API",
    description="Unified API for managing CloudFlare DNS, Google Cloud, Namesilo, and GoDaddy",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(cloudflare_router, prefix="/cloudflare", tags=["CloudFlare"])
app.include_router(gcp_router, prefix="/gcp", tags=["Google Cloud"])
app.include_router(namesilo_router, prefix="/namesilo", tags=["Namesilo"])
app.include_router(godaddy_router, prefix="/godaddy", tags=["GoDaddy"])
app.include_router(unified_router, prefix="/unified", tags=["Unified Operations"])

@app.get("/")
def read_root():
    return {
        "message": "Infrastructure Management API",
        "version": "1.0.0",
        "documentation": "/docs",
        "services": {
            "cloudflare": {
                "status": "active" if os.getenv("CLOUDFLARE_API_TOKEN") else "not configured",
                "endpoints": "/cloudflare"
            },
            "google_cloud": {
                "status": "active" if os.getenv("GOOGLE_PROJECT_ID") else "not configured",
                "endpoints": "/gcp"
            },
            "namesilo": {
                "status": "active" if os.getenv("NAMESILO_API_KEY") else "not configured",
                "endpoints": "/namesilo"
            },
            "godaddy": {
                "status": "active" if os.getenv("GODADDY_API_KEY") else "not configured",
                "endpoints": "/godaddy"
            }
        }
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "services": {
            "cloudflare": bool(os.getenv("CLOUDFLARE_API_TOKEN")),
            "google_cloud": bool(os.getenv("GOOGLE_PROJECT_ID")),
            "namesilo": bool(os.getenv("NAMESILO_API_KEY")),
            "godaddy": bool(os.getenv("GODADDY_API_KEY"))
        }
    }

if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    debug = os.getenv("DEBUG_MODE", "true").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug
    )

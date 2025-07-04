# Infrastructure Management API

A unified API for managing CloudFlare DNS, Google Cloud Platform, Namesilo, and GoDaddy services. Designed for integration with OpenWebUI and AI agents.

## 🚀 Live Demo

- **API Endpoint**: https://tools.worklocal.studio/
- **Documentation**: https://tools.worklocal.studio/docs
- **Health Check**: https://tools.worklocal.studio/health

## 📋 Features

- **Multi-Provider DNS Management**: CloudFlare, Namesilo, GoDaddy
- **Google Cloud Integration**: Execute commands, manage instances
- **GitHub Integration**: Manage repositories, issues, pull requests
- **Unified Search**: Search DNS records across all providers
- **API Key Authentication**: Secure access control
- **OpenWebUI Ready**: Built for AI agent integration

## 🛠️ Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/worklocalinc/infrastructure-api.git
cd infrastructure-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API credentials

# Run the server
python main.py
```

### Docker Deployment

```bash
# Using Docker
docker build -t infrastructure-api .
docker run -d -p 8000:8000 --env-file .env infrastructure-api

# Using Docker Compose
docker-compose up -d
```

## 🔑 API Authentication

All API endpoints require authentication using Bearer tokens:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://tools.worklocal.studio/health
```

## 📚 Documentation

Full API documentation is available at:
- **Swagger UI**: https://tools.worklocal.studio/docs
- **ReDoc**: https://tools.worklocal.studio/redoc

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Deployed on [Google Cloud Run](https://cloud.google.com/run)
- DNS managed by [CloudFlare](https://www.cloudflare.com/)

# Deployment Guide

This guide covers deploying the Infrastructure Management API to Google Cloud Run.

## Prerequisites

- Google Cloud Project with billing enabled
- `gcloud` CLI installed and authenticated
- Docker installed (optional, for local testing)
- CloudFlare account (for DNS management)

## Deployment Steps

### 1. Clone the Repository

```bash
git clone https://github.com/worklocalinc/infrastructure-api.git
cd infrastructure-api
```

### 2. Set Up Environment Variables

Create your `.env` file with your actual credentials:

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Deploy to Cloud Run

#### Option A: Deploy from Source (Recommended)

```bash
# Deploy directly from source
gcloud run deploy infrastructure-api \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars="$(cat .env | grep -v '^#' | grep -v '^$' | tr '\n' ',')"
```

#### Option B: Build and Deploy Container

```bash
# Build container
docker build -t gcr.io/YOUR_PROJECT_ID/infrastructure-api .

# Push to Container Registry
docker push gcr.io/YOUR_PROJECT_ID/infrastructure-api

# Deploy
gcloud run deploy infrastructure-api \
  --image gcr.io/YOUR_PROJECT_ID/infrastructure-api \
  --region us-central1 \
  --allow-unauthenticated
```

### 4. Set Up Secrets (Production)

For production, use Google Secret Manager:

```bash
# Create secret
gcloud secrets create api-env --data-file=.env

# Grant access
gcloud secrets add-iam-policy-binding api-env \
  --member="serviceAccount:YOUR-SERVICE-ACCOUNT@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"

# Update Cloud Run to use secret
gcloud run services update infrastructure-api \
  --region us-central1 \
  --update-secrets="/secrets/.env=api-env:latest"
```

### 5. Set Up Custom Domain

#### Using API Gateway (Bypasses org restrictions)

```bash
# Enable API Gateway
gcloud services enable apigateway.googleapis.com

# Create API
gcloud api-gateway apis create infrastructure-api

# Create API config (use provided openapi-spec.yaml)
gcloud api-gateway api-configs create v1 \
  --api=infrastructure-api \
  --openapi-spec=openapi-spec.yaml

# Create gateway
gcloud api-gateway gateways create main-gateway \
  --api=infrastructure-api \
  --api-config=v1 \
  --location=us-central1
```

#### Update DNS

In CloudFlare:
1. Add CNAME record: `tools` → `your-gateway-url.gateway.dev`
2. Enable proxy (orange cloud)

### 6. Verify Deployment

```bash
# Check health
curl https://your-service-url.run.app/health

# Or with custom domain
curl https://tools.yourdomain.com/health
```

## Environment Variables

Required environment variables:

```env
# CloudFlare
CLOUDFLARE_API_TOKEN=your_token
CLOUDFLARE_EMAIL=your_email

# Namesilo
NAMESILO_API_KEY=your_key

# GoDaddy
GODADDY_API_KEY=your_key
GODADDY_API_SECRET=your_secret

# GitHub
GITHUB_TOKEN=your_token

# Google Cloud
GOOGLE_PROJECT_ID=your-project-id

# API Security
API_KEYS=key1,key2,key3

# Server Config
API_PORT=8080
```

## Troubleshooting

### Organization Policy Blocks Public Access

Use API Gateway to bypass restrictions (see step 5).

### Missing Environment Variables

Check Cloud Run logs:
```bash
gcloud run logs read infrastructure-api --region us-central1
```

### DNS Not Resolving

- Verify CNAME record in CloudFlare
- Check DNS propagation: `nslookup tools.yourdomain.com`
- Clear browser cache

## Monitoring

View metrics and logs:
```bash
# Logs
gcloud run logs read infrastructure-api --region us-central1

# Metrics
gcloud monitoring metrics list --filter="resource.type=cloud_run_revision"
```

## Cost Optimization

- Cloud Run scales to zero when not in use
- API Gateway has minimal cost for low traffic
- Use Cloud Scheduler for keep-alive if needed

## Security Best Practices

1. Use Secret Manager for production
2. Enable Cloud Armor for DDoS protection
3. Rotate API keys regularly
4. Set up monitoring alerts
5. Use least-privilege service accounts

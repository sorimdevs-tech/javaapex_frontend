# Vercel Deployment Guide - Java Migration Accelerator

## **Step 1: Prepare Your GitHub Repository**

1. Go to https://github.com/sorimdevs-tech/javaapex_frontend (or your frontend repo)
2. Make sure all code is committed and pushed

## **Step 2: Deploy Frontend to Vercel (Free)**

### Option A: Using Vercel CLI (Recommended)

```powershell
# Install Vercel CLI globally
npm install -g vercel

# Navigate to project root
cd 'C:\Users\PULIMURUGAN T\Downloads\java-migration-accelerator-clean-main\java-migration-accelerator-clean-main'

# Deploy to Vercel
vercel

# Follow the prompts:
# - Link to existing project? No
# - Project name: java-migration-accelerator
# - Framework: Other
# - Root directory: java-migration-frontend
# - Build command: npm run build
# - Output directory: dist
```

### Option B: Using Vercel Web Dashboard

1. Go to https://vercel.com/login
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository: `https://github.com/sorimdevs-tech/javaapex_frontend`
4. Configure:
   - **Framework**: Other (Vite)
   - **Root Directory**: `java-migration-frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Click **"Deploy"**

## **Step 3: Configure Environment Variables in Vercel**

1. Go to your Vercel project dashboard
2. Click **Settings** → **Environment Variables**
3. Add this variable:

```
VITE_API_URL = https://your-backend-url.onrender.com
```

(Replace with your actual backend URL once deployed)

## **Step 4: Deploy Backend (Optional - If Needed)**

For backend, use **Render** free tier:
- Go to https://render.com
- Create new Web Service
- Connect GitHub repo: `https://github.com/sorimdevs-tech/javaapex_backend`
- Configure runtime and environment variables

## **Step 5: Update API Routes**

Update `vercel.json` with your backend URL once deployed:

```json
"rewrites": [
  {
    "source": "/api/(.*)",
    "destination": "https://your-backend-url.onrender.com/api/$1"
  }
]
```

## **Your Vercel URL**

Once deployed, your app will be live at:
```
https://java-migration-accelerator.vercel.app
```

## **Free Tier Limitations**

✅ Included:
- 100 GB bandwidth/month
- Unlimited deployments
- Auto-scaling
- SSL certificate
- Custom domains (up to 3)

## **Troubleshooting**

### Build Fails
- Check `package.json` build command
- Ensure Node version 18+ is set in vercel.json
- Verify all dependencies are in package.json (not just package-lock.json)

### API Not Working
- Verify backend URL in environment variables
- Check CORS settings on backend
- Test API endpoint directly in browser

### Port Issues
- Vercel uses port 3000 by default (don't worry, it's handled automatically)
- Local development still uses 5173/5174

## **Next Steps**

1. Deploy frontend to Vercel (this guide)
2. Deploy backend to Render
3. Connect frontend to backend via environment variables
4. Test the full application
5. Custom domain (optional)

---

**Need Help?** Contact support or check Vercel docs: https://vercel.com/docs

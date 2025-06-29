# Deploying Noa to Vercel

This guide will help you deploy your Noa social media automation platform to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: Your code should be in a GitHub repository
3. **Supabase Setup** (Optional): For production database

## Step 1: Prepare Your Repository

Make sure your repository contains these files:
- `app.py` - Main Flask application
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `config.py` - Configuration settings
- `supabase_service.py` - Supabase integration
- `templates/` - HTML templates
- `static/` - CSS, JS, and images

## Step 2: Environment Variables Setup

### For Supabase (Recommended for Production)

1. Go to your Supabase project dashboard
2. Get your project URL and anon key
3. In Vercel, add these environment variables:
   - `SUPABASE_URL` = Your Supabase project URL
   - `SUPABASE_KEY` = Your Supabase anon key
   - `SECRET_KEY` = A random secret key for Flask sessions

### For Local Development Only

If you want to use SQLite locally but Supabase in production:
- Set `USE_SUPABASE=true` in Vercel environment variables
- Keep `USE_SUPABASE=false` in your local `.env` file

## Step 3: Deploy to Vercel

### Option A: Deploy via Vercel Dashboard

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Import your GitHub repository
4. Configure environment variables (see Step 2)
5. Click "Deploy"

### Option B: Deploy via Vercel CLI

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy from your project directory:
   ```bash
   vercel
   ```

4. Follow the prompts to configure your project

## Step 4: Configure Custom Domain (Optional)

1. In your Vercel dashboard, go to your project
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Configure DNS settings as instructed

## Step 5: Verify Deployment

1. Visit your deployed URL
2. Test the email subscription form
3. Test the contact form
4. Check the admin dashboard at `/admin`

## Important Notes

### Database Considerations

- **SQLite**: Not recommended for production on Vercel (serverless functions don't persist data)
- **Supabase**: Recommended for production (data persists and scales)
- **Admin Dashboard**: Access via `/admin` to view submissions

### Environment Variables

Make sure to set these in Vercel:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SECRET_KEY=your-secret-key
USE_SUPABASE=true
```

### File Structure

Your project should look like this:
```
├── app.py
├── config.py
├── supabase_service.py
├── vercel.json
├── requirements.txt
├── runtime.txt
├── .gitignore
├── templates/
│   ├── index.html
│   ├── features.html
│   ├── pricing.html
│   ├── about.html
│   ├── contact.html
│   ├── admin.html
│   ├── 404.html
│   └── 500.html
└── static/
    ├── css/
    ├── js/
    └── images/
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are in `requirements.txt`
2. **Database Errors**: Ensure Supabase credentials are correct
3. **Static Files Not Loading**: Check that all files are in the `static/` directory
4. **Environment Variables**: Verify all required variables are set in Vercel

### Support

If you encounter issues:
1. Check Vercel deployment logs
2. Verify environment variables
3. Test locally first
4. Check Supabase connection

## Post-Deployment

After successful deployment:

1. **Test all functionality**:
   - Email subscription forms
   - Contact forms
   - Admin dashboard
   - All pages load correctly

2. **Monitor performance**:
   - Check Vercel analytics
   - Monitor Supabase usage
   - Set up error tracking if needed

3. **SEO Setup**:
   - Update meta tags with your domain
   - Set up Google Analytics
   - Configure social media meta tags

Your Noa platform is now live on Vercel! 🚀 
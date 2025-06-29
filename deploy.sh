#!/bin/bash

# Noa Vercel Deployment Script

echo "🚀 Preparing Noa for Vercel deployment..."

# Check if required files exist
echo "📋 Checking required files..."

required_files=("app.py" "vercel.json" "requirements.txt" "runtime.txt" "config.py" "supabase_service.py")

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file missing!"
        exit 1
    fi
done

# Check if templates and static directories exist
if [ -d "templates" ]; then
    echo "✅ templates/ directory exists"
else
    echo "❌ templates/ directory missing!"
    exit 1
fi

if [ -d "static" ]; then
    echo "✅ static/ directory exists"
else
    echo "❌ static/ directory missing!"
    exit 1
fi

echo ""
echo "🎉 All files are ready for deployment!"
echo ""
echo "📝 Next steps:"
echo "1. Push your code to GitHub"
echo "2. Go to vercel.com and create a new project"
echo "3. Import your GitHub repository"
echo "4. Set environment variables:"
echo "   - SUPABASE_URL"
echo "   - SUPABASE_KEY" 
echo "   - SECRET_KEY"
echo "   - USE_SUPABASE=true"
echo "5. Deploy!"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions" 
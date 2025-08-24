#!/bin/bash

# Portfolio Setup Script

echo "🚀 Setting up Pratik Ingale Portfolio..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To start the portfolio:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run the application: python app.py"
echo "3. Visit http://127.0.0.1:5000 in your browser"
echo ""
echo "📝 Remember to add your images to static/images/ folder:"
echo "  - profile_pic.png (your profile picture)"
echo "  - cicd_project.png (project screenshot)"
echo "  - k8s_monitoring.png (project screenshot)"

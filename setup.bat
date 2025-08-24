@echo off

echo 🚀 Setting up Pratik Ingale Portfolio...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python first.
    pause
    exit /b 1
)

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

echo ✅ Setup complete!
echo.
echo To start the portfolio:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Run the application: python app.py
echo 3. Visit http://127.0.0.1:5000 in your browser
echo.
echo 📝 Remember to add your images to static/images/ folder:
echo   - profile_pic.png (your profile picture)
echo   - cicd_project.png (project screenshot)
echo   - k8s_monitoring.png (project screenshot)
pause

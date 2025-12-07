@echo off
echo ========================================
echo SOVEREIGN INTERFACE - LAUNCHER
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    echo Please install Python 3.14 or add it to PATH
    pause
    exit /b 1
)

REM Check if dependencies are installed
echo Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Starting backend server...
start "Sovereign Interface Backend" python server.py

REM Wait for server to start
timeout /t 3 /nobreak >nul

echo Opening dashboard...
start "" "wallpaper_1.html"

echo.
echo ========================================
echo Dashboard launched successfully!
echo Backend: http://localhost:5000
echo ========================================
echo.
echo Press any key to stop the backend server...
pause >nul

REM Kill the Python server when user presses a key
taskkill /FI "WindowTitle eq Sovereign Interface Backend*" /T /F >nul 2>&1
echo Backend stopped.

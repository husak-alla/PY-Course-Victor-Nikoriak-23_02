@echo off

echo.
echo ============================================
echo   Python Course -- Environment Setup
echo ============================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo.
    echo Download Python 3.10+ from: https://python.org
    echo During install: check "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [1/5] Python found:
python --version
echo.

:: Create .venv
if exist .venv\ (
    echo [2/5] .venv already exists, skipping...
) else (
    echo [2/5] Creating virtual environment .venv ...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Could not create .venv
        pause
        exit /b 1
    )
    echo        OK
)
echo.

:: Install packages
echo [3/5] Installing packages (2-3 min) ...
.venv\Scripts\pip.exe install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Package installation failed
    pause
    exit /b 1
)
echo        OK
echo.

:: Register nbextensions
echo [4/5] Setting up Jupyter extensions ...
.venv\Scripts\jupyter.exe contrib nbextension install --user >nul 2>&1
.venv\Scripts\jupyter.exe nbextension enable hide_input/main           >nul 2>&1
.venv\Scripts\jupyter.exe nbextension enable collapsible_headings/main >nul 2>&1
.venv\Scripts\jupyter.exe nbextension enable codefolding/main          >nul 2>&1
echo        OK
echo.

:: Register kernel
echo [5/5] Registering Python kernel ...
.venv\Scripts\python.exe -m ipykernel install --user --name python-course --display-name "Python Course" >nul 2>&1
echo        OK
echo.

echo ============================================
echo   Done! Run start_course.bat to begin.
echo ============================================
echo.
pause

@echo off
chcp 65001 >nul

if not exist .venv\ (
    echo [ПОМИЛКА] Середовище не знайдено.
    echo Спочатку запустіть install_course.bat
    echo.
    pause
    exit /b 1
)

echo Запуск Jupyter Notebook...
.venv\Scripts\jupyter.exe notebook

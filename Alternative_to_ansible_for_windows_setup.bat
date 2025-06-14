@echo off
echo ----------------------------
echo Setting up Azul Environment
echo ----------------------------

:: Create virtual environment
python -m venv venv

:: Activate and install requirements
echo Installing dependencies...
call venv\Scripts\activate
venv\Scripts\pip install --upgrade pip
venv\Scripts\pip install -r requirements.txt
venv\Scripts\pip install flake8 pytest

:: Optional: install ansible (will not work without WSL)
:: venv\Scripts\pip install ansible

echo ----------------------------
echo Setup complete!
echo ----------------------------

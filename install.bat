@echo off
echo Installing AI Learn Platform...
echo.

REM Upgrade pip first
python -m pip install --upgrade pip

REM Install packages one by one to avoid build issues
echo Installing Streamlit...
pip install streamlit>=1.28.0

echo Installing Streamlit Option Menu...
pip install streamlit-option-menu>=0.3.6

echo Installing Plotly...
pip install plotly>=5.17.0

echo Installing Pandas (pre-built wheel)...
pip install pandas>=2.0.0

echo Installing Python Dotenv...
pip install python-dotenv>=1.0.0

echo Installing ReportLab...
pip install reportlab>=4.0.0

echo Installing QRCode with Pillow...
pip install qrcode[pil]>=7.4.0

echo Installing Pillow...
pip install Pillow>=10.0.0

echo Installing Requests...
pip install requests>=2.31.0

echo.
echo Installation complete!
echo.
echo To run the application, type: streamlit run app.py
pause

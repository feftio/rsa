call .env/Scripts/activate.bat
pip install -r requirements.txt
pyinstaller -F generator.py
pyinstaller -F encryptor.py
pyinstaller -F decryptor.py
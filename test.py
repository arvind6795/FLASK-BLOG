import os

from dotenv import load_dotenv

load_dotenv()
print("MAIL_USER:", os.environ.get("MAIL_USER"))
print("MAIL_PASS:", os.environ.get("MAIL_PASS"))  # Avoid printing passwords in real applications!


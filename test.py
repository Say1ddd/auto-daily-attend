import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('CLIENT_SECRETS_JSON'))
print(os.getenv('TOKEN_JSON'))

from google_auth_oauthlib.flow import InstalledAppFlow
import os
import json

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def main():
    try:
        if not os.path.exists(CLIENT_SECRETS_FILE):
            raise FileNotFoundError(f"{CLIENT_SECRETS_FILE} not found. Please ensure the file exists.")

        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)

        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

        print("Authentication successful, token saved to token.json.")

    except FileNotFoundError as fnf_error:
        print(f"File not found error: {fnf_error}")
    except json.JSONDecodeError as json_error:
        print(f"JSON error: {json_error}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

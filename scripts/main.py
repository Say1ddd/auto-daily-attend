import gspread
from google.oauth2.credentials import Credentials
from datetime import datetime
import os
from dotenv import load_dotenv
import json
import sys

load_dotenv()

days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
months = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

def log_error(error_message):
    log_file = "README.md"
    with open(log_file, "a") as f:
        f.write(f"\n### {datetime.now()}\n")
        f.write(f"```\n{error_message}\n```\n")

def get_credentials():
    try:
        json.loads(os.getenv('CLIENT_SECRETS_JSON'))
        token_json = json.loads(os.getenv('TOKEN_JSON'))

        creds = Credentials.from_authorized_user_info(token_json)
        return creds
    except Exception as e:
        error_message = f"Error getting credentials: {e}"
        log_error(error_message)
        raise

def main():
    try:
        today = datetime.now()

        if today.weekday() >= 5:
            print("It's weekend. Data will not be sent to the sheet.")
            return

        creds = get_credentials()
        client = gspread.authorize(creds)

        sheet_url = os.getenv("SHEET_URL")
        spreadsheet = client.open_by_url(sheet_url)

        sheet_name = os.getenv("SHEET_NAME")
        sheet = spreadsheet.worksheet(sheet_name)

        day_name = days[today.weekday()]
        month_name = months[today.month - 1]
        date_string = f"{today.day} {month_name} {today.year}"
        date_time = f"{day_name}, {date_string}"

        next_no = len(sheet.get_all_values()) + 1

        jam_masuk = "08:45"
        jam_selesai = "17:00"
        keterangan = "Hadir"
        sheet.append_row([next_no, date_time, jam_masuk, jam_selesai, keterangan])
        print(f"Data sent successfully.")

    except gspread.exceptions.APIError as e:
        error_message = f"Google Sheets API error: {e}"
        log_error(error_message)
        print(error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        log_error(error_message)
        print(error_message)
        sys.exit(1)

if __name__ == "__main__":
    main()

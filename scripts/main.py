import gspread
from google.oauth2.credentials import Credentials
from datetime import datetime
import os
from dotenv import load_dotenv
import json

load_dotenv()

days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
months = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]


def get_credentials():
    try:
        json.loads(os.getenv('CLIENT_SECRETS_JSON'))
        token_json = json.loads(os.getenv('TOKEN_JSON'))

        creds = Credentials.from_authorized_user_info(token_json)
        return creds
    except Exception as e:
        print(f"Error getting credentials: {e}")
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
        print(f"Google Sheets API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

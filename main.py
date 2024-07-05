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
    json.loads(os.getenv('CLIENT_SECRETS_JSON'))
    token = json.loads(os.getenv('TOKEN_JSON'))
    creds = Credentials.from_authorized_user_info(token)
    return creds


def main():
    creds = get_credentials()
    client = gspread.authorize(creds)

    sheet_url = os.getenv("SHEET_URL")
    sheet = client.open_by_url(sheet_url).sheet1

    today = datetime.now()
    day_name = days[today.weekday()]
    month_name = months[today.month - 1]
    date_string = f"{today.day} {month_name} {today.year}"
    date_time = f"{day_name}, {date_string}"

    next_no = len(sheet.get_all_values()) + 1

    jam_masuk = "08:00"
    jam_selesai = "17:00"
    keterangan = "Hadir"
    sheet.append_row([next_no, date_time, jam_masuk, jam_selesai, keterangan])


if __name__ == "__main__":
    main()

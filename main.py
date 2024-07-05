import gspread
from google.oauth2.credentials import Credentials
from datetime import datetime
import os
import json
import locale

locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')


def get_credentials():
    client_secrets = json.loads(os.environ['CLIENT_SECRETS_JSON'])
    token = json.loads(os.environ['TOKEN_JSON'])
    creds = Credentials.from_authorized_user_info(token)
    return creds


def main():
    creds = get_credentials()
    client = gspread.authorize(creds)

    sheet_url = os.environ["SHEET_URL"]
    sheet = client.open_by_url(sheet_url).sheet1

    today = datetime.now()
    day_name = today.strftime("%A")
    date_string = today.strftime("%d %B %Y")
    date_time = f"{day_name}, {date_string}"

    next_no = len(sheet.get_all_values())

    jam_masuk = "08:00"
    jam_selesai = "17:00"
    keterangan = "Hadir"
    sheet.append_row([next_no, date_time, jam_masuk, jam_selesai, keterangan])


if __name__ == "__main__":
    main()

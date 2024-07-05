import gspread
from google.oauth2.credentials import Credentials
from datetime import datetime
import os
from dotenv import load_dotenv
import json

load_dotenv()


def get_credentials():
    json.loads(os.getenv('CLIENT_SECRETS_JSON'))

    token = json.loads(os.getenv('TOKEN_JSON'))

    creds = Credentials.from_authorized_user_info(token)
    return creds


def main():
    creds = get_credentials()
    client = gspread.authorize(creds)

    sheet_url = 'https://docs.google.com/spreadsheets/d/1vlR8f60iC7501m63uykecz_hhWb82WATdndR8Qjtkk8/edit#gid=0'
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

# Auto Daily Attendance

This repository contains a Python script that automates the process of recording daily attendance into a Google Spreadsheet. The script uses Google Sheets API for accessing and updating the sheet. A GitHub Actions workflow is set up to run the script every day at 2 AM UTC.

## Prerequisites

- Python 3.x
- Google Cloud Platform (GCP) account
- Google Sheets API enabled

## Getting Started

### 1. Obtain Google Sheets API Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the Google Sheets API for your project.
4. Create OAuth 2.0 credentials:
    - Go to the **APIs & Services > Credentials** page.
    - Click on **Create Credentials** and select **OAuth 2.0 Client IDs**.
    - Configure the consent screen if prompted.
    - Create a Desktop or Web application type OAuth 2.0 client ID.
    - Download the `client_secret.json` file.

### 2. Generate a Refresh Token

1. Install the required Python libraries:
    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2
    ```

2. Use the `get_refresh_token.py` script to generate the refresh token

3. Run the script:
    ```bash
    python scripts/get_refresh_token.py
    ```

4. Save the contents of `client_secret.json` and `token.json`.

### 3. Add Secrets to GitHub

1. Navigate to your GitHub repository.
2. Go to repository **Settings > Secrets & Variables**.
3. Add the following secrets:
    - `CLIENT_SECRETS_JSON`: The content of your `client_secret.json`.
    - `TOKEN_JSON`: The content of your `token.json`.
    - `SHEET_URL`: The URL of your Google Spreadsheet.
    - `SHEET_NAME`: The sheet name of your Google Spreadsheet.

### 4. Create GitHub Actions Workflow

Create a `.github/workflows/attendance.yml` file with the following content:

```yaml
name: Attend

on:
  schedule:
    - cron: '0 2 * * *'

jobs:
  update-sheet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install gspread google-auth python-dotenv

      - name: Run script
        env:
          SHEET_URL: ${{ secrets.SHEET_URL }}
          SHEET_NAME: ${{ secrets.SHEET_NAME }}
          CLIENT_SECRETS_JSON: ${{ secrets.CLIENT_SECRETS_JSON }}
          TOKEN_JSON: ${{ secrets.TOKEN_JSON }}
        run: python scripts/main.py
```

### 5. The GitHub actions workflow should run automatically everyday at 2AM UTC.

![image](https://github.com/user-attachments/assets/3a797c61-208b-4f73-9b77-896a9f756471)

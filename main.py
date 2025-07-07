from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
sheet_id = os.getenv("GOOGLE_SHEET_ID")

try:
    credentials = Credentials.from_service_account_file("creds.json", scopes=scopes)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(sheet_id).sheet1
except FileNotFoundError:
    print("Error: 'creds.json' file not found. Please ensure it exists in the current directory.")
except gspread.SpreadsheetNotFound:
    print(f"Error: Spreadsheet with ID '{sheet_id}' not found. Please check the ID and ensure you have access.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")









#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib gspread
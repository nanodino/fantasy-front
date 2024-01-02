import gspread
import streamlit as st
import os
from streamlit_gsheets import GSheetsConnection


from dotenv import load_dotenv
load_dotenv()
gsheets_url = os.getenv('SHEET_LINK')
gspread_config = os.getenv('FILE_LOCATION')


def get_spreadsheets():
    gc = gspread.service_account(
        filename=gspread_config)
    # this requires access to the google drive API
    sh = gc.open("Sandbox - Marta Strikes Back")
    sheets = sh.worksheets()
    return sheets


def add_new_week(conn):
    # adds new lineup week and new scoring week to the workbook
    # conn.create(worksheet='Test Week', data=['hello world'])
    st.write("Adding new week...")
    pass


def main():
    conn = st.connection(
        "gsheets", type=GSheetsConnection)
    df = conn.read()
    st.title('Admin Functions')
    if st.button("Create new week"):
        add_new_week(conn)


if __name__ == "__main__":
    main()

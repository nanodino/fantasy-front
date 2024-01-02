import streamlit as st
from streamlit_gsheets import GSheetsConnection
import gspread

import os
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


def main():
    st.title('Marta strikes back!')
    conn = st.connection(
        "gsheets", type=GSheetsConnection)
    df = conn.read()

    # add help button
    st.button("Help", on_click=st.help, args=(conn,))
    if st.button("Create new week"):
        conn.create(worksheet='Test Week', data=['hello world'])
    if st.button("get spreadsheet"):
        st.write(get_spreadsheets())


if __name__ == "__main__":
    main()

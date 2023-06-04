from datetime import datetime, date

import streamlit as st


def main():
    st.title("ZodiHack")

    # Input form
    name = st.text_input("Hey there! What's your name?")
    min_date = datetime(1900, 1, 1).date()
    max_date = date.today()
    birthdate = st.date_input(f"Hi {name}, what is your birthdate?",
                              value=max_date,
                              min_value=min_date,
                              max_value=max_date)


if __name__ == "__main__":
    main()

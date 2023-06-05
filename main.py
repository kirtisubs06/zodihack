import os
from datetime import datetime, date
import streamlit as st
from langchain.llms import AzureOpenAI


def main():
    # Set Streamlit app theme
    st.set_page_config(
        page_title="ZodiHack",
        page_icon="🌟",
        layout="wide",
        initial_sidebar_state="auto",
    )

    st.title("ZodiHack")

    # Input form
    name = st.text_input("Hey there! What's your name?")
    min_date = datetime(1900, 1, 1).date()
    max_date = date.today()
    birthdate = st.date_input(
        f"Hi {name}, what is your birthdate?",
        value=max_date,
        min_value=min_date,
        max_value=max_date,
    )
    llm = load_llm(0.5)
    llm_responses(llm, birthdate)


def llm_responses(llm, birthdate):
    response = llm(f"You are an expert astrologer. Your job is to identify the zodiac sign based on a birthdate"
                   f"and list the personality traits of that zodiac sign."
                   f"Birthdate: {birthdate}"
                   f"Your response should be in the following format:"
                   f"Zodiac: [zodiac sign]"
                   f"[insert a line break here]"
                   f"Traits: [traits of that zodiac sign, comma separated]")
    # Extract the zodiac sign
    zodiac_start_index = response.index("Zodiac: ") + len("Zodiac: ")
    zodiac_end_index = response.index("\n", zodiac_start_index)
    zodiac = response[zodiac_start_index:zodiac_end_index].strip()

    # Extract the traits
    traits_start_index = response.index("Traits: ") + len("Traits: ")
    traits = response[traits_start_index:].strip()

    # Print the zodiac sign and traits
    st.markdown("<h3>Zodiac Sign</h3>", unsafe_allow_html=True)
    st.write(f"You are a **{zodiac}**!")
    st.write("**Your traits:**")
    st.write(f"You are {traits}")
    st.write("\n")

    response = llm(f"You are an expert astrologer. Your job is to identify the spirit animal based on a birthdate"
                   f"and list the personality traits of that spirit animal."
                   f"Birthdate: {birthdate}"
                   f"Your response should be in the following format:"
                   f"Spirit Animal: [spirit animal]"
                   f"[insert a line break here]"
                   f"Traits: [traits of that spirit animal, comma separated]")
    # Extract the spirit animal
    animal_start_index = response.index("Spirit Animal: ") + len("Spirit Animal: ")
    animal_end_index = response.index("\n", animal_start_index)
    animal = response[animal_start_index:animal_end_index].strip()

    # Extract the traits
    traits_start_index = response.index("Traits: ") + len("Traits: ")
    traits = response[traits_start_index:].strip()

    # Print the Spirit Animals and traits
    st.write("<h3>Spirit Animal</h3>", unsafe_allow_html=True)
    st.write(f"Your spirit animal is a **{animal}**!")
    st.write(f"You are {traits}")


def load_llm(temperature):
    os.environ["OPENAI_API_TYPE"] = st.secrets["OPENAI_API_TYPE"]
    os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    os.environ["DEPLOYMENT_NAME"] = st.secrets["DEPLOYMENT_NAME"]
    os.environ["MODEL_NAME"] = st.secrets["MODEL_NAME"]
    return AzureOpenAI(temperature=temperature,
                       deployment_name=os.environ["DEPLOYMENT_NAME"],
                       model_name=os.environ["MODEL_NAME"])


if __name__ == "__main__":
    main()

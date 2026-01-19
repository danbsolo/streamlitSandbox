import streamlit as st
from snowflake.snowpark.functions import col
import requests


# Write directly to the app
st.title(f"This is a title.")
st.write(
  """This is a subtitle.
  """
)

cnx = st.connection("snowflake")
session = cnx.session()

myRequest = f"https://my.smoothiefroot.com/api/fruit/watermelon"

st.write(f"Request output: {requests.get(myRequest)}")


privateKey = st.text_input("Key here", "placeholder)
st.write("Your private key is", privateKey)

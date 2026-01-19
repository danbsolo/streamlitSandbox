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

#myRequest = f"https://my.smoothiefroot.com/api/fruit/watermelon"
#st.write(f"Request output: {requests.get(myRequest)}")


privateKey = st.text_input("Key here", "placeholder")
st.write("Your private key is", privateKey)


if privateKey:
  url = "https://FINCAN-POC.snowflakecomputing.com/api/v2/databases/TAX_POLICY/schemas/GST/agents/TESTAGENT:run"
  
  headers = {
      "Authorization": "Bearer " + privateKey,
      "Content-Type": "application/json",
      "Accept": "application/json",
  }
  
  payload = {
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "What are the sales trends?"
                  }
              ]
          }
      ]
  }
  
  response = requests.post(url, headers=headers, json=payload)
  response.raise_for_status()
  
  # st.write(response.json())


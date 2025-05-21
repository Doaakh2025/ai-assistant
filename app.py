import streamlit as st
import requests

st.set_page_config(page_title="Smart Medical Bot", layout="centered")
st.title("🤖 Smart Medical Bot")
st.markdown("Please enter your symptoms, and the bot will provide an initial medical suggestion.")

# User input
user_input = st.text_input("✍️ Describe your symptoms:")

# When user clicks the button
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter your symptoms.")
    else:
        # API configuration
        url = "https://udify.app/chat/BXE7UHClh3Liaf7T"
        headers = {
            "Authorization": "Bearer app-MvMNfrvLnaD8mR9eKbP1Q4I1",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": user_input,
            "response_mode": "blocking"
        }

        # Send the request
        with st.spinner("⏳ Please wait..."):
            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()  # Raise error for bad status codes

                # Show raw response (for debugging)
                st.subheader("📦 Raw Response (for debugging):")
                st.code(response.text)

                # Try to parse the JSON response
                result = response.json()
                reply = result.get("answer") or result.get("response") or result.get("text") or "⚠️ No valid answer received."

                st.success("🩺 Bot's Response:")
                st.write(reply)

            except requests.exceptions.JSONDecodeError:
                st.error("❌ Failed to decode the response. The server might not have returned valid JSON.")
                st.code(response.text)

            except requests.exceptions.RequestException as e:
                st.error("🚨 Request failed:")
                st.code(str(e))

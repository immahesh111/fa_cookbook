import streamlit as st
import pandas as pd

st.set_page_config(page_title="Padget Error Code Analysis", page_icon="", layout="wide")

df = pd.read_excel("Moto.xlsx")

# Display header
st.markdown("""<h1 style="color:#002b50;">FA Cook Book</h1>""", unsafe_allow_html=True)

# Sidebar with logo and date picker
st.sidebar.image("images/Padget.png") 

# Search bar for Failure Code
search_code = st.text_input("Enter Failure Code to search:")

# Button to perform the search
if st.button("Search"):
    # Filter DataFrame based on input
    filtered_df = df[df['Failure Code'].astype(str).str.contains(search_code, na=False)]

    # Check if any results were found
    if not filtered_df.empty:
        # Create two columns for displaying results
        a1, a2 = st.columns(2)

        with a1:
            st.subheader("Failure Code:")
            # Display Failure Codes with colors and spacing
            for f_code in filtered_df['Failure Code']:
                st.markdown(f"<div style='background-color: #e7f3fe; padding: 10px; margin-bottom: 10px; border-radius: 5px;'>- {f_code}</div>", unsafe_allow_html=True)

        with a2:
            st.subheader("Details:")
            # Display other relevant information in a vertical layout for each row
            for index, row in filtered_df.iterrows():
                st.markdown(f"<div style='background-color: #d1e7dd; padding: 15px; border-radius: 5px; margin-bottom: 10px;'><b>Station:</b> {row['Station']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color: #fff3cd; padding: 15px; border-radius: 5px; margin-bottom: 10px;'><b>Symptoms:</b>< {row['Symptoms']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color: #cfe2ff; padding: 15px; border-radius: 5px; margin-bottom: 10px;'><b>Root Cause:</b> {row['Root Cause']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color: #f9c2c2; padding: 15px; border-radius: 5px; margin-bottom: 10px;'><b>Action Taken:</b> {row['Action Taken']}</div>", unsafe_allow_html=True)

                st.markdown("---")  # Add a separator between entries

    else:
        st.warning("No results found for the given Failure Code.")
# Display full DataFrame (optional)
# st.dataframe(df)
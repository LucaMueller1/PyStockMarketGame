# PAGE IMPORTS
import pages.side_bar as side_bar
import streamlit as st
import pages.about_settings.helperfunctions as hf


def run(session_state):
    side_bar.run(session_state)

    st.title("Settings")
    st.header("Transaction Fee")

    # Slider for setting the transaction fee (step size = 0.5)
    transaction_fee_current = hf.get_transaction_fees(session_state.auth_key)
    transaction_fee = st.slider("Gebühren:", 1.0, 30.0, step = 0.5, value= float(transaction_fee_current))
    if st.button("Apply"):
        hf.post_new_transaction_fees(session_state.auth_key, transaction_fee)
        st.success("The transaction fee have been changed successfully!")


    if st.button("Delete User"):
        st.warning("Are you sure that you want to delete your Profile? This action can not be reversed.")
        if st.button("I am sure"):
            hf.delete_user(session_state.auth_key)
            session_state.page = "login"
            st.experimental_rerun()



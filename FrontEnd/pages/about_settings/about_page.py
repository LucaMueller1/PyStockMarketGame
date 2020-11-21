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
    transaction_fee = st.slider(
        "Gebühren:", 1.0, 30.0, step=0.5, value=float(transaction_fee_current)
    )
    if st.button("Apply"):
        hf.post_new_transaction_fees(session_state.auth_key, transaction_fee)
        st.success("The transaction fee has been changed successfully!")
    st.write("---")
    st.header("Loading Screen GIF selection")
    gifs = ["AustinPowers", "TheOffice", "Gay", "Penis", "Cats", "Dogs", "Cute_Animals"]
    pre_selected_index_of_gif = session_state.gif_tag[1]
    gif_selected = st.selectbox("GIF Topic:", gifs, index=pre_selected_index_of_gif)
    index_in_gif = gifs.index(gif_selected)
    session_state.gif_tag = (gif_selected, index_in_gif)
    st.write("---")
    st.header("Delete Profile")
    st.warning("This action cannot be reversed")
    if st.button("Delete User"):
        hf.delete_user(session_state.auth_key)
        session_state.page = "login"
        st.experimental_rerun()

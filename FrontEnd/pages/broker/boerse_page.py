# PAGE IMPORTS
import pages.side_bar as side_bar
import streamlit as st


def run(session_state):

    side_bar.run(session_state)
    # Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("FrontEnd/css/style.css")

    st.title("broker")
    st.subheader("Willkommen zur Börse. Hier kannst du Wertpapiere kaufen oder deine vorhandenen Wertpapiere verkaufen.")

    # switch between BUY and SELL
    mode_switch = st.radio("Bitte wähle aus, ob du Werpapiere kaufen oder verkaufen möchtest", ("Kaufen", "Verkaufen"))

    if mode_switch == "Kaufen":
        test_array = []
        if session_state.stock_id:
            test_array.append(session_state.stock_id)
        else:
            test_array.append("")
        # Get the WKN from the User
        st.write("Gib hier eine Wertpapier Kennnummer (WKN) ein, sowie die Anzahl der zu kaufenden Aktien")
        wkn_user_eingabe = st.selectbox("WKN:", test_array + session_state.stock_names)

        if wkn_user_eingabe == " ":
            st.error("Please choose a WKN")
        # Get the quantity from user
        wkn_anzahl_user = st.text_input("Anzahl:")

        # If button is clicked --> Entry submitted
        if st.button("Eingabe bestätigen"):
            wkn_anzahl_user_eingabe = wkn_user_eingabe.title()
            st.success("Success")

            # We are only defining the layout here in order to split the page into two parts.
            # The lefthand part will be filled with the total amount and the "Kaufen" button
            # Righthand part will be filled with Aktieninfos (Aktienname, Aktienwert, Dividendenrendite, Symbol)
            col1, col2 = st.beta_columns(2)

            # Aktienwert is calculated by 190 (later changed to chosen Stock from wkn_user_eingabe) times the amount chosen by user
            aktienwert = 190 * int(wkn_anzahl_user)

            # Gebuehren is static for now, but will later be fetched from database
            gebuehren = 9.90

            # Dividendenrendite is static for now, but will later be fetched from database
            dividendenrendite_raw = 0.06
            dividendenrendite = str(dividendenrendite_raw * 100) + "%"

            # Add Gebuehren to aktienwert
            realisierender_kaufwert = str(aktienwert + gebuehren) + "€"

            # Place price information and "Kaufen" button on the left side
            with col1:
                st.subheader("Verkaufsübersicht")
                st.write("----------------------")
                st.write("Aktienkaufpreis:", aktienwert)
                st.write("Gebühren:", "", gebuehren)
                st.write("----------------------")
                st.subheader("Kaufpreis:")
                st.title(realisierender_kaufwert)
                if st.button("Kaufen"):
                    st.write("Du kannst deine gekauften Aktien nun im Depot beobachten.")
                    # This is where the actual buy happens
                    # Once connected to BE: Get Price of chosen stock & fee --> Calculate end price

            # Place Stock information on the right side
            with col2:
                st.markdown("""
                                <div class="greyish padding">
                                <h2>Aktieninformationen</h2>
                                <p>Aktienname: <b>Adidas</b></p>
                                <p>Aktienwert: <b>""" + "190" + """<b></p>
                                <p>Dividendenrendite: <b>""" + dividendenrendite + """<b></p>
                                <img class = "circle_and_center" src = "https://logo.clearbit.com/apple.com">
                                </div>
                                """
                            , unsafe_allow_html=True)


    elif mode_switch == "Verkaufen":
        session_state.page = "sell"
        st.experimental_rerun()


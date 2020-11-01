# Pages Import
import pages.side_bar as side_bar

# Modules Import
import streamlit as st

def run(session_state):
    side_bar.run(session_state)

    # Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("FrontEnd/css/style.css")

    st.header("Börse")
    st.subheader("Willkommen zur Börse. Hier kannst du Wertpapiere kaufen oder deine vorhandenen Wertpapiere verkaufen.")

    # switch between BUY and SELL
    mode_switch = st.radio("Bitte wähle aus, ob du Werpapiere kaufen oder verkaufen möchtest", ("Kaufen", "Verkaufen"))

    if mode_switch == "Verkaufen":

        st.write("Wähle deine Aktie aus, die du verkaufen möchtest.")

        # Get the stock from user, which he / she wants to sell
        wkn_verkaufen_user_eingabe = st.selectbox("WKN:",[" "] + session_state.stock_names)



        # Connect to Databse later!!!
        quantity_of_stock_im_Depo = 6

        # By standard all stocks are sold, UNLESS user ticks this box:
        if st.checkbox("Alle Aktien verkaufen", value=True):
            # Set the Value of quantity to the amount user has in Depot
            # For now this is STATIC
            stock_quantity = 6

        else:
            # Die Seite wird aufgeteilt, sodass der User auf der rechten Seite eine Angabe hat, wie viele Aktien er von der ausgewählten Aktie im Depot hat
            col1, col2 = st.beta_columns((4, 1))

            # Auswahl der Quantität
            with col1:
                # Sollte der User eine genau Anzahl eingeben wollen, so kann er hier "textfeld" auswaehlen
                input_methode = st.radio("Inputmethode", ("Slider", "Textfeld"))

                # Slider
                if input_methode == "Slider":
                    stock_quantity = st.slider("Wähle aus, wie viele Aktien du verkaufen möchtest", 1, 6)

                # Textfeld & Button
                if input_methode == "Textfeld":
                    stock_quantity_raw = st.text_input("Oder gib die genaue Anzahl hier ein:", value=1)
                    stock_quantity = 1
                    if st.button("Bestätigen"):
                        stock_quantity = int(stock_quantity_raw.title())

            # Anzeige der Quantitaät der ausgewaählten Aktie im Depot
            with col2:
                st.markdown("""
                        <div class="greyish padding">
                        <h4>Quantität im Depot:</h4>
                        <h1>""" + str(quantity_of_stock_im_Depo) + """</h1>
                        </div>
                        """
                            , unsafe_allow_html=True)

        # Vorbereiten der Seitenaufteilung:
        col1, col2 = st.beta_columns(2)

        # Vorbereiten der Variablen (Verkaufspreis, Ordergebühren)

        # Verkaufspreis hier mit STATISCH adidas --> VON DB holen die Aktie!
        aktienverkaufswert = stock_quantity * 169.88

        # verkaufsgebuehren, hier statisch --> von DB holen!
        verkaufsgebuehren = 9.90

        # Verkaufspreis mit Abzug der Gebuehren:
        realisierender_verkaufswert = str(aktienverkaufswert - verkaufsgebuehren) + "€"

        # Dividendenrendite Standardmässig 0 setzen
        dividendenrendite2_raw = 0.06
        dividendenrendite2 = str(dividendenrendite2_raw * 100) + "%"

        # Auflistung Verkaufspreis mit Ordergebühren
        with col1:
            st.subheader("Verkaufsübersicht")
            st.write("----------------------")
            st.write("Aktienverkaufswert:", aktienverkaufswert)
            st.write("Gebühren: -", verkaufsgebuehren)
            st.write("----------------------")
            st.subheader("Verkaufswert:")
            st.title(realisierender_verkaufswert)

            #Sell button
            if st.button("Verkaufen"):
                st.subheader("Verkauft")


        # Aktieninformationen neben der Verkaufsauflistung anzeigen
        with col2:
            st.markdown("""
                                        <div class="greyish padding">
                                        <h2>Aktieninformationen</h2>
                                        <p>Aktienname: <b>Adidas</b></p>
                                        <p>Aktienwert: <b>""" + "190" + """<b></p>
                                        <p>Dividendenrendite: <b>""" + dividendenrendite2 + """<b></p>
                                        <img class = "circle_and_center" src = "https://logo.clearbit.com/adidas-group.com">
                                        </div>
                                        """
                        , unsafe_allow_html=True)

    elif mode_switch == "Kaufen":
        session_state.page = "boerse"
        st.experimental_rerun()

import streamlit as st


def run(session_state):
    #Load CSS File for Formatting
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    local_css("style.css")

    st.header("Börse")
    st.subheader("Willkommen zur Börse. Hier kannst du Wertpapiere kaufen oder deine vorhandenen Wertpapiere verkaufen.")

    # switch between BUY and SELL
    mode_switch = st.radio("Bitte wähle aus, ob du Werpapiere kaufen oder verkaufen möchtest", ("Kaufen", "Verkaufen"))

    # KAUFEN ---------------------------------------
    if mode_switch == "Kaufen":

        # Get the WKN from the User
        st.write("Gib hier eine Wertpapier Kennnummer (WKN) ein, sowie die Anzahl der zu kaufenden Aktien")
        wkn_user_eingabe = st.selectbox("WKN:",["", "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE", "DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE", "MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE"])

        # Get the quantity from user
        wkn_anzahl_user = st.text_input("Anzahl:")

        # If button is clicked --> Entry submitted
        if st.button("Eingabe bestätigen"):
            wkn_anzahl_user_eingabe = wkn_user_eingabe.title()
            st.success("Success" )


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
            dividendenrendite = str(dividendenrendite_raw * 100)+"%"


            # Add Gebuehren to aktienwert
            endpreis = float(aktienwert) + float(gebuehren)


            # Place price information and "Kaufen" button on the left side
            with col1:
                st.write("Aktienkaufpreis:",  aktienwert)
                st.write("Gebühren:", "", gebuehren)
                st.write("----------------------")
                st.subheader("Kaufpreis:")
                st.header(endpreis)
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
                    <p>Aktienwert: <b>""" + str(aktienwert) + """<b></p>
                    <p>Dividendenrendite: <b>""" + dividendenrendite + """<b></p>
                    <img class = "circle_and_center" src = "https://logo.clearbit.com/adidas-group.com">
                    </div>
                    """
                    , unsafe_allow_html=True)



    # VERKAUFEN --------------------------------------
    if mode_switch == "Verkaufen":
        st.write("Wähle deine Aktie aus, die du verkaufen möchtest.")

        # Get the stock from user, which he / she wants to sell
        wkn_verkaufen_user_eingabe = st.selectbox("WKN:", ["", "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "CON.DE", "1COV.DE", "DAI.DE", "DHER.DE", "DKB.DE", "DB1.DE", "DPW.DE", "DTE.DE", "DWNI.DE", "EOAN.DE", "FRE.DE", "FME.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "LIN.DE", "MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VOW3.DE", "VNA.DE"])

        #Connect to Databse later!!!
        quantity_of_stock_im_Depo = 6

        # By standard all stocks are sold, UNLESS user ticks this box:
        if st.checkbox("Alle Aktien verkaufen", value=True):
            # Set the Value of quantity to the amount user has in Depot
            # For now this is STATIC
            stock_quantity = 6

        else:
            #Die Seite wird aufgeteilt, sodass der User auf der rechten Seite eine Angabe hat, wie viele Aktien er von der ausgewählten Aktie im Depot hat
            col1, col2 = st.beta_columns((4,1))

            #Auswahl der Quantität
            with col1:
                # Sollte der User eine genau Anzahl eingeben wollen, so kann er hier "textfeld" auswaehlen
                input_methode = st.radio("Inputmethode", ("Slider", "Textfeld"))

                # Slider
                if input_methode == "Slider":
                    stock_quantity = st.slider("Wähle aus, wie viele Aktien du verkaufen möchtest",1, 6)

                # Textfeld & Button
                elif input_methode == "Textfeld":
                    stock_quantity_raw = st.text_input("Oder gib die genaue Anzahl hier ein:")
                    if st.button("Bestätigen"):
                        stock_quantity = stock_quantity_raw.title()
                        st.success("Success")

                else:
                    st.error("Error")

            #Anzeige der Quantitaät der ausgewaählten Aktie im Depot
            with col2:
                st.markdown("""
                <div class="greyish padding">
                <h4>Quantität im Depot:</h4>
                <h1>"""+str(quantity_of_stock_im_Depo)+"""</h1>
                </div>
                """
                    , unsafe_allow_html = True)


        # VERKAUFEN --------------------------------------
        if mode_switch == "Verkaufen":
            st.write("nothing here yet")

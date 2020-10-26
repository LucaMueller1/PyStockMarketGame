import streamlit as st


def run(session_state):
    #Setting up layout of FE
    col1, col2 = st.beta_columns((4, 1))

    with col1:
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

                col2.write("Das hier sind Aktieninfos")

                # This is where the actual buy happens
                # Once connected to BE: Get Price of chosen stock & fee --> Calculate end price





        # VERKAUFEN --------------------------------------
        if mode_switch == "Verkaufen":
            st.write("nothing here yet")
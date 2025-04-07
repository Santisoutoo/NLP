import lmstudio as lms
import streamlit as st

st.title("TWR controller agent")

st.markdown("""
Writte a promt as you where an ATC and the app will show what the pilot should say
- RYR684V wind 240 8kt cleared to land runway 24L -> expeted output -> cleared to land runway 24R RYA684V
- VLG54WT taxi to HP01 runway 24L via M, P, L, k  -> Taxi to HP01 runway 24L via M, P, L, k, VLG54WT
""")


# Specify context usage

context = """
You are a pilot and your ouput will be a simple phase that will try to match what a pilot says after the atc give them an instruction.
Normally, you only have to repit everything the tell your but the callsing and elements like wind and traffic information should not be repited.
You will face different types of comunication from 3 different dependencies: delivery, tower, and ground.
"""

# Create buttoms

buttom = st.button("Enviar solicitud")
buttom_text = st.text_area("ATC message: ")
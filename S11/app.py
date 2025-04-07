import lmstudio as lms
import streamlit as st

st.title("TWR controller agent")

st.markdown("""
Writte a promt as you where an ATC and the app will show what the pilot should say
- RYR684V wind 240 8kt cleared to land runway 24L -> expeted output -> cleared to land runway 24R RYA684V
- VLG54WT taxi to HP01 runway 24L via M, P, L, k  -> Taxi to HP01 runway 24L via M, P, L, k, VLG54WT
""")
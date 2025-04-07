import lmstudio as lms
import streamlit as st

st.title("🗼 TWR Controller Agent")

st.markdown("""
Enter an ATC instruction and the app will generate the expected pilot readback.

**Examples:**
- ATC: `RYR684V wind 240 8kt cleared to land runway 24L`  
  Pilot: `Cleared to land runway 24L, RYR684V`

- ATC: `VLG54WT taxi to HP01 runway 24L via M, P, L, K`  
  Pilot: `Taxi to HP01 runway 24L via M, P, L, K, VLG54WT`
""")

context = """
You are a pilot. Respond ONLY with a short and realistic readback phrase that a pilot would say after receiving ATC instructions. 
Do NOT include internal thoughts, explanations, or reasoning. 
Only output the exact pilot response as a single line.
"""

# Buttoms and text box
prompt = st.text_area("✈️ ATC Instruction:", height=100)
button = st.button("🎧 Generate Pilot Response")

if button and prompt.strip():
    model = lms.llm("deepseek-r1-distill-qwen-7b")
    full_prompt = context + "\n\n" + prompt
    result = model.respond(full_prompt)

    # Filter the response so the output is concice
    response_text = result.content.strip()
    if "<think>" in response_text:
        clean_response = response_text.split("<think>")[-1].strip().split("\n")[-1]
    else:
        clean_response = response_text.split("\n")[-1]

    st.markdown("#### 🧑‍✈️ Pilot Response:")
    st.success(clean_response)

elif button:
    st.warning("Please enter an ATC instruction before submitting.")

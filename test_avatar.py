import streamlit as st

st.title("Avatar Test")

html = """
<div style="background: blue; color: white; padding: 20px; border-radius: 10px;">
    <h2>Test Avatar</h2>
    <p>If you see this styled, HTML is working!</p>
</div>
"""

st.markdown(html, unsafe_allow_html=True)

st.write("If you see blue box above, it's working!")

import streamlit as st
from backend.knowledge_engine import KnowledgeEngine

st.set_page_config(page_title="AI Smart Support System")

st.title("AI Powered Knowledge for Smart Support & Ticket Resolution")

engine = KnowledgeEngine("data/knowledge.csv")

st.subheader("Describe Your Issue")

user_query = st.text_area("Enter your issue here:")

if st.button("Submit Ticket"):
    if user_query.strip() == "":
        st.warning("Please enter an issue description.")
    else:
        ticket_id, solution, category = engine.create_ticket(user_query)

        st.success(f"Ticket Created Successfully! ID: {ticket_id}")
        st.info(f"Category: {category}")
        st.write("### Suggested Solution:")
        st.write(solution)

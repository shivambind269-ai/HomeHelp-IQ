import streamlit as st

from agents.issue_agent import detect_issue
from agents.safety_agent import safety_advice
from agents.cost_agent import estimate_cost
from agents.workorder_agent import create_workorder
from agents.retrieval_agent import retrieve_knowledge
from agents.urgency_agent import get_urgency
from pdf_generator import generate_pdf

st.set_page_config(
    page_title="HomeHelp IQ",
    page_icon="🏠"
)

st.title("🏠 HomeHelp IQ")
st.subheader("Multi-Agent Home Maintenance Assistant")

problem = st.text_area(
    "Describe your home issue:",
    height=150
)

if st.button("Analyze Issue"):

    issue = detect_issue(problem)

    urgency = get_urgency(issue)

    safety = safety_advice(issue)

    cost = estimate_cost(issue)

    knowledge = retrieve_knowledge(issue)

    workorder = create_workorder(
        issue,
        cost,
        urgency
    )

    st.success("Analysis Complete")

    st.write("### Issue Category")
    st.write(issue)

    st.write("### Urgency Level")
    st.write(urgency)

    st.write("### Safety Advice")
    st.write(safety)

    st.write("### Estimated Cost")
    st.write(cost)

    st.write("### Work Order")
    st.code(workorder)

    pdf_file = generate_pdf(
        issue,
        urgency,
        safety,
        cost
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="HomeHelp_Report.pdf",
            mime="application/pdf"
        )

    st.write("### Knowledge Base")
    st.text(knowledge)
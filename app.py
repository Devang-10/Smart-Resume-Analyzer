import streamlit as st
import nltk
from io import BytesIO
from utils.extract_text import extract_text_from_file
from utils.keyword_analysis import analyze_resume
from utils.job_matching import match_resume_to_job
from utils.feedback_generator import generate_feedback
from utils.visualizer import plot_skill_match_chart
from utils.report_generator import generate_pdf_report
from utils.tips_generator import get_resume_tips

nltk.download('punkt')

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")
st.title("📄 Smart Resume Analyzer using NLP")
st.write("Upload your resume and get instant feedback powered by NLP.")

# Upload
uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Optional: Paste Job Description for skill matching")

if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        resume_text = extract_text_from_file(uploaded_file)

    st.subheader("📑 Extracted Resume Text")
    st.text_area("Text Output", resume_text, height=250)

    st.subheader("🧠 NLP Highlights")
    extracted_data = analyze_resume(resume_text)

    col1, col2, col3 = st.columns(3)

    # with col2:
    #     st.metric("Education", len(extracted_data.get('education', [])))
    #     st.write(", ".join(extracted_data.get('education', [])[:2]) + ("..." if len(extracted_data.get('education', [])) > 2 else ""))

    with col1:
        st.metric("Skills", len(extracted_data.get('skills', [])))
        # st.write(", ".join(extracted_data.get('skills', [])[:5]) + ("..." if len(extracted_data.get('skills', [])) > 5 else ""))

    # with col3:
    #     st.metric("Experience", len(extracted_data.get('experience', [])))
    #     st.write(", ".join(extracted_data.get('experience', [])[:2]) + ("..." if len(extracted_data.get('experience', [])) > 2 else ""))

    st.subheader("📌 Resume Score Breakdown")
    st.progress(min(extracted_data.get("skills_score", 0), 100) / 100)
    st.write("**Skills:**", f"{extracted_data.get('skills_score', 0)}%")
    st.write("**Experience:**", f"{extracted_data.get('experience_score', 0)}%")
    st.write("**Education:**", f"{extracted_data.get('education_score', 0)}%")

    # Skill Matching
    score = None
    matched_skills = []
    if job_description:
        score, matched_skills = match_resume_to_job(extracted_data['skills'], job_description)
        st.subheader("📊 Skill Match Score")
        st.metric("Matching Score", f"{score}%")
        st.subheader("🎯 Matched Skills")

        if matched_skills:
            st.markdown("Here are the skills from your resume that matched the job description:")
            cols = st.columns(4)
            for i, skill in enumerate(matched_skills):
                cols[i % 4].markdown(
                    f"<div style='background-color:#50C878; padding:6px 10px; border-radius:10px; "
                    f"text-align:center; font-size:14px; margin-bottom:8px;'>{skill}</div>",
                    unsafe_allow_html=True
                )
        else:
            st.info("No significant skill matches found. Try adding more relevant skills based on the job description.")

        # Chart
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        plot_skill_match_chart(score, width=4, height=3)
  # Smaller chart size
        st.markdown("</div>", unsafe_allow_html=True)

    # Feedback
    feedback = generate_feedback(extracted_data, job_description)
    st.subheader("📝 Resume Feedback")
    st.markdown(generate_feedback(extracted_data, job_description))

    # Download Report
    st.subheader("📥 Download Report")
    pdf_buffer = BytesIO()
    generate_pdf_report(
        output_path=pdf_buffer,
        resume_text=resume_text,
        extracted_data=extracted_data,
        feedback=feedback,
        score=score,
        matched_skills=matched_skills
    )
    pdf_buffer.seek(0)
    st.download_button(
        label="Download PDF Report",
        data=pdf_buffer,
        file_name="resume_analysis_report.pdf",
        mime="application/pdf"
    )

    # Resume Tips
    if job_description:
        st.subheader("💡 Resume Tips for This Role")
        tips = get_resume_tips(job_description)
        st.write(tips)

def generate_feedback(data, job_description):
    feedback = []

    if data.get("skills_score", 0) < 50:
        feedback.append("🔧 Add more relevant technical and soft skills to strengthen your profile.")
    if data.get("experience_score", 0) < 60:
        feedback.append("💼 Expand on your past internships, work experience, or projects.")
    if data.get("education_score", 0) < 60:
        feedback.append("🎓 Mention academic highlights, relevant coursework, and certifications.")
    if job_description:
        feedback.append("📌 Tailor your resume to better align with the job description.")

    if feedback:
        return "\n".join([f"- {point}" for point in feedback])
    else:
        return "✅ Your resume looks well-balanced and job-ready!"



def get_role_based_tips(job_description: str) -> str:
    job_description = job_description.lower()

    tips_dict = {
        "data scientist": [
            "📊 Include specific projects involving data analysis or machine learning.",
            "🧠 Highlight tools like Python, R, SQL, Pandas, and Scikit-learn.",
            "📈 Showcase knowledge of statistics and data visualization (e.g., Matplotlib, Seaborn)."
        ],
        "web developer": [
            "💻 Emphasize frontend and backend technologies (HTML, CSS, JS, React, Node).",
            "🌐 Showcase responsive design skills and GitHub links to your projects.",
            "🗃️ Include details about APIs, databases, and deployment experience."
        ],
        "network engineer": [
            "🛠️ Highlight certifications (CCNA, CCNP), and network troubleshooting experience.",
            "🌐 Mention routing/switching protocols, firewalls, and networking tools.",
            "🧰 Emphasize experience with command-line diagnostics and monitoring tools."
        ]
    }

    for role, tips in tips_dict.items():
        if role in job_description:
            return "\n".join([f"- {tip}" for tip in tips])

    # Default general tips
    default_tips = [
        "🔍 Tailor your resume to highlight the most relevant skills for the job.",
        "📝 Use clear formatting, concise bullet points, and strong action verbs.",
        "📄 Avoid generic objectives; use a specific, tailored career summary."
    ]
    return "\n".join([f"- {tip}" for tip in default_tips])

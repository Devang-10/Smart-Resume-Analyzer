def get_resume_tips(job_description: str) -> str:
    job_description = job_description.lower()

    tips = {
        "data scientist": [
            "Highlight your experience with Python, R, or SQL.",
            "Include machine learning projects with measurable outcomes.",
            "Mention data visualization tools like Tableau or Power BI.",
            "Showcase statistical analysis and hypothesis testing skills."
        ],
        "software engineer": [
            "Focus on your proficiency in languages like Java, Python, C++.",
            "Include collaborative projects with GitHub links.",
            "Emphasize experience with system design or scalable systems.",
            "Mention contributions to open-source projects if any."
        ],
        "web developer": [
            "Highlight full-stack development experience (HTML, CSS, JS, frameworks).",
            "Include responsive design and cross-browser compatibility.",
            "Mention experience with RESTful APIs and databases.",
            "Link to a portfolio or personal projects website."
        ],
        "network engineer": [
            "Include certifications like CCNA, CCNP, or CompTIA Network+.",
            "Mention hands-on experience with routing and switching.",
            "Detail any experience with network monitoring or troubleshooting tools.",
            "Highlight documentation skills and network design experience."
        ]
    }

    default_tips = [
        "Customize your resume to highlight relevant skills and experience for the target job.",
        "Use strong action verbs and quantify achievements.",
        "Keep formatting clean and professional.",
        "Tailor each resume for the specific job role."
    ]

    selected_tips = default_tips
    for role, role_tips in tips.items():
        if role in job_description:
            selected_tips = role_tips
            break

    return "\n".join(f"- {tip}" for tip in selected_tips)

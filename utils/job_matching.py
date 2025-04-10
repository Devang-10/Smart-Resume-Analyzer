from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_job(resume_skills, job_description):
    if not resume_skills or not job_description:
        return 0, []

    # Clean and prepare text
    resume_text = " ".join([skill.strip().lower() for skill in resume_skills if len(skill.strip()) > 1])
    job_description = job_description.lower()

    documents = [resume_text, job_description]

    # Compute similarity score
    tfidf = TfidfVectorizer().fit_transform(documents)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    # Find matched skills
    matched = [skill for skill in resume_skills if skill.lower() in job_description]

    return round(score * 100), matched

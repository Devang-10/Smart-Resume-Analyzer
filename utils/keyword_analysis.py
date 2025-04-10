import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.data import find

# Download necessary resources only if missing
for pkg in ['punkt', 'stopwords', 'wordnet']:
    try:
        find(f'tokenizers/{pkg}' if pkg == 'punkt' else f'corpora/{pkg}')
    except LookupError:
        nltk.download(pkg)

def analyze_resume(text):
    text = text.lower()
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    keywords = [word for word in tokens if word.isalpha() and word not in stop_words]

    # Use WordNet to validate that the word has meaning
    skills = [word for word in keywords if wordnet.synsets(word)]

    # Bonus: add some known technical skill keywords to boost results
    tech_keywords = ['python', 'java', 'sql', 'html', 'css', 'javascript', 'machine', 'learning', 'networking']
    for tech in tech_keywords:
        if tech in text and tech not in skills:
            skills.append(tech)

    skills = sorted(set(skills))

    # Simple estimation logic (placeholders or basic keyword matches)
    experience_keywords = ['intern', 'experience', 'worked', 'project', 'developer', 'engineer']
    education_keywords = ['bachelor', 'master', 'degree', 'university', 'college', 'school']

    experience_score = min(sum(1 for word in experience_keywords if word in text) * 10, 100)
    education_score = min(sum(1 for word in education_keywords if word in text) * 10, 100)

    return {
        "skills": skills,
        "skills_score": min(len(skills), 100),
        "experience_score": experience_score,
        "education_score": education_score
    }

# 📄 Smart Resume Analyzer using NLP & Streamlit

A powerful web-based resume analyzer tool that uses NLP techniques to evaluate resumes, match skills to job descriptions, and provide intelligent feedback and suggestions.

---

## 🚀 Features

- 🔍 **Resume Text Extraction** (PDF/DOCX)
- 📊 **Skill Extraction & Scoring**
- 🎯 **Job Description Matching & Skill Match Visualization**
- 📝 **Intelligent Resume Feedback**
- 💡 **Role-Based Resume Tips**
- 📄 **PDF Report Generation**
- 📧 **Email Report Delivery** *(optional)*

---

## 🛠️ Built With

- 🐍 Python
- 💻 Streamlit
- 📚 NLP Libraries (NLTK, Scikit-learn)
- 📈 Matplotlib
- 📄 ReportLab (PDF Report Generation)

---

## 📦 Installation

1. **Clone the Repository**

(bash)
git clone https://github.com/Devang-10/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer

2. **Create a Virtual Environment (Optional but Recommended)**

python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows

3. Install Dependencies
   
pip install -r requirements.txt

4. ▶️ Run the App

streamlit run app.py

📁 Project Structure
smart-resume-analyzer/
│
├── app.py                         # Main Streamlit app
├── extract_text.py                # File text extraction logic
├── analyzer.py                    # NLP analysis functions
├── job_matcher.py                 # Skill-to-JD matcher
├── feedback_generator.py          # Personalized feedback and tips
├── visualizer.py                  # Chart plotting (skill match)
├── pdf_report.py                  # PDF report generator
├── sample_job_description.txt     # Example job description
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

📬 Contact
Created by Devang Jain – feel free to reach out or contribute!


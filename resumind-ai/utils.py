import PyPDF2

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text.lower()


def extract_skills(text):
    SKILLS = {
        "python": ["python"],
        "machine learning": ["machine learning", "ml"],
        "data analysis": ["data analysis", "analytics"],
        "html": ["html"],
        "css": ["css"],
        "javascript": ["javascript", "js"],
        "sql": ["sql", "mysql"],
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "tensorflow": ["tensorflow"],
        "react": ["react"],
        "node": ["node", "nodejs"],
        "mongodb": ["mongodb"]
    }

    found = {}

    for skill, variations in SKILLS.items():
        count = sum(text.count(word) for word in variations)
        if count > 0:
            found[skill] = count

    return found


def calculate_score(skills):
    return min(len(skills) * 10, 100)


def missing_skills(skills, role):
    role_map = {
        "Software Developer": ["python", "dsa", "oop"],
        "Frontend Developer": ["html", "css", "javascript", "react"],
        "Backend Developer": ["node", "sql"],
        "AI Engineer": ["python", "machine learning", "tensorflow"],
        "Data Scientist": ["python", "pandas", "numpy", "data analysis"],
        "UI/UX Designer": ["figma", "ui", "ux"]
    }

    required = role_map.get(role, [])
    return [s for s in required if s not in skills]
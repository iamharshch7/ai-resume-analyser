# AI Resume Analyzer 🚀

A professional, production-ready full-stack web application built with Django and OpenAI to analyze resumes, provide ATS compatibility scores, and match candidates with job descriptions.

## ✨ Features

- **User Authentication**: Secure registration, login, and profile management.
- **Resume Upload**: Support for PDF and DOCX formats with instant text extraction.
- **AI-Powered Analysis**: 
  - Overall & ATS Compatibility scores (0-100).
  - Technical and Soft skills identification.
  - Strengths, weaknesses, and actionable improvement recommendations.
- **Job Description Matcher**: Compare your resume against specific job postings to find keyword gaps.
- **Modern Dashboard**: Visualize your progress and history with an intuitive SaaS-style interface.
- **History Tracking**: Keep a record of all your previous analyses and scores.

## 🛠️ Tech Stack

- **Backend**: Django 5.0, Python 3.12.10
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **AI/NLP**: OpenAI GPT API, PyMuPDF (fitz), python-docx
- **Database**: SQLite (Local), PostgreSQL (Production ready)
- **Deployment**: Gunicorn, WhiteNoise, Render/Railway

## 🚀 Getting Started

### Prerequisites
- Python 3.12.10
- OpenAI API Key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iamharshch7/ai-resume-analyser.git
   cd ai-resume-analyser
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and add:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

## 📸 Screenshots

*(Add your screenshots here!)*

## 📄 License

This project is licensed under the MIT License.

---
Built with ❤️ by [iamharshch7](https://github.com/iamharshch7)
🤖 Generated with [Claude Code](https://claude.com/claude-code)

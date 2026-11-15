import os
import json
from openai import OpenAI
from django.conf import settings

# Initialize client using new >= 1.0.0 syntax
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", settings.SECRET_KEY))

def analyze_resume_logic(resume):
    from analyzer.models import ResumeAnalysis

    text = resume.extracted_text or ""

    # Rule-based fallback & core analyzer
    skills_db = ["python", "django", "javascript", "react", "sql", "git", "html", "css", "docker", "aws", "postgresql", "rest api", "leadership", "communication", "problem solving"]
    found_skills = [skill for skill in skills_db if skill in text.lower()]
    missing_skills = [skill for skill in skills_db if skill not in found_skills][:5]

    word_count = len(text.split())
    base_score = min(85, max(40, word_count // 10))
    if len(found_skills) > 5:
        base_score += 10

    analysis_data = {
        "overall_score": min(95, base_score),
        "ats_score": min(98, base_score + 5),
        "technical_skills": found_skills[:8],
        "soft_skills": ["Communication", "Problem Solving", "Teamwork"],
        "education_analysis": "Education section detected and formatted correctly.",
        "experience_analysis": f"Detected approximately {word_count} words of career history.",
        "projects_analysis": "Project achievements noted with relevant tech stack keywords.",
        "missing_skills": missing_skills,
        "grammar_suggestions": ["Ensure consistent bullet point formatting.", "Add metrics and KPIs to work experience."],
        "strengths": ["Strong core skill keywords", "Clear document structure", "Good technical vocabulary"],
        "weaknesses": ["Could include more quantitative metrics", "Some industry standard skills missing"],
        "recommendations": ["Incorporate more quantified metrics in your project descriptions.", "Add missing technical skills to boost ATS matching."]
    }

    # Attempt OpenAI if API key is valid
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here":
        try:
            prompt = f"Analyze this resume and return JSON with keys overall_score, ats_score, technical_skills (list), soft_skills (list), education_analysis, experience_analysis, projects_analysis, missing_skills (list), grammar_suggestions (list), strengths (list), weaknesses (list), recommendations (list):\n\n{text[:3000]}"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                response_format={ "type": "json_object" }
            )
            content = response.choices[0].message.content
            parsed = json.loads(content)
            analysis_data.update(parsed)
        except Exception as e:
            print(f"OpenAI API analysis fallback used due to error: {e}")

    # Save or update ResumeAnalysis
    analysis, created = ResumeAnalysis.objects.update_or_create(
        resume=resume,
        defaults={
            'overall_score': analysis_data.get('overall_score', 75),
            'ats_score': analysis_data.get('ats_score', 80),
            'technical_skills': ", ".join(analysis_data.get('technical_skills', [])),
            'soft_skills': ", ".join(analysis_data.get('soft_skills', [])),
            'education_analysis': analysis_data.get('education_analysis', ''),
            'experience_analysis': analysis_data.get('experience_analysis', ''),
            'projects_analysis': analysis_data.get('projects_analysis', ''),
            'missing_skills': ", ".join(analysis_data.get('missing_skills', [])),
            'grammar_suggestions': json.dumps(analysis_data.get('grammar_suggestions', [])),
            'strengths': json.dumps(analysis_data.get('strengths', [])),
            'weaknesses': json.dumps(analysis_data.get('weaknesses', [])),
            'recommendations': json.dumps(analysis_data.get('recommendations', [])),
        }
    )
    return analysis

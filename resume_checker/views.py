from django.shortcuts import render

from .forms import ResumeForm

import pdfplumber


JOB_SKILLS = {

    "Python Developer": [
        "python",
        "django",
        "flask",
        "sql",
        "git",
        "api",
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "tailwind",
    ],

    "Backend Developer": [
        "django",
        "node",
        "sql",
        "api",
        "mongodb",
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "django",
        "sql",
    ],

    "Data Analyst": [
        "python",
        "excel",
        "sql",
        "power bi",
        "pandas",
    ],
}


def home(request):

    result = None

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            uploaded_file = request.FILES['resume']

            selected_role = request.POST.get("job_role")

            text = ""

            with pdfplumber.open(uploaded_file) as pdf:

                for page in pdf.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted.lower()

            required_skills = JOB_SKILLS.get(selected_role, [])

            matched_skills = []

            missing_skills = []

            for skill in required_skills:

                if skill in text:
                    matched_skills.append(skill)

                else:
                    missing_skills.append(skill)

            score = int(
                (len(matched_skills) / len(required_skills)) * 100
            )

            result = {
                "filename": uploaded_file.name,

                "job_role": selected_role,

                "score": score,

                "matched_skills": matched_skills,

                "missing_skills": missing_skills,

                "resume_text": text[:2000],
            }

    else:

        form = ResumeForm()

    return render(
        request,
        'index.html',
        {
            "form": form,
            "result": result,
        }
    )

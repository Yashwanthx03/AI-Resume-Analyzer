#  AI Resume Analyzer

A modern ATS (Applicant Tracking System) based Resume Analyzer built using Django and Python. This application helps recruiters and hiring teams evaluate resumes efficiently by extracting content from PDF resumes, analyzing skills against job-specific requirements, calculating ATS compatibility scores, and identifying skill gaps.

The platform provides automated resume screening, role-based skill matching, and an intuitive user interface to simplify the recruitment process.

---

#  Live Demo

Add your Render deployment link here.

Example:

https://your-app-name.onrender.com

---

#  Features

*  Upload PDF Resumes
*  ATS Score Calculation
*  Job Role Based Evaluation
*  Skill Matching Analysis
*  Missing Skills Detection
*  PDF Text Extraction
*  Real-Time Resume Processing
*  Modern Responsive UI
*  Cloud Deployment using Render

---

#  Technologies Used

## Backend

* Python
* Django

## Frontend

* HTML5
* Tailwind CSS
* JavaScript

## PDF Processing

* PDFPlumber

## Deployment & Server

* Render
* Gunicorn
* WhiteNoise

## Version Control

* Git
* GitHub

---

#  Project Structure

```bash
AI-Resume-Analyzer/
│
├── core/
├── resume_checker/
├── templates/
├── static/
│   └── images/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Project Screenshots

## Upload Resume

![Upload Resume](static/images/upload.png)

---

## ATS Analysis Result

![ATS Result](static/images/result.png)

---

## Skill Matching Analysis

![Skill Matching](static/images/skills.png)

---

#  Installation Guide

## Clone Repository

```bash
git clone https://github.com/Yashwanthx03/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Development Server

```bash
python manage.py runserver
```

Application will run at:

```bash
http://127.0.0.1:8000/
```

---

#  Deployment

This project is deployed using Render.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn core.wsgi
```

---

#  Challenges Faced

During development and deployment, the following issues were resolved:

* Django template configuration errors
* PDF extraction handling
* ATS score calculation logic
* GitHub repository setup
* Render deployment issues
* Gunicorn configuration
* DisallowedHost errors
* Static file configuration

---

#  What I Learned

Through this project, I learned:

* Django Project Structure
* File Upload Handling
* PDF Processing using PDFPlumber
* ATS Scoring Logic
* Skill Matching Systems
* Tailwind CSS UI Development
* Git & GitHub Workflow
* Render Deployment
* Debugging Production Issues
* Full-Stack Project Development

---

#  Author

### Yashwanth

GitHub:
https://github.com/Yashwanthx03

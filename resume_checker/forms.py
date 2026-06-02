from django import forms


JOB_CHOICES = [
    ("Python Developer", "Python Developer"),
    ("Frontend Developer", "Frontend Developer"),
    ("Backend Developer", "Backend Developer"),
    ("Full Stack Developer", "Full Stack Developer"),
    ("Data Analyst", "Data Analyst"),
]


class ResumeForm(forms.Form):

    job_role = forms.ChoiceField(
        choices=JOB_CHOICES
    )

    resume = forms.FileField()
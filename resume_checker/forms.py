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
        choices=JOB_CHOICES,

        widget=forms.Select(
            attrs={
                "class": "w-full p-4 rounded-2xl bg-slate-800 border border-slate-700 text-white outline-none"
            }
        ),
    )

    resume = forms.FileField(

        widget=forms.ClearableFileInput(
            attrs={
                "class": "w-full p-4 rounded-2xl bg-slate-800 border border-slate-700 text-white"
            }
        )
    )
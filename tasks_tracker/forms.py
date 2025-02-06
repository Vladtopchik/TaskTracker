from django import forms
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "priority",
            "status",
            "due_date"
        ]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].widget = forms.DateTimeInput(attrs={"type": "datetime-local"})


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ("", "All"),
        ("todo", "To Do"),
        ("inprogress", "In progress"),
        ("done", "Done"),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label='Статус')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "rating",
            "content",
            "media"
        ]
        widgets = {
            'media': forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].label = ""
        self.fields["rating"].label = ""

        self.fields["rating"].initial = 5
        self.fields["rating"].widget.attrs.update({
            "min": "1",
            "max": "5",
            "hidden": "true"
        })

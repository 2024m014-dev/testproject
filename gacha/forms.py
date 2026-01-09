from django import forms
from .models import Action


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ["content"]
        labels = {"content": "今日のえらいこと"}
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "例  ちゃんと起きた  提出した  洗濯した",
                    "maxlength": "200",
                }
            )
        }

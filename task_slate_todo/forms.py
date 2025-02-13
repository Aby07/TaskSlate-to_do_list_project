from django import forms
from .models import Task, User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_completed']

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Title',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter Any Description',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'placeholder': 'Created DateTime',
        'class': 'w-full py-4 px-6 rounded-xl',
        'readonly': 'readonly'  
    }), required=False)  

    due_date = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'Deadline',
        'class': 'w-full py-4 px-6 rounded-xl',
        'type': 'date'
    }))

    is_completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }), required=False) 

    priority = forms.ChoiceField(choices=Task.PRIORITY_CHOICES, widget=forms.Select(attrs={
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}))
    fullname = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'fullname', 'phone_number']

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))

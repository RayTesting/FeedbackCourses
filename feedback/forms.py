from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment

RATES = [(1,1),(2,2),(3,3),(4,4),(5,5)]
LIKED = [(True,'Sí'), (False,'No')]
auth_class_input = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'

class CommentForm(forms.ModelForm):
    content_rate = forms.ChoiceField(
        label = 'Calificación del contenido',
        required=True,
        choices=RATES, 
        widget=forms.RadioSelect(
            attrs={
                "class":"flex items-center gap-3"
            }
        )
    )
    class_rate = forms.ChoiceField(
        label = 'Calificación de las clases',
        required=True,
        choices=RATES, 
        widget=forms.RadioSelect(
            attrs={
                "class":"flex items-center gap-3"
            }
        )
    )
    facilitator_rate = forms.ChoiceField(
        label = 'Calificación del tallerista',
        required=True,
        choices=RATES, 
        widget=forms.RadioSelect(
            attrs={
                "class":"flex items-center gap-3"
            }
        )
    )
    description = forms.CharField(
        label = 'Comentarios (opcional)',
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Escribe tu opinión del curso, ayúdanos a mejorar",
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
            }
        )
    )
    liked = forms.ChoiceField(
        label='En general, ¿Te gustó el curso?',
        required=True,
        choices=LIKED,
        widget=forms.RadioSelect(
            attrs={
                "class":"flex items-center gap-3 "
            }
        )
    )


    class Meta:
        model = Comment
        fields = ('content_rate','class_rate','facilitator_rate','description','liked')

class AuthForm(AuthenticationForm):
    username = forms.CharField(
        label='User',
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Enter your username",
                "class": auth_class_input
            }
        )
    )

    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Enter your password",
                "class": auth_class_input
            }
        )
    )

    class Meta:
        model = User
        # fields = '__all__' todos
        # fields = 'username' solo uno
        # fields = ('username', 'password') varios
        
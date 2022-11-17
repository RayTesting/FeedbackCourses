from django.shortcuts import render,redirect
from .forms import CommentForm, AuthForm
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    success = False
    form = CommentForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            success = True

    context = {
        'form':form,
        'success':success
    } 
    return render(request, 'index.html', context)

@login_required(login_url='login')        
def reportes(request):
    comments = Comment.objects.all()
    average = 0
    content_average = 0
    class_average = 0
    facilitator_average = 0
    for comment in comments:
        average += comment.get_average()
        content_average += comment.content_rate
        class_average += comment.class_rate
        facilitator_average += comment.facilitator_rate
    
    content_average /= comments.count()
    class_average /= comments.count()
    facilitator_average /= comments.count()

    context = {
        "comments":comments,
        "average":round(average,2),
        "content_average": round(content_average,2),
        "class_average": round(class_average,2),
        "facilitator_average": round(facilitator_average,2),
    }

    return render(request,'reportes.html',context)

def login_view(request):
    msg = None
    form = AuthForm(data=request.POST or None)

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        if form.is_valid():
            print('is valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next = request.GET.get('next')
                if next: 
                    return redirect(next)
                return redirect('index')
            else:
                msg = "USERNAME OR PASSWORD INCORRECT"
        else:
            print('is not valid')

    return render(request, 'login.html',{"msg":msg, "form":form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('login')


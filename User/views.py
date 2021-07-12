from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from os import name
from .models import post, user
from .forms import PostsForm, SignupForm

# Create your views here.

def validity(a):
    for b in a:
        if (b.isalnum()==True or b=='_'):
            continue
        else:
            return False
    return True


global check1 
check1 = False

global signup
signup = False

global invalid
invalid = False

global same
same = False

global invalid_post
invalid_post = False

global Username
Username = "Vinay"

global login
login = False

global check_post
check_post = False


usr_nm=[]

def give_username():
    global Username
    return Username

def updateUsername():
    param = user.objects.all()
    for a in param:
            if a.username not in usr_nm:
                if len(a.username)==0:
                    continue
                usr_nm.append(a.username)

def login(request):
    global signup
    global check1
    temp_signup = signup
    temp_check1 = check1
    signup = False
    check1 = False
    updateUsername()
    if request.method=='POST' and temp_signup==True:
        username = request.POST['username']
        if(validity(username)==False):
            global invalid
            invalid = True
            return redirect('signup/')
        if username in usr_nm:
            global same
            same = True
            return redirect('signup/') 
        form = SignupForm(request.POST)
        if(form.is_valid()):
            form.save()
    return render(request, 'User/login.html', {'check':temp_check1, 'signup':temp_signup})

def signup(request):
    global signup
    signup = True

    global same
    same_temp = same
    same = False

    global invalid
    invalid_temp = invalid
    invalid = False
    
    form = SignupForm
    return render(request, 'User/sign_up.html', {'form':form, 'same':same_temp, 'invalid':invalid_temp})

def check(request):
    global check1
    check1 = True

    global login
    login = True
    param = user.objects.all()
    
    updateUsername()
    pass_unq = []
    for a in param:
        if a.password not in pass_unq:
            if len(a.password)==0:
                continue
            pass_unq.append(a.password)

    if request.method=='POST':
        global Username
        Username = request.POST['username']
        password = request.POST['password']
        if Username in usr_nm and password in pass_unq:
            return redirect('/user/posts')
    return redirect('../')

def posts(request):
    global login
    global check_post
    if(login==True or check_post==True):
        #login=False not done because every time /posts will be reloaded we'll have to login. Else we'll have to login every time the server restarts now.
        param = post.objects.all()
        global invalid_post
        invalid_post_temp = invalid_post
        invalid_post = False
        return render(request, 'User/posts.html', {'invalid_post':invalid_post_temp, 'param':param,})
    return redirect('/user')

def add_post(request):
    form = PostsForm
    return render(request, 'User/add_post.html', {'form':form})

def check_post1(request):
    if request.method=='POST':
        form = PostsForm(request.POST)
        if(form.is_valid()):
            form.save()
            global check_post
            check_post = True
            return redirect('/user/posts/')

        else:
            global invalid_post
            invalid_post = True
            return redirect('../')

    return redirect('/user')
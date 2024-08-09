from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # information received
        if form.is_valid():
            login(request, form.save()) # valid information saved
            return redirect("posts:list") # redirect to specific page
    else:
        form = UserCreationForm() # create an empty form
    return render(request, "users/register.html", { "form": form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST) # set kwargs to data
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST: # login from "new post", get into "new post"
                return redirect(request.POST.get("next")) 
            else: # login from "login", get into "posts list"
                return redirect("posts:list")
    else:
        form = AuthenticationForm() 
    return render(request, "users/login.html", { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")
    return render(request, "users/logout.html")
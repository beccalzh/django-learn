from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # information received
        if form.is_valid():
            form.save() # valid information saved
            return redirect("posts:list") # redirect to specific page
    else:
        form = UserCreationForm() # create an empty form
    return render(request, "users/register.html", { "form": form })
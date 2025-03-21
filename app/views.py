from django.shortcuts import render, redirect

# Index page
def index(request):
    return render(request,"app/index.html")

# Edit page
def edit_view(request):
    return render(request,"app/edit.html")
from django.shortcuts import render, redirect

# Index page
def index(request):
    if request.method == "POST":
        redirect("app:edit_view")
    return render(request,"app/index.html")

def edit_view(request):
    return render(request,"app/edit.html")
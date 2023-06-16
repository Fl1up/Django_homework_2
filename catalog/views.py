
from django.shortcuts import render


def head(request):
    return render(request, 'main/1/head.html')


def contacts(request):
    if request.method == "POST":
        firstname = request.POST.get("firstName")
        lastname = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        print(f"{firstname}, {lastname}:{username},{email}")

    return render(request, 'main/1/contacts.html')

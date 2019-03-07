from django.shortcuts import render, redirect
from .models import ContactUsModel
from .forms import ContactUsForm


# Create your views here.

# view renders to the index page
def index(request):
    return render(request, "CodeCrewApp/index.html")

# anout us page
def aboutUs(request):
    return render(request, "CodeCrewApp/aboutUs.html")

# renders to the rsource page
def resources(request):
    return render(request, "CodeCrewApp/resources.html")

# view renders to the gallery page
def gallery(request):
    return render(request, "CodeCrewApp/gallery.html")

# view has form on contacts page and renders to the contact page
def contactUs(request):
    form = ContactUsForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("allContacts")
    return render(request, "CodeCrewApp/contactUs.html", {"form": form})


# view that will list all contacts but currently incomplete
def allContacts(request):
    return render(request, "CodeCrewApp/allContacts.html", {"allContacts": ContactUsModel.objects.all()})

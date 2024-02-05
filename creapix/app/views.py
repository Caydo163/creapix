from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from features import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            with open("media/uploads/" + uploaded_file.name, "wb") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            # Traitez le fichier téléversé ici (par exemple, enregistrez-le)
            # handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "app/upload.html", {"form": form})
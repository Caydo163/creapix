from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from features import *

# Create your views here.
def index():
    return HttpResponse("Hello, world. You're at the polls index.")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            transform_type = request.POST["transform_type"]

            with open("media/uploads/" + uploaded_file.name, "wb") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            image = open_image(uploaded_file.name)

            match transform_type:
                case "grayscale":
                    image = grayscale(image)
                case "black_and_white":
                    image = black_and_white(image)
                case "fusion":
                    image = fusion(image, image, 0.5) #Ajouter la deuxième image et la sélection du ratio
                case "resize":
                    image = resize(image, (300,300)) #Ajouter la sélection de la taille
                case "gif":
                    image = animation([image, image], 1000) #Ajouter la sélection de la durée + autres images

            save_image(image)

            return render(request, "app/upload.html", {"form": form, "image": path_output_image("output.png")})
    else:
        form = UploadFileForm()

    return render(request, "app/upload.html", {"form": form})
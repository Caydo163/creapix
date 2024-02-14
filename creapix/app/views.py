from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from features import *
import os

# Create your views here.
def index(request):
    return redirect("upload")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        uploaded_files = request.FILES.getlist("files")
        transform_type = request.POST["transform_type"]

        images = []
        for uploaded_file in uploaded_files:
            with open("media/uploads/" + uploaded_file.name, "wb") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            images.append(open_image(uploaded_file.name))

        delete_images('outputs/')

        match transform_type:
            case "grayscale":
                image = grayscale(images[0])
            case "black_and_white":
                image = black_and_white(images[0])
            case "fusion":
                if len(images) < 2:
                    return render(request, "app/upload.html", {"form": form, "error": "Il faut deux images pour fusionner"})
                ratio = float(request.POST['fusion_ratio'])
                x = int(request.POST['fusion_x'])
                y = int(request.POST['fusion_y'])
                image = fusion(images[0], images[1], ratio, x, y)
            case "resize":
                width = int(request.POST['resize_width'])
                height = int(request.POST['resize_height'])
                image = resize(images[0], (height, width))
            case "gif":
                duration = int(request.POST['gif_duration'])
                filename = animation(images, duration)
            case "alignment":
                direction = True if request.POST['alignment_direction'] == "horizontal" else False
                image = alignment(images, direction)
            case _:
                image = images[0]

        if transform_type != "gif":
            filename = save_image(image, transform_type)

        delete_images('uploads/')

        return render(request, "app/upload.html", {"form": form, "image": path_output_image(filename)})
    else:
        form = UploadFileForm()

    return render(request, "app/upload.html", {"form": form})

def delete_images(folder):
    directory = "media/" + folder
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
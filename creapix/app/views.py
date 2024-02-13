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

        uploaded_files = request.FILES.getlist("files")
        transform_type = request.POST["transform_type"]

        images = []
        for uploaded_file in uploaded_files:
            with open("media/uploads/" + uploaded_file.name, "wb") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            images.append(open_image(uploaded_file.name))


        match transform_type:
            case "grayscale":
                image = grayscale(images[0])
            case "black_and_white":
                image = black_and_white(images[0])
            case "fusion":
                if len(images) < 2:
                    return render(request, "app/upload.html", {"form": form, "error": "Il faut deux images pour fusionner"})
                ratio = float(request.POST['fusion_ratio'])
                image = fusion(images[0], images[1], ratio)
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

        return render(request, "app/upload.html", {"form": form, "image": path_output_image(filename)})
    else:
        form = UploadFileForm()

    return render(request, "app/upload.html", {"form": form})
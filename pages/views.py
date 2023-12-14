from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from .forms import ImageForm
from .models import Image


class HomePageView(TemplateView):
    template_name = "home.html"


class ImageListView(ListView):
    model = Image
    template_name = "image_list.html"
    context_object_name = "images"


def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = ImageForm()
    return render(request, "upload.html", {"form": form})


def image_edit_view(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = ImageForm(instance=image)

    return render(request, "image_edit.html", {"form": form, "image": image})


def image_delete_view(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == "POST":
        image.delete()
        return redirect("image_list")

    return render(request, "image_delete.html", {"image": image})

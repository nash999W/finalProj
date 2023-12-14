from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageForm
from .models import Image
from django.core.files.storage import default_storage


class HomePageView(TemplateView):
    template_name = "home.html"


class ImageListView(ListView):
    model = Image
    template_name = "image_list.html"
    context_object_name = "images"

@login_required
def image_upload_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect("image_list")
    else:
        form = ImageForm()
    return render(request, "upload.html", {"form": form})


@login_required
def image_edit_view(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    try:
        # Check if the logged in user is the author of the image
        if image.author != request.user:
            messages.error(request, "You Dont have Permission to edit this image.")
            return redirect("home")
    except Image.author.RelatedObjectDoesNotExist:
        messages.error(request, "This image has no associated author.")
        return redirect('home')

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect("image_list")
    else:
        form = ImageForm(instance=image)
    return render(request, "image_edit.html", {"form": form, "image": image})


@login_required
def image_delete_view(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    try:
        # Check if the logged in user is the author of the image
        if image.author != request.user:
            messages.error(request, "You Dont have Permission to delete this image.")
            return redirect('home')
    except Image.author.RelatedObjectDoesNotExist:
        messages.error(request, "This image has no associated author.")
        return redirect('home')

    if request.method == "POST":
        image.delete()
        messages.error(request, "The image was successfully deleted!")
        return redirect('image_list')

    return render(request, "image_delete.html", {"image": image})
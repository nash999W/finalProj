from django.urls import path

from pages import views
from .views import HomePageView, image_upload_view, ImageListView, image_edit_view, image_delete_view

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("upload/", image_upload_view, name="upload"),
    path("image-list/", ImageListView.as_view(), name="image_list"),
    path("image-edit/<int:image_id>/", image_edit_view, name="image_edit"),
    path('image/<int:image_id>/', image_delete_view, name='image_delete')
]
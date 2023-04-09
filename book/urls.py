from django.urls import path, include
from .views import *

urlpatterns = [
    # path("hello/", HelloAPI.as_view()),
    path("books/", BooksAPIMixins.as_view()),
    path("book/<int:bid>/", BookAPIMixins.as_view()),
]

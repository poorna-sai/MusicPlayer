from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name='Home'),
    path("Upload/" , Upload_song , name ="Upload_song"),
    path("ViewFolder/<pk>/" , ViewFolder , name = "ViewFolder"),
    path("DeleteSong/<pk>/" , DeleteSong , name = "DeleteSong"),

]
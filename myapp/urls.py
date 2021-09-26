from django.urls import path
from .views import *


urlpatterns = [
    path('aboutus/', show_about_page, name='about'),
    path('home/', show_home_page, name='home'),
    path('category/<int:cid>/', show_category_page, name='category'),
    path('home/<int:iid>/', show_images_detail, name='detail'),
    path('', home),
]

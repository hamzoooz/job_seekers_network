from django.urls import path 
from .import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    path('category', views.category, name='category'),
    path('price', views.price, name='price'),
    path('blog-home', views.blog_home, name='blog_home'),
    path('contact', views.contact, name='contact'),

    path('elements', views.elements, name='elements'),
    path('search', views.search, name='search'),
    path('single/<int:id>', views.single, name='single'),
]




from django.urls import path
from .views import home_view,contact_view,blog_view,blog_detail_view,services_view,team_view, portfolio_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('contact/',contact_view,name='contact-page'),
    path('blog.html',blog_view,name='blog-page'),
    path('blog/<int:id>/',blog_detail_view,name='blog-detail-page'),
    path('services.html',services_view,name='services-page'),
    path('team/',team_view,name='team-page'),
    path('portfolio-1.html',portfolio_view,name='portfolio-page'),
]

from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('/index', TemplateView.as_view(template_name='index.html'), name='index'),
    path('/contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('/product', TemplateView.as_view(template_name='product.html'), name='product'),

    path('users/', include('users.urls')),
]
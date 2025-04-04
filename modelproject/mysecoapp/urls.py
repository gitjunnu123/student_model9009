from django.contrib import admin
from django.urls import path
from mysecoapp import views

urlpatterns=[
    path("admin/", admin.site.urls),
    path('raj/',views.raj_view),
    path('test/',views.test_view)


]
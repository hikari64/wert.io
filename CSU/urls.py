"""CSU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import path, include
from django.contrib import admin
from Home import views
urlpatterns=[
    path('',views.home, name='home'),
	path('gpasystem/',include('GPA_System.urls')),
	path('admin/',admin.site.urls)
]

"""CSU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import path, include
from django.contrib import admin
from csu import views as csu
urlpatterns=[
	path('',csu.home,name='csu'),
	path('gpasystem/',include('gpasystem.urls')),
	path('admin/',admin.site.urls)
]

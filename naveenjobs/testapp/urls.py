from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home_page_View),
    path('hydjobs/',views.Hyd_View)
]
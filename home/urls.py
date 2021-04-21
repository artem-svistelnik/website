from django.urls import path
from .views import HomePageView,AboutCompanyPageView,Activities,TestView
app_name = "home"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('home_pages/', HomePageView.as_view()),
    path('about_company/', AboutCompanyPageView.as_view()),
    path('activities/', TestView.as_view()),
    # path('ggg/', HomePageGalleryView.as_view()),
    # path('test/', TestView.as_view()),
]

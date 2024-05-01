from django.urls import path
from .views import HomePageView, AboutPageView, ProjectsView, ContactView

urlpatterns = [
   path("about/", AboutPageView.as_view(), name="about"), # new
   path("", HomePageView.as_view(), name="home"),
   path("projects/", ProjectsView.as_view(), name="projects"),
    path("contact/", ContactView.as_view(), name="contact"),
]
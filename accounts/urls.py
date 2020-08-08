from django.urls import path
from . import views
urlpatterns = [
    path("logout", views.logout, name="logout" ),
    path("update/<str:pk>/", views.update, name="update" ),
    path("delete/<str:pk>", views.supprimer, name="delete"), 
    path("publish", views.afficher, name="publish"),
    path("offres", views.submitoffer, name="offres"),
    path("register", views.register, name="register"),
    path("", views.signin, name="login"),
]

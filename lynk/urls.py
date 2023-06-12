from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout/", views.logout, name="logout"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile/<int:user_id>/edit", views.edit_profile, name="edit_profile"),
    path("create_user", views.create_user, name="create_user"),
    path("update_user/<int:user_id>/", views.update_user, name="update_user"),
    path("p/<str:username>/", views.public_show, name="public_show"),
    path("profile/<int:user_id>/create_element",
         views.create_element, name="create_element"),
    path("profile/<int:user_id>/elements/new/",
         views.add_element, name="add_element"),
    path("profile/<int:user_id>/elements/edit/<int:element_id>/",
         views.edit_element, name="edit_element"),
    path("profile/<int:user_id>/elements/update/<int:element_id>",
         views.update_element, name="update_element"),
    path("profile/<int:user_id>/elements/delete/<int:element_id>",
         views.delete_element, name="delete_element"),
]

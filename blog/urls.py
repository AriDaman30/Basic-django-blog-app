from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_post,name='create_post'),
    path('delete/<int:post_id>/', views.delete_post,name='delete_post'),
]
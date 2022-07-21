from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>/', views.viewPost, name='post'),
    path('add/', views.addPhoto, name='add'),
    path('data/', views.load_post_data_view, name='data'),
    path('gallery/<str:category>', views.view_category, name='view_category'),
    path('rate-post/', views.rate_post, name='rate'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userPage, name='user'),
    path('view_publications/', views.userViewPublications, name='view_publications'),
    path('add_publication/', views.userAddPublications, name='add_publication'),
    path('delete_publications/', views.userDeletePublications, name='del_publications'),
    path('edit_publications/', views.userEditPublications, name='edit_publications'),
    path('update_publications/', views.userUpdatePublications, name='update_publications'),
    path('search-publication/', views.search_publication, name='search-publication')
]
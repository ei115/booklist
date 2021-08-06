from django.urls import path
from .views import Index, Create, Detail, Update, Delete, Login, SignUp
from .import views


app_name = 'booklist'

urlpatterns = [
    path('',views.Index.as_view(), name='index'),  
    path('create',views.Create.as_view(), name='create'), 
    path('detail/<int:pk>',views.Detail.as_view(), name='detail'), 
    path('update/<int:pk>',views.Update.as_view(), name='update'), 
    path('delete/<int:pk>',views.Delete.as_view(), name='delete'),
    path('login',views.Login.as_view(), name='login'), 
    path('logout',views.Logout.as_view(), name='logout'), 
    path('signup',views.SignUp.as_view(), name='signup'), 
]
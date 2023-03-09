
from unicodedata import name
from . import views
from django.urls import path
from accounts.views import register,login,logout

# urlpatterns = [
    
    # path('',views.postlist.as_view(),name='home'),
    # path('<slug:slug>/',views.postlist.as_view(),name='postdetail')
   
    # path('new',views.new,name='new'),
    # path('signin',views.signin,name="signin"),
    # path('postsign',views.postsign)
     
urlpatterns = [

    path('index',views.index,name="index"),
    path('detailed/',views.index,name='detailed'),

    path("",register), 
    path("login/",login),
    path("logout/",logout),

    # path('', views.signIn),
    # path('postsignIn/', views.postsignIn),
    # path('signUp/', views.signUp, name="signup"),
    # path('logout/', views.logout, name="log"),
    # path('postsignUp/', views.postsignUp),
    path('check',views.check,name="check"),


]
 
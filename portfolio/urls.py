from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.login),
    path('register/',views.register,name='register'),
    path('home/',views.postsignIn),
    path('Home/',views.home,name='home'),
    path('signup/',views.postsignup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('transaction/',views.transaction,name='transaction'),
    path('graphics/',views.graphics,name='graphics'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('transaction/',views.add,name='add')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
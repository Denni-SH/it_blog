
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from blog_auth import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/login/', blog_views.SignIn.as_view(), name='login'),
    url(r'^account/logup/', blog_views.SignUp.as_view(), name='register'),
    url(r'^account/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'',include('blog_auth.urls')),
]

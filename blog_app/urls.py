from django.conf.urls import url
from blog_app import views
urlpatterns = [
    url(r'^$',views.hello,name='hello'),
]
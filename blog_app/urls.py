from django.conf.urls import url
from blog_app import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$',views.CategoryListView.as_view(), name='CategoryList'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_list, name='PostList'),
    url(r'^post/(?P<pk>[0-9]+)$', views.PostDetails.as_view(), name='PostDetail'),
    url(r'^new_post$', views.NewPost.as_view(), name='NewPost'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.EditPost.as_view(), name='EditPost'),
    # url(r'^$', views.BookListView.as_view(), name='SearchPost'),
    # url(r'^$', views.BookListView.as_view(), name='AddComment'),
    # url(r'^$', views.BookListView.as_view(), name='EditComment'),
]

from django.conf.urls import url
from blog_auth import views



urlpatterns = [
    url(r'^$',views.CategoryListView.as_view(), name='CategoryList'),
    url(r'^(?P<pk>\d+)/$', views.post_list, name='PostList'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetails.as_view(), name='PostDetail'),
    url(r'^new_post$', views.NewPost.as_view(), name='NewPost'),
    url(r'^edit/(?P<pk>\d+)$', views.EditPost.as_view(), name='EditPost'),
    url(r'^post/(?P<pk>\d+)/add_comment/$', views.add_comment, name='AddComment'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.remove_comment, name='RemoveComment'),
    url(r'^post/(?P<pk>\d+)/addlike/', views.add_like, name='add_like'),
]

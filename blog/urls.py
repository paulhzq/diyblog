from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^blogs/$',views.BlogListView.as_view(),name='blogs'),
    url(r'^blogs/(?P<pk>\d+)$',views.BlogDetailView.as_view(), name='blog-detail'),
]

from django.conf.urls import patterns, url
from books import views

urlpatterns = patterns('',
    url(r'^$', views.BooksModelView.as_view(), name='index'), # /books

    url(r'^book/$', views.BookList.as_view(), name='book_list'), # /books/book/
    url(r'^author/$', views.AuthorList.as_view(), name='author_list'), # /books/author/
    url(r'^publisher/$', views.PublisherList.as_view(), name='publisher_list'), # /books/publisher/

    url(r'^book/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'), # /books/book/3
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'), # /books/author/3
    url(r'^publisher/(?P<pk>\d+)/$', views.PublisherDetail.as_view(), name='publisher_detail'), # /books/publisher/3
)


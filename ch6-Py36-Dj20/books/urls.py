from django.urls import path
from books import views


app_name = 'books'
urlpatterns = [
    path('', views.BooksModelView.as_view(), name='index'), # /books/

    path('book/', views.BookList.as_view(), name='book_list'), # /books/book/
    path('author/', views.AuthorList.as_view(), name='author_list'), # /books/author/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'), # /books/publisher/

    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'), # /books/book/3
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'), # /books/author/3
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'), # /books/publisher/3
]

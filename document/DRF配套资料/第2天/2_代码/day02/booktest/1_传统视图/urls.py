from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^books/$', views.BookInfoView.as_view()),
    url(r'^books/(?P<book_id>\d+)/$', views.BookInfoDetailView.as_view()),
]
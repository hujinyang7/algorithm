from booktest import views

urlpatterns = [
]

#1,url部分
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('books', views.BookViewSet, base_name="books")
urlpatterns += router.urls
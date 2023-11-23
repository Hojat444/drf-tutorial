from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

# baraye bedoon viewset ha
# urlpatterns = [
#     path("users/",views.UserList.as_view()),
#     path("users/<int:pk>",views.UserDetail.as_view()),
#     path("<int:pk>/",views.BookDetail.as_view()),
#     path("",views.BookList.as_view()),
# ]

router = SimpleRouter()
router.register("users",views.UserViewSet,basename="users")
router.register("",views.BookViewSet,basename="books")

urlpatterns = router.urls



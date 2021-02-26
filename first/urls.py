from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from demo import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]

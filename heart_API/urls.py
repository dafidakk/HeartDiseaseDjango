from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('heart_API', views.ApprovalsView)


urlpatterns = [
    path('',views.index, name='index'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
    path('form/', views.cxcontact, name = 'heart_disease'),
]

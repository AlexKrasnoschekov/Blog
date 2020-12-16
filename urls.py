from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
from .import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

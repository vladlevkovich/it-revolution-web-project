from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('pizza/<int:pizza_pk>/', buy, name='buy'),
    path('create-order/', create_order, name='order')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

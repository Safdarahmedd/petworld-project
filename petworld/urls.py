from django.contrib import admin
from django.urls import path,include
from pets import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

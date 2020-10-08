"""booking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from booking_app import views

# 2 imports for media
from django.conf import settings
from django.conf.urls.static import static

# 2 imports for registration
from registration.backends.simple.views import RegistrationView
from django.urls import reverse

# Overridden RegistrationView
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('booking_app:register_profile')

# Urls
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('booking_system/', include('booking_app.urls')),
    path('admin/', admin.site.urls),
    
    # Reference to the registration package
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    
    # Final step for media (serve static content from MEDIA_URL)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

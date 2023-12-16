from django.contrib import admin
from django.urls import path, include  # Include the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Event_App.urls')),  # Include the URLs of 'event_app'
    # Add other URL patterns if needed
]

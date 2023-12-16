from django.urls import path
from .views import EventBookingView

urlpatterns = [
    path('book-event/', EventBookingView.as_view(), name='book-event'), 
]

#EventBookingView (as a View):
# The EventBookingView is expected to be a Django class-based view that handles the logic for booking an event. 
# In Django, views process incoming requests and return responses.
# A view can render a template, return JSON data, perform actions on the database, etc., 
# depending on your application's requirements.
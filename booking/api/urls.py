from django.urls import path
from booking.api import views


urlpatterns = [
    path("", views.testView),
    #
    path("checkAvailability/",views.checkAvailabilityView),
    path("allResources/",views.allResource.as_view()),
    path("book/",views.bookView),
    path("allBookings",views.getAllBookings)
]

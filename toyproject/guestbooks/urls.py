from django.urls import path
from guestbooks.views import *

urlpatterns = [
    path('<int:guestbook_id>/', guestbook_detail, name = "guestbook_detail"),
    path('', guestbook_list, name = "guestbook_list")
]
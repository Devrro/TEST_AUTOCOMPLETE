from django.urls import path

from apps.user.views import CreateListUserView

urlpatterns = [
    path('', CreateListUserView.as_view())
]
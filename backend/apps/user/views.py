from apps.user.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CreateListUserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        qs = self.queryset
        qs.filter(__)

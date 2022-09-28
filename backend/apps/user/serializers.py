from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model
from .models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id',
            'is_staff',
            'is_superuser',
            'created_at',
            'updated_at',
            'email',
            'password',
            'profile',
        )
        read_only_fields = (
            'id',
            'is_staff',
            'is_superuser',
            'created_at',
            'updated_at',
            'profile',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user

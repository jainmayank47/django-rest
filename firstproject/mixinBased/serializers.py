from rest_framework import serializers
from mixinBased.models import UserInfo

class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
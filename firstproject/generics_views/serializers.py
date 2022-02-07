
from rest_framework import serializers
from generics_views.models import TechnologyInfo,FrameworkInfo

class TechnologyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=TechnologyInfo
        fields = "__all__"

class FrameworkInfoSerializers(serializers.ModelSerializer):
    framework = TechnologyInfoSerializers(read_only=True,many=False)
    class Meta:
        model = FrameworkInfo
        fields = "__all__"
        #depth = 1

class TechnologyInfoListSerializers(serializers.ModelSerializer):
    framework = TechnologyInfoSerializers(read_only=True,many=True)
    class Meta:
        model=TechnologyInfo
        fields = ("id","name","framework")

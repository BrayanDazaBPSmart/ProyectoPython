from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from men_data.models import Info

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()

class FirstQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['ies','graduados','matriculados']

class SecondQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['nivel_formacion','matriculados']

class ThirdQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['nivel_formacion','matriculados']

class FifthQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['ies','matriculados']

class SeventhQSerializer(ModelSerializer):
    masculino = serializers.IntegerField()
    femenino = serializers.IntegerField()
    cantida_jovenes = serializers.IntegerField()

    class Meta:
        model = Info
        fields = ['anio','ies','masculino','femenino','cantida_jovenes']

class EtniaQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['anio','matriculados']
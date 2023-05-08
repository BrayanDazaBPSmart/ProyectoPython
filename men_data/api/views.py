from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from django.forms import model_to_dict
from men_data.models import Info
import men_data.api.serializers as serializers

class InfoApiViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSerializer

class FirstApiViewSet(ModelViewSet):
    queryset = Info.objects.values('ies').annotate(graduados=Sum('graduados')).annotate(matriculados=Sum('matriculados')).order_by('-graduados')
    serializer_class = serializers.FirstQSerializer

class SecondApiViewSet(ModelViewSet):
    queryset = Info.objects.values('nivel_formacion').annotate(matriculados=Sum('matriculados')).order_by()
    serializer_class = serializers.SecondQSerializer

class ThirdApiViewSet(ModelViewSet):
    queryset = Info.objects.values('nivel_formacion').annotate(matriculados=Sum('matriculados')).order_by('-matriculados')
    serializer_class = serializers.ThirdQSerializer

class FifthApiViewSet(ModelViewSet):
    queryset = Info.objects.values('ies').annotate(matriculados=Sum('matriculados')).order_by('-matriculados')
    serializer_class = serializers.FifthQSerializer

class SeventhApiViewSet(ModelViewSet):
    queryset = Info.objects.values('anio','ies').annotate(masculino=Sum('matriculados',filter=Q(sexo='MASCULINO'))).annotate(femenino=Sum('matriculados',filter=Q(sexo='FEMENINO'))).annotate(cantida_jovenes=Sum('matriculados')).order_by('-cantida_jovenes')
    serializer_class = serializers.SeventhQSerializer

class EtniaApiViewSet(ModelViewSet):
    queryset = Info.objects.values('anio').annotate(matriculados=Sum('matriculados')).order_by()
    serializer_class = serializers.EtniaQSerializer

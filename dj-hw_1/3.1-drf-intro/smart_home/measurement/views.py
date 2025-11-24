# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ChangeSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateMeasurementView(CreateAPIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        data = request.data
        sensor = Sensor.objects.get(id=data['sensor'])
        temperature = data['temperature']
        Measurement(sensor=sensor, temperature=temperature).save()
        return Response({'status': 'OK'})

class SensorDetailsView(RetrieveAPIView):

    queryset = Sensor.objects.all().prefetch_related('sensor')
    serializer_class = SensorDetailSerializer


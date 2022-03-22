from rest_framework import generics
from .models import Covid
from .serializer import CovidSerializer
from api.mixins import IsStaffEditorPermissionMixin
class CovidListCreateAPIView(IsStaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Covid.objects.all()
    serializer_class = CovidSerializer
    
    # def perform_create(self,serializer):
    #     #print(serializer.validated_data)
    #     iso_code = serializer.validated_data.get('iso_code')
    #     location = serializer.validated_data.get('location') or None
    #     if location is None:
    #         iso_code = location
    #     serializer.save(location=location)

class CovidDetailAPIView(IsStaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Covid.objects.all()
    serializer_class = CovidSerializer
    #lookup_field = "pk"

class CovidUpdateAPIView(IsStaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Covid.objects.all()
    serializer_class = CovidSerializer
    lookup_field = "pk"

    # def perform_update(self,serializer):
    #     instance = serializer.save()
    #     if not instance.location:
    #         instance.location = instance.iso_code

class CovidDestroyAPIView(IsStaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Covid.objects.all()
    serializer_class = CovidSerializer
    lookup_field = "pk"

    def perform_destroy(self,instance):
        #instance
        super().perform_destroy(instance)



    

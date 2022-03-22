from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Covid

class CovidSerializer(serializers.ModelSerializer):
    edit_detail_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name="data-detail",lookup_field = "pk")
    class Meta:
        model = Covid
        fields = '__all__'
    
    def get_edit_detail_url(self,obj):
        #return f"/api/covid/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("edit-data-detail",kwargs={"pk":obj.pk},request=request)
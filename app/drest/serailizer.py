from dynamic_rest import serializers
from dynamic_rest.fields import *

from .models import Lno


class LnoSerializer(serializers.DynamicModelSerializer):
    rname = DynamicField(source='rname.username', read_only=True)

    class Meta:
        model = Lno
        name = 'lottery'
        fields = ('id', 'lno', 'cname', 'rname', 'contact', 'address')

# class ResellerSerializer(serializers.DynamicModelSerializer):
#     saledatas = serializers.RelatedField(queryset=Lno.objects.all(), many=True, default=True)
#
#     class Meta:
#         model = Reseller
#         fields = ('reseller_name', 'ph', 'address', 'saledatas')

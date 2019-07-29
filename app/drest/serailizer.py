from dynamic_rest import serializers
from dynamic_rest.fields import *

from .models import Lno


class LnoSerializer(serializers.DynamicModelSerializer):
    reseller = DynamicField(source='reseller.username', read_only=True)

    class Meta:
        model = Lno
        name = 'lottery'
        fields = ('id', 'lno', 'cname', 'reseller', 'contact', 'address')

# # class UserSerializer(serializers.DynamicModelSerializer):
# #     # lotteries = DynamicRelationField('LnoSerializer', source='lno_set', many=True, deferred=True)
# #     # lot_count = CountField('lotteries', required=False, deferred=True)
# #     lotteries = DynamicRelationField(source='Lno')
# 
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'lotteries')

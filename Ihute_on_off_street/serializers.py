from rest_framework import serializers
from .models import *

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class Proposed_insucoversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposed_insucovers
        fields = '__all__'
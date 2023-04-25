from rest_framework import serializers

from .models import Package, Subscription

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['filter', 'sku', 'descriptions', 'avatar', 'price', 'duration']


class SubscriptionSerializers(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ['package', 'created_time', 'expire_time']

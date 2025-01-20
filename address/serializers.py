from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


    def validate_zip_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Zip code faqat raqamlardan iborat bo'lishi kerak.")
        return value

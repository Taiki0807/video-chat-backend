from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["username", "password"]

    def create(self, validated_data):
        user = Account(
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

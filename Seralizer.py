from rest_framework import  serializers
from .models import post

class PostSeralizer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields =(
            "Email",
            "Password",
            "Server",
            "Port"
        )
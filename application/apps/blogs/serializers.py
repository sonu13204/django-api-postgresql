from rest_framework import serializers
from .models import Blogs
from django.contrib.auth import get_user_model


class BlogSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    class Meta:
        model = Blogs
        fields = ('id', 'user', 'fullname','title', 'content', 'created_on')

    def validate_title(self, value):
        qs = Blogs.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Tittle already used.')
        return value

    def get_fullname(self,obj):
        full_name = obj.user.username
        return full_name
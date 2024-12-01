from rest_framework import serializers
from.models import BlogPost

class BlogPostSeializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost 
        fields = ["id", "title", "published_date"]
        

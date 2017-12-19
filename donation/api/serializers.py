from rest_framework import serializers

class CommentSerializer(serializers.Serializer): 

    email = serializers.EmailField()
    message = serializers.CharField()
    # name = serializers.CharField()
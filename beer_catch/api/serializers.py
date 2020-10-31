from rest_framework import serializers
from .models import ImageUpload, User, Beer, Review, Like, Ingredient

class ImageUploadSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ImageUpload
        fields = ('url', 'pk', 'title', 'image')

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('__all__')

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    like = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'user_id', 'name', 'nickname', 'email', 'gender', 'type', 'like')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'content', 'date', 'score', 'beer', 'user')

class ReviewInfoSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Review
        fields = ('id', 'content', 'date', 'score', 'nickname')

class BeerSerializer(serializers.ModelSerializer):
    review = ReviewInfoSerializer(many=True, read_only=True)
    ingredient = serializers.StringRelatedField(many=True)
    class Meta:
        model = Beer
        fields = ('id', 'kor_name', 'eng_name', 'description', 'country', 'alcohol', 'type', 'ingredient', 'review')

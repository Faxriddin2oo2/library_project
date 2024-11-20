from drf_yasg.codecs import VALIDATORS
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        # print(data)
        title = data.get('title', None)
        author = data.get("author", None)


        # check title if it contain only alphabetical chars
        if title.isalpha():
            raise ValidationError(
                {
                    "status" : False,
                    "message" : "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak"
                }
            )

        # check title and author from database existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise  ValidationError(
                {
                    "status": False,
                    "message": "Narx notog'ri kiritilgan"
                }
            )

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#     subtitle = serializers.CharField()

# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length=150)
#     output = serializers.CharField(max_length=120)
from rest_framework import serializers
from Library.models import Book
from Users.models import Enrollment, User
import datetime


class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'genre']


class ListMyBookSerializer(serializers.ModelSerializer):
    book = ListBookSerializer()
    days_held = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['book', 'data', 'days_held']

    def get_days_held(self, obj):
        today = datetime.date.today()
        delta = today - obj.data
        return delta.days


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'address']


class ListDebtorsSerializer(serializers.ModelSerializer):
    book = ListBookSerializer()
    days_held = serializers.SerializerMethodField()
    reader = ReaderSerializer()

    class Meta:
        model = Enrollment
        fields = ['reader', 'book', 'data', 'days_held']

    def get_days_held(self, obj):
        today = datetime.date.today()
        delta = today - obj.data
        return delta.days

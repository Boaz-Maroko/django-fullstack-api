from rest_framework import serializers
from .models import Student

# creating serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'age']


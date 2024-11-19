from rest_framework import serializers
from .models import Question, Subject


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        

from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    def validate_name(self, value):
        if Subject.objects.filter(name=value).exists():
            raise serializers.ValidationError("Subject with this name already exists.")
        return value

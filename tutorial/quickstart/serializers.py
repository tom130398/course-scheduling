from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Course
from .models import Curriculum
from .models import Groupstudy
from .models import Implementation
from .models import Room
from .models import Teacher
from .models import TeacherImplementation

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'code', 'name', 'credit', 'curriculumid')


class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'groupid')

class GroupstudySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Groupstudy
        fields = ('url', 'code', 'degreeprogram')

class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implementation
        fields = ('url', 'group', 'courseid')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'room', 'topic', 'courseid')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'name', 'code')

class TeacherImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherImplementation
        fields = ('url', 'teacherid', 'implementationid')        
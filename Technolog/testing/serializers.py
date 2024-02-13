from rest_framework import serializers
from testing.models import ForeignKeyTest, ForeignKeyTestF

class ForeignKeyTestS(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    number = serializers.IntegerField()
    class Meta:
      model = ForeignKeyTest
      fields = ("id", "name","number")


class ForeignKeyTestFS(serializers.ModelSerializer):
    id = serializers.IntegerField()
    foreign_key_test = serializers.SlugRelatedField(
       slug_field = "name",
       queryset = ForeignKeyTest.objects,

    )
    name_f = serializers.CharField(max_length=255)
    number_f = serializers.IntegerField()
    class Meta:
      model = ForeignKeyTestF
      fields = ("id", "name_f","number_f", 'foreign_key_test')
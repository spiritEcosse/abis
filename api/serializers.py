from rest_framework import serializers
from api.models import Person
from random import randint


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', )

    def to_representation(self, instance):
        context = super(PersonSerializer, self).to_representation(instance)
        context['similarity'] = randint(110, 200)
        context['person_type'] = ''
        context['person_id'] = 175609
        return context


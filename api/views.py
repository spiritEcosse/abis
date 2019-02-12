# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponseBadRequest

from api.models import Person
from api.serializers import PersonSerializer

from random import randint
from collections import OrderedDict
import json

class JsonResponse409(JsonResponse):
    status_code = 409


class JsonResponse400(JsonResponse):
    status_code = 400


class JsonResponse401(JsonResponse):
    status_code = 401


class JsonResponse201(JsonResponse):
    status_code = 201


class JsonResponse201(JsonResponse):
    status_code = 201


class IdentificationViews(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(OrderedDict([
            ('count', len(serializer.data)),
            ('queue', self.request.GET['queue']),
            ('status', 3),
            ('status_detail', 'Detail'),
            ('persons', [{"similarity": 500, "person_id": 175609}]),
        ]))

    def post(self, request, **kwargs):
        # return JsonResponse401({'detail': 'Помилка авторизації: надано недійсний токен, або такий, що не дозволяє виконувати поточний запит'})
        return Response({'queue': randint(1, 100000000)})


class VerificationViews(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['post', 'get']

    def retrieve(self, request, *args, **kwargs):
        return Response(OrderedDict([
            ('queue', self.request.GET['queue']),
            ('status', 3),
            ('status_detail', 'Detail'),
            # ('similarity', randint(110, 200))
            ('similarity', randint(1, 2))
        ]))

    def post(self, request, *args, **kwargs):
        return Response({'queue': randint(1, 100000000)})


class CreateViews(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['post', 'get']

    def retrieve(self, request, *args, **kwargs):
        # return JsonResponse400({'detail': 'CreateViews detail'})
        # return JsonResponse409({'status_detail': 'CreateViews Detail'})
        return Response(OrderedDict([
            ('queue', self.request.GET['queue']),
            ('status', 3),
            ('status_detail', 'CreateViews Detail'),
        ]))

    def post(self, request, *args, **kwargs):
        queue = randint(1, 100000000)
        return Response({'queue': queue})


class RnokppRejectionViews(viewsets.GenericViewSet):
    queryset = Person.objects.all()
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        # return JsonResponse400({'detail': 'CreateViews detail'})
        raise Exception(type(request.data), request.data)
        return Response(json.loads(request.data))


class DeleteViews(viewsets.generics.RetrieveDestroyAPIView):
    def get(self, request, *args, **kwargs):
        # return JsonResponse409({'detail': 'DeleteViews detail'})
        return Response(OrderedDict([
            ('queue', self.request.GET['queue']),
            ('status', 3),
            # ('status_detail', 'Detail'),
        ]))

    def delete(self, request, *args, **kwargs):
        return Response({'queue': randint(1, 100000000)})

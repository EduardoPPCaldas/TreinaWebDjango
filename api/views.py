from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .service.cidades_atendimento_service import listar_diaristas_cidade
from .serializers import diaristas_cidade_serializer
from .pagination.diaristas_cidade_pagination import DiaristasCidadePagination

class DiaristasCidadeList(APIView, DiaristasCidadePagination):
  def get(self, request, format=None):
    cep = self.request.query_params.get("cep", None)
    diaristas = listar_diaristas_cidade(cep)
    resultado = self.paginate_queryset(diaristas, request)
    serializer = diaristas_cidade_serializer.DiaristaCidadeSerializer(resultado, many=True, context={"request":request})

    return self.get_paginated_response(serializer.data)
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view()  # defaultu GET tir
def home(request):
    return Response({"home": "This is home page"})

# http methods----->
# GET,(DB den veri çağırma, public)
# POST(DB de değişiklil, creative, privative)
# PUL(DB kayıt değişikliği)
# DELETE(DB de kasyıt silme)
# PATCH(tek fielda değişiklik yapılınca sadece onu update yapar DB)
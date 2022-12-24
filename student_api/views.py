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
# PUT(DB kayıt değişikliği)
# DELETE(DB de kasyıt silme)
# PATCH(tek fielda değişiklik yapılınca sadece onu update yapar DB)

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    # print(students)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer =StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message": f'Student updated succesfully...'
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def student_detail(request, pk):
  
    student = get_object_or_404.get(id=pk)
    # student = Student.object.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)   

@api_view(['PUT'])
def student_update(request,pk):
    student = get_object_or_404.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)




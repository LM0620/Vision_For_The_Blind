from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
from rest_framework import status
from testUpload import text as txt
from os import path as path


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            up_pic = request.FILES['file']
            new_path = path.dirname(path.abspath(__file__)) + up_pic.name
            destination = open(new_path,'wb+')
            for chunk in up_pic.chunks():
                destination.write(chunk)
            output = txt.get_setence(new_path)
            destination.close()
            return Response(output, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

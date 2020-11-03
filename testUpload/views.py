from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
from rest_framework import status


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            up_pic = request.FILES['file']
            destination = open('/Users/wenruowang/Downloads/CS499/testUpload/media' + up_pic.name,'wb+')
            for chunk in up_pic.chunks():
                destination.write(chunk)
            destination.close()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

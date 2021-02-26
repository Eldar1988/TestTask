from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Image, ImageAction
from .serializers import ImageCreateSerializer, ImageListSerializer
from .service import new_image_action, send_image_uploaded_mail


class ImageListView(APIView):

    def get(self, request, pk):
        images = Image.objects.filter(user_id=pk)
        serializer = ImageListSerializer(images, many=True)
        return Response(serializer.data)


class ImageActionsView(APIView):
    """
    Метод get - удаляет картинку по id
    Метод post - добавляет картинку по id
    Метод put - изменяет картинку по id
    """

    parser_classes = [MultiPartParser, FileUploadParser]

    def get(self, request, pk):
        image = Image.objects.get(id=pk)
        image_actions = ImageAction.objects.filter(image_id=image.id)
        for i in image_actions:
            i.delete()
        image.delete()
        return Response(status=200)

    def post(self, request, pk):
        serializer = ImageCreateSerializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.save(user_id=pk)
            new_image_action(ImageAction, obj, 'uploaded')
            send_image_uploaded_mail(request.user, obj)
            return Response(status=200)

    def put(self, request, pk):
        image = Image.objects.get(id=pk)
        serializer = ImageCreateSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            obj = serializer.save()
            new_image_action(ImageAction, obj, 'updated')
            return Response(status=200)

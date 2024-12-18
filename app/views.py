from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Shortened, ShortenRequest
from .serializers import ShortenedSerializer, ShortenRequestSerializer

from django.shortcuts import redirect
from django.utils import timezone
import pytz
import uuid


@api_view(["GET"])
def home(request: Request):
    return Response()


@api_view(["GET"])
def auto_redirect(request: Request, shortened_url: str):
    shorten_response = Shortened.objects.filter(shortCode__exact=shortened_url).first()
    if shorten_response:
        return redirect(shorten_response.url)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def set_shorten(request: Request):
    request_serializer = ShortenRequestSerializer(data=request.data)
    if request_serializer.is_valid():
        shorten_response = Shortened.objects.filter(
            url__exact=request_serializer.data["url"]
        ).first()
        if shorten_response:
            return Response(
                {"shortCode": shorten_response.shortCode},
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            shortened = Shortened()
            shortened.shortCode = str(uuid.uuid4()).split("-")[0]
            shortened.url = request_serializer.data["url"]
            shortened.createdAt = timezone.now()
            shortened.save()
            return Response(
                {"shortCode": shortened.shortCode}, status=status.HTTP_201_CREATED
            )
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def shorten(request: Request, shortened_url: str):
    shorten_response = Shortened.objects.filter(shortCode__exact=shortened_url).first()
    if shorten_response:
        if request.method == "GET":
            return Response(ShortenedSerializer(shorten_response).data)
        if request.method == "PUT":
            request_serializer = ShortenRequestSerializer(data=request.data)
            if request_serializer.is_valid():
                shorten_response.url = request_serializer.data["url"]
                shorten_response.updatedAt = timezone.now()
                shorten_response.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        if request.method == "DELETE":
            shorten_response.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

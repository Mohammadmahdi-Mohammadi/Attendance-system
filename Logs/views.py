from .serializers import Createlog_Serializer,Deletelog_Serializer,Upadatelog_Serializer, CreateLeave_Serializer, DeleteLeave_Serializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics


class CreateLog(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Createlog_Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        current_user = request.user
        serializer.context["user_request"] = current_user
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteLog(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Deletelog_Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        current_user = request.user
        serializer.context["user_request"] = current_user
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Upadatelog(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = Upadatelog_Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        current_user = request.user
        serializer.context["user_request"] = current_user
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateLeave(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateLeave_Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        current_user = request.user
        serializer.context["user_request"] = current_user
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteLeave(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DeleteLeave_Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        current_user = request.user
        serializer.context["user_request"] = current_user
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
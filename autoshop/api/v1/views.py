from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from autoshop.api.v1.serializers import UserProfileSerializer
from core.models import Profile


class UserProfileViewSet(ModelViewSet):
    permissions_classes = (permissions.IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

    def list(self, request):
        queryset = Profile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        queryset = Profile.objects.get(pk=kwargs.get('pk'))
        serializer = UserProfileSerializer(queryset, data=request.data, partial=True)
        serializer.save()
        return JsonResponse(serializer.data)

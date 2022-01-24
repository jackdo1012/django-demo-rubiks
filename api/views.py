from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import RubiksSerializer
from .models import Rubiks

class RubiksView(APIView):

    def get(self, request):
        rubiks = Rubiks.objects.all()
        data = RubiksSerializer(rubiks, many=True).data
        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RubiksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SpecificRubiksView(APIView):

    def get_object(self, pk):
        try:
            return Rubiks.objects.get(pk=pk)
        except Rubiks.DoesNotExist:
            return Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = RubiksSerializer(snippet)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        print('hllo')
        Rubiks.objects.get(pk = pk).delete()
        return Response({"success": True, "message": "Rubiks deleted"}, status=status.HTTP_200_OK)

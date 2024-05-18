from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import report
from .serializer import ReportPostSerializer


# Create your views here.
def get_data(request):
    return render(request, 'GetReport/getdata.html')


class ReportPostListCreate(generics.ListCreateAPIView):
    queryset = report.objects.all()
    serializer_class = ReportPostSerializer

    def delete(self, request, *args, **kwargs):
        report.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReportPostUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = report.objects.all()
    serializer_class = ReportPostSerializer
    lookup_field = "pk"

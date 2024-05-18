from django.urls import path
from . import views

urlpatterns = [
    path('getdata/', views.get_data, name='getdata'),
    path('report/', views.ReportPostListCreate.as_view(), name='Report-Post-List-Create'),
    path('report/<int:pk>', views.ReportPostUpdateDestroy.as_view(), name='Report-Post-Update-Destroy'),

]


from django.urls import path,include
from Logs import views



urlpatterns = [
    path('Createlog/', views.CreateLog.as_view()),
    path('Deletelog/', views.DeleteLog.as_view()),
    path('Updatelog/', views.Upadatelog.as_view()),
    path('Createleave/', views.CreateLeave.as_view()),
    path('Deleteleave/', views.DeleteLeave.as_view()),
    # path('Updateleave/', views.CreateLog),

]

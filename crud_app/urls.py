from django.urls import path
from .views import Employers


urlpatterns=[
    path('employers/',Employers.as_view(),name='employers'),
    path('employers/<int:id>/',Employers.as_view(),name='idview')
]
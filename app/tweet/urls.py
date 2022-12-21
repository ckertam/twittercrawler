from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path("simplesimulation/", views.GetTweetsSimpleSimulationAPIView.as_view(), name="get tables and send email"),
    path("complexsimulation/", views.GetTweetsComplexSimulationAPIView.as_view(), name="get tables and send email"),
    path("", views.GetTweetsAPIView.as_view(), name="get tables and send email"),
]
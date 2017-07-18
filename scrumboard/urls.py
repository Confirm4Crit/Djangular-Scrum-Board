from django.conf.urls import url
from django.views.generic import TemplateView

from .api import ListApi, CardApi

urlpatterns = [

    url(r'^cards$', CardApi.as_view()),
    url(r'^list$', ListApi.as_view()),
    url(r'^home', TemplateView.as_view(template_name="scrumboard/home.html")),
]

"""oeeBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from stops.views import StopList, StopDetail
from items.views import ItemList, ItemDetail
from plants.views import PlantList, PlantDetail
from workstations.views import WorkstationList, WorkstationDetail
from bom.views import BomList, BomDetail
from job_orders.views import JobOrderList, JobOrderDetail
from shifts.views import ShiftList, ShiftDetail
from job_orders_data.views import JobOrderDataList, JobOrderDataDetail
from quality_issues.views import QualityIssueList, QualityIssueDetail
from job_quality_issues.views import JobQualityIssueList, JobQualityIssueDetail
from job_stops.views import JobStopList, JobStopDetail


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^stops/$', StopList.as_view()),
    re_path(r'^stops/(?P<pk>[0-9]+)$', StopDetail.as_view()),
    re_path(r'^items/$', ItemList.as_view()),
    re_path(r'^items/(?P<pk>[0-9]+)$', ItemDetail.as_view()),
    re_path(r'^plants/$', PlantList.as_view()),
    re_path(r'^plants/(?P<pk>[0-9]+)$', PlantDetail.as_view()),
    re_path(r'^ws/$', WorkstationList.as_view()),
    re_path(r'^ws/(?P<pk>[0-9]+)$', WorkstationDetail.as_view()),
    re_path(r'^bom/$', BomList.as_view()),
    re_path(r'^bom/(?P<pk>[0-9]+)$', BomDetail.as_view()),
    re_path(r'^job_order/$', JobOrderList.as_view()),
    re_path(r'^job_order/(?P<pk>[0-9]+)$', JobOrderDetail.as_view()),
    re_path(r'^shift/$', ShiftList.as_view()),
    re_path(r'^shift/(?P<pk>[0-9]+)$', ShiftDetail.as_view()),
    re_path(r'^job_order_partial/$', JobOrderDataList.as_view()),
    re_path(r'^job_order_partial/(?P<pk>[0-9]+)$', JobOrderDataDetail.as_view()),
    re_path(r'^q_issue/$', QualityIssueList.as_view()),
    re_path(r'^q_issue/(?P<pk>[0-9]+)$', QualityIssueDetail.as_view()),
    re_path(r'^job_q_issue/$', JobQualityIssueList.as_view()),
    re_path(r'^job_q_issue/(?P<pk>[0-9]+)$', JobQualityIssueDetail.as_view()),
    re_path(r'^job_stop/$', JobStopList.as_view()),
    re_path(r'^job_stop/(?P<pk>[0-9]+)$', JobStopDetail.as_view()),
]

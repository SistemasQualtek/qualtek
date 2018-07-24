from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ReporteQualtekExcel,
    ReporteTWExcel,
    ReporteTQTKExcel,
    ReporteCQExcel,
    ReporteMExcel,
)
urlpatterns = [
    url(r'^Reportes/',views.reportes,name="reporteslist"),
    url(r'^PDF/Dia',views.pdfdia,name="pdfdia"),
    url(r'^PDF/General',login_required(views.pdfgen),name="pdfgen"),
    url(r'^PDF/Cinchos',login_required(views.pdfcin),name="pdfcin"),
    url(r'^PDF/TuboQualtek',login_required(views.pdftq),name="pdftq"),
    url(r'^PDF/TuboW',login_required(views.pdfW),name="pdfw"),
    url(r'^PDF/Miscelanea',login_required(views.pdfM),name="pdfm"),
    url(r'^PDF/Release',login_required(views.pdfrel),name="pdfrel"),
    url(r'^XML/General', login_required(ReporteQualtekExcel.as_view()), name="reporteexcel"),
    url(r'^XML/TuboW', login_required(ReporteTWExcel.as_view()), name="reporteexceltw"),
    url(r'^XML/TuboQualtelk', login_required(ReporteTQTKExcel.as_view()), name="reporteexceltqtk"),
    url(r'^XML/CinchosQualtek', login_required(ReporteCQExcel.as_view()), name="reporteexcelcq"),
    url(r'^XML/Miscelanea', login_required(ReporteMExcel.as_view()), name="reporteexcelm"),
]

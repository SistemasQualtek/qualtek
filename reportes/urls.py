from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    ReporteQualtekExcel
)
urlpatterns = [
    url(r'^Pdf/Dia',views.pdfdia,name="pdfdia"),
    url(r'^Pdf/General',login_required(views.pdfgen),name="pdfgen"),
    url(r'^Pdf/Cinchos',login_required(views.pdfcin),name="pdfcin"),
    url(r'^Pdf/TuboQualtek',login_required(views.pdftq),name="pdftq"),
    url(r'^Pdf/TuboW',login_required(views.pdfW),name="pdfw"),
    url(r'^Pdf/Release',login_required(views.pdfrel),name="pdfrel"),
    url(r'^excel/', login_required(ReporteQualtekExcel.as_view()), name="reporteexcel"),
]

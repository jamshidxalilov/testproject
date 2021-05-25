from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Report

class MainIndex(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['report'] = Report.objects.all()

        return context




from django.db.models import Avg, Max, Count
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Country, Region, District, Street
import time


class MainIndex(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        start = time.perf_counter()
        context['district'] = District.objects.only('region').filter(id__gt=3290)
        q = Street.objects.values('district').annotate(total=Count('id')) # manytomany obyektlar soni
        print(q[len(q) - 1]['total'])

        # q = Region.objects.values('country_id').annotate(total=Count('id'))  # manytomany obyektlar soni
        # print(q[1].total)


        # books = list(District.objects.all())
        # for i in range(100):
        #     temp_books = [books.pop(0) for i in range(10)]
        #     store = Street.objects.create()
        #     store.district.set(temp_books)
        #     store.save()
        # context['street'] = Street.objects.prefetch_related('district')
        #
        # print(time.perf_counter() - start)
        # print(context['district'])
        # print(context['district'].query)
        # print(context['district'])
        return context




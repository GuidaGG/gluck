from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Page, Image, Text, Event
from itertools import chain
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from gluck.views import Section
from datetime import datetime
from django.db.models.functions import ExtractYear

# Create your views here.


# Create your views here.
def get_section(section_name):

    images = Image.objects.filter(section_fk__page=1).select_related()
    text = Text.objects.filter(section_fk__page=1).select_related()
    sections = sorted(
        chain(images, text), key=lambda test: (test.section_fk.id, test.order))
    return sections

def get_events():
    today = datetime.today()
   
    events = Event.objects.filter(date__gte=today)
    return events

def index(request):
    try:
        today = datetime.today()
        sections = get_section(1)
        events = get_events()
        years = Event.objects.filter(date__gte=today).values('date').annotate(Year=ExtractYear('date'))
        years = years.values('Year').distinct()
   
        section_titles = Section.objects.filter(page__title="GluckGluck").select_related()
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'gluck/index.html', {'sections' : sections, 'events' : events, 'section_titles' : section_titles, 'years': years})


def impressum(request):
    try:
        sections = Section.objects.filter(page__title='Impressum')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'gluck/functional.html', {'sections' : sections})

def datenschutzerklarung(request):
    try:
        sections = Section.objects.filter(page__title='Datenschutzerklärung')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'gluck/functional.html', {'sections' : sections})



class SectionDetailView(DetailView):

    model = Section

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context



class SectionListView(ListView):

    model = Section
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
from django.shortcuts import render_to_response
from django.template import RequestContext
from radio_station.models import Spot
from radio_events.models import Event
from django.template import loader, RequestContext
from django import http

def server_error(request, template_name='500.html'):
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(RequestContext(request, {})))

def home(request):
    import datetime
    now = datetime.datetime.now()

    current_spot = Spot.objects.get_current_spot(now)
    next_spots = Spot.objects.filter_next_spots(now)[:6]
    weekday_str = 'MTWRFSU'[current_spot.to_datetime().weekday()]


    today = datetime.datetime.now()
    tomorrow = today+datetime.timedelta(days=1)
    day_after = tomorrow+datetime.timedelta(days=1)

    events = {
        'today':Event.objects.filter(date=today).order_by('-weight')[:3],
        'tomorrow':Event.objects.filter(date=tomorrow).order_by('-weight')[:3],
        'day_after':Event.objects.filter(date=day_after).order_by('-weight')[:3],
    }

    ctxt = {
        'today':now,
        'tomorrow':now+datetime.timedelta(days=1),
        'day_after_tomorrow':now+datetime.timedelta(days=2),
        'current_spot':current_spot,
        'next_spots':next_spots,
        'weekday_str':weekday_str,
        'events':events,
    }
    return render_to_response('home.html', ctxt, context_instance=RequestContext(request)) 

from django.shortcuts import render, render_to_response, redirect
from landing.models import Event


def index(request):
    # return render(request, 'landing.html')
    return redirect('/event/1/')

def event(request, event_id):
    try:
        Event.objects.all().get(id=event_id)
    except:
        return redirect('/404/')
    return render(request, 'landing.html')


def handler404(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response

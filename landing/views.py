from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from landing.forms import UserProfileForm
from landing.models import Event


def index(request):
    # return render(request, 'landing.html')
    return redirect('/event/1/')

def event(request, event_id):
    try:
        Event.objects.all().get(id=event_id)
    except:
        return redirect('/404/')
    context = {}
    user_profile_form = UserProfileForm(request.POST or None)
    if request.method == 'POST':
        if user_profile_form.is_valid():
            user_profile = user_profile_form.save(commit=False)
            user_profile.save()
            return HttpResponseRedirect('/thank_you/')
        else:
            context['anchor'] = 'registration'

    context["user_profile_form"] = user_profile_form
    return render(request, 'landing.html', context)


def thank_you(request):
    return render(request, 'thank_you.html')

def handler404(request):
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response

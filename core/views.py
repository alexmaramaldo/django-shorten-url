from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import LinkForm
from core.models import Link
import short_url
from django.apps import apps
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


def link(request):
    form = LinkForm()
    return render(request, 'home.html', {'form': form, "url_registered": ""})

def register_link(request):
    if request.method == 'POST':
        url = request.POST['url']
        shorten = Link(url=url)
        shorten.save()
        shorten.shorten_url = (short_url.encode_url(shorten.id))
        shorten.save()

        full_path = "https://" + request.get_host() + "/" + shorten.shorten_url 
        data = {
            'url_registered': full_path,
        }
        return JsonResponse(data, safe=False)
        

def redirect_view(request, tiny):
    try:
        id = short_url.decode_url(tiny)
    except ValueError:
        raise Http404('Bad encoded ID.')

    print("result")
    print(id)
    try:
        shorten = Link.objects.get(pk=id)
    except Link.DoesNotExist:
       raise Http404('Shorten not found.') 

    return HttpResponseRedirect(shorten.url)
    # obj = get_object_or_404(model, pk=id)
    # return redirect(obj)
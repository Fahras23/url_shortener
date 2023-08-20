from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import Urls
import string
import random


def generate_chars(length):
    chars = string.ascii_letters + string.digits
    random_string = "".join(random.choices(chars, k=length))

    return random_string


def home(request):
    output_url = ""
    if request.method == "POST":
        # check if https is already in link
        if "https" in request.POST["url"]:
            input_url = request.POST["url"]
        else:
            input_url = f"https://{request.POST['url']}"
        # generate string in url
        output_url = f"http://127.0.0.1:8000/{generate_chars(6)}"
        # Make safe that theres no copy of link in db
        if Urls.objects.filter(output_url=output_url).first() is None:
            data = {
                "input_url": input_url,
                "output_url": output_url,
            }
            url = Urls(**data)
            url.save()
    return render(request, "home.html", context={"output_url": output_url})


def redirect_site(request, url):
    url = Urls.objects.filter(output_url=f"http://127.0.0.1:8000/{url}").first()
    if url is not None:
        return HttpResponseRedirect(url.input_url)
    else:
        return HttpResponse("Url doesnt exist")

from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify
from django.urls import reverse

from django.views import View

from .dummy_data import gadgets

# Create your views here.wearabletracker-x10

from django.views.generic.base import RedirectView


def start_page_view(request):
    return render(request, "tech_gadgets/test.html", {'gadget_list': gadgets})


class RedirectToGadgetView(RedirectView):
    # RedirectToGadgetView erbt von RedirectView, um dynamische Weiterleitungen zu ermöglichen
    pattern_name = (
        "gadget_slug_url"  # Name des URL-Musters, das als Ziel der Weiterleitung dient
    )

    def get_redirect_url(self, *args, **kwargs):
        # Erstelle einen slugifizierten Namen aus dem Gadget-Namen, basierend auf gadget_id
        # kwargs.get("gadget_id", 0) liefert die ID des Gadgets oder 0 als Standardwert, falls gadget_id fehlt
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])

        # Aktualisiere die Parameter für das Ziel-URL-Muster mit dem neuen Slug
        new_kwarg = {"gadget_slug": slug}

        # Rufe die get_redirect_url-Methode der Elternklasse auf und übergebe die aktualisierten Parameter
        return super().get_redirect_url(*args, **new_kwarg)


def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("URL not found")


class GadgetView(View):

    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das hat geklappt"})
        except:
            return JsonResponse({"response": "Das hat nicht geklappt"})


def single_gadget_view(request, gadget_slug=""):
    if request.method == "GET":
        gadget_match = None

        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data}")
            return JsonResponse({"response": "Das hat geklappt"})
        except:
            return JsonResponse({"response": "Das hat nicht geklappt"})

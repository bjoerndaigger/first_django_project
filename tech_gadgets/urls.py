from django.urls import path
from .views import start_page_view, single_gadget_int_view, GadgetView, RedirectToGadgetView, single_manufacturer_view, single_manufacturer_post_view


urlpatterns = [
    path("start/", start_page_view),
    path("", RedirectToGadgetView.as_view()),
    path("gadget/", RedirectToGadgetView.as_view()),
    path("gadget/<int:gadget_id>", single_gadget_int_view),
    path("gadget/<slug:gadget_slug>", GadgetView.as_view(), name="gadget_slug_url"),
    path("manufacturers/<int:manufacturer_id>", single_manufacturer_view),
    path("manufacturers/send_manufacturer/", single_manufacturer_post_view),
]


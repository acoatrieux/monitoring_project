from django.views.generic import DeleteView
from django import http
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from .models import WebsiteModel


class WebsiteDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'website/utils/delete.html'
    model = WebsiteModel

    def test_func(self):
        self.object = self.get_object()
        return True

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_website = self.get_success_website()
        self.object.delete()
        return http.HttpResponseRedirect(success_website)

    def get_success_website(self):
        return reverse("website:index")
from django.views.generic import View, ListView, TemplateView  # , DetailView, CreateView, UpdateView, DeleteView,
from django.contrib import messages
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse  # Http404

from .models import MenuItem

from pprint import pprint


class Tree(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["path"] = self.request.path[1:-1]
        # pprint(context)
        return context


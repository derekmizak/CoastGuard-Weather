from django.shortcuts import render, get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import SourceURL
from ..forms import SourceURLForm  


class SourceURLListView(ListView):
    model = SourceURL
    template_name = 'sourceurl_list.html'
    context_object_name = 'sourceurls'

class SourceURLDetailView(DetailView):
    model = SourceURL
    template_name = 'sourceurl_detail.html'


class SourceURLCreateView(CreateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = 'sourceurl_form.html'
    success_url = reverse_lazy('sourceurl_list')


class SourceURLUpdateView(UpdateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = 'sourceurl_form.html'
    success_url = reverse_lazy('sourceurl_list')


class SourceURLDeleteView(DeleteView):
    model = SourceURL
    template_name = 'sourceurl_confirm_delete.html'
    success_url = reverse_lazy('sourceurl_list')

from django.shortcuts import render, get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import SourceURL
from ..forms import SourceURLForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SourceURLListView(LoginRequiredMixin, ListView):
    model = SourceURL
    template_name = 'sourceurl_list.html'
    context_object_name = 'sourceurls'

class SourceURLDetailView(LoginRequiredMixin, DetailView):
    model = SourceURL
    template_name = 'sourceurl_detail.html'


class SourceURLCreateView(LoginRequiredMixin, CreateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = 'sourceurl_form.html'
    success_url = reverse_lazy('sourceurl_list')


class SourceURLUpdateView(LoginRequiredMixin, UpdateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = 'sourceurl_form.html'
    success_url = reverse_lazy('sourceurl_list')


class SourceURLDeleteView(LoginRequiredMixin, DeleteView):
    model = SourceURL
    template_name = 'sourceurl_confirm_delete.html'
    success_url = reverse_lazy('sourceurl_list')

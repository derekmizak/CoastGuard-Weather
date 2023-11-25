from django.shortcuts import render, get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SourceFormat, SourceURL
from .forms import SourceFormatForm, SourceURLForm  

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

class SourceFormatListView(ListView):
    model = SourceFormat
    template_name = 'sourceformat_list.html'
    context_object_name = 'sourceformats'

class SourceFormatDetailView(DetailView):
    model = SourceFormat
    template_name = 'sourceformat_detail.html'


class SourceFormatCreateView(CreateView):
    model = SourceFormat
    form_class = SourceFormatForm
    template_name = 'sourceformat_form.html'
    success_url = reverse_lazy('sourceformat_list')


class SourceFormatUpdateView(UpdateView):
    model = SourceFormat
    form_class = SourceFormatForm
    template_name = 'sourceformat_form.html'
    success_url = reverse_lazy('sourceformat_list')


class SourceFormatDeleteView(DeleteView):
    model = SourceFormat
    template_name = 'sourceformat_confirm_delete.html'
    success_url = reverse_lazy('sourceformat_list')

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Show

class ShowList(ListView):
    model = Show
    template_name = 'shows/show_list.html'
    context_object_name = 'shows'

class ShowDetail(DetailView):
    model = Show
    template_name = 'shows/show_detail.html'
    context_object_name = 'show'


class ShowCreate(CreateView):
    model = Show
    template_name = 'shows/show_form.html'
    fields = ['title', 'genre', 'description']
    success_url = reverse_lazy('show_list')

class ShowUpdate(UpdateView):
    model = Show
    template_name = 'shows/show_form.html'
    fields = ['title', 'genre', 'description']
    success_url = reverse_lazy('show_list')

class ShowDelete(DeleteView):
    model = Show
    template_name = 'shows/show_confirm_delete.html'
    success_url = reverse_lazy('show_list')

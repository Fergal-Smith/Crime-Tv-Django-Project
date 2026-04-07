from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Show

class ShowList(ListView):
    model = Show
    template_name = 'shows/show_list.html'

class ShowDetail(DetailView):
    model = Show
    template_name = 'shows/show_detail.html'

class ShowCreate(CreateView):
    model = Show
    fields = ['title', 'genre', 'description', 'image']
    template_name = 'shows/show_form.html'

class ShowUpdate(UpdateView):
    model = Show
    fields = ['title', 'genre', 'description', 'image']
    template_name = 'shows/show_form.html'

class ShowDelete(DeleteView):
    model = Show
    success_url = reverse_lazy('show_list')
    template_name = 'shows/show_confirm_delete.html'

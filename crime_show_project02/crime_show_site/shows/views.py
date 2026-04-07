from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Show

# List all shows
class ShowList(ListView):
    model = Show
    template_name = 'shows/show_list.html'
    context_object_name = 'shows'  # used in template for iteration

# Detail of a single show
class ShowDetail(DetailView):
    model = Show
    template_name = 'shows/show_detail.html'
    context_object_name = 'show'

# Create a new show
class ShowCreate(CreateView):
    model = Show
    template_name = 'shows/show_form.html'
    fields = ['title', 'genre', 'description']  # adjust fields to your model
    success_url = reverse_lazy('show_list')

# Update an existing show
class ShowUpdate(UpdateView):
    model = Show
    template_name = 'shows/show_form.html'
    fields = ['title', 'genre', 'description']
    success_url = reverse_lazy('show_list')

# Delete a show
class ShowDelete(DeleteView):
    model = Show
    template_name = 'shows/show_confirm_delete.html'
    success_url = reverse_lazy('show_list')

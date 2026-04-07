# shows/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Show, Rating
from .forms import RatingForm

# -----------------------------
# Index/List of Shows
# -----------------------------
class ShowList(ListView):
    model = Show
    template_name = 'shows/show_list.html'
    context_object_name = 'shows'

# -----------------------------
# Function-based Detail View (with Ratings)
# -----------------------------
def show_detail(request, pk):
    show = get_object_or_404(Show, pk=pk)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        if form.is_valid():
            rating, created = Rating.objects.update_or_create(
                show=show,
                user=request.user,
                defaults={'stars': form.cleaned_data['stars']}
            )
            show.update_average_rating()
            return redirect('show-detail', pk=show.pk)
    else:
        form = RatingForm()

    return render(request, 'shows/show_detail.html', {'show': show, 'form': form})

# -----------------------------
# CRUD: Create, Update, Delete
# -----------------------------
class ShowCreate(CreateView):
    model = Show
    fields = ['title', 'description']
    template_name = 'shows/show_form.html'

class ShowUpdate(UpdateView):
    model = Show
    fields = ['title', 'description']
    template_name = 'shows/show_form.html'

class ShowDelete(DeleteView):
    model = Show
    template_name = 'shows/show_confirm_delete.html'
    success_url = reverse_lazy('show-list')

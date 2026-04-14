from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Show
from django.shortcuts import redirect
from django.views.generic import CreateView
from reviews.models import Review 
from django.db.models import Avg

class HomeView(ListView):
    model = Show
    template_name = 'home.html'
    context_object_name = 'shows'

    def get_queryset(self):
        return Show.objects.annotate(
            avg_rating=Avg('reviews__rating')
        ).order_by('-avg_rating')

class ShowList(ListView):
    model = Show
    template_name = 'shows/show_list.html'
    context_object_name = 'shows'
    
class ShowDetail(DetailView):
    model = Show
    template_name = 'shows/show_detail.html'
    context_object_name = 'show'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()

        score = request.POST.get('score')
        comment = request.POST.get('comment')

        if score:
            Rating.objects.create(
                show=self.object,
                user=request.user,
                score=score
            )

        return redirect('show_detail', pk=self.object.pk)

class ShowCreate(LoginRequiredMixin, CreateView):
    model = Show
    fields = ['title', 'genre', 'description', 'image']
    template_name = 'shows/show_form.html'
    success_url = reverse_lazy('home')

class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Show
    fields = ['title', 'genre', 'description', 'image']
    template_name = 'shows/show_form.html'
    success_url = reverse_lazy('show_list')

class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    template_name = 'shows/show_confirm_delete.html'
    success_url = reverse_lazy('show_list')

class ReviewCreate(CreateView):
    model = Review
    fields = ['show', 'comment', 'score']
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
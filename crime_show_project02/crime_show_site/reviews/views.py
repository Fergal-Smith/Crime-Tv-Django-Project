from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import Review
from shows.models import Show


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ReviewList(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['show', 'comment', 'rating']
    success_url = reverse_lazy('show_list')  # FIX THIS NAME TO MATCH urls.py

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def submit_rating(request, show_id):
    if not request.user.is_authenticated:
        return redirect('login')

    show = get_object_or_404(Show, id=show_id)
    score = int(request.POST.get('score'))

    Review.objects.update_or_create(
        user=request.user,
        show=show,
        defaults={'score': score}
    )

    return redirect('show_detail', pk=show.id)
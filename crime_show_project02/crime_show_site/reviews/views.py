from django.views.generic import ListView, CreateView
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ReviewList(ListView):
    model = Review
    template_name = 'reviews/review_list.html'

class ReviewCreate(CreateView):
    model = Review
    fields = ['show', 'comment', 'rating']
    template_name = 'reviews/review_form.html'
    success_url = '/reviews/'

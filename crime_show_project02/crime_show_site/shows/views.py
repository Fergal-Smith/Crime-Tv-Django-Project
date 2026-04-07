from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Show, Rating

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
        if score:
            Rating.objects.create(
                show=self.object,
                user=request.user,
                score=score
            )
        return self.get(self, request, *args, **kwargs)

class ShowCreate(LoginRequiredMixin, CreateView):
    model = Show
    fields = ['title', 'genre', 'description']
    template_name = 'shows/show_form.html'
    success_url = reverse_lazy('showlist')

class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Show
    fields = ['title', 'genre', 'description']
    template_name = 'shows/show_form.html'
    success_url = reverse_lazy('showlist')

class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    template_name = 'shows/show_confirm_delete.html'
    success_url = reverse_lazy('showlist')

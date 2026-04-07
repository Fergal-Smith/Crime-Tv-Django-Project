from django.shortcuts import redirect
from .models import Review
from shows.models import Show

def add_review(request, show_id):
    if request.method == "POST":
        show = Show.objects.get(id=show_id)
        Review.objects.create(
            show=show,
            user=request.user,
            rating=request.POST['rating'],
            comment=request.POST['comment']
        )
    return redirect('show_detail', pk=show_id)

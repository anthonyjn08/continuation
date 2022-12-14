from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Trainers


class TrainerList(generic.ListView):
    """
    A view to show all trainers.
    """
    model = Trainers
    queryset = Trainers.objects.all()
    template_name = 'trainers/trainers.html'
    paginate_by = 6


class TrainerDetail(View):
    """
    Trainer detail view to display trainers bio in detail.
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Trainers.objects.all()
        trainer = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "trainers/trainer_detail.html",
            {
                "trainer": trainer,
            },
        )

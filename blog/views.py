from django.shortcuts import render
from .models import Postear
from django.utils import timezone

def post_list(request):
    posts = Postear.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
    return render(request, 'blog/post_list.html', {'posts': posts})


# Create your views here.

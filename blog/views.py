from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Postear
from django.utils import timezone

def post_list(request):
    posts = Postear.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
     post = get_object_or_404(Post, pk=pk)
     return render(request, 'blog/post_detail.html', {'post': post})
# Create your views here.

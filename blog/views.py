from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def vista_inicio(request):
    vista_inicio = get_object_or_404
    return render(request, 'blog/base.html', {})

def vista_mañana(request):
    vista_mañana = get_object_or_404
    return render(request, 'blog/turnos/mañana.html', {})

def vista_tarde(request):
    vista_tarde = get_object_or_404
    return render(request, 'blog/turnos/tarde.html', {})

def vista_Suiza(request):
    vista_Suiza = get_object_or_404
    return render(request, 'blog/paises/Suiza.html', {})

def vista_uzbekistan(request):
    vista_uzbekistan = get_object_or_404
    return render(request, 'blog/paises/Uzbekistán.html', {})

def vista_afganistan(request):
    vista_afganistan = get_object_or_404
    return render(request, 'blog/paises/Afganistán.html', {})

def vista_belgica(request):
    vista_belgica = get_object_or_404
    return render(request, 'blog/paises/Bélgica.html', {})

def vista_españa(request):
    vista_españa = get_object_or_404
    return render(request, 'blog/paises/España.html', {})

def vista_cuba(request):
    vista_cuba = get_object_or_404
    return render(request, 'blog/paises/cuba.html', {})

def vista_kuwait(request):
    vista_kuwait = get_object_or_404
    return render(request, 'blog/paises/kuwait.html', {})

def vista_indonesia(request):
    vista_indonesia = get_object_or_404
    return render(request, 'blog/paises/Indonesia.html', {})

def vista_grecia(request):
    vista_grecia = get_object_or_404
    return render(request, 'blog/paises/Grecia.html', {})

def vista_lituania(request):
    vista_lituania = get_object_or_404
    return render(request, 'blog/paises/Lituania.html', {})

def vista_yemen(request):
    vista_yemen = get_object_or_404
    return render(request, 'blog/paises/Yemen.html', {})

def vista_austria(request):
    vista_austria = get_object_or_404
    return render(request, 'blog/paises/Austria.html', {})

def vista_egipto(request):
    vista_egipto = get_object_or_404
    return render(request, 'blog/paises/Egipto.html', {})

def vista_africana(request):
    vista_africana = get_object_or_404
    return render(request, 'blog/paises/Africana.html', {})

def vista_brunei(request):
    vista_brunei = get_object_or_404
    return render(request, 'blog/paises/brunei.html', {})

def vista_guatemala(request):
    vista_guatemala = get_object_or_404
    return render(request, 'blog/paises/guatemala.html', {}) 

def vista_croacia(request):
    vista_croacia = get_object_or_404
    return render(request, 'blog/paises/croacia.html', {})

def vista_catar(request):
    vista_catar = get_object_or_404
    return render(request, 'blog/paises/catar.html', {})

def vista_turquia(request):
    vista_turquia = get_object_or_404
    return render(request, 'blog/paises/turquia.html', {})

def vista_cabo(request):
    vista_cabo = get_object_or_404
    return render(request, 'blog/paises/cabo.html', {})

def vista_hungria(request):
    vista_hungria = get_object_or_404
    return render(request, 'blog/paises/hungria.html', {})

def vista_venezuela(request):
    vista_venezuela = get_object_or_404
    return render(request, 'blog/paises/venezuela.html', {})

def vista_coreadelsur(request):
    vista_coreadelsur = get_object_or_404
    return render(request, 'blog/paises/coreadelsur.html', {})

def vista_argentina(request):
    vista_argentina = get_object_or_404
    return render(request, 'blog/paises/argentina.html', {})

def vista_marino(request):
    vista_marino = get_object_or_404
    return render(request, 'blog/paises/marino.html', {})

def vista_etiopia(request):
    vista_etiopia = get_object_or_404
    return render(request, 'blog/paises/etiopia.html', {})
# Create your views here.

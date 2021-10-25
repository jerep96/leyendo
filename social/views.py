from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import UserRegisterForm, PostForm, UrlForm, EditProfileForm, ModoProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def feed(request):
    posts = Post.objects.all()
    urls = Url.objects.filter(user=request.user)
    context = {'urls': urls}
    return render(request, 'social/feed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = {'form': form, 'title': 'Registrar Usuario', 'boton': 'Registrarse'}
    return render(request, 'social/register.html', context)


@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form': form})


@login_required
def url(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        file = request.FILES
        form = UrlForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Su URL se cargo correctamente')
            # return HttpResponse(file)
            return redirect('feed')
    else:
        form = UrlForm()
    return render(request, 'social/post.html', {'form': form})


@login_required
def profile(request, username=None, ):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
        urls = Url.objects.filter(user=request.user)

    return render(request, 'social/profile.html',
                  {'user': user, 'posts': posts, 'current_path': request.get_full_path()})


@login_required
def editprofile(request, username):
    user = Profile.objects.get(user__username=username)
    form = EditProfileForm(instance=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # return redirect('feed')
    return render(request, 'social/register.html', {'form': form, 'title': 'Editar Usuario', 'boton': 'Guardar'})


@login_required
def eliminarProducto(request, urls):
    # current_user = request.user
    urls = Url.objects.filter(title=urls)
    eliminado = False
    urls.delete()
    contexto = {
        eliminado: True
    }
    return redirect('feed')


@login_required
def editarUrl(request, title):
    url = None
    if title:
        url = Url.objects.filter(title=title).first()
        form = UrlForm(instance=url)
    if request.method == 'POST':
        form = UrlForm(request.POST, instance=url)
        if form.is_valid():
            form.save()
            return redirect('feed')
    return render(request, 'social/edit.html', {'form': form})


def link(request, username):
    user = username
    usuarios = Profile.objects.filter(user__username=user).values()
    modoPerfil = usuarios.values('modo')
    colorboton = usuarios.values('colorBoton')
    colorfondo = usuarios.values('colorFondo')
    portada = usuarios.values('portada')

    if colorfondo == 'Negro' or 'negro':
        urlimg = 'logo_white.png'
    else:
        urlimg = 'logo_black.png'

    urls = Url.objects.filter(user__username=user).values()
    urls2 = urls.filter(modo__icontains=modoPerfil)
    # return HttpResponse(urls)
    context = {'urls': urls2, 'usuario': usuarios, 'user': user, 'colorboton': colorboton, 'colorfondo': colorfondo,
               'urlimg': urlimg, 'portada': portada}
    return render(request, 'social/link.html', context)


def ver(request, username):
    user = username
    usuarios = Profile.objects.filter(user__username=user).values()
    colorboton = usuarios.values('colorBoton')
    modoPerfil = usuarios.values('modo')
    portada = usuarios.values('portada')
    urls = Url.objects.filter(user__username=user).values()
    urls2 = urls.filter(modo__icontains=modoPerfil)
    return HttpResponse(urls)


def index(request):
    return render(request, 'social/index.html')


def actions(request):
    return render(request, 'actions.html')

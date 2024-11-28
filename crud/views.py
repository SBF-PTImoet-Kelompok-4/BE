from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Film
from .forms import FilmForm
from django.shortcuts import render

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
def index(request):
    films = Film.objects.all()
    return render(request, 'crud/index.html', {'films': films})

@login_required
@user_passes_test(is_admin)
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.user = request.user
            film.save()
            return redirect('crud:index')
    else:
        form = FilmForm()
    return render(request, 'crud/film_form.html', {'form': form, 'form_title': 'Tambah Film', 'button_text': 'Simpan'})

@login_required
@user_passes_test(is_admin)
def edit_film(request, id):
    film = get_object_or_404(Film, id=id, user=request.user)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('crud:index')
    else:
        form = FilmForm(instance=film)
    return render(request, 'crud/film_form.html', {'form': form, 'form_title': 'Edit Film', 'button_text': 'Update'})

@login_required
@user_passes_test(is_admin)
def delete_film(request, id):
    film = get_object_or_404(Film, id=id, user=request.user)
    if request.method == 'POST':
        film.delete()
        return redirect('crud:index')
    return render(request, 'crud/confirm_delete.html', {'film': film})
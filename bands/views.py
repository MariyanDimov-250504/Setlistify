from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Band
from .forms import BandForm

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'bands/band_list.html', {'bands': bands})


def band_detail(request, pk):
    band = get_object_or_404(Band, pk=pk)
    songs = band.songs.all()
    concerts = band.concerts.all()
    return render(request, 'bands/band_detail.html', {
        'band': band,
        'songs': songs,
        'concerts': concerts
    })


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            messages.success(request, f'Band "{band.name}" created successfully!')
            return redirect('band_detail', pk=band.pk)
    else:
        form = BandForm()

    return render(request, 'bands/band_form.html', {
        'form': form,
        'title': 'Add New Band'
    })


def band_update(request, pk):
    band = get_object_or_404(Band, pk=pk)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            messages.success(request, f'Band "{band.name}" updated successfully!')
            return redirect('band_detail', pk=band.pk)
    else:
        form = BandForm(instance=band)

    return render(request, 'bands/band_form.html', {
        'form': form,
        'title': f'Edit: {band.name}'
    })


def band_delete(request, pk):
    band = get_object_or_404(Band, pk=pk)

    if request.method == 'POST':
        band_name = band.name
        band.delete()
        messages.success(request, f'Band "{band_name}" deleted successfully!')
        return redirect('band_list')

    return render(request, 'bands/band_confirm_delete.html', {'band': band})
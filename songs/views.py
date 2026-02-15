from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from bands.models import Band
from .models import Song
from .forms import SongForm

# Create your views here.
def song_list(request):
    songs = Song.objects.select_related('band').all()
    band_id = request.GET.get('band')
    if band_id:
        songs = songs.filter(band_id=band_id)

    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song.objects.select_related('band'), pk=pk)

    concerts = song.setlistentry_set.all().select_related('concert__band')
    return render(request, 'songs/song_detail.html', {
        'song': song,
        'concerts': concerts
    })

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save()
            messages.success(request, f'Song "{song.title}" created successfully!')
            return redirect('song_detail', pk=song.pk)
    else:
        # Check if band was passed in URL
        band_id = request.GET.get('band')
        initial_data = {}
        if band_id:
            try:
                band = Band.objects.get(pk=band_id)
                initial_data['band'] = band
            except Band.DoesNotExist:
                pass
        form = SongForm(initial=initial_data)

    return render(request, 'songs/song_form.html', {
        'form': form,
        'title': 'Add New Song'
    })

def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save()
            messages.success(request, f'Song "{song.title}" updated successfully!')
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm(instance=song)

    return render(request, 'songs/song_form.html', {
        'form': form,
        'title': f'Edit: {song.title}'
    })

def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)

    if request.method == 'POST':
        song_title = song.title
        song.delete()
        messages.success(request, f'Song "{song_title}" deleted successfully!')
        return redirect('song_list')

    return render(request, 'songs/song_confirm_delete.html', {'song': song})

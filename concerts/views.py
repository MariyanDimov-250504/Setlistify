from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Concert, SetlistEntry
from .forms import ConcertForm, SetlistEntryForm

# Create your views here.
def concert_list(request):
    concerts = Concert.objects.select_related('band').all().order_by('-date')
    return render(request, 'concerts/concert_list.html', {'concerts': concerts})


def concert_detail(request, pk):
    concert = get_object_or_404(Concert.objects.select_related('band'), pk=pk)
    setlist = concert.setlist.all().select_related('song')
    return render(request, 'concerts/concert_detail.html', {
        'concert': concert,
        'setlist': setlist
    })


def concert_create(request):
    if request.method == 'POST':
        form = ConcertForm(request.POST)
        if form.is_valid():
            concert = form.save()
            messages.success(request, f'Concert at {concert.venue} created successfully!')
            return redirect('concert_detail', pk=concert.pk)
    else:
        form = ConcertForm()

    return render(request, 'concerts/concert_form.html', {
        'form': form,
        'title': 'Add New Concert'
    })


def concert_update(request, pk):
    concert = get_object_or_404(Concert, pk=pk)

    if request.method == 'POST':
        form = ConcertForm(request.POST, instance=concert)
        if form.is_valid():
            concert = form.save()
            messages.success(request, f'Concert updated successfully!')
            return redirect('concert_detail', pk=concert.pk)
    else:
        form = ConcertForm(instance=concert)

    return render(request, 'concerts/concert_form.html', {
        'form': form,
        'title': f'Edit: {concert.band.name} at {concert.venue}'
    })


def concert_delete(request, pk):
    concert = get_object_or_404(Concert, pk=pk)

    if request.method == 'POST':
        concert_info = f"{concert.band.name} at {concert.venue}"
        concert.delete()
        messages.success(request, f'Concert "{concert_info}" deleted successfully!')
        return redirect('concert_list')

    return render(request, 'concerts/concert_confirm_delete.html', {'concert': concert})


def add_setlist_entry(request, concert_pk):
    concert = get_object_or_404(Concert, pk=concert_pk)

    if request.method == 'POST':
        form = SetlistEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.concert = concert
            entry.save()
            messages.success(request, f'Song added to setlist!')
            return redirect('concert_detail', pk=concert.pk)
    else:
        # Suggest next order number
        next_order = concert.setlist.count() + 1
        form = SetlistEntryForm(initial={'order': next_order})

    # Filter songs to only show songs from this band
    form.fields['song'].queryset = concert.band.songs.all()

    return render(request, 'concerts/add_setlist.html', {
        'form': form,
        'concert': concert
    })


def edit_setlist_entry(request, concert_pk, entry_pk):
    entry = get_object_or_404(SetlistEntry, pk=entry_pk, concert_id=concert_pk)
    concert = entry.concert

    if request.method == 'POST':
        form = SetlistEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, f'Setlist entry updated!')
            return redirect('concert_detail', pk=concert.pk)
    else:
        form = SetlistEntryForm(instance=entry)

    form.fields['song'].queryset = concert.band.songs.all()

    return render(request, 'concerts/add_setlist.html', {
        'form': form,
        'concert': concert,
        'edit_mode': True
    })


def delete_setlist_entry(request, concert_pk, entry_pk):
    entry = get_object_or_404(SetlistEntry, pk=entry_pk, concert_id=concert_pk)
    concert = entry.concert

    if request.method == 'POST':
        entry.delete()
        messages.success(request, f'Setlist entry removed!')
        return redirect('concert_detail', pk=concert.pk)

    return render(request, 'concerts/delete_setlist.html', {'entry': entry, 'concert': concert})

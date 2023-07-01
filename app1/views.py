from django.shortcuts import get_object_or_404, redirect, render

from app1.forms import CommentForm
from .models import Club
from .forms import ClubForm

# Create your views here.



def home(request):
    clubs= Club.objects.all()
    return render(request, 'home.html', {'clubs' :clubs})

def club_detail_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    return render(request, 'club_detail.html', {'club': club})


def add_club_view(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClubForm()
    
    return render(request, 'add_club.html', {'form': form})



def edit_club_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            return redirect('club_detail', club_id=club_id)
    else:
        form = ClubForm(instance=club)

    return render(request, 'edit_club.html', {'form': form, 'club': club})


def delete_club_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    
    if request.method == 'POST':
        club.delete()
        return redirect('home')
    
    return render

def add_comment_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.club = club
            comment.save()
            return redirect('club_detail', club_id=club_id)
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form})
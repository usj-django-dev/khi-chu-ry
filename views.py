from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Musician, Album
from second_app import forms
from django.db.models import Avg,Max

# Create your views from here.


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title':"Home Page",'musician_list':musician_list}
    return render(request,'second_app/index.html',context=diction )


def album_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))



    diction = {'title':"List of Albums",'artist_info':artist_info,'album_list':album_list,
    'artist_rating':artist_rating}
    return render(request,'second_app/album_list.html',context=diction )


def musician_form(request):
    form = forms.Musician_Form()
    if request.method == 'POST':
        form =forms.Musician_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)




    diction = {'title':"Add Musician",'musician_form':form}
    return render(request,'second_app/musician_form.html',context=diction )


def album_form(request):
    form = forms.Album_Form()

    if request.method == 'POST':
        form = forms.Album_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':"Add Album",'album_form':form}
    return render(request,'second_app/album_form.html',context=diction )



def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.Musician_Form(instance=artist_info)

    if request.method == 'POST':
        form = forms.Musician_Form(request.POST, instance=artist_info )

        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)


    diction ={'edit_form':form}
    return render(request, 'second_app/edit_artist.html', context=diction)




def edit_album(request,album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.Album_Form(instance=album_info)
    diction = {}

    if request.method=="POST":
        form=forms.Album_Form(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!'})


    diction.update({'edit_form':form})
    diction.update({'album_id':album_id})
    return render(request,'second_app/edit_album.html',context=diction)



def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success':'Album deleted successfully!'}

    return render(request, 'second_app/delete.html',context=diction)



def delete_musician (request,artist_id):
    artist = Musician.objects.get(pk=artist_id).delete(0)
    diction = {'delete_success':'Musician deleted successfully!'}
    return render(request,'second_app/delete.html', context=diction)

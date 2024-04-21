from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.


#rooms = [
    #{'id': 1, 'name':'Food and culture'},
    #{'id': 2, 'name':'Baking adventures'},
    #{'id': 3, 'name':'Kitchen hacks'},
    #{'id': 4, 'name': 'Food trends'},
    #{'id': 5, 'name': 'Restaurant recommendations'},
#] 

def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    """the form will be prefilled with the room's value"""
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)



def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
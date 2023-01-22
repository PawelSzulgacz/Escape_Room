from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


"""
def home(request):
    rooms = Pokoj.objects.all()
    context = {
        'rooms' : rooms
    }
    return render(request, 'testER/main.html',context)
"""
class PostListView(ListView):
    model = Pokoj
    template_name = 'testER/main.html'
    context_object_name = 'rooms'

class PostDetailView(DetailView):
    model = Pokoj
    template_name = 'testER/room_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['reviews'] = Recenzje.objects.filter(pokoj_id=self.kwargs['pk'])
        return context

class PostCreateView(LoginRequiredMixin,UserPassesTestMixin ,CreateView):
    model = Pokoj
    fields = ['nazwa','kategoria','opis','trudnosc','max_czas','kat_cenowa']
    template_name = 'testER/add_room.html'

    def form_valid(self, form):
        form.instance.firma = EscapeRoom.objects.get(wlasc_id=self.request.user.profile)
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.user_type == "W":
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pokoj
    fields = ['nazwa','kategoria','opis','trudnosc','max_czas','kat_cenowa']
    template_name = 'testER/add_room.html'

    def form_valid(self, form):
        form.instance.firma = EscapeRoom.objects.get(wlasc_id=self.request.user.profile)
        return super().form_valid(form)

    def test_func(self):
        room =  self.get_object()
        if self.request.user.profile == room.firma.wlasc_id:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pokoj
    template_name = 'testER/pokoj_confirm_delete.html'
    success_url = '/';
    def test_func(self):
        room =  self.get_object()
        if self.request.user.profile == room.firma.wlasc_id:
            return True
        return False

class ReservationCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Rezerwacje
    template_name = 'testER/add_reservation.html'
    fields = ['data','godzina']

    def form_valid(self, form):
        pk = self.request.get_full_path()
        room_id = pk.split("/")[1]
        room = Pokoj.objects.get(pk=room_id)
        form.instance.klient_id = self.request.user.profile
        form.instance.pokoj_id = room
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.user_type == "K":
            return True
        return False

def your_reservations(request):
    reservations = Rezerwacje.objects.filter(klient_id=request.user.profile)
    res_dict = {
        'reservations' : reservations
    }
    return render(request,"testER/reservations.html", res_dict)

class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Recenzje
    template_name = 'testER/add_review.html'
    fields = ['ocena','komentarz']

    def form_valid(self, form):
        pk = self.request.get_full_path()
        room_id = pk.split("/")[1]
        room = Pokoj.objects.get(pk=room_id)
        form.instance.klient_id = self.request.user.profile
        form.instance.pokoj_id = room
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.user_type == "K":
            return True
        return False
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import AddRoomForm#,AddPromotionForm

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
    def get(self, request, *args, **kwargs):
        context = {'form': AddRoomForm(self.request.user)}
        return render(request, 'testER/add_room.html', context)
    def post(self, request, *args, **kwargs):
        form = AddRoomForm(self.request.user, request.POST)
        if form.is_valid():
            room = form.save()
            room.save()
        return redirect('Escape_Room_app')

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

class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Rezerwacje
    template_name = 'testER/reservation_confirm_delete.html'
    success_url = '/';
    def test_func(self):
        res =  self.get_object()
        if self.request.user.profile == res.klient_id:
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

#Escape room dodaje
class ErCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = EscapeRoom
    template_name = 'testER/add_ER.html'
    fields = ['nazwa', 'adres', 'telefon']
    def form_valid(self, form):
        form.instance.wlasc_id = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.profile.user_type == "W":
            return True
        return False

class ErDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EscapeRoom
    template_name = 'testER/er_confirm_delete.html'
    success_url = '/';
    def test_func(self):
        er =  self.get_object()
        if self.request.user.profile == er.wlasc_id:
            return True
        return False

class ErUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EscapeRoom
    fields = ['nazwa', 'adres', 'telefon']
    template_name = 'testER/add_ER.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        er =  self.get_object()
        if self.request.user.profile == er.wlasc_id:
            return True
        return False

#your escape rooms
def your_er(request):
    er = EscapeRoom.objects.filter(wlasc_id=request.user.profile)
    er_dict = {
        'escaperooms' : er
    }
    return render(request,"testER/companies_user.html", er_dict)

#all companies
class erListView(ListView):
    model = EscapeRoom
    template_name = 'testER/companies.html'
    context_object_name = 'escaperooms'

#rooms from company
def rooms_from_company(request, *args, **kwargs):
    er = Pokoj.objects.filter(firma=kwargs['pker'])
    company = EscapeRoom.objects.filter(id=kwargs['pker'])
    #er = EscapeRoom.objects.filter(wlasc_id=request.user.profile)
    context = {
        'rooms' : er,
        'company' : company
    }
    return render(request, "testER/company_rooms.html",context)

def search_room(request):
    if request.method == "POST":
        searched = request.POST['searched']
        rooms = Pokoj.objects.filter(nazwa__contains=searched)
        return render(request, "testER/search_rooms.html", {'searched':searched, 'rooms':rooms})
    else:
        return render(request, "testER/search_rooms.html")

#promocje
"""
class PromotionCreateView(LoginRequiredMixin,UserPassesTestMixin ,CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': AddPromotionForm(self.request.user)}
        return render(request, 'testER/add_promotion.html', context)
    def post(self, request, *args, **kwargs):
        form = AddRoomForm(self.request.user, request.POST)
        if form.is_valid():
            prom = form.save()
            prom.save()
        return redirect('Escape_Room_app')

    def test_func(self):
        if self.request.user.profile.user_type == "W":
            return True
        return False
"""

def change_reservations(request):
    er = EscapeRoom.objects.filter(wlasc_id=request.user.profile)
    rooms = Pokoj.objects.filter(firma__in=er)
    reservations = Rezerwacje.objects.filter(pokoj_id__in=rooms)
    context = {
        'rooms':rooms,
        'reservations':reservations,
    }

    if request.method == "POST":
        escaped = request.POST['escaped']
        time = request.POST['time']
        id = request.POST['id']
        print(escaped,time,id)
        return render(request, 'testER/reservations_to_visited.html', context)
    return render(request, 'testER/reservations_to_visited.html', context)
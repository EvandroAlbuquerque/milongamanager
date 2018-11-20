from django.shortcuts import render
from milonga.models import Pessoa, Danca
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

# PESSOA
class PessoaCreateView(CreateView):
    model = Pessoa
    fields = ['nome', 'sexo']


class PessoaDetailView(DetailView):
    model = Pessoa


class PessoaListView(ListView):
    model = Pessoa


class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = ['nome', 'sexo']


class PessoaDeleteView(DeleteView):
    model = Pessoa


# Danca
class DancaCreateView(CreateView):
    model = Danca
    fields = ['hora_inicio', 'hora_fim']


class DancaDetailView(DetailView):
    model = Danca


class DancaListView(ListView):
    model = Danca


class DancaUpdateView(UpdateView):
    model = Danca
    fields = ['hora_inicio', 'hora_fim']


class DancaDeleteView(DeleteView):
    model = Danca
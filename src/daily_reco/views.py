from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from daily_reco.models import Journal


class JournalListView(ListView):
    model = Journal
    template_name = "journal_list.html"


class JournalCreateView(CreateView):
    model = Journal
    template_name = "create_journal_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("daily_reco:journal_list")


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = "update_journal_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("daily_reco:journal_list")


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = "delete_journal_form.html"
    success_url = reverse_lazy("daily_reco:journal_list")

from django.contrib import admin
from django.urls import path

from daily_reco.views import JournalListView, JournalCreateView, JournalUpdateView, JournalDeleteView

app_name = "daily_reco"

urlpatterns = [
    path("journal/list", JournalListView.as_view(), name="journal_list"),
    path("journal/create", JournalCreateView.as_view(), name="create_journal"),
    path("journal/update/<pk>", JournalUpdateView.as_view(), name="update_journal"),
    path("journal/delete/<pk>", JournalDeleteView.as_view(), name="delete_journal"),
]

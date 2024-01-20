from django.urls import path

from . import views

app_name = "input_site"

urlpatterns = [
    # Home page
    path("", views.index, name='index'),
    # Page containing threads
    path("threads/", views.threads, name='threads'),
    # The full page for a thread
    path('threads/<int:thread_id>/', views.thread, name='thread'),
    # Page for creating a new thread
    path('new_thread/', views.new_thread, name='new_thread'),
    # Page for adding new comments
    path('new_comment/<int:thread_id>/', views.new_comment, name='new_entry'),
    # About page
    path("about/", views.about, name='about'),
    # delete button
    path("delete/<int:thread_id>", views.delete, name='delete'),

]



from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return redirect(reverse("input_site:about"))

def threads(request):
    """Show all threads"""
    threads = Thread.objects.order_by('date_added')
    
    context = {'threads': threads}
    return render(request, 'input_site/threads.html', context)
@login_required
def thread(request, thread_id):
    """Show the complete page for a single thread"""
    thread = Thread.objects.get(id=thread_id)
    if request.method != 'POST':
        # No data submitted
        form = CommentForm()
    else:
        # POST data submitted; proccess data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner=request.user
            new_comment.thread = thread
            new_comment.save()
            return redirect("input_site:thread", thread_id=thread_id)
    comments = thread.comment_set.order_by("-date_added")
    context = {'thread': thread, 'form':form, "comments": comments}
    return render(request,'input_site/thread.html', context)

@login_required
def new_thread(request):
    """Add a new thread"""
    if request.method != 'POST':
        # No data submitted
        form = ThreadForm()
    else:
        # POST data submitted; proccess data
        form = ThreadForm(data=request.POST)
        if form.is_valid():
            new_thread = form.save(commit=False)
            new_thread.owner=request.user
            new_thread.save()
            return redirect('input_site:threads')
    # Display a blank or invalid form
    context = {'form':form}
    return render(request, 'input_site/new_thread.html', context)

def new_comment(request, thread_id):
    """Add a new comment under a thread or comment"""
    thread = Thread.objects.get(id=thread_id)

    if request.method != 'POST':
        # No data submitted
        form = CommentForm()
    else:
        # POST data submitted; proccess data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.thread = thread
            new_comment.save()
            return redirect("input_site:thread", thread_id=thread_id)
    # Display a blank or invalid form
    context = {"thread": thread, 'form':form}
    return render(request, 'input_site/new_comment.html', context)

def about(request):
    return render(request, 'input_site/about.html')

def delete(request, id):
  discussion = Thread.objects.get(id=id)

  #thread.delete()
  return render(request, 'input_site/delete.html')
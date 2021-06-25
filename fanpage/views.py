from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Fanpage, FanpageForms
from django.utils import timezone
# Create your views here.

def index(request):
    entries = Fanpage.objects.filter(is_active=True).order_by('-date_added')
    ctx = {
        "entries": entries
    }
    return render(request, "main.html", ctx)


def add(request):
    if request.method == "POST":
        entry = FanpageForms(request.POST)
        if entry.is_valid():
            entry.save()
            return redirect("fanpage:main")
    else:
        form = FanpageForms()

    ctx = {
        "form": form,
    }
    return render(request, "add.html", ctx)


def edit(request, pk):
    post = Fanpage.objects.get(id=pk)
    if request.method == "POST":
        entry = FanpageForms(request.POST, instance=post)
        if entry.is_valid():
            post.last_updated = timezone.now()
            entry.save()
            return redirect("fanpage:main")
    else:
        form = FanpageForms(instance=post)

    ctx = {
        "pk": pk,
        "form": form,
    }
    return render(request, "edit.html", ctx)


def delete(request, pk):
    post = Fanpage.objects.get(id=pk)
    post.is_active = False
    post.save()
    return redirect("fanpage:main")

from django.shortcuts import render


def index(request):
    return render(request, "rating/happinessrating.html", "rating/__base_head.html")

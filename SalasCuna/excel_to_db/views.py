from django.shortcuts import render

# Create your views here.

from SalasCuna_api.models import ChildState

from django.http import HttpResponse

def migration(request):
    rta = "todo bien"

    try:
        salacuna = ChildState.objects.create(
            name = "my state is in the moon"
        )

    except Exception as e:
        rta = f"error: {e}"

    return HttpResponse(rta)



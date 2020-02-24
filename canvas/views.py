from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TextForm


@login_required
def write(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if not form.is_valid():
            return render(request, 'canvas/canvas.html', {'note': 'error', 'form': form})
        else:
            text = form.save(commit=False)
            text.author = request.user
            text.save()
            return redirect(write)  # this is a way to resolve NoReverseMatch
            # TODO: add feedback that the entry was successfully saved
    else:
        form = TextForm(None)
    return render(request, 'canvas/canvas.html', {'form': form})
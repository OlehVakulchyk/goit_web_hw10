from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TagForm

# Create your views here.
def main(request):
    return render(request, 'quotes/index.html')

def index(request):
    host = request.META["HTTP_HOST"]  # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    user_ip = request.META["REMOTE_ADDR"]

    return HttpResponse(f"""<h2>Hello, world. This is my first site.</h2>
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
        <p>User-ip: {user_ip}
    """)
    # return HttpResponse("<h2>Hello, world. This is my first site.</h2>")


def quote(request):
    return HttpResponse("<h3>Hello, world. This is my first site.</h3>")


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})

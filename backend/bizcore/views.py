from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)
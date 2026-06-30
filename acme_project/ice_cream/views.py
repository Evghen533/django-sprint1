from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'ice_cream_list': []})

def ice_cream_list(request):
    return render(request, 'list.html', {'ice_cream_list': []})

def ice_cream_detail(request, id):
    return render(request, 'detail.html', {'cream': None})

def about(request):
    return render(request, 'description.html')

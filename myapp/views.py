from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def search(request):
    search_content = request.POST.get('search')
    context = {
        'search': search_content,
    }
    return render(request, 'my_app/search.html', context)

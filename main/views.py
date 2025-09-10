from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Football Shop',
        'category' : 'Clothes',
        'name': 'Baju',
        'description': 'Keren',
        'thumbnail': ''
    }

    return render(request, "main.html", context)
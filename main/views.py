from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Football Shop',
        'nama' : 'Fernando Lawrence',
        'kelas': 'PBP B',
    }

    return render(request, "main.html", context)
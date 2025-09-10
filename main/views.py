from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '24016365313',
        'name': 'Herdayani Elision Sitio',
        'class': 'PBP KKI',
    }
    return render(request, "main.html", context)

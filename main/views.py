from django.shortcuts import render

def show_info(request):
    context = {
        'app_name': 'Sports World',
        'student_name': 'Herdayani Elision Sitio',
        'student_class': 'PBP KKI',   
    }
    return render(request, "main.html", context)

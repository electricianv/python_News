from django.shortcuts import render

def no_permission(request, exception):
    return render(request, '403.html', status=403)
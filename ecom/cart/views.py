from django.shortcuts import render

def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_add(request):
    ...

def cart_delete(request, pk):
    ...

def cart_update(request, pk):
    ...
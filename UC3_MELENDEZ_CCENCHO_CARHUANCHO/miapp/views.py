from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request,'index.html')

def inicios(request):
    cursos = ['Gestion de base de datos', 'Dinamica de sistemas', 'LP3', 'Teoria general de sistemas', 'Algoritmo de computacion grafica', 'Gestion de procesos', 'Legislacion informatica']
    return render(request, 'inicios.html', {'cursos': cursos})



def primitos(request,a=1,b=100):

    if a > b:
        a, b = b, a

    primos = []

    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)

    return render(request, 'primos.html', {'primos': primos, 'a': a, 'b': b})

def examen(request):
    return render(request,'examen.html')

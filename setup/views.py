from django.shortcuts import render


def homepage(request):
    nome = "Matheus"
    pessoa = {
        'nome': 'Maria',
        'idade': 30,
        'cidade': 'Belém'
    }
    return render(request, "home.html", {"nome": nome, 'pessoa': pessoa})


def about(request):
    frutas = ["Maçã", "Banana", "Laranja", "Uva"]
    return render(request, "about.html", {"frutas": frutas})

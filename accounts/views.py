from django.shortcuts import render

# Create your views here.
from math import sqrt
from .models import Operations


def fact(number):
    i = number
    result = 1
    while i:
        result = result * i
        i = i - 1

    return result


def fibbo(number):
    a = 0
    b = 1
    result = 0

    if number == 1:
        result = 0
    elif number == 2:
        result = 1
    else:
        i = 3
        while i <= number:
            result = a + b
            a = b
            b = result
            i = i + 1

    return result


def index(request):

    if request.POST:
        number = int(request.POST['num1'])

        if 'sq' in request.POST:
            result = number * number
            MyOperations = Operations(type='sq', input=number, result=result)
            MyOperations.save()
            return render(request, "inputPage.html", {"result": result})

        elif 'sqrt' in request.POST:
            result = sqrt(number)
            MyOperations = Operations(type='sqrt', input=number, result=result)
            MyOperations.save()
            return render(request, "inputPage.html", {"result": result})

        elif 'fact' in request.POST:
            result = fact(number)
            MyOperations = Operations(type='fact', input=number, result=result)
            MyOperations.save()
            return render(request, "inputPage.html", {"result": result})

        elif 'fibbo' in request.POST:
            result = fibbo(number)
            MyOperations = Operations(type='fibbo', input=number, result=result)
            MyOperations.save()
            return render(request, "inputPage.html", {"result": result})

        elif 'history' in request.POST:
            if number > 0:
                data = Operations.objects.all()[:number]
                print(data[0].type)
            else:
                data = Operations.objects.all()

            return render(request, "inputPage.html", {"data": data})

    return render(request, 'inputPage.html')

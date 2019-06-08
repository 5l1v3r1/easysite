import datetime

from django.shortcuts import render

from django.http import HttpResponse
from .models import Buy


def dio(request):
    return render(request, 'mysite/index.html')


def about(request):
    return render(request, 'mysite/about.html')


def thanks(request):
    return render(request, 'mysite/thanks.html')


def zakaz(request):
    summ = 0;
    h = open('history.txt', 'a')
    if request.method == 'POST':
        h.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + '\n')

        if request.POST.get('doner') != '':
            h.write((request.POST.get('doner') + 'x' + ' донер\n'))

            print(request.POST.get('doner') + 'x' + ' донер')
            summ = summ + (int(request.POST.get('doner')) * 600)

        if request.POST.get('bors') != '':
            h.write((request.POST.get('bors') + 'x' + ' борщеллионе\n'))

            print(request.POST.get('bors') + 'x' + ' борщеллионе')
            summ = summ + (int(request.POST.get('bors')) * 5000)

        if request.POST.get('frik') != '':
            h.write(request.POST.get('frik') + 'x' + ' фрикаделька\n')
            print(request.POST.get('frik') + 'x' + ' фрикаделька')
            summ = summ + (int(request.POST.get('frik')) * 1000)

        if request.POST.get('name') == '':
            h.write('*имя отсутствует* ')
            print('*имя отсутствует*')
        else:
            name = request.POST.get('name')
            h.write(name + ' ')
            print(name)

        if request.POST.get('surname') == '':

            h.write('*фамилия отсутствует* ')
            print('*фамилия отсутствует*')
        else:
            surname = request.POST.get('surname')
            h.write(surname + ' ')
            print(surname)

        if request.POST.get('fathername') == '':
            h.write('*отчество отсутствует*\n')
            print('*отчество отсутствует*')
        else:
            fathername = request.POST.get('fathername')
            h.write(fathername + '\n')
            print(fathername)

        if request.POST.get('phone') == '':
            h.write('*отсутствует номер телефона*\n')
            print('*отсутствует номер телефона*')
        else:
            phone = request.POST.get('phone')
            h.write(phone + '\n')
            print(phone)

        if request.POST.get('email') == '':
            h.write('*email отсутствует*\n')
            print('*email отсутствует*')
        else:
            email = request.POST.get('email')
            h.write(email + '\n')
            print(email)

        if request.POST.get('adress') == '':
            h.write('*адрес отсутствует*\n')
            print('*адрес отсутствует*')
        else:
            adress = request.POST.get('adress')
            h.write(adress + '\n')
            print(adress)

        if request.POST.get('dr') == 'on':
            h.write('*У покупателя день рождения*\n')
            print('*У покупателя день рождения*')
        else:
            h.write('*У покупателя не день рождения*\n')
            print('*У покупателя не день рождения*')

        if (summ) < 5000:
            summ = summ + 600

        if (summ) >= 20000:
            summ = summ * 0.85
        elif request.POST.get('dr') == 'on':
            summ = summ * 0.9

        h.write('Сумма заказа= ' + str(summ) + ' тг\n\n\n')
        print('Сумма заказа= ' + str(summ) + ' тг')

        # c = Buy(name=name)
        # c.save()

        return render(request, 'mysite/thanks.html')

    else:
        return render(request, 'mysite/zakaz.html')

# def output(request):

# Create your views here.

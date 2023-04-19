from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import *
from .forms import *


def home(request):
    pizza = Pizza.objects.all()
    context = {
        'pizza': pizza
    }
    return render(request, 'home.html', context)


def buy(request, pizza_pk):
    pizza = get_object_or_404(Pizza, pk=pizza_pk)
    ingredients = Ingredient.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.total_price = pizza.price
            order.save()

            all_ingredients = request.POST.getlist('ing')

            selected_ingredients = Ingredient.objects.filter(pk__in=all_ingredients)

            for ingredient in selected_ingredients:
                order.ingredient.add(ingredient)
                order.total_price += ingredient.price

            order.save()
            form.save_m2m()

            send_mail(
                subject=f'Ви замовили піцу {pizza.name}',
                message=f'Щойно ви замовили піцу {pizza.name} за адресою {order.address}'
                f' загальна сума становить {order.total_price}. Дякуємо щи Ви з нами!',
                from_email='levkovich.vlad.2004@gmail.com',
                recipient_list=[order.email],
                fail_silently=False
            )

            return redirect('home')
    else:
        form = OrderForm()

    context = {
        'pizza': pizza,
        'ingredients': ingredients,
        'form': form
    }
    print('context:', context)
    return render(request, 'buy.html', context)

#
# def email(request):
#     send_mail(
#         subject=f'Ви замовили піцу small',
#         message=f'Щойно ви замовили піцу small за адресою slavuta'
#                 f' загальна сума становить 278 UAN. Дякуємо щи Ви з нами!',
#         from_email='levkovich.vlad.2004@gmail.com',
#         recipient_list=['mega.game3278@gmail.com'],
#         fail_silently=False
#     )
#     return redirect('home')


def create_order(request):
    if 'ing' in request.POST:
        ing = request.POST['ing']
        print('ing:', type(ing))

    return redirect('home')

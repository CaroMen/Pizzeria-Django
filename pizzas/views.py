from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import PizzaForm
# Create your views here.


def index(request):
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}

    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, p_id):
    pizza = Pizza.objects.get(id=p_id)
    toppings = pizza.topping_set.order_by('pizza_id')

    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'pizzas/pizza.html', context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('pizzas:pizza', p_id=pizza_id)

    context = {'form': form, 'pizza': pizza}
    return render(request, 'pizzas/new_comment.html', context)

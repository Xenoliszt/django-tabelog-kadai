from django.shortcuts import render
from .models import Store, Category, FoodCategory
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm





def store_list(request):
    stores = Store.objects.all()
    categories = Category.objects.all()
    food_categories = FoodCategory.objects.all()



    # フリーワード検索
    q = request.GET.get("q")
    if q:
        stores = stores.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q) |
            Q(food_categories__name__icontains=q)
        ).distinct()

    return render(request, 'store_list.html', {'stores': stores, 'categories': categories, 'food_categories': food_categories})
    
    



def food_category(request, food_category_id):
    current_food = get_object_or_404(FoodCategory, id=food_category_id)
    categories = Category.objects.all()
    stores = Store.objects.filter(food_categories=current_food)


    # フリーワード検索
    q = request.GET.get("q")
    if q:
        stores = stores.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q) |
            Q(food_category__name__icontains=q)
        )

    # 予算検索
    budget = request.GET.get("budget")
    if budget and budget.isdigit():
        stores = stores.filter(price__lte=int(budget))

    context = {
        "current_category": current_food,  # ← テンプレ流用
        "categories": categories,
        "stores": stores,
        "selected_budget": budget,
        "is_food": True,                   # ← 判別用
    }


    return render(request, "category_store_list.html", context)



def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    return render(request, 'store_detail.html', {'store': store})



def store_category(request, category_id):
    current_category = Category.objects.get(id=category_id)
    stores = Store.objects.filter(category=current_category)
    categories = Category.objects.all()


    q = request.GET.get("q")
    if q:
        stores = stores.filter(
            Q(name__icontains=q) |
            Q(category__name__icontains=q) |
            Q(food_categories__name__icontains=q)
        ).distinct()



    budget = request.GET.get("budget")
    if budget:
        stores = stores.filter(price__lte=budget)

    context = {
        "current_category": current_category,
        "categories": categories,
        "stores": stores,
        "selected_budget": budget,
    }

    return render(request, "category_store_list.html", context)


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'
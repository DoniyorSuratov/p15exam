from django.shortcuts import render, redirect
from django.views import View
from .models import Product
# Create your views here.





class ShoppingCartView(View):
    temlate_name = 'cart.html'
    context = {}
    def get(self, request):
        if request.user.id is None:
            return redirect ('/accounts/login')
        shopping_cart = Product.objects.filter(user = request.user)
        data=[]
        print(shopping_cart)
        for carts in shopping_cart:
            data.append(carts)

        self.context.update({'shopping_cart_products': data})
        self.context.update({'name': request.user})




        return render(request,self.temlate_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        Product.objects.get(pk = shopping_cart_id).delete()
        return redirect('/cart')


class TodosView(View):
    template_name='todos.html'
    context={}
    def get(self, request):
        return render(request, self.template_name, self.context)


    def post(self, request):
        text = request.POST.get('text')
        count = request.POST.get('count')



        todos = Product.objects.create(
            text=text,
            count=count,
            user=request.user

        )
        todos.save()
        return redirect('/cart')

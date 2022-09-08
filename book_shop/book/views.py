from book.models import BookProduct, Cart,Order
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.views import View


# Create your views here.
# list the books in home page while sending get request
def show_book_list(request):

    context = {}
    if request.method == "GET":
        books = BookProduct.objects.all()
        paginator = Paginator(books, 3)
        # Showing 3 books per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"books": page_obj}
    return render(request, "pages/home.html", context)


def show_book_detail(request, pk):
    context = {}
    if request.method == "GET":
        books = BookProduct.objects.get(id=pk)
        context = {
            "book": books,
        }
        return render(request, "pages/book_detail.html", context)
    
    if request.method == "POST":
        try:
            pk = request.POST['id']  
        except:
            HttpResponse("Didn't get the valid id")
        current_user = request.user
        book = BookProduct.objects.get(id=pk)
        print(book)
        order = Order.objects.create()
        order.customer = current_user
        order.books = book
        order.save()
        return render(request, "pages/order.html", {})


# Adding books to the Cart
# There is a single cart created for each user during User object creation
# Add books to the cart of respective user who logged in the website
def add_to_cart(request, pk):
    current_user = request.user
    book = BookProduct.objects.get(id=pk)
    print(book.book_name)
    user_cart = Cart.objects.filter(customer=current_user).first()
    user_cart.books.add(book)
    user_cart.save()

    return render(request, "pages/cart.html", {})


# Place order for a given book by sending book_id in
# the POST request after clicking the order now
def add_to_order(request):
    if request.method == "POST":
        try:
            pk = request.POST['id']  
        except:
            HttpResponse("Didn't get the valid id")
        current_user = request.user
        book = BookProduct.objects.get(id=pk)
        print(book)
        order = Order.objects.create()
        order.customer = current_user
        order.books = book
        order.save()
    return render(request, "pages/order.html", {})


class CartView(View):
    template_name = 'pages/cart.html'
    context = {}
    def get(self,request):
        current_user = request.user
        cart = Cart.objects.get(customer=current_user)
        all_books = cart.books.all()
        context={
            'books':all_books
        }
        print(context)  
        return render(request, self.template_name, self.context)
    

    
# def make_order(request,pk):
# if request.method == "POST":

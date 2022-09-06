from book.models import BookProduct, Cart,Order
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
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


def add_to_cart(request, pk):
    current_user = request.user
    book = BookProduct.objects.get(id=pk)
    print(book.book_name)
    # user_cart = Cart(customer=current_user)
    # user_cart.save()
    # user_cart.books.add(book)
    user_cart = Cart.objects.filter(customer=current_user).first()
    user_cart.books.add(book)
    user_cart.save()

    return render(request, "pages/cart.html", {})


def add_to_order(request,pk):
    current_user = request.user
    book = BookProduct.objects.get(id=pk)
    print(book)
    order = Order.objects.create()
    order.customer = current_user
    order.books = book
    order.save()
    return render(request, "pages/order.html", {})

    
# def make_order(request,pk):
# if request.method == "POST":

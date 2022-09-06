import datetime

from django.db import models

# from users.models import User


# Create your models here.
def get_date_list():
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    return YEAR_CHOICES


class TimeStamps(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BookProduct(models.Model):
    # Creating choices list
    FICTION = "FC"
    NONFICTION = "NF"
    ACADEMIC = "AC"
    ENTERTAINMENT = "ET"
    SELFIMPROVEMENT = "SI"
    MYSTIC = "MY"
    SCI_FI = "SF"
    BIOGRAPHY = "BG"
    BOOKS_CATEGORIES = [
        (FICTION, "Fiction"),
        (NONFICTION, "Non-fiction"),
        (ACADEMIC, "Academic"),
        (ENTERTAINMENT, "Entertainment"),
        (SELFIMPROVEMENT, "SelfImprovement"),
        (MYSTIC, "Mystic"),
        (SCI_FI, "Science-fiction"),
        (BIOGRAPHY, "Biography"),
    ]

    book_name = models.CharField(max_length=200)
    serial_no = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    published_year = models.IntegerField(
        ("year"), choices=get_date_list(), default=datetime.datetime.today().year
    )
    price = models.FloatField()
    discount_pct = models.FloatField()
    available_qty = models.IntegerField()
    goodread_rating = models.FloatField(max_length=200)
    author_name = models.CharField(max_length=200)
    cover_image = models.ImageField(default=None)
    genre = models.CharField(
        max_length=2,
        choices=BOOKS_CATEGORIES,
        default=NONFICTION,
    )

    def __str__(self):
        return self.book_name

    @property
    def marked_price(self):
        marked_price = (self.price * 100) / (100 - self.discount_pct)
        return int(marked_price)

    @property
    def category(self):
        for i in range(len(self.BOOKS_CATEGORIES)):
            if self.BOOKS_CATEGORIES[i][0] == self.genre:
                return self.BOOKS_CATEGORIES[i][1]

    @property
    def rating(self):
        return int(self.goodread_rating)


class Category(models.Model):

    title = models.CharField(max_length=30)
    books = models.ManyToManyField(BookProduct)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


# To keep the data of each customer
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=100)


# Cart to track books desired by customer and books
class Cart(TimeStamps):
    books = models.ManyToManyField(BookProduct, blank=True)
    customer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer)


class Order(TimeStamps):

    DELIVERED = "DE"
    NOT_DELIVERED = "ND"
    ON_PROCESS = "OP"
    VERIFIED = "VF"
    NOT_VERIFIED = "NV"

    ORDER_CATEGORIES = [
        (DELIVERED, "Delivered"),
        (NOT_DELIVERED, "Notdelivered"),
        (ON_PROCESS, "Onprocess"),
        (VERIFIED, "Verified"),
        (NOT_VERIFIED, "Notverified"),
    ]
    #Ref_No = models.CharField(max_length=100,null=True)
    books = models.ForeignKey(BookProduct, on_delete=models.CASCADE, null=True,blank=True)
    customer = models.ForeignKey("users.User", on_delete=models.CASCADE,null=True,blank=True)
    order_status = models.CharField(max_length=2,choices=ORDER_CATEGORIES, default=ON_PROCESS)

    class Meta:
        ordering = ["created_time"]

    def __str__(self):
        return self.created_time

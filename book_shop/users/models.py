from book.models import Cart
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for BOOk SHOP.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def user_created_handler(instance, created, sender, *args, **kwargs):
        if created:
            print("this is signak sddadsadadsa")
            user_cart = Cart.objects.get_or_create(customer=instance)
            user_cart = user_cart[0]
            user_cart.save()


# Use post_save signal to do something using user_created_handler function
post_save.connect(User.user_created_handler, sender=User)

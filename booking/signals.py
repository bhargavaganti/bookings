
from django.db.models.signals import post_save
from django.dispatch import receiver

from booking.models import (
    QuoteAllotment, QuoteTransfer, QuoteExtra,
    BookingAllotment, BookingTransfer, BookingExtra)
from booking.services import BookingService


@receiver(post_save, sender=QuoteAllotment)
def update_allotment_quote(sender, instance, **kwargs):
    quote = instance.quote
    BookingService.update_quote(quote)


@receiver(post_save, sender=QuoteTransfer)
def update_transfer_quote(sender, instance, **kwargs):
    quote = instance.quote
    BookingService.update_quote(quote)


@receiver(post_save, sender=QuoteExtra)
def update_extra_quote(sender, instance, **kwargs):
    quote = instance.quote
    BookingService.update_quote(quote)


@receiver(post_save, sender=BookingAllotment)
def update_allotment_booking(sender, instance, **kwargs):
    booking = instance.booking
    BookingService.update_booking(booking)


@receiver(post_save, sender=BookingTransfer)
def update_transfer_booking(sender, instance, **kwargs):
    booking = instance.booking
    BookingService.update_booking(booking)


@receiver(post_save, sender=BookingExtra)
def update_extra_booking(sender, instance, **kwargs):
    booking = instance.booking
    BookingService.update_booking(booking)

from django import template

from booking.tables import (
    QuoteServiceTable, QuotePaxVariantTable, BookingServiceTable, BookingPaxTable)

register = template.Library()


@register.simple_tag
def quoteservices_table(quote):
    table = QuoteServiceTable(
        quote.quote_services.all(),
        order_by=('datetime_from', 'datetime_to'))
    return table


@register.simple_tag
def quotepaxvariant_table(quote):
    table = QuotePaxVariantTable(
        quote.quote_paxvariants.all(),
        order_by=('pax_quantity',))
    return table


@register.simple_tag
def bookingservices_table(booking):
    table = BookingServiceTable(booking.booking_services.all(),
                                order_by=('datetime_from', 'datetime_to'))
    return table
    # table = BookingServiceTable(bs)
    # return {'table': bs}


@register.simple_tag
def booking_pax_table(booking):
    """ Gives a table object with rooming list"""
    return BookingPaxTable(booking.rooming_list.all())

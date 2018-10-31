import django_tables2 as tables

from django.urls import reverse
from django.contrib.admin.utils import quote
from django.utils.html import format_html
from booking.models import (
    Order, OrderService, OrderPaxVariant,
    Booking, BookingService, BookingPax)
from booking.constants import ORDERSERVICE_TYPES, BOOKINGSERVICE_TYPES


class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'reference', 'agency', 'date_from', 'date_to', 'currency', 'status']

    def render_reference(self, value, record):
        return format_html(
            '<a href="#services-list-%s" data-toggle="collapse">%s</a>' % (record.id, value))

    def before_render(self, request):
        self.columns.hide('id')


class OrderServiceTable(tables.Table):
    class Meta:
        model = OrderService
        template_name = 'booking/orderservices_list.html'
        fields = ['name', 'service_type', 'datetime_from', 'datetime_to', 'status']
    def render_name(self, value, record):
        obj_url = reverse(
            'common:booking_%s_change' % (ORDERSERVICE_TYPES[record.service_type]),
            args=(quote(record.pk),)
        )
        return format_html('<a href="%s">%s</a>' % (obj_url, value))

    def before_render(self, request):
        self.columns.hide('service_type')


class OrderPaxVariantTable(tables.Table):
    class Meta:
        model = OrderPaxVariant
        template_name = 'booking/orderservices_list.html'
        fields = [
            'pax_quantity',
            'cost_single_amount', 'cost_double_amount', 'cost_triple_amount',
            'price_single_amount', 'price_double_amount', 'price_triple_amount']


class BookingTable(tables.Table):
    class Meta:
        model = Booking
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'reference', 'agency', 'date_from',
                  'date_to', 'cost_amount', 'price_amount']

    def render_reference(self, value, record):
        return format_html(
            '<a href="#services-list-%s" data-toggle="collapse">%s</a>' % (record.id, value))

    def before_render(self, request):
        self.columns.hide('id')


class BookingServiceTable(tables.Table):
    class Meta:
        model = BookingService
        template_name = 'booking/bookingservices_list.html'
        fields = ['name', 'service_type', 'datetime_from', 'datetime_to', 'cost_amount',
                  'price_amount']
    def render_name(self, value, record):
        obj_url = reverse(
            'common:booking_%s_change' % (BOOKINGSERVICE_TYPES[record.service_type]),
            args=(quote(record.pk),)
        )
        return format_html('<a href="%s">%s</a>' % (obj_url, value))

    def before_render(self, request):
        self.columns.hide('service_type')


class BookingPaxTable(tables.Table):
    class Meta:
        model = BookingPax
        template_name = 'booking/bookingservices_list.html'
        fields = ['pax_name', 'pax_age']

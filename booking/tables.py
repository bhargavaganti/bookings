import django_tables2 as tables

from django.urls import reverse
from django.contrib.admin.utils import quote
from django.utils.html import format_html
from booking.models import (
    Quote, QuoteService, QuotePaxVariant,
    Booking, BookingService, BookingPax)
from booking.constants import QUOTESERVICE_TYPES, BOOKINGSERVICE_TYPES


class QuoteTable(tables.Table):
    class Meta:
        model = Quote
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'reference', 'agency', 'date_from', 'date_to', 'currency', 'status']

    def render_reference(self, value, record):
        return format_html(
            '<a href="#services-list-%s" data-toggle="collapse">%s</a>' % (record.id, value))

    def before_render(self, request):
        self.columns.hide('id')


class QuoteServiceTable(tables.Table):
    class Meta:
        model = QuoteService
        template_name = 'booking/quoteservices_list.html'
        fields = ['name', 'service_type', 'datetime_from', 'datetime_to', 'status']
    def render_name(self, value, record):
        obj_url = reverse(
            'common:booking_%s_change' % (QUOTESERVICE_TYPES[record.service_type]),
            args=(quote(record.pk),)
        )
        return format_html(
            '<a class="related-widget-wrapper-link" href="%s?_popup=1">%s</a>' % (obj_url, value))

    def before_render(self, request):
        self.columns.hide('service_type')


class QuotePaxVariantTable(tables.Table):
    class Meta:
        model = QuotePaxVariant
        template_name = 'booking/quoteservices_list.html'
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

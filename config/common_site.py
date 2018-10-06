from common.sites import SiteModel, CommonTabularInline, CommonStackedInline

from django.conf.urls import url
from django.contrib import admin, messages
from django.contrib.admin.options import csrf_protect_m, IS_POPUP_VAR, TO_FIELD_VAR
from django.contrib.admin import helpers
from django.contrib.admin.checks import ModelAdminChecks
from django.contrib.admin.utils import unquote
from django.core import checks
from django.core.exceptions import FieldDoesNotExist, ValidationError, PermissionDenied
from django.db import router, transaction
from django import forms
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _, ungettext

from config.forms import (
    AllotmentRoomTypeInlineForm
)
from config.models import (
    Location, RoomType,
    Allotment, AllotmentRoomType, AllotmentBoardType, AllotmentSupplement,
    Transfer, TransferSupplement,
    Extra, ExtraSupplement,
    AgencyAllotmentService, AgencyAllotmentDetail,
    AgencyTransferService, AgencyTransferDetail,
    AgencyExtraService, AgencyExtraDetail,
    ProviderAllotmentService, ProviderAllotmentDetail,
    ProviderTransferService, ProviderTransferDetail,
    ProviderExtraService, ProviderExtraDetail,
)

from functools import update_wrapper, partial

from reservas.admin import bookings_site


MENU_LABEL_CONFIG_BASIC = 'Configuration'

class IncorrectLookupParameters(Exception):
    pass

class LocationSiteModel(SiteModel):
    model_order = 6010
    menu_label = MENU_LABEL_CONFIG_BASIC
    fields = ('name', 'enabled',)
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)
    search_fields = ('name',)


class RoomTypeSiteModel(SiteModel):
    model_order = 6020
    menu_label = MENU_LABEL_CONFIG_BASIC
    fields = ('name', 'enabled',)
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)
    search_fields = ('name',)


class AllotmentRoomTypeInline(CommonTabularInline):
    model = AllotmentRoomType
    extra = 0
    show_change_link = True

    form = AllotmentRoomTypeInlineForm


class AllotmentRoomTypeSiteModel(SiteModel):
    fields = ('allotment', 'room_type', 'room_capacity',)
    list_display = ('allotment', 'room_type', 'room_capacity',)
    list_filter = ('room_type', 'room_capacity',)
    search_fields = ('allotment__name',)
    ordering = ('allotment__name',)


class AllotmentBoardTypeInline(CommonTabularInline):
    model = AllotmentBoardType
    extra = 0


class AllotmentSupplementInline(CommonTabularInline):
    model = AllotmentSupplement
    extra = 0


class AllotmentSiteModel(SiteModel):
    model_order = 6110
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Configuration Services'
    fields = ('name', 'location', 'time_from', 'time_to', 'enabled',)
    list_display = ('name', 'location', 'time_from', 'time_to', 'enabled',)
    list_filter = ('location', 'enabled',)
    search_fields = ('name', 'location__name',)
    ordering = ('enabled', 'name',)
    inlines = [AllotmentRoomTypeInline, AllotmentBoardTypeInline, AllotmentSupplementInline]


class TransferSupplementInline(CommonTabularInline):
    model = TransferSupplement
    extra = 0


class TransferSiteModel(SiteModel):
    model_order = 6120
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Configuration Services'
    fields = ('name', 'enabled',)
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)
    search_fields = ('name',)
    ordering = ('enabled', 'name',)
    readonly_fields = ('name',)
    inlines = [TransferSupplementInline]


class ExtraSupplementInline(CommonTabularInline):
    model = ExtraSupplement
    extra = 0


class ExtraSiteModel(SiteModel):
    model_order = 6130
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Configuration Services'
    fields = ('name', 'enabled',)
    list_display = ('name', 'enabled',)
    list_filter = ('enabled',)
    search_fields = ('name',)
    ordering = ('enabled', 'name',)
    inlines = [ExtraSupplementInline]


class ProviderAllotmentDetailInline(CommonStackedInline):
    model = ProviderAllotmentDetail
    extra = 1
    fields = (
        ('room_type','board_type',),
        ('ad_1_amount','ch_1_ad_1_amount','ch_2_ad_1_amount','ch_3_ad_1_amount',),
        ('ad_2_amount','ch_1_ad_2_amount','ch_2_ad_2_amount','ch_3_ad_2_amount',),
        ('ad_3_amount','ch_1_ad_3_amount','ch_2_ad_3_amount','ch_3_ad_3_amount',),
        ('ch_1_ad_0_amount','ch_2_ad_0_amount','ch_3_ad_0_amount',),
    )


class ProviderAllotmentServiceSiteModel(SiteModel):
    model_order = 7220
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Provider Catalogue'
    fields = ('provider', 'service', 'date_from', 'date_to', 'cost_type',)
    list_display = ('provider', 'service', 'date_from', 'date_to', 'cost_type',)
    search_fields = ('provider.name','service.name',)
    inlines = [ProviderAllotmentDetailInline]


class ProviderTransferDetailInline(CommonStackedInline):
    model = ProviderTransferDetail
    extra = 1
    fields = (
        ('a_location_from','a_location_to',),
        ('ad_1_amount','ch_1_ad_1_amount','ch_2_ad_1_amount','ch_3_ad_1_amount',),
        ('ad_2_amount','ch_1_ad_2_amount','ch_2_ad_2_amount','ch_3_ad_2_amount',),
        ('ad_3_amount','ch_1_ad_3_amount','ch_2_ad_3_amount','ch_3_ad_3_amount',),
        ('ch_1_ad_0_amount','ch_2_ad_0_amount','ch_3_ad_0_amount',),
    )


class ProviderTransferServiceSiteModel(SiteModel):
    model_order = 7230
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Provider Catalogue'
    fields = ('provider', 'service', 'date_from', 'date_to', 'cost_type',)
    list_display = ('provider', 'service', 'date_from', 'date_to', 'cost_type',)
    search_fields = ('provider.name','service.name',)
    inlines = [ProviderTransferDetailInline]


class ProviderExtraDetailInline(CommonStackedInline):
    model = ProviderExtraDetail
    extra = 1
    fields = (
        ('ad_1_amount','ch_1_ad_1_amount','ch_2_ad_1_amount','ch_3_ad_1_amount',),
        ('ad_2_amount','ch_1_ad_2_amount','ch_2_ad_2_amount','ch_3_ad_2_amount',),
        ('ad_3_amount','ch_1_ad_3_amount','ch_2_ad_3_amount','ch_3_ad_3_amount',),
        ('ch_1_ad_0_amount','ch_2_ad_0_amount','ch_3_ad_0_amount',),
    )


class ProviderExtraServiceSiteModel(SiteModel):
    model_order = 7240
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Provider Catalogue'
    fields = ('provider', 'service', 'date_from', 'date_to', 'cost_type',)
    list_display = ('provider', 'service', 'date_from', 'date_to', 'cost_type',)
    search_fields = ('provider.name','service.name',)
    inlines = [ProviderExtraDetailInline]


class AgencyAllotmentDetailInline(CommonStackedInline):
    model = AgencyAllotmentDetail
    extra = 1
    fields = (
        ('room_type','board_type',),
        ('ad_1_amount','ch_1_ad_1_amount','ch_2_ad_1_amount','ch_3_ad_1_amount',),
        ('ad_2_amount','ch_1_ad_2_amount','ch_2_ad_2_amount','ch_3_ad_2_amount',),
        ('ad_3_amount','ch_1_ad_3_amount','ch_2_ad_3_amount','ch_3_ad_3_amount',),
        ('ch_1_ad_0_amount','ch_2_ad_0_amount','ch_3_ad_0_amount',),
    )


class AgencyAllotmentServiceSiteModel(SiteModel):
    model_order = 7120
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Agency Catalogue'
    fields = ('agency', 'service', 'date_from', 'date_to', 'cost_type',)
    list_display = ('agency', 'service', 'date_from', 'date_to', 'cost_type',)
    search_fields = ('agency.name','service.name',)
    inlines = [AgencyAllotmentDetailInline]


class AgencyTransferDetailInline(CommonStackedInline):
    model = AgencyTransferDetail
    extra = 1
    fields = (
        ('a_location_from','a_location_to',),
        ('ad_1_amount','ch_1_ad_1_amount','ch_2_ad_1_amount','ch_3_ad_1_amount',),
        ('ad_2_amount','ch_1_ad_2_amount','ch_2_ad_2_amount','ch_3_ad_2_amount',),
        ('ad_3_amount','ch_1_ad_3_amount','ch_2_ad_3_amount','ch_3_ad_3_amount',),
        ('ch_1_ad_0_amount','ch_2_ad_0_amount','ch_3_ad_0_amount',),
    )


class AgencyTransferServiceSiteModel(SiteModel):
    model_order = 7130
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Agency Catalogue'
    fields = ('agency', 'service', 'date_from', 'date_to', 'cost_type',)
    list_display = ('agency', 'service', 'date_from', 'date_to', 'cost_type',)
    search_fields = ('agency.name','service.name',)
    inlines = [AgencyTransferDetailInline]


class AgencyExtraDetailInline(CommonStackedInline):
    model = AgencyExtraDetail
    extra = 1
    fields = (
        ('ad_1_amount','ch_1_ad_1_amount','ch_2_ad_1_amount','ch_3_ad_1_amount',),
        ('ad_2_amount','ch_1_ad_2_amount','ch_2_ad_2_amount','ch_3_ad_2_amount',),
        ('ad_3_amount','ch_1_ad_3_amount','ch_2_ad_3_amount','ch_3_ad_3_amount',),
        ('ch_1_ad_0_amount','ch_2_ad_0_amount','ch_3_ad_0_amount',),
    )


class AgencyExtraServiceSiteModel(SiteModel):
    model_order = 7140
    menu_label = MENU_LABEL_CONFIG_BASIC
    menu_group = 'Agency Catalogue'
    fields = ('agency', 'service', 'date_from', 'date_to', 'cost_type',)
    list_display = ('agency', 'service', 'date_from', 'date_to', 'cost_type',)
    search_fields = ('agency.name','service.name',)
    inlines = [AgencyExtraDetailInline]


bookings_site.register(Location, LocationSiteModel)
bookings_site.register(RoomType, RoomTypeSiteModel)

bookings_site.register(AllotmentRoomType, AllotmentRoomTypeSiteModel)

bookings_site.register(Allotment, AllotmentSiteModel)
bookings_site.register(Transfer, TransferSiteModel)
bookings_site.register(Extra, ExtraSiteModel)

bookings_site.register(AgencyAllotmentService, AgencyAllotmentServiceSiteModel)
bookings_site.register(AgencyTransferService, AgencyTransferServiceSiteModel)
bookings_site.register(AgencyExtraService, AgencyExtraServiceSiteModel)

bookings_site.register(ProviderAllotmentService, ProviderAllotmentServiceSiteModel)
bookings_site.register(ProviderTransferService, ProviderTransferServiceSiteModel)
bookings_site.register(ProviderExtraService, ProviderExtraServiceSiteModel)

# coding: utf-8
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from django.contrib import admin
from eventex.subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'subscription_date', 'today_date')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True

    def subscription_date(self, obj):
        return obj.created_at.date()

    subscription_date.short_description = _(u'Data Inscrição')
    def today_date(self, obj):
        return datetime.today().date()

    today_date.short_description = _(u'Hoje')

admin.site.register(Subscription, SubscriptionAdmin)


from django.contrib import admin
from .models import Subscriber, Transaction, Provider,Proposed_insucovers


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Proposed_insucovers)
class Proposed_insucoversAdmin(admin.ModelAdmin):
    pass
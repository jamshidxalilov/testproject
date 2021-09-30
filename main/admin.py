from django.contrib import admin
from .models import Country, Region, District, Partner, Organization, Branch, Status, Action, Report, Street

class CountryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

    class Meta:
        model = Country

admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'country'
    ]

    class Meta:
        model = Region

admin.site.register(Region, RegionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'country',
        'region'
    ]

    class Meta:
        model = District

admin.site.register(District, DistrictAdmin)

class PartnerAdmin(admin.ModelAdmin):
    pass


    class Meta:
        model = Partner

admin.site.register(Partner, PartnerAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Organization

admin.site.register(Organization, OrganizationAdmin)

class BranchAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Branch

admin.site.register(Branch, BranchAdmin)

class StatusAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class ActionAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Action

admin.site.register(Action, ActionAdmin)

class ReportAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Report

admin.site.register(Report, ReportAdmin)


class StreetAdmin(admin.ModelAdmin):
    pass

    class Meta:
        model = Street

admin.site.register(Street, StreetAdmin)
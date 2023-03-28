from django.contrib import admin


class OtpCodeAdmin(admin.ModelAdmin):
    list_display = [
        'phone',
        'code',
        'created',
    ]
    list_filter = [
        'created',
    ]
    search_fields = [
        'phone',
        'code',
    ]
    ordering = [
        '-created',
    ]

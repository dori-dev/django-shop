from django.contrib import admin

from account import models
from account.admin import user, otp

admin.site.register(models.User, user.UserAdmin)
admin.site.register(models.OtpCode, otp.OtpCodeAdmin)

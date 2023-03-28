from django.contrib import admin
from django.contrib.auth.models import Group

from account import models
from account.admin import user, otp

admin.site.unregister(Group)
admin.site.register(models.User, user.UserAdmin)
admin.site.register(models.OtpCode, otp.OtpCodeAdmin)

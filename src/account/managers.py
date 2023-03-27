from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, email, password, full_name=None):
        if not phone:
            raise ValueError('User should have a phone number')
        if not email:
            raise ValueError('User should have a email address')
        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password, full_name=None):
        user = self.create_user(phone, email, password, full_name)
        user.is_admin = True
        user.save(using=self._db)
        return user

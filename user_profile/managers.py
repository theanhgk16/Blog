from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Người dùng phải được thiết lập")

        if not email:
            raise ValueError("Email phải được thiết lập")

        if not password:
            raise ValueError("Mật khẩu phải được thiết lập")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("The superuser must have is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("The superuser must have is_superuser=True")

        return self.create_user(
            username,
            email,
            password,
            **extra_fields
        )
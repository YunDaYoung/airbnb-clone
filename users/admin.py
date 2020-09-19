from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # admin 패널에서 user을 보고 싶다
class CustomUserAdmin(UserAdmin):  # user을 컨트롤하는 클래스

    """Custom User Admin """

    # list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ('language', 'currency', 'superhost', )

    # field 집합    #Banana가 소제목, fields투플이 내부 필드들
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

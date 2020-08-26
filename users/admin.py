from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# # User 모델을 admin site에서 입력 값을 바꿀 수 있게 Custom 사용법을 이용합니다.
# admin.site.resiger(models.User, CustomUserAdmin) 와 같다.
@admin.register(User)  # 어떤 model로 생성?
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profiles",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
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
    )
    list_filter = UserAdmin.list_filter + ("superhost",)

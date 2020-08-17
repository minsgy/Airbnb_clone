from django.contrib import admin
from .models import User

# Register your models here.
# # User 모델을 admin site에서 입력 값을 바꿀 수 있게 Custom 사용법을 이용합니다.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

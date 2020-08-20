from django.db import models

# 모델들의 공통 값 넣기
# 해당 모델은 DB에 들어가면안되고, 이 모델을 쓰는 다른 Model이 들어가야함.
class TimeStempedModel(models.Model):
    """Time Stamp Model"""

    created = models.DateTimeField(auto_now_add=True)
    # 각 모델들이 만들어진 시기
    # auto_now_add=True (Model 생성할 때, date, time 업데이트)
    updated = models.DateTimeField(auto_now=True)
    # 각 모델들이 업데이트 된 시기
    # auto_now=True (Model을 저장할 때마다  date, time 기록 저장)

    class Meta:  # 특이사항
        abstract = True  # abstract Model은, DB에 들어가지 않는 Model


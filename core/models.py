from django.db import models


class TimeStempModel(models.Model):

    """ Time Stemp Model """

    created = models.DateTimeField(auto_now_add=True)  # 생성 될때마다 기록
    updated = models.DateTimeField(auto_now=True)  # 세이브 될때마다 기록

    # 이 클래스의 created와 updated는 디비에 구조를 만들지 않고 다른 어플리케이션에서 재사용을 위해서만 사용하기 위해

    class Meta:
        abstract = True  # abstract을 이용해 데이터베이스에는 나타나지 않는 모델로 지정가능

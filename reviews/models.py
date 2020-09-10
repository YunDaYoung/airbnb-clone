from django.db import models
from core import models as core_models


class Review(core_models.TimeStempModel):

    """ Review Model definition """

    review = models.TextField()

    accuracy = models.IntegerField()  # 정확성
    communication = models.IntegerField()  # 의사소통
    cleanliness = models.IntegerField()  # 청결도
    location = models.IntegerField()  # 위치
    check_in = models.IntegerField()  # 체크인
    value = models.IntegerField()  # 가격대비 만족도

    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"  # form(형태) 지정

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6

        return round(avg, 2)  # 소수점 2번째 자리까지

    rating_average.short_description = "Avg."
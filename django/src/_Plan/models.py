from django.db import models

class TimeSlot(models.Model):
    start_time       = models.TimeField()
    end_time         = models.TimeField()

    def __str__(self):
        return '{} {}'.format(self.start_time, self.end_time)

class Address(models.Model):
    location_name    = models.CharField(max_length=45)
    address          = models.TextField()

    # map api를 사용할 때 정확한 위치를 나타내 주기 위해 정의
    latitude         = models.CharField(max_length=45) # 위도
    longitude        = models.CharField(max_length=45) # 경도

    def __str__(self):
        return '{} {}'.format(self.location_name, self.address)

class Plan(models.Model):
    user_id          = models.ForeignKey('_User.User', on_delete=models.CASCADE)
    plan_name        = models.CharField(max_length=45)
    share_flag       = models.BooleanField()            # share_flag (true:공유 가능 / false:공유 불가능)
    start_datetime   = models.DateField(auto_now_add=False)
    start_address_id = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='start_time')
    end_datetime     = models.DateField(auto_now_add=False)
    end_address_id   = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='end_time')

    def __str__(self):
        return self.plan_name

class Plan_Item(models.Model):
    plan_id          = models.ForeignKey('Plan', on_delete=models.CASCADE)
    item_id          = models.ForeignKey('_Item.Item', on_delete=models.CASCADE)
    timeslot_id      = models.ForeignKey('TimeSlot', on_delete=models.CASCADE)
    day              = models.IntegerField() # 장소에서 몇일 동안 머무를 것인지 나타내 주는 데이터ㄴㄴ

    def __str__(self):
        return str(self.day)
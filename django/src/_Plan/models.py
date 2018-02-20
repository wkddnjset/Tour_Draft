from django.db import models

class TimeSlot(models.Model):
    start_time       = models.TimeField()
    end_time         = models.TimeField()

    def __str__(self):
        return '{} {}'.format(self.start_time, self.end_time)

class Address(models.Model):
    location_name    = models.CharField(max_length=45)
    address          = models.TextField()
    latitude         = models.CharField(max_length=45)
    longitude        = models.CharField(max_length=45)

    def __str__(self):
        return '{} {}'.format(self.location_name, self.address)

class Plan(models.Model):
    user_id          = models.ForeignKey('_User.User', on_delete=models.CASCADE, primary_key=True)
    plan_name        = models.CharField(max_length=45)
    share_flag       = models.BooleanField()
    start_datetime   = models.DateField(auto_now_add=True)
    start_address_id = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='start_time')
    end_datetime     = models.DateField(auto_now_add=True)
    end_address_id   = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='end_time', default=0)

    def __str__(self):
        return self.plan_name

class Plan_Item(models.Model):
    item_id          = models.ForeignKey('_Item.Item', on_delete=models.CASCADE)
    itemslot_id      = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    day              = models.IntegerField()

    def __str__(self):
        return self.day
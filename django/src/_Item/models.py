from django.db import models

# Create your models here.

class Item(models.Model):
    category_id     = models.ForeignKey('_User.Category', on_delete=models.CASCADE)
    title           = models.CharField(max_length=45)
    subtitle        = models.TextField()
    content         = models.TextField()
    main_img        = models.ImageField(blank=True)
    sub_img_1       = models.ImageField(blank=True)
    sub_img_2       = models.ImageField(blank=True)
    sub_img_3       = models.ImageField(blank=True)
    address         = models.TextField()
    latitude        = models.CharField(max_length=45)
    longitude       = models.CharField(max_length=45)
    tel             = models.CharField(max_length=45)
    open_time       = models.TimeField()
    close_time      = models.TimeField()

    def __str__(self):
        return str(self.title)



class Tag(models.Model):
    tag_name    = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tag_name)

class Item_Tag(models.Model):
    class Meta:
        unique_together = (('item_id', 'tag_id'),)

    item_id     = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag_id      = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Distance(models.Model):
    class Meta:
        unique_together = (('src','dst'),)

    src = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = "src")
    dst = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = "dst")
    distance = models.IntegerField()

    def __str__(self):
        return str(self.distance)

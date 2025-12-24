from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="カテゴリ名"
    )

    keyword = models.CharField(
        max_length=50,
        verbose_name="キーワード",
        null=True,
        blank=True
    )
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ一覧"


class FoodCategory(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="食べ物名"
    )


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "食べ物"
        verbose_name_plural = "食べ物一覧"


class Store(models.Model):
    name = models.CharField(max_length=200)

    price = models.PositiveIntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)


    food_categories = models.ManyToManyField(
        FoodCategory,
        blank=True,
        related_name='stores'
    )
    

    image = models.ImageField(upload_to='store_images/', blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    business_hours = models.CharField(max_length=100, blank=True, null=True)

    holiday = models.CharField(max_length=100, blank=True, null=True)

    postal_code = models.CharField(max_length=10, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
    


category = models.CharField(
    max_length=20,
    choices=[
        ('japanese', '和食'),
        ('western', '洋食'),
        ('chinese', '中華'),
    ]
)



food_category = models.CharField(
    max_length=50,
    blank=True,
    null=True
)



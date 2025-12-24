from django.contrib import admin
from .models import Store, Category, FoodCategory



class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'get_food_categories')
    search_fields = ('name',)
    list_filter = ('category', 'food_categories')
    filter_horizontal = ('food_categories',)

    def get_food_categories(self, obj):
        return ", ".join(fc.name for fc in obj.food_categories.all())

    get_food_categories.short_description = 'Food Categories'


    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class Food_categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)



admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodCategory, Food_categoryAdmin)
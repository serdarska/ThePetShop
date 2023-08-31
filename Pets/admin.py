from django.contrib import admin

from .models import DogBed, DogFood, DogToy, DogCollar, CatFood, CatToy, UserProfile

# Register your models here.
admin.site.register(DogToy)
admin.site.register(DogBed)
admin.site.register(DogFood)
admin.site.register(DogCollar)
admin.site.register(CatToy)
admin.site.register(CatFood)


class UserProfileAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(UserProfile, UserProfileAdmin)

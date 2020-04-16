from django.contrib import admin
from app.instance import models


class InstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Instance, InstanceAdmin)


class InstanceRoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.InstanceRoom, InstanceRoomAdmin)


class InstanceObjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.InstanceObject, InstanceObjectAdmin)


class InstanceNpcAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.InstanceNpc, InstanceNpcAdmin)


class InstanceLogAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.InstanceLog, InstanceLogAdmin)

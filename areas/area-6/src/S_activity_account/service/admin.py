from django.contrib import admin

from service import models

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ScientificActivity)
class ScientificActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.IndividualPlan)
class IndividualPlanAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ScientificWork)
class ScientificWorkAdmin(admin.ModelAdmin):
    pass

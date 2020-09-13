from django.contrib import admin
from .models import product,slider,order,feedback



# Register your models here.
admin.site.site_header="Admin Pannel"
admin.site.register(product)
admin.site.register(slider)
admin.site.register(order)
admin.site.register(feedback)
# admin.site.register(registerform)

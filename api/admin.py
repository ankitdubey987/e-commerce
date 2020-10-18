from django.contrib import admin
from api.models import Category,CustomerProfile,OrderDetail,Orders,Payment,Product,Shippers,Supplier
# Register your models here.
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(CustomerProfile)
admin.site.register(Orders)
admin.site.register(OrderDetail)
admin.site.register(Payment)
admin.site.register(Shippers)
admin.site.register(Product)


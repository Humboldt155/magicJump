from django.contrib import admin
from import_export import resources

from .models import Model
from .models import Product
from .models import Department
from .models import Attribute
from .models import Value

# Register your models here.
admin.site.register(Model)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Attribute)
admin.site.register(Value)

class ModelResource(resources.ModelResource):
    class Meta:
        model = Model
        fields = ('id', 'name')
        export_order = ('id', 'name')

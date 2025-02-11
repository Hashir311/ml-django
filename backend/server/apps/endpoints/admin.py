from django.contrib import admin
from .models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest

print(admin.site.register(Endpoint))
print(admin.site.register(MLAlgorithm))
print(admin.site.register(MLAlgorithmStatus))
print(admin.site.register(MLRequest))


# class EndpointAdmin(admin.ModelAdmin):
#     list_display = ('name', 'owner', 'created_at')  # Fields to display in the list view
#     search_fields = ('name', 'owner')  # Add a search bar for these fields

# class MLAlgorithmAdmin(admin.ModelAdmin):
#     list_display = ('name', 'version', 'owner', 'parent_endpoint')
#     list_filter = ('version', 'owner')  # Add filters for these fields

# class MLAlgorithmStatusAdmin(admin.ModelAdmin):
#     list_display = ('status', 'active', 'created_by', 'parent_mlalgorithm')
#     list_filter = ('status', 'active')

# class MLRequestAdmin(admin.ModelAdmin):
#     list_display = ('input_data', 'response', 'parent_mlalgorithm', 'created_at')
#     list_filter = ('parent_mlalgorithm',)
# admin.site.register(Endpoint, EndpointAdmin)
# admin.site.register(MLAlgorithm, MLAlgorithmAdmin)
# admin.site.register(MLAlgorithmStatus, MLAlgorithmStatusAdmin)
# admin.site.register(MLRequest, MLRequestAdmin)

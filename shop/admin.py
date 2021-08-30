from django.contrib.admin import AdminSite


class AppAdmin(AdminSite):
    def index(self, request, extra_context=None):
        # Update extra_context with new variables
        return super().index(request, extra_context)
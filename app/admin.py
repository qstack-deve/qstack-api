from django.contrib import admin
from django.utils.html import format_html
from .models import (
    User, Profile, Staff, Category, Skill, Role, Portfolio, Social, Tag, Contact
)
from .models.jobs import Job, Responsibility, Requirement, Benefit, SalaryRange

# --- Inlines ---
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    
class SocialInline(admin.TabularInline):
    model = Social
    extra = 1
    fields = ('platform', 'url')

class ResponsibilityInline(admin.TabularInline):
    model = Responsibility
    extra = 1

class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1

class BenefitInline(admin.TabularInline):
    model = Benefit
    extra = 1

class SalaryRangeInline(admin.StackedInline):
    model = SalaryRange
    can_delete = False # Usually 1-to-1 jobs have exactly one salary range

# --- Admin Classes ---
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'message')

    # def mark_as_read(self, request, queryset):
    #     updated = queryset.update(is_read=True)
    #     self.message_user(request, f"{updated} message(s) marked as read.")
    # mark_as_read.short_description = "Mark selected messages as read"

    # def mark_as_unread(self, request, queryset):
    #     updated = queryset.update(is_read=False)
    #     self.message_user(request, f"{updated} message(s) marked as unread.")
    # mark_as_unread.short_description = "Mark selected messages as unread"
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [SocialInline]
    list_display = ('display_avatar', 'first_name', 'last_name', 'role', 'email')
    list_display_links = ('display_avatar', 'first_name', 'last_name')
    list_filter = ('role', 'skills')
    search_fields = ('first_name', 'last_name', 'email')
    prepopulated_fields = {"slug": ("first_name", "last_name")} # Automates slug entry
    filter_horizontal = ('skills',) # Better UI for ManyToMany fields

    def display_avatar(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width: 40px; height: 40px; border-radius: 50%;" />', obj.avatar.url)
        return "No Image"
    display_avatar.short_description = 'Avatar'

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'title', 'category', 'status', 'created_at')
    list_filter = ('status', 'category', 'tags')
    search_at = ('title', 'client')
    filter_horizontal = ('tags',)
    list_editable = ('status',) # Change status directly from the list view

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 4px;" />', obj.image.url)
        return "—"

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [ResponsibilityInline, RequirementInline, BenefitInline, SalaryRangeInline]
    list_display = ('title', 'department', 'location', 'job_type', 'posted_at')
    list_filter = ('job_type', 'department', )
    search_fields = ('title', 'description')
    date_hierarchy = 'posted_at' # Adds a date drill-down at the top

# --- Simple Registers ---

@admin.register(Category, Skill, Role, Tag)
class LookupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(User)
admin.site.register(Profile)
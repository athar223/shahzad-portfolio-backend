from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Video, Skill, ContactMessage, ClientReview, Organization, Expertise, SiteSettings


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'thumbnail_preview', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    list_filter = ['category']

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;border-radius:4px;" />', obj.thumbnail.url)
        return "—"
    thumbnail_preview.short_description = "Thumbnail"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'video_type', 'thumbnail_preview', 'order', 'created_at']
    list_editable = ['order', 'category']
    search_fields = ['title']
    list_filter = ['category']

    def video_type(self, obj):
        if obj.video_file:
            return "Uploaded File"
        return "Embed URL"
    video_type.short_description = "Type"

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;border-radius:4px;" />', obj.thumbnail.url)
        return "—"
    thumbnail_preview.short_description = "Thumbnail"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read', 'created_at']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'message', 'created_at']


@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'rating', 'image_preview', 'order', 'created_at']
    list_editable = ['rating', 'order']
    search_fields = ['client_name']

    def image_preview(self, obj):
        if obj.client_image:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:cover;border-radius:50%;" />', obj.client_image.url)
        return "—"
    image_preview.short_description = "Photo"


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'youtube_link', 'order']
    list_editable = ['order']
    search_fields = ['name']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80" height="40" style="object-fit:contain;background:#fff;padding:2px;border-radius:4px;" />', obj.logo.url)
        return "—"
    logo_preview.short_description = "Logo"


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_name', 'order']
    list_editable = ['order', 'icon_name']
    search_fields = ['title']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image_preview', 'email', 'cv_preview', 'updated_at']
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title_line1', 'hero_title_line2', 'hero_subtitle'),
            'description': 'Edit the main hero text on the homepage.',
        }),
        ('Hero Stats', {
            'fields': ('stat1_value', 'stat1_label', 'stat2_value', 'stat2_label'),
        }),
        ('About Section', {
            'fields': ('about_bio',),
            'description': 'Edit the bio paragraph in the About section. Expertise cards are managed separately under "Expertise Areas".',
        }),
        ('Profile & CV', {
            'fields': ('profile_image', 'cv_file'),
        }),
        ('Contact Details', {
            'fields': ('email', 'phone', 'location', 'whatsapp_number'),
        }),
        ('Social Media Links', {
            'fields': ('youtube_url', 'instagram_url', 'linkedin_url', 'twitter_url', 'facebook_url'),
        }),
    )

    def image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="40" height="40" style="object-fit:cover;border-radius:50%;" />', obj.profile_image.url)
        return "—"
    image_preview.short_description = "Photo"

    def cv_preview(self, obj):
        if obj.cv_file:
            return format_html('<a href="{}" target="_blank">Download CV</a>', obj.cv_file.url)
        return "—"
    cv_preview.short_description = "CV"

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

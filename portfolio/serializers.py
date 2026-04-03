from rest_framework import serializers
from .models import Project, Video, Skill, ContactMessage, ClientReview, Organization, Expertise, SiteSettings


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'thumbnail', 'category', 'link']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'category', 'embed_url', 'video_file', 'thumbnail', 'description']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency', 'icon']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message']


class ClientReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientReview
        fields = ['id', 'client_name', 'review_text', 'client_image', 'rating']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'logo', 'youtube_link']


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ['id', 'title', 'description', 'icon_name']


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            'profile_image', 'cv_file',
            'hero_title_line1', 'hero_title_line2', 'hero_subtitle',
            'stat1_value', 'stat1_label', 'stat2_value', 'stat2_label',
            'about_bio',
            'email', 'phone', 'location', 'whatsapp_number',
            'youtube_url', 'instagram_url', 'linkedin_url',
            'twitter_url', 'facebook_url',
        ]

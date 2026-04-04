from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings as django_settings
from .models import Project, Video, Skill, ClientReview, Organization, Expertise, SiteSettings
from .serializers import (
    ProjectSerializer, VideoSerializer, SkillSerializer,
    ContactMessageSerializer, ClientReviewSerializer,
    OrganizationSerializer, ExpertiseSerializer, SiteSettingsSerializer,
)


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        # Send email notification
        try:
            site = SiteSettings.objects.first()
            admin_email = site.email if site and site.email else None
            if admin_email:
                send_mail(
                    subject=f"New Contact Message from {contact.name}",
                    message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                    from_email=django_settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[admin_email],
                    fail_silently=True,
                )
        except Exception:
            pass

        return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)


class ClientReviewListView(generics.ListAPIView):
    queryset = ClientReview.objects.all()
    serializer_class = ClientReviewSerializer


class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ExpertiseListView(generics.ListAPIView):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer


class SiteSettingsView(APIView):
    def get(self, request):
        settings = SiteSettings.objects.first()
        if settings:
            serializer = SiteSettingsSerializer(settings, context={'request': request})
            return Response(serializer.data)
        return Response({
            "profile_image": None, "cv_file": None,
            "hero_title_line1": "Shahzad", "hero_title_line2": "Ahmad",
            "hero_subtitle": "Professional Video Editor & Graphic Designer",
            "stat1_value": "5+", "stat1_label": "Years Experience",
            "stat2_value": "1000+", "stat2_label": "Projects Completed",
            "about_bio": "",
            "email": "", "phone": "", "location": "",
            "whatsapp_number": "",
            "youtube_url": "", "instagram_url": "", "linkedin_url": "",
            "twitter_url": "", "facebook_url": "",
        })

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


CATEGORY_CHOICES = [
    ('reels', 'Reels Editing'),
    ('podcast', 'Podcast Editing'),
    ('documentary', 'Documentary Editing'),
]


class Video(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='reels')
    embed_url = models.URLField(blank=True, help_text="YouTube/Vimeo embed URL (optional if uploading a file)")
    video_file = models.FileField(upload_to='videos/files/', blank=True, help_text="Upload video directly (MP4, WebM)")
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency percentage (0-100)")
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.email}"


class ClientReview(models.Model):
    client_name = models.CharField(max_length=150)
    review_text = models.TextField()
    client_image = models.ImageField(upload_to='reviews/', blank=True)
    rating = models.IntegerField(default=5, help_text="Rating from 1 to 5")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.client_name} — {self.rating} stars"


class Organization(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='organizations/')
    youtube_link = models.URLField(blank=True, help_text="YouTube channel or video link")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Expertise(models.Model):
    title = models.CharField(max_length=100, help_text="e.g. Video Editing, Graphic Design")
    description = models.TextField()
    icon_name = models.CharField(max_length=50, default='video', help_text="Icon: video, image, calendar, camera, code, palette")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Expertise Areas"

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    # Hero Section
    hero_title_line1 = models.CharField(max_length=50, default='Shahzad', help_text="First line of name")
    hero_title_line2 = models.CharField(max_length=50, default='Ahmad', help_text="Second line of name")
    hero_subtitle = models.CharField(max_length=200, default='Professional Video Editor & Graphic Designer crafting stunning visual experiences that captivate and inspire.', help_text="Tagline below name")
    stat1_value = models.CharField(max_length=20, default='5+', help_text="First stat value")
    stat1_label = models.CharField(max_length=50, default='Years Experience', help_text="First stat label")
    stat2_value = models.CharField(max_length=20, default='1000+', help_text="Second stat value")
    stat2_label = models.CharField(max_length=50, default='Projects Completed', help_text="Second stat label")

    # About Section
    about_bio = models.TextField(
        default="I'm Shahzad Ahmad, a passionate video editor and graphic designer with over 5 years of experience. I specialize in creating high-quality visual content that helps brands stand out and connect with their audiences.",
        help_text="About section bio paragraph"
    )

    # Profile & CV
    profile_image = models.ImageField(upload_to='profile/', blank=True, help_text="Profile photo for hero section")
    cv_file = models.FileField(upload_to='cv/', blank=True, help_text="Upload your CV/Resume (PDF)")

    # Contact Details
    email = models.EmailField(blank=True, help_text="Contact email")
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=200, blank=True)
    whatsapp_number = models.CharField(max_length=30, blank=True, help_text="With country code e.g. +923001234567")

    # Social Media
    youtube_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

import uuid
from django.db import models
from django.utils.text import slugify

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    
    # Relationships
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            # Create slug: "Hassan Saidu" -> "hassan-saidu"
            original_slug = slugify(f"{self.first_name} {self.last_name}")
            queryset = Staff.objects.exclude(pk=self.pk).filter(slug=original_slug)
            
            # Handle duplicate names by appending a random string or ID
            if queryset.exists():
                self.slug = f"{original_slug}-{uuid.uuid4().hex[:4]}"
            else:
                self.slug = original_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Social(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('website', 'Portfolio/Website'),
    ]
    
    staff = models.ForeignKey(Staff, related_name="socials", on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=255)

    class Meta:
        unique_together = ('staff', 'platform') # Prevents duplicate platforms per user

    def __str__(self):
        return f"{self.staff.first_name}'s {self.platform}"
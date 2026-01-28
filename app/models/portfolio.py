from django.db import models
import uuid

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    STATUS_CHOICES = [
        ("live", "Live"),
        ("development", "In Development"), # Tweaked the grammar slightly
        ("managing", "Managing")
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(help_text="Short summary for cards")
    long_description = models.TextField(blank=True, help_text="Detailed case study")
    
    image = models.ImageField(upload_to='portfolio/%Y/%m/', blank=True, null=True)
    
    # Relationships
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="projects" # Allows category.projects.all()
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="projects")
    is_pinned = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='development')
    client = models.CharField(max_length=100, blank=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # Shows newest projects first by default

    def __str__(self):
        return self.title
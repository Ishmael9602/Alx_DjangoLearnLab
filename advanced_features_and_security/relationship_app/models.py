from django.db import models
from accounts.models import CustomUser as User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    """
    Author model representing book authors
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Book(models.Model):
    """
    Book model with a ForeignKey relationship to Author and custom permissions
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    class Meta:
        ordering = ['title']
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]


class Library(models.Model):
    """
    Library model with a ManyToMany relationship to Book
    """
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Libraries"


class Librarian(models.Model):
    """
    Librarian model with a OneToOne relationship to Library
    """
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    
    def __str__(self):
        return f"{self.name} - {self.library.name}"
    
    class Meta:
        ordering = ['name']


class UserProfile(models.Model):
    """
    UserProfile model extending Django's User model with role-based access control
    """
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'), 
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create UserProfile when a new User is created
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save UserProfile when User is saved
    """
    instance.userprofile.save()

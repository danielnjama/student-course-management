from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class OnlineStudents(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    email = models.EmailField(max_length=40, verbose_name="Email")
    course_ordered = models.CharField(max_length=50, verbose_name="Course Ordered")
    date_paid = models.DateTimeField(blank=True, null=True, verbose_name="Date Paid")
    date_completed = models.DateTimeField(blank=True, null=True, verbose_name="Date Completed")
    amount_paid = models.IntegerField(verbose_name="Amount Paid")
    order_id = models.IntegerField(verbose_name="Order ID")
    user_id = models.IntegerField(verbose_name="User ID")
    order_status = models.CharField(max_length=30, verbose_name="Order Status")

    class Meta:
        verbose_name = "Online Student"
        verbose_name_plural = "Online Students"
        unique_together = ['order_id', 'user_id']
        
    def __str__(self):
        return self.name


class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
@receiver(pre_save, sender=EmailTemplate)
def ensure_single_active(sender, instance, **kwargs):
    if instance.active:
    # Deactivate all other active EmailTemplate instances
        EmailTemplate.objects.exclude(pk=instance.pk).update(active=False)

from django.core.mail import send_mail
from django.contrib import admin, messages
from .models import OnlineStudents, EmailTemplate,EmailSettings


#get default senders email
try:
    email_settings = EmailSettings.objects.first()
except:
    email_settings = None
default_email_sender = ''
if email_settings:
    default_email_sender = email_settings.default_from_email



class OnlineStudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course_ordered', 'date_paid', 'date_completed', 'amount_paid')
    list_filter = ('date_paid', 'date_completed', 'order_status')
    search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
    date_hierarchy = 'date_paid'
    actions = ['send_email']

    def send_email(self, request, queryset):
        active_template = EmailTemplate.objects.filter(active=True).first()
        if not active_template:
            self.message_user(request, "No active email template found.", level=messages.ERROR)
            return

        for student in queryset:
            # Render the email content using the active template and student's data
            email_content = active_template.message.format(student_name=student.name, course=student.course_ordered)

            # Send email
            send_mail(
                active_template.subject,
                email_content,
                default_email_sender,  # Replace with your email sender
                [student.email],
                fail_silently=False,
            )

        self.message_user(request, "Emails sent successfully.")

    send_email.short_description = "Send email to selected students"


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'active')
    list_editable = ('active',)






class EmailSettingsAdmin(admin.ModelAdmin):
    list_display = ('host', 'user', 'default_from_email', 'port','use_tls')  # Customize the displayed fields in admin




admin.site.register(OnlineStudents, OnlineStudentsAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(EmailSettings, EmailSettingsAdmin)
















# from django.core.mail import send_mail
# from django.contrib import admin, messages
# from django import forms
# from django.template.response import TemplateResponse
# from .models import OnlineStudents, EmailTemplate





# class OnlineStudentsAdmin(admin.ModelAdmin):
#     list_display = ('name','email','course_ordered', 'date_paid', 'date_completed', 'amount_paid')
#     list_filter = ('date_paid', 'date_completed', 'order_status')
#     search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
#     date_hierarchy = 'date_paid'
    

# class EmailTemplateAdmin(admin.ModelAdmin):
#     list_display = ('subject','date','active')
#     list_editable = ('active',)


# admin.site.register(OnlineStudents, OnlineStudentsAdmin)
# admin.site.register(EmailTemplate,EmailTemplateAdmin)



# class OnlineStudentsAdmin(admin.ModelAdmin):
#     list_display = ('name','email','course_ordered', 'date_paid', 'date_completed', 'amount_paid')
#     list_filter = ('date_paid', 'date_completed', 'order_status')
#     search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
#     date_hierarchy = 'date_paid'

    

#     actions = ['send_email_template']




from django.core.mail import send_mail
from django.contrib import admin, messages
from .models import OnlineStudents, EmailTemplate


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
                'inmotion@dtechnologys.com',  # Replace with your email sender
                [student.email],
                fail_silently=False,
            )

        self.message_user(request, "Emails sent successfully.")

    send_email.short_description = "Send email to selected students"


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date', 'active')
    list_editable = ('active',)


admin.site.register(OnlineStudents, OnlineStudentsAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
















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



































# from django.core.mail import send_mail
# from django.contrib import admin
# from django import forms
# from django.contrib import messages
# from django.template.response import TemplateResponse  
# from .models import OnlineStudents, EmailTemplate

# class EmailForm(forms.Form):
#     email_template = forms.ModelChoiceField(queryset=EmailTemplate.objects.all(), label='Email Template', required=False)

#     def __init__(self, *args, **kwargs):
#         initial_template = kwargs.pop('initial_template', None)
#         super().__init__(*args, **kwargs)
#         if initial_template:
#             self.fields['email_template'].initial = initial_template


# def send_email_action(modeladmin, request, queryset):
#     initial_template = EmailTemplate.objects.first()
#     print("POST request received.")
#     if 'email_template' in request.POST:
#         print("Rendering template.")
#         form = EmailForm(request.POST, initial_template=initial_template)
#         print("Form:", form)
#         if form.is_valid():
#             print("Form is valid!")
#             selected_students = queryset
#             email_template = form.cleaned_data['email_template']
#             if email_template:
#                 selected_emails = selected_students.values_list('email', flat=True)
#                 for email in selected_emails:
#                     try:
#                         send_mail(
#                             subject=email_template.subject,
#                             message=email_template.message,
#                             from_email='inmotion@dtechnologys.com',
#                             recipient_list=[email],
#                             fail_silently=False,
#                         )
#                         print("Email sent to:", email)
#                     except Exception as e:
#                         print("Error sending email:", str(e))
#                 modeladmin.message_user(request, "Emails have been sent successfully.")
#             else:
#                 print("No email template selected.")
#         else:
#             print("Form is not valid:", form.errors)
#     else:
#         form = EmailForm(initial={'email_template': initial_template})
#         print("Form in GET:", form)

#     context = {
#         'form': form,
#         'title': 'Send email to selected students',
#     }
#     return TemplateResponse(request, 'admin/send_email_action.html', context)



# send_email_action.short_description = "Send email to selected students"

# class OnlineStudentsAdmin(admin.ModelAdmin):
#     list_display = ('name','email','course_ordered', 'date_paid', 'date_completed', 'amount_paid')
#     list_filter = ('date_paid', 'date_completed', 'order_status')
#     search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
#     date_hierarchy = 'date_paid'
#     actions = [send_email_action]

# admin.site.register(OnlineStudents, OnlineStudentsAdmin)
# admin.site.register(EmailTemplate)








































# from django.core.mail import send_mail
# from django.contrib import admin
# from django import forms
# from django.contrib import messages
# from django.template.response import TemplateResponse  
# from .models import OnlineStudents, EmailTemplate

# class EmailForm(forms.Form):
#     email_template = forms.ModelChoiceField(queryset=EmailTemplate.objects.all(), label='Email Template', required=False)

#     def __init__(self, *args, **kwargs):
#         initial_template = kwargs.pop('initial_template', None)
#         super().__init__(*args, **kwargs)
#         if initial_template:
#             self.fields['email_template'].initial = initial_template


# def send_email_action(modeladmin, request, queryset):
#     initial_template = EmailTemplate.objects.first()
#     print("POST request received.")
#     if 'send_email_action' in request.POST:
#         print("Rendering template.")
#         form = EmailForm(request.POST, initial_template=initial_template)
#         print("Form:", form)
#         if form.is_valid():
#             print("Form is valid!")
#             selected_students = queryset
#             email_template = form.cleaned_data['email_template']
#             if email_template:
#                 selected_emails = selected_students.values_list('email', flat=True)
#                 for email in selected_emails:
#                     try:
#                         send_mail(
#                             subject=email_template.subject,
#                             message=email_template.message,
#                             from_email='inmotion@dtechnologys.com',
#                             recipient_list=[email],
#                             fail_silently=False,
#                         )
#                         print("Email sent to:", email)
#                     except Exception as e:
#                         print("Error sending email:", str(e))
#                 modeladmin.message_user(request, "Emails have been sent successfully.")
#             else:
#                 print("No email template selected.")
#         else:
#             print("Form is not valid:", form.errors)
#     else:
#         form = EmailForm(initial={'email_template': initial_template})
#         print("Form in GET:", form)

#     context = {
#         'form': form,
#         'title': 'Send email to selected students',
#     }
#     return TemplateResponse(request, 'admin/send_email_action.html', context)


# send_email_action.short_description = "Send email to selected students"

# class OnlineStudentsAdmin(admin.ModelAdmin):
#     list_display = ('name','email','course_ordered', 'date_paid', 'date_completed', 'amount_paid')
#     list_filter = ('date_paid', 'date_completed', 'order_status')
#     search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
#     date_hierarchy = 'date_paid'
#     actions = [send_email_action]

# admin.site.register(OnlineStudents, OnlineStudentsAdmin)
# admin.site.register(EmailTemplate)















































# from django.core.mail import send_mail
# from django.contrib import admin
# from django import forms
# from django.contrib import messages
# from django.template.response import TemplateResponse  
# from .models import OnlineStudents, EmailTemplate

# class EmailForm(forms.Form):
#     email_template = forms.ModelChoiceField(queryset=EmailTemplate.objects.all(), label='Email Template')

#     def __init__(self, *args, **kwargs):
#         initial_template = kwargs.pop('initial_template', None)
#         super().__init__(*args, **kwargs)
#         if initial_template:
#             self.fields['email_template'].initial = initial_template


# def send_email_action(modeladmin, request, queryset):
#     initial_template = EmailTemplate.objects.first()
#     if request.POST.get('action') == 'send_email_action':
#         form = EmailForm(request.POST, initial_template=initial_template)
#         print(form)
#         print(form.is_valid())
#         if form.is_valid():
#             selected_students = queryset
#             email_template = form.cleaned_data['email_template']
#             selected_emails = selected_students.values_list('email', flat=True)
#             for email in selected_emails:
#                 try:
#                     send_mail(
#                         subject=email_template.subject,
#                         message=email_template.message,
#                         from_email='inmotion@dtechnologys.com',
#                         recipient_list=[email],
#                         fail_silently=False,
#                     )
#                     print("Email sent to:", email)
#                 except Exception as e:
#                     print("Error sending email:", str(e))
#             modeladmin.message_user(request, "Emails have been sent successfully.")
#     else:
#         form = EmailForm(initial={'email_template': initial_template})
#         print("form in GET")
#         print(form)

#     context = {
#         'form': form,
#         'title': 'Send email to selected students',
#     }
#     return TemplateResponse(request, 'admin/send_email_action.html', context)


# send_email_action.short_description = "Send email to selected students"

# class OnlineStudentsAdmin(admin.ModelAdmin):
#     list_display = ('name','email','course_ordered', 'date_paid', 'date_completed', 'amount_paid')
#     list_filter = ('date_paid', 'date_completed', 'order_status')
#     search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
#     date_hierarchy = 'date_paid'
#     actions = [send_email_action]

# admin.site.register(OnlineStudents, OnlineStudentsAdmin)
# admin.site.register(EmailTemplate)













































# from django.contrib import admin
# from django.core.mail import send_mail
# from .models import OnlineStudents, EmailTemplate
# from django import forms
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib import messages
# from django.template.response import TemplateResponse

# class EmailForm(forms.Form):
#     email_template = forms.ModelChoiceField(queryset=EmailTemplate.objects.all(), label='Email Template')

# def send_email_action(modeladmin, request, queryset):
#     if 'apply' in request.POST:
#         form = EmailForm(request.POST)
#         print("we will check if form is valid")
#         if form.is_valid():
#             print("print form is valid")
#             selected_students = queryset
#             email_template = form.cleaned_data['email_template']
#             selected_emails = selected_students.values_list('email', flat=True)
#             print("email List" + selected_emails)
#             # for email in selected_emails:
#                 # Send email using the selected template
#             send_mail(
#                 subject=email_template.subject,
#                 message=email_template.message,
#                 from_email='inmotion@dtechnologys.com',
#                 recipient_list=[selected_emails,],
#                 fail_silently=False,
#             )
#             print("email sent!")
#             # Set success message
#             messages.success(request, "Emails have been sent successfully.")

#             # Redirect back to change list view after sending emails
#             return HttpResponseRedirect(request.get_full_path())
#     else:
#         form = EmailForm()

#     context = {
#         'form': form,
#         'title': 'Send email to selected students',
#     }

#     return TemplateResponse(request, 'admin/send_email_action.html', context)

# # send_email_action.short_description = "Send email to selected students"

# def send_email_action_template(request, **kwargs):
#     return admin.site.index(request, **kwargs)


# class OnlineStudentsAdmin(admin.ModelAdmin):
#     list_display = ('name','email','course_ordered', 'date_paid', 'date_completed', 'amount_paid')
#     list_filter = ('date_paid', 'date_completed', 'order_status')
#     search_fields = ('name', 'course_ordered', 'order_id', 'user_id')
#     date_hierarchy = 'date_paid'
#     actions = [send_email_action]

# admin.site.register(OnlineStudents, OnlineStudentsAdmin)
# admin.site.register(EmailTemplate)

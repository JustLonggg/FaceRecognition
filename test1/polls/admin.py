from django.contrib import admin
from polls.models import BookInfo,UserLogin

# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']

class UserLoginAdmin(admin.ModelAdmin):
    list_display = ['id', 'mail_address', 'password']


admin.site.register(BookInfo, BookInfoAdmin)

admin.site.register(UserLogin,UserLoginAdmin)
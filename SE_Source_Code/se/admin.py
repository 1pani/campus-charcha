from django.contrib import admin
from .models import Topic,Question,Answer,Comment,AnswerFlag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('no_of_views', 'no_of_posts',)

admin.site.register(Topic , PostAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(AnswerFlag)

admin.site.site_header = 'Campus Charcha Admin Dashboard '



from django.contrib import admin
from app1.models import home_video_links
from app1.models import video_page_links
from app1.models import table_user

admin.site.register(home_video_links)
admin.site.register(video_page_links)
admin.site.register(table_user)

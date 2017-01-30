from django.core.management.base import BaseCommand, CommandError
from page.models import Page

class Command(BaseCommand):

    def handle(self, *args, **options):
        print 'Hello!!'
        for i in range(100):
            page = Page()
            page.title = 'dddsadfasfas'
            page.content = 'sdfsdf sdfsd'
            page.meta_content = 'ffff'
            page.meta_title = 'title'
            page.meta_keywords = 'ddddd'
            page.slug = 'slug'
            page.save()
            print 'It has done %s - %s!!!' % (i,i)

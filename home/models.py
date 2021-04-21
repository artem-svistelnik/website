from django.db import models

from wagtail.core.models import Page,Orderable
from wagtail.core.fields import RichTextField,Creator,StreamField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel,MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

#api
from wagtail.api import APIField


from phonenumber_field.modelfields import PhoneNumberField
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from django.utils import timezone
#Теги
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.models import ClusterableModel

class HomePage(Page):
    contact_data_email = models.EmailField(blank=False,verbose_name='Email для связи',default='example@mail.com')
    contact_data_phone = PhoneNumberField(blank=False, region='UA', verbose_name='Контактный номер',default='+380999999999')

    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('contact_data_email', ),
        FieldPanel('contact_data_phone', ),
        InlinePanel('gallery_images', label="Галлерея изображений"),
    ]

    # Export fields over the API
    # api_fields = [
    #     APIField('title_ru'),
    #     APIField('title_uk'),
    #     APIField('body_ru'),
    #     APIField('body_uk'),
    #     APIField('contact_data_email'),
    #     APIField('contact_data_phone'),
    #     APIField('contact_data_phone'),
    #     APIField('gallery_images'),
    #     APIField('about_company'),
    #
    #       # This will nest the relevant BlogPageAuthor objects in the API response
    # ]


class HomeHeaderGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250,verbose_name='Подпись к изображению')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
    # api_fields = [
    #     APIField('image'),
    # ]


class AboutCompanyPage(Page):
    page=ParentalKey(HomePage, on_delete=models.CASCADE, related_name='about_company',verbose_name='О компании',default=3)
    about_company_text = RichTextField(blank=False,verbose_name='Текст о компании')
    content_panels = Page.content_panels + [
        FieldPanel('about_company_text', classname="full"),
        InlinePanel('activities', label="Виды деятельности"),
    ]
    # api_fields = [
    #     APIField('about_company_text_ru'),
    #     APIField('about_company_text_uk'),
    #     APIField('activities'),
    # ]


class Activities(Orderable):
    page=ParentalKey(AboutCompanyPage, on_delete=models.CASCADE, related_name='activities',verbose_name='Вид деятельности')
    kind_of_activity=models.TextField(max_length=1000,verbose_name='Вид деятельности')
    panels = [
        FieldPanel('kind_of_activity'),
    ]
    # api_fields = [
    #     APIField('kind_of_activity_ru'),
    #     APIField('kind_of_activity_uk'),
    # ]
######################################



# class HeadingNewsPublications(Orderable,ClusterableModel,models.Model):
#     name_heading_ru=models.CharField(max_length=255,verbose_name='Название рубрики')
#     name_heading_uk=models.CharField(max_length=255,verbose_name='Назва рубрики',default='News')
#
#     panels=[
#         FieldPanel('name_heading_ru'),
#         FieldPanel('name_heading_uk'),
#     ]
#     api_fields = [
#         APIField('name_heading_ru'),
#         APIField('name_heading_uk'),
#     ]
#     def __str__(self):
#         # return self.name_heading
#         return self.name_heading_ru + '/' + self.name_heading_uk

class NewsPublicationPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'NewsPublicationPage',
        related_name='tagged_items',
        verbose_name='Теги',
        on_delete=models.CASCADE
    )






class HeadingNewsPublicationsTypes(Orderable,ClusterableModel,models.Model):
    name_heading_ru=models.CharField(max_length=255,verbose_name='Название рубрики')
    name_heading_uk=models.CharField(max_length=255,verbose_name='Назва рубрики')
    # def __str__(self):
    #     return self.name_heading
    def __str__(self):
        # return self.name_heading
        return self.name_heading_ru + '/' + self.name_heading_uk

    class Meta:
        verbose_name_plural='Рубрики для новостей/публикаций'
        verbose_name='Рубрики для новостей/публикаций'

    content_panels = Page.content_panels + [
        FieldPanel('name_heading_ru'),
        FieldPanel('name_heading_uk'),
    ]
    # api_fields = [
    #     APIField(name_heading_ru),
    #     APIField(name_heading_uk),
    # ]

from rest_framework import routers, serializers
class HeadingNewsPublicationsTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeadingNewsPublicationsTypes

        fields = ('name_heading_ru','name_heading_uk')
        # fields = '__all__'


class NewsPublicationPage(Page,models.Model):
    publication_heading_2=models.ForeignKey('HeadingNewsPublicationsTypes',related_name='publication_2',on_delete=models.CASCADE,
                                            verbose_name='Название рубрики',
                                            blank=True,default=3)
    # publication_heading=ParentalKey(HeadingNewsPublications,related_name='publication',on_delete=models.CASCADE,verbose_name='Название рубрики')
    publication_heading=ParentalKey(HeadingNewsPublicationsTypes,related_name='publication',on_delete=models.CASCADE,verbose_name='Название рубрики')
    publication_title=models.CharField(max_length=255,verbose_name='Название публикации/новости')
    publication_text =models.TextField(max_length=10000,verbose_name='Текст публикации/новости')
    tags = ClusterTaggableManager(through=NewsPublicationPageTag, blank=True)
    publication_image = models.ForeignKey('wagtailimages.Image', blank=False,
                                                                 on_delete=models.CASCADE,
                                                                 related_name='+')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации/новости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания публикации/новости',
                                   editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения публикации/новости')
    caption = models.CharField(blank=True, max_length=255, verbose_name='Подпись к изображению')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('tags'),
        ], heading="Теги"),
        MultiFieldPanel([
            FieldPanel('publication_heading'),
            FieldPanel('publication_heading_2'),
            # InlinePanel('news_page_headings'),
            FieldPanel('publication_title'),
            FieldPanel('publication_text'),
        ], heading="Текстовая информация публикации"),

        MultiFieldPanel([
            ImageChooserPanel('publication_image'),
            FieldPanel('caption'),
        ], heading="Изображение для публикации/новости"),

    ]
    # api_fields = [
    #     APIField('publication_heading'),
    #     APIField('publication_heading_2'),
    #     APIField('publication_title_ru'),
    #     APIField('publication_title_ru'),
    #     APIField('publication_title_uk'),
    #     APIField('publication_text_ru'),
    #     APIField('publication_text_uk'),
    #     APIField('tags'),
    #     APIField('publish'),
    #     APIField('updated'),
    #     APIField('publication_image'),
    #     APIField('caption_ru'),
    #     APIField('caption_uk'),
    # ]



class HeadingNewsPublications(Orderable,models.Model):
    page = ParentalKey(NewsPublicationPage, on_delete=models.CASCADE,related_name='news_page_headings', verbose_name='Страница новости',)
    heading_name=models.ForeignKey(HeadingNewsPublicationsTypes,on_delete=models.CASCADE,verbose_name='Рубрика',related_name='heading_name')
    panels = [
        SnippetChooserPanel('heading_name'),
    ]
    # api_fields = [
    #     APIField('heading_name'),
    # ]



from .models import HomePage,AboutCompanyPage,Activities,NewsPublicationPage,HeadingNewsPublicationsTypes
from wagtail_modeltranslation.translation import TranslationOptions

# from wagtail_modeltranslation.decorators import register
from modeltranslation.decorators import register

@register(HomePage)
class HomeTR(TranslationOptions):
    fields = (
       # 'title',
       'body',
    )

@register(AboutCompanyPage)
class AboutCompanyTR(TranslationOptions):
    fields = (
       'about_company_text',
    )
@register(Activities)
class ActivitiesTR(TranslationOptions):
    fields = (
        'kind_of_activity',
    )
@register(NewsPublicationPage)
class NewsPublicationPageTR(TranslationOptions):
    fields = (
        'publication_title',
        'publication_text',
        'caption',
    )

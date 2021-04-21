from rest_framework import serializers
from .models import HomePage,HomeHeaderGalleryImage,AboutCompanyPage,Activities
from wagtail.images.models import Image

#Gallery
class ImageSerialier(serializers.ModelSerializer):
    class Meta:
        model=Image
        # fields='__all__'
        fields=('id','title','file','width','height')
class HomeHeaderGalleryImageSerializer(serializers.ModelSerializer):
    image=ImageSerialier()
    class Meta:
        model=HomeHeaderGalleryImage
        fields='__all__'


#Activities
class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Activities
        fields='__all__'
        # fields=('kind_of_activity_ru','kind_of_activity_uk')

class AboutCompanySerializer(serializers.ModelSerializer):
    # activities=ActivitiesSerializer(many=True,read_only=True)
    activities=ActivitiesSerializer()
    class Meta:
        model=AboutCompanyPage
        # fields=('about_company_text_ru','about_company_text_uk','activities')/
        fields='__all__'


class HomePageSerializer(serializers.ModelSerializer):
    gallery_images=HomeHeaderGalleryImageSerializer(many=True,read_only=True)
    # about_company=AboutCompanySerializer()
    class Meta:
        model=HomePage
        # fields='__all__'
        fields=('title_ru','title_uk','seo_title_ru','seo_title_uk','body_ru','body_uk','gallery_images')



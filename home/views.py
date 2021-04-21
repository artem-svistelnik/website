from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HomePage
from wagtail.images.models import Image
# class HomePageView(APIView):
#     def get(self, request):
#         HomePages = HomePage.objects.all()
#         return Response({"HomePages": HomePages})
#

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import HomePage,HomeHeaderGalleryImage,AboutCompanyPage,Activities
from .serializers import HomePageSerializer,HomeHeaderGalleryImageSerializer,ImageSerialier,AboutCompanySerializer,ActivitiesSerializer
class HomePageView(APIView):
    def get(self, request):
        # home_pages = HomePage.objects.all()
        home_pages = HomePage.objects.get(id=3)
        # serializer = HomePageSerializer(home_pages, many=True)
        serializer = HomePageSerializer(home_pages)
        # about=AboutCompanySerializer()
        print(serializer)
        return Response({"home_page":serializer.data})


class AboutCompanyPageView(APIView):
    def get(self,request):
        pages=AboutCompanyPage.objects.get(id=6)
        # for i in pages:
        print(pages.serializable_data())
        serializer = AboutCompanySerializer(pages)
        return Response({"AboutCompany": serializer.data})


class TestView(APIView):
    def get(self, request):
        pages = Activities.objects.all()
        serializer = ActivitiesSerializer(pages)
        return Response({"Activities": serializer.data})


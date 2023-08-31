from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .functions import read_and_save_deals, get_info_about_top_customers
from .serializers import DealFileSerializer


class DealCreateView(APIView):

    @method_decorator(cache_page(60*60))
    def get(self, request, *args, **kwargs):
        """
            API для получения информации о 5 клиентах,
            потративших наибольшую сумму за весь период.
        """
        response = get_info_about_top_customers()
        return Response({'response': response})

    def post(self, request, *args, **kwargs):
        """
            API для сохранения информации о совершенных сделках с csv-файла.
        """
        serializer = DealFileSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            try:
                read_and_save_deals(file=file)
            except Exception as e:
                return Response(
                    {
                        'Status': 'Error',
                        'Desc': f'{str(e)} - в процессе обработки файла произошла ошибка',
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            else:
                cache.clear()
                return Response(
                    {'Status': 'OK - файл был обработан без ошибок'},
                    status=status.HTTP_200_OK,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

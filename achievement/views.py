from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status
import logging
from rest_framework.response import Response

from achievement.models import AchievementNumbers
from achievement.serializers import AchievementNumbersSerializer

logger = logging.getLogger(__name__)

class NumbersApi(GenericAPIView):
    """
    Создание задачи
    """

    serializer_class = AchievementNumbersSerializer

    def get_queryset(self):
        return AchievementNumbers.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        current_number = serializer.validated_data['number']
        numbers_from_db = AchievementNumbers.objects.filter(number__in=[current_number, current_number + 1])
        if numbers_from_db:
            if current_number == numbers_from_db.first().number:
                logger.warning(f"Number {current_number} already exists")
                raise exceptions.ValidationError(f"Number {current_number} already exists")
            if (current_number + 1) == numbers_from_db.first().number:
                logger.warning(f"Number {current_number} is the previous number of an already existing number {current_number + 1}")
                raise exceptions.ValidationError(
                    f"Number {current_number} is the previous number of an already existing number {current_number + 1}")
        AchievementNumbers.objects.create(number=current_number)
        return Response(data=f"Next number: {current_number + 1}", status=status.HTTP_200_OK)



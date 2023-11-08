from rest_framework import serializers


class AchievementNumbersSerializer(serializers.Serializer):
    """
    Допускаются числа >= 0
    """

    number = serializers.IntegerField(min_value=0)

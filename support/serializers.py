from rest_framework import serializers
from .models import *
from order.serializers import OrderSerializer

class TechnicianNegativePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianNegativePoints
        fields = "__all__"


class TechnicianPositivePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianPositivePoints
        fields = "__all__"


class TechnicianSurveySerializer(serializers.ModelSerializer):
    orderId=OrderSerializer()
    technicianPositivePoints = TechnicianPositivePointsSerializer()
    technicianNegativePoints= TechnicianNegativePointsSerializer()
    class Meta:
        model = TechnicianSurvey
        fields = "__all__"


class CustomerNegativePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerNegativePoints
        fields = "__all__"


class CustomerPositivePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPositivePoints
        fields = "__all__"


class CustomerSurveySerializer(serializers.ModelSerializer):
    orderId = OrderSerializer()
    customerPositivePoints = CustomerPositivePointsSerializer()
    customerNegativePoints = CustomerNegativePointsSerializer()

    class Meta:
        model = CustomerSurvey
        fields = "__all__"


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = "__all__"


class TicketPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPriority
        fields = "__all__"


class TicketsSerializer(serializers.ModelSerializer):
    ticketStatus = TicketStatusSerializer(read_only=True)
    ticketPriority = TicketPrioritySerializer(read_only=True)

    class Meta:
        model = Tickets
        fields = "__all__"


class TicketChatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketChats
        fields = "__all__"

class TicketFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketFiles
        fields = "__all__"
from rest_framework import serializers
from api.models import (Transactions, TransactionDetails, StatementOfOrg,
                       Payee, ElectionActivity, Donor, CommitteesList,
                       CommitteeHistory, Ballots)

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'

class TransactionDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TransactionDetails
        fields = '__all__'

class StatementOfOrgSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StatementOfOrg
        fields = '__all__'

class PayeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payee
        fields = '__all__'

class ElectionActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ElectionActivity
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Donor
        fields = '__all__'

class CommitteesListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommitteesList
        fields = '__all__'

class CommitteeHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommitteeHistory
        fields = '__all__'

class BallotsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ballots
        fields = '__all__'

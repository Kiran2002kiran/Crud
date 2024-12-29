from rest_framework import serializers
from .models import Company

class EmploySerialzer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id','username','age','place','email','job','image','password']
        extra_kwargs={'password':{'write_only':True}}

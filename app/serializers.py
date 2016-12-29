from app.models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model=Register
		fields=('id','name','ph_no','address','date','linenos')
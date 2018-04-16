from rest_framework import serializers
from wxapi.models import UserInfo, Merchants, Job, SignUp


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'name', 'school', 'tel', 'gender', 'grade', 'openid', 'email', 'user_id')


class MerchantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchants
        fields = ('id', 'name', 'industry', 'tel', 'size', 'address', 'openid', 'email', 'Introduction', 'headerName', 'image',
        'user_id')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'tel','name', 'user_id', 'address', 'Introduction', 'image', 'peoplenum', 'paymethod', 'jobdate', 'jobtime',
        'overtime', 'commission', 'treatment', 'treatmentType', 'jobtype', 'communicate', 'communicatenum')


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'user_id', 'merchants_id', 'job_id', 'tel', 'signtime')

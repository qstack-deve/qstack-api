from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from django.utils.translation import gettext_lazy as _
from app.models.staff import Staff

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'password2')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(DefaultLoginSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs.get('user')

        if user:
            try:
                staff_profile = user.staff_profile
                if staff_profile.active_status != 'active':
                    raise serializers.ValidationError(
                        _("Your account is not active. Please contact an administrator.")
                    )
                if not staff_profile.role:
                    raise serializers.ValidationError(
                        _("Your account does not have a role assigned. Please contact an administrator.")
                    )
            except Staff.DoesNotExist:
                raise serializers.ValidationError(
                    _("You do not have a staff profile. Access denied.")
                )
        return attrs




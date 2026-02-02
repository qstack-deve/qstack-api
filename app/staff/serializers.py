from rest_framework import serializers
from app.models.staff import Staff, Social, Role, Skill
from app.models.users import User

from rest_framework import serializers
from app.models.staff import Skill, Staff
from app.models import (
    Job, Role, 
    Social
)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')

class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['platform', 'url']

class StaffProfileSerializer(serializers.ModelSerializer):
    # Writable fields
    first_name = serializers.CharField(source='user.first_name', required=False, max_length=150)
    last_name = serializers.CharField(source='user.last_name', required=False, max_length=150)
    socials = SocialsSerializer(many=True, required=False)

    # Read-only fields
    email = serializers.EmailField(source='user.email', read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    role = RoleSerializer(read_only=True)
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Staff
        fields = [
            'id', 'first_name', 'last_name', 'email', 'full_name', 
            'avatar', 'bio', 'role', 'skills', 'socials'
        ]
        read_only_fields = [
            'id', 'email', 'full_name', 'avatar', 'role', 'skills'
        ]

    def update(self, instance, validated_data):
        # Handle nested update for user's first_name and last_name
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.save()

        # Handle nested update for socials
        socials_data = validated_data.pop('socials', None)
        if socials_data is not None:
            seen_platforms = set()
            for social_data in socials_data:
                platform = social_data.get('platform')
                if platform:
                    seen_platforms.add(platform)
                    Social.objects.update_or_create(
                        staff=instance,
                        platform=platform,
                        defaults=social_data
                    )
            # Delete any of the user's socials that were not in the request
            instance.socials.exclude(platform__in=seen_platforms).delete()

        # Update the staff instance with any remaining data
        return super().update(instance, validated_data)

class StaffAvatarSerializer():
    class Meta:
        model = Staff
        fields = ['avatar']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'user_role')
        read_only_fields = ('id', 'email')

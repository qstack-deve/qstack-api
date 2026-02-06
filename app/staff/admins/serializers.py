from rest_framework import serializers
from app.models.staff import Skill, Staff
from app.models import (
    Job, Role, 
    Social
)
from app.models.jobs import (
    Responsibility, Requirement, Benefit, SalaryRange
)
from app.models.portfolio import (
    Portfolio,
    Category,
    Tag
)
from app.models.contact import (
    Contact
)
from ..serializers import (
    SkillSerializer,
    RoleSerializer,
    SocialsSerializer,
    UserSerializer,
    TagSerializer,
    CategorySerializer,
    BenefitSerializer,
    ResponsibilitySerializer,
    RequirementSerializer,
    SalaryRangeSerializer,
)

# ------------------STAFF HERE -----------------

class MemberSerializer(serializers.ModelSerializer):
    # For writing, we expect the ID of the role and skills
    skills = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Skill.objects.all(), required=False
    )
    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), required=False, allow_null=True
    )

    # These are for reading (GET requests) and are read-only
    full_name = serializers.ReadOnlyField()
    socials_read = SocialsSerializer(many=True, read_only=True, source='socials')
    user = UserSerializer(read_only=True)


    class Meta:
        model = Staff
        fields = [
            'id', 'user', 'avatar', 'bio', 'role', 'skills', 
            'active_status', 'slug', 'created_at', 'updated_at', 
            'full_name', 'socials_read'
        ]

    def to_representation(self, instance):
        """
        Customize the output for GET requests.
        This will show the full nested objects for skills and role instead of just IDs.
        """
        representation = super().to_representation(instance)
        representation['skills'] = SkillSerializer(instance.skills.all(), many=True).data
        representation['role'] = RoleSerializer(instance.role).data if instance.role else None
        return representation

    def update(self, instance, validated_data):
        # DRF's default update will handle the simple fields and the
        # PrimaryKeyRelatedFields (role, skills) automatically.
        instance = super().update(instance, validated_data)

        # We still need custom logic for the nested 'socials' if we want to update them.
        # For now, this serializer won't handle writing to socials.
        
        instance.save()
        return instance

# -----------------portfolio here -----------------

class PortfolioSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), required=False
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Portfolio
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tags'] = TagSerializer(instance.tags.all(), many=True).data
        representation['category'] = CategorySerializer(instance.category).data if instance.category else None
        return representation


class JobSerializer(serializers.ModelSerializer):
    responsibilities = ResponsibilitySerializer(many=True, read_only=True)
    requirements = RequirementSerializer(many=True, read_only=True)
    benefits = BenefitSerializer(many=True, read_only=True)
    salary_range = SalaryRangeSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

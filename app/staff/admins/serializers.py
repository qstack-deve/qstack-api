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
    Portfolio
)
from app.models.contact import (
    Contact
)
from ..serializers import (
    SkillSerializer,
    RoleSerializer,
    SocialsSerializer,
    UserSerializer
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
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name')

class PortfolioListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Portfolio
        fields = "__all__"


# from ..serializers import (
#     BenefitSerializer,
#     ResponsibilitySerializer,
#     RequirementSerializer,
#     SalaryRangeSerializer,
# )
# --------JOBS HRERE--------
class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('description',)

class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ['description']

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['description']

class SalaryRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRange
        fields = ('min_salary', 'max_salary')

class JobSerializer(serializers.ModelSerializer):
    responsibilities = ResponsibilitySerializer(many=True, read_only=True)
    requirements = RequirementSerializer(many=True, read_only=True)
    benefits = BenefitSerializer(many=True, read_only=True)
    salary_range = SalaryRangeSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'



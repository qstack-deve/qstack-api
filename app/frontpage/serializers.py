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


# --------------CONTACT US HERE -------------------

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


# ------------------STAFF HERE -----------------

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

class StaffSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    role = RoleSerializer()
    full_name = serializers.ReadOnlyField()
    socials = SocialsSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'

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



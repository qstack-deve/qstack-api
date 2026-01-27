from rest_framework import serializers
from app.models.staff import Skill, Staff
from app.models import (
    Job, Role, 
    Social
)
from app.models.jobs import (
    Responsibility, Requirement, Benefit, SalaryRange
)
from app.models.portfolio import Portfolio

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

class StaffListSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    socials = SocialsSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = ('id', 'slug', 'full_name', 'role', 'avatar', 'bio', 'socials')


class StaffDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    role = RoleSerializer()
    full_name = serializers.ReadOnlyField()
    socials = SocialsSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'


class PortfolioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'description', 'status',  'image', 'tags', 'url')

class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ('description',)

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ('description',)

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('description',)

class SalaryRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryRange
        fields = ('min_salary', 'max_salary')

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



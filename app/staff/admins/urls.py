from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import (
    MemberViewSet,
    JobViewSet, 
    PortfolioViewSet,
    CategoryViewSet,
    TagViewSet,
)

from ..views import (
    RoleViewSet,
    SkillViewSet,
    SocialViewSet
)

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

# tools
router.register(r'roles', RoleViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    # path('members/<str:member_id>/activate/', ActivateMemberView.as_view(), name='activate-member'),

]


urlpatterns +=  [
    path('', include(router.urls)),

]
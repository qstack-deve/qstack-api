from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SuggestionView(APIView):
    def get(self, request):
        suggestions = [
            "Optimize images to improve page load speed.",
            "Implement a mobile-responsive design.",
            "Improve SEO by using relevant keywords.",
            "Add a clear call-to-action on the homepage.",
            "Simplify the navigation menu.",
            "Use a consistent color scheme and branding.",
            "Ensure the website is accessible to people with disabilities.",
            "Add a blog to provide valuable content to users.",
            "Integrate social media to engage with your audience.",
            "Use analytics to track user behavior and make data-driven decisions."
        ]
        return Response(suggestions, status=status.HTTP_200_OK)

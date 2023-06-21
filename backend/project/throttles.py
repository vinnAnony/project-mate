from rest_framework.throttling import AnonRateThrottle

class ProjectRateThrottle(AnonRateThrottle):
    scope = 'project'
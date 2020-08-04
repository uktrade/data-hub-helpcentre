from django.conf import settings


def shared_settings(request):
    return {
        "feedback_url": settings.FEEDBACK_URL,
        "git_commit": settings.GIT_COMMIT,
        "git_branch": settings.GIT_BRANCH,
        "show_banner": settings.SHOW_ENV_BANNER,
        "env_name": settings.ENV_NAME,
    }

from datetime import timedelta
from decouple import config

SOCIAL_AUTH_APPS = [
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'social_django',
]

SOCIAL_AUTH_MIDDLEWARE = [
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

SOCIAL_AUTH_CONTEXT_PROCESSOR = [
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
]

SOCIAL_AUTH_DEFAULT_AUTHENTICATION_CLASSES = 'rest_framework_simplejwt.authentication.JWTAuthentication'

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    #'ROTATE_REFRESH_TOKENS': True,
    #'BLACKLIST_AFTER_ROTATION': True
    #'ALGORITHM': 'HS256',
    #'SIGNING_KEY': SECRET_KEY,
}

 # URL you add to google developers console as allowed to make redirection
WHITE_LIST = []
WHITE_LIST_ENV = config('WHITE_LIST', default='localhost')
if WHITE_LIST_ENV:
    WHITE_LIST.extend(WHITE_LIST_ENV.split(','))

DJOSER = {
    "LOGIN_FIELD": "email", # Field we use to login on extended User model
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    #'TOKEN_MODEL': 'rest_framework_simplejwt.authentication.JWTAuthentication',
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': WHITE_LIST, # Redirected URL we listen on google console
}

AUTHENTICATION_BACKENDS = (
    # GitHub OAuth2
    #'social_core.backends.github.GithubOAuth2',

    # Facebook OAuth2
    #'social_core.backends.facebook.FacebookAppOAuth2',
    #'social_core.backends.facebook.FacebookOAuth2',

    # Instagram OAuth2
    #'social_core.backends.instagram.InstagramOAuth2',

    # Google  OAuth2
    #'social_core.backends.google.GoogleOpenId',
    #'social_core.backends.google.GoogleOAuth',
    'social_core.backends.google.GoogleOAuth2',
    #'drf_social_oauth2.backends.GoogleIdentityBackend',

    # Twitter
    #'social_core.backends.twitter.TwitterOAuth',

    # drf_social_oauth2
    #'drf_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)
# GitHub configuration
SOCIAL_AUTH_GITHUB_KEY = config('GITHUB_CLIENT_KEY', default='<your app key goes here>')
SOCIAL_AUTH_GITHUB_SECRET = config('GITHUB_CLIENT_SECRET', default='<your app secret goes here>')

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = config('FACEBOOK_CLIENT_KEY', default='<your app key goes here>')
SOCIAL_AUTH_FACEBOOK_SECRET = config('FACEBOOK_CLIENT_SECRET', default='<your app secret goes here>')
# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'email, first_name, last_name'
}

# Instagram configuration
SOCIAL_AUTH_INSTAGRAM_KEY = config('INSTAGRAM_CLIENT_KEY', default='<your app key goes here>')
SOCIAL_AUTH_INSTAGRAM_SECRET = config('INSTAGRAM_CLIENT_SECRET', default='<your app secret goes here>')
SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'likes comments relationships'}

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_CLIENT_KEY', default='<your app key goes here>')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_CLIENT_SECRET', default='<your app secret goes here>')
# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid',
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']
SOCIAL_AUTH_GOOGLE_OAUTH2_USER_FIELDS = ['username','first_name', 'last_name', 'email']

# Twitter
SOCIAL_AUTH_TWITTER_KEY = config('TWITTER_CLIENT_KEY', default='<your app key goes here>')
SOCIAL_AUTH_TWITTER_SECRET = config('TWITTER_CLIENT_SECRET', default='<your app secret goes here>')

SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_REQUIRE_POST = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    #'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

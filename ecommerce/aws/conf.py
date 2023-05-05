import datetime
import os

from dotenv import load_dotenv


load_dotenv("D:/Programming/PythonEnV/.env.txt")
AWS_USERNAME = 'django-s3-user'
AWS_GROUP_NAME = 'django-ecommerce'
# AWS config
AWS_SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY")
AWS_ACCESS_KEY_ID = os.getenv("ACCESS_KEY")
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_DEFAULT_ACL = 'public-read'

DEFAULT_FILE_STORAGE = 'django_s3.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'django_s3.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'django-ecommerce-dokusho'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
S3DIRECT_REGION = 'eu-central-1'
STATIC_LOCATION = 'static'
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWS_S3_FILE_OVERWRITE = False
two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()),),
}

# Dokusho Vernissage eCommerce App
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
 ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
 ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
 ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
 ![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)
 ![PyTest](https://img.shields.io/badge/Pytest-003A9B?style=for-the-badge&logo=pytest&logoColor=white)
 ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
 ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
 ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
 ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
 ![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
 ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)

Dokusho Vernissage eCommerce is a Django-based web application that allows users to browse and purchase products online. The application is deployed on Vercel at https://dokusho-vernissage.vercel.app/.

The project consists of several Django applications including:

- Account: User authentication and account management
- Basket: Basket and checkout functionality
- Catalogue: Product browsing and searching
- Checkout: Payment integration with PayPal
- Orders: Management of user orders

The frontend is developed using Bootstrap 5, jQuery, and AJAX. The application's database is hosted on Railway and created using PostgresSQL. Static and media files are stored in an AWS S3 Bucket. Tests are written using PyTest.

## Features
- User authentication and account management, including email confirmation for account activation
- Password reset functionality with or without logging in via email
- Product browsing and searching
- Wish list for saving favorite products
- Basket and checkout functionality
- PayPal payment integration for secure and easy payment processing
- Multiple shipping addresses for users
- Toggle between dark and light mode for customizable user experience

## Installation

1. Clone the repository to your local machine or download and extract in a folder:
```
git clone https://github.com/Veluthil/eCommerce-Store.git
```
2. Open in Visual Studio Code or Pycharm.

3. Commands:
```
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py manage.py runserver
```
4. In settings.py change each of environmental variables for your own - this includes:
- load_dotenv("INSERT HERE YOUR OWN PATH TO .ENV FILE"),
- Django SECRET_KEY,
- Whole PostgresSQL settings, if you want to use this database, also you can change HOST and PORT to this:
```
'HOST': 'localhost',
'PORT': '5432',
```
- AWS_ACCESS_KEY_ID,
- AWS_SECRET_ACCESS_KEY,
- EMAIL_HOST_USER,
- EMAIL_HOST_PASSWORD,
- PAYPAL_CLIENT_ID,
- PAYPAL_SECRET,

5. In development mode change this:
```
DEBUG = False

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```
To this:
```
DEBUG = True

#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
```

6. You can uncomment SQLite settings and comment out PostgresSQL settings, if you want to use SQLite database (not recommended, if you want to deploy your app).

7. AWS S3 bucket settings are for deployment, you can create your own bucket, or uncomment below settings for local server usage.
Uncomment this section:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
```
And comment out AWS S3 Bucket settings.

8. Email settings: 
- for local server usage and sending email to your console uncomment this section:
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
```
And comment out email settings for SMTP section.

9. For PayPal usage you need to create your own developer account.

## Usage

1. Open your web browser and navigate to http://localhost:8000/.
2. Create* your account and/or login.
2*. Confirm and activate your account by clicking on activation link sent to your email.
3. Browse the available products and add items to your cart or wish list.
4. Click the "Checkout Securely" button to enter your payment and shipping information.
5. Review your orderm choose shipping method, choose PayPal payment methos and submit it for processing.
6. Edit your Account and Address details (you can add multiple addresses and decide which is the main one).

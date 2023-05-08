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
- Product browsing and searching via Categories
- Wish list for saving favorite products
- Basket and checkout functionality
- PayPal payment integration for secure and easy payment processing
- Multiple shipping addresses for users
- Toggle between dark and light mode for customizable user experience

Sure, here's an improved version of the installation and usage guide:

## Installation

1. Clone the repository to your local machine or download and extract it into a folder:
```
git clone https://github.com/Veluthil/eCommerce-Store.git
```
2. Open the project in your preferred code editor and create a virtual environment. Activate the virtual environment using the following commands:
```
py -m venv venv
venv\Scripts\activate
```
3. Install the required packages using: 
```
pip install -r requirements.txt
```

4. Set up the environment variables by updating the `settings.py` file with the appropriate values for the following variables:
- `load_dotenv("INSERT HERE YOUR OWN PATH TO .ENV FILE")`
- `SECRET_KEY`
- `DATABASES`: If you want to use PostgresSQL database, update the `USER`, `PASSWORD`, `HOST`, and `PORT` variables accordingly. Alternatively, you can use SQLite database by commenting out the PostgresSQL settings and uncommenting the SQLite settings.
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `PAYPAL_CLIENT_ID`
- `PAYPAL_SECRET`

5. To use the application in development mode, comment out the following lines in the `settings.py` file:
```
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```
And change DEBUG = False to:
```
DEBUG = True
```

6. For local server usage, uncomment the following lines in the `settings.py` file:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
```
And comment out the AWS S3 Bucket settings.

7. To set up email functionality, update the `settings.py` file as follows:
- For local server usage and sending email to your console, uncomment the following lines in settings.py:
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
```
And comment out the email settings for the SMTP section.
- Add following method to Customer class in ecommerce/apps/account/models.py:
```
 def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            "l@1.com",
            [self.email],
            fail_silently=False,
        )
 ```
 - In acccount_register view at ecommerce/apps/account/views.py comment out following code:
 ```
             with get_connection(
                    host=settings.EMAIL_HOST,
                    port=settings.EMAIL_PORT,
                    username=settings.EMAIL_HOST_USER,
                    password=settings.EMAIL_HOST_PASSWORD,
                    use_tls=settings.EMAIL_USE_TLS
            ) as connection:
                subject = subject
                email_from = settings.EMAIL_HOST_USER
                recipient = [user.email]
                message = message
                EmailMessage(subject, message, email_from, recipient, connection=connection).send()
```
And uncomment this:
```
user.email_user(subject=subject, message=message)
print(message)
```            

8. To use PayPal, you need to create your own developer account.

## Usage

1. Open your web browser and navigate to http://localhost:8000/.
2. Create an account and/or log in. If you create an account, you will receive an activation link by email that you need to click to confirm and activate your account.
3. Browse the available products and add items to your cart or wish list.
4. Click the "Checkout Securely" button to enter your payment and shipping information.
5. Review your order, choose a shipping method, select PayPal as your payment method, and submit your order for processing.
6. Edit your account and address details as necessary (you can add multiple addresses and choose which one is the primary address).

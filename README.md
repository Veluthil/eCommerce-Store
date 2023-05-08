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

The project is composed of several Django applications, including:
- **Account** for user authentication and account management (passwords and addresses), 
- **Basket** for basket functionality (adding items, updating quantities, calculating total prices), 
- **Catalogue** for creating products, product types, product specifications, and categories, 
- **Checkout** for payment integration with PayPal and delivery options, 
- **Orders** for managing user orders and payment confirmation.

For the frontend, Bootstrap 5, jQuery, and AJAX were used. The application's database is hosted on Railway and created using PostgresSQL. Static and media files are stored in an AWS S3 Bucket. Tests were written using PyTest, FactoryBoy, and Faker.

## Features
- User authentication and account management, including email confirmation for account activation (you will recieve an activation email from dokushovernissage@gmail.com)
- Password reset functionality with or without logging in via email
- Product browsing and searching via Categories
- Wish list for saving favorite products
- Basket and checkout functionality
- PayPal payment integration for secure and easy payment processing
- Multiple shipping addresses for users
- Toggle between dark and light mode for customizable user experience

Sure, here's an improved version of the installation and usage guide:

## Dokusho Vernissage eCommerce App Preview
![dv-ss-1](https://user-images.githubusercontent.com/108438343/236901510-dde96cfd-4528-42e1-8315-7597a5dd37af.png)
![dv-ss-2](https://user-images.githubusercontent.com/108438343/236901542-975e175e-de3c-4a01-83aa-dd4b4ece4233.png)
![dv-ss-3](https://user-images.githubusercontent.com/108438343/236901641-5f69d267-2515-4b89-8ace-5ddd0f663839.png)
![dv-ss-4](https://user-images.githubusercontent.com/108438343/236901659-f516155b-74cb-4e95-979f-1379f96241dd.png)
![dv-ss-5](https://user-images.githubusercontent.com/108438343/236901678-732299a9-e94a-4a5b-8024-13dc5325e4ff.png)
![dv-ss-6](https://user-images.githubusercontent.com/108438343/236901693-f8a1e5f6-fcaa-444e-b4ba-00f3ed0573c4.png)
![dv-ss-7](https://user-images.githubusercontent.com/108438343/236901717-9cba09e6-0ed3-4bd4-ade5-93ba3d486f7e.png)
![dv-ss-8](https://user-images.githubusercontent.com/108438343/236901759-0ef87555-2eaa-4ed9-912d-6c5550e0259c.png)
![dv-ss-9](https://user-images.githubusercontent.com/108438343/236901780-27c1492d-3b00-4cb1-948a-1e8730a43edb.png)
![dv-ss-10](https://user-images.githubusercontent.com/108438343/236928457-e978e9b6-5488-4dfd-85bc-55468ae26a4f.png)
![dv-ss-11](https://user-images.githubusercontent.com/108438343/236928472-a57ebe37-94c6-4391-a6d3-2401db187f6d.png)
![dv-ss-12](https://user-images.githubusercontent.com/108438343/236928495-9be241e9-c0f1-40d2-be47-823eb1b92cab.png)
![dv-ss-13](https://user-images.githubusercontent.com/108438343/236928512-bfa373b7-f7f8-42d5-b89f-5b6eeb697819.png)


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

5. To use the application in development mode, comment out the following lines or change to `False` in the `settings.py` file:
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

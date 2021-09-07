import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

from pathlib import Path 
from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES
from oscar.defaults import *
import logging
logging.basicConfig(filename='client_application.log', level=logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'ruynfepj-$l0v7faw8&%$zm!-an-gy=hymjy1b@ce&@^t+f%%f'

DEBUG = True 

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'shop.urls'

WSGI_APPLICATION = 'shop.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
USE_L10N = True
USE_TZ = True

# English default
LANGUAGES = DJANGO_LANGUAGES

STATIC_URL = "/static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'shop', 'static'),
)

SITE_ID = 1

INSTALLED_APPS = [
    'simpleui',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_audio',
    'shop',
    'django.contrib.flatpages',

    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    'oscar.apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
    'aldryn_apphooks_config',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'djangocms_blog',
    'rest_framework',
    'oscarapi',
    'oscar_invoices',
    'pinax.badges',
    'pinax.messages',
    'pinax.announcements',
    'pinax.calendars',
    'imagekit',
    'pinax.events',
    'pinax.testimonials',
    'photologue',
    'corsheaders',
    'absolute',
    'emailit',
    'gdpr_assist',
    'payments',
    'newsletter',
    'captcha',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'otp_yubikey',
    'djangocms_history',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'shop', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'two_factor.middleware.threadlocals.ThreadLocals',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]



AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    'pinax.announcements.auth_backends.AnnouncementPermissionsBackend',
)

ADMINS = (
    ('John Lennon', 'jlennon@example.com'), # Change this to your Admins
    ('Paul McCartney', 'pmacca@example.com'), # Change this to your Admins
)

MANAGERS = (
    ('George Harrison', 'gharrison@example.com'), # Change this to your Managers
    ('Ringo Starr', 'ringo@example.com'), # Change this to your Managers
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alternatecms', # Please change Me
        'USER': 'testuser', # Please change Me
        'PASSWORD': 'Tester2021', # Please change Me
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'gdpr_log': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'gdpr-log.sqlite3'),
    },
}

DATABASE_ROUTERS = ['gdpr_assist.routers.EventLogRouter']

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

META_SITE_PROTOCOL = 'https'  # set 'http' for non ssl enabled websites
META_USE_SITES = True
META_USE_OG_PROPERTIES=True
META_USE_TWITTER_PROPERTIES=True
META_USE_GOOGLEPLUS_PROPERTIES=True # django-meta 1.x+
META_USE_SCHEMAORG_PROPERTIES=True  # django-meta 2.x+

PINAX_EVENTS_IMAGE_THUMBNAIL_SPEC = "pinax.events.specs.ImageThumbnail"
PINAX_EVENTS_SECONDARY_IMAGE_THUMBNAIL_SPEC = "pinax.events.specs.SecondaryImageThumbnail"

SIMPLEUI_HOME_INFO = True
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_HOME_ACTION = True
SIMPLEUI_HOME_TITLE = 'AlternateCMS'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']

DJANGOCMS_PICTURE_NESTING = True

PAYMENT_HOST = '0.0.0.0:8000'
PAYMENT_USES_SSL = False
PAYMENT_MODEL = 'shop.Payment'
PAYMENT_VARIANTS = {
    'default': ('payments.dummy.DummyProvider', {}),
    'authorizenet': ('payments.authorizenet.AuthorizeNetProvider', {
        'login_id': '1234login',
        'transaction_key': '1234567890abcdef',
        'endpoint': 'https://test.authorize.net/gateway/transact.dll'}),
    'braintree': ('payments.braintree.BraintreeProvider', {
        'merchant_id': '112233445566',
        'public_key': '1234567890abcdef',
        'private_key': 'abcdef123456',
        'sandbox': True}),
    'coinbase': ('payments.coinbase.CoinbaseProvider', {
        'key': '123abcd',
        'secret': 'abcd1234',
        'endpoint': 'sandbox.coinbase.com'}),
    'cybersource': ('payments.cybersource.CyberSourceProvider', {
        'merchant_id': 'example',
        'password': '1234567890abcdef',
        'capture': False,
        'sandbox': True}),
    'dotpay': ('payments.dotpay.DotpayProvider', {
        'seller_id': '123',
        'pin': '0000',
        'lock': True,
        'endpoint': 'https://ssl.dotpay.pl/test_payment/'}),
    'paypal': ('payments.paypal.PaypalProvider', {
        'client_id': 'user@example.com',
        'secret': 'iseedeadpeople',
        'endpoint': 'https://api.sandbox.paypal.com',
        'capture': False}),
    'paypal': ('payments.paypal.PaypalCardProvider', {
        'client_id': 'user@example.com',
        'secret': 'iseedeadpeople'}),
    'sage': ('payments.sagepay.SagepayProvider', {
        'vendor': 'example',
        'encryption_key': '1234567890abcdef',
        'endpoint': 'https://test.sagepay.com/Simulator/VSPFormGateway.asp'}),
    'sage': ('payments.sofort.SofortProvider', {
        'id': '123456',
        'key': '1234567890abcdef',
        'project_id': '654321',
        'endpoint': 'https://api.sofort.com/api/xml'}),
    'stripe': ('payments.stripe.StripeProvider', {
        'secret_key': 'sk_test_123456',
        'public_key': 'pk_test_123456'})    
        }

NEWSLETTER_THUMBNAIL = 'sorl-thumbnail'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SIMPLEUI_CONFIG = {
    'system_keep':False,
    'menus': [{
        'name': 'AlternateCMS Official Docs',
        'icon': 'fas fa-code',
        'url': 'https://docs.alternatecms.com'
    }, 
    {
        'name': 'SALES',
        'icon': 'fas fa-dollar-sign',
        'models': [
            {
            'name': 'Billing Addresses',
            'url': 'order/billingaddress/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Communication Events',
            'url': 'order/communicationevents/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Line Attributes',
            'url': 'order/lineattributes/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Line Prices',
            'url': 'order/lineprices/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Order Discounts',
            'url': 'order/orderdiscount/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Order Lines',
            'url': 'order/orderline/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Order Notes',
            'url': 'order/ordernote/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Order Status Changes',
            'url': 'order/orderstatuschange/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Orders',
            'url': 'order/order/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Payment Event Types',
            'url': 'order/paymenteventtype/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Payment Events',
            'url': 'order/paymentevent/',
            'icon': 'fab fa-search-dollar'
            },
            {
            'name': 'Shipping',
            'models': [
              {
                'name': 'Order and Item Chargers',
                'url': 'catalogue/product/'
              }, {
                'name': 'Weight-based Shipping Methods',
                'url': 'catalogue/productattribute/'
              }, {
                'name': 'Shipping Events Types',
                'url': 'order/shippingeventstype/',
                },
                {
                'name': 'Shipping Events',
                'url': 'order/shippingevent/',
                },
                {
                'name': 'Shipping Addresses',
                'url': 'order/shippingaddress/',
                'icon': 'fab fa-search-dollar'
                },
            ]},
            {
            'name': 'Surcharges',
            'url': 'order/Surcharge/',
            'icon': 'fab fa-search-dollar'
            },]
    },
    {
        'name': 'CATALOG',
        'icon': 'fas fa-box-open',
        'models': [
          {
            'name': 'Products',
            'models': [
              {
                'name': 'Products',
                'url': 'catalogue/product/'
              }, {
                'name': 'Product Attributes',
                'url': 'catalogue/productattribute/'
              }, {
                'name': 'Product Attribute Values',
                'url': 'catalogue/productattributevalue/'
              }, {
                'name': 'Product Categories',
                'url': 'catalogue/productcategory/'
              }, {
                'name': 'Product Classes',
                'url': 'catalogue/productclass/'
              }, {
                'name': 'Product Images',
                'url': 'catalogue/productimage/'
              }, {
                'name': 'Options',
                'url': 'catalogue/product/option/'
              }, {
                'name': 'Attribute Option Groups',
                'url': 'catalogue/attributeoptiongroup/'
              },
            ]
          },{
            'name': 'Invoices',
            'models': [
              {
                'name': 'Invoices',
                'url': 'oscar_invoices/invoice/'
              }, {
                'name': 'Legal Entities',
                'url': 'oscar_invoices/legalentity/'
              }, {
                'name': 'Legal Entity Addresses',
                'url': 'oscar_invoices/legalentityaddress/'
              }
            ]
          }, {
            'name': 'Reviews',
            'models': [
              {
                'name': 'Product Reviews',
                'url': 'reviews/productreview/'
              }, {
                'name': 'Votes',
                'url': 'reviews/vote/'
              },
            ]
          },  {
            'name': 'Offer',
            'models': [
              {
                'name': 'Benefits',
                'url': 'offer/benefit/'
              }, {
                'name': 'Conditional Offers',
                'url': 'offer/conditionaloffer/'
              }, {
                'name': 'Conditions',
                'url': 'offer/condition/'
              }, {
                'name': 'Ranges',
                'url': 'offer/range/'
              },
            ]
          },]
    }, {
        'name': 'CUSTOMERS',
        'icon': 'fas fa-male',
        'models': [
          {
            'name': 'Address',
            'models': [
              {
                'name': 'Countries',
                'url': 'address/country/'
              }, {
                'name': 'User Addresses',
                'url': 'address/useraddress/'
              },
            ]
          },{
            'name': 'Payment',
            'models': [
              {
                'name': 'Bankcards',
                'url': 'payment/bankcard/'
              }, {
                'name': 'Source Types',
                'url': 'payment/sourcetype/'
              }, {
                'name': 'Sources',
                'url': 'payment/source/'
              },  {
                'name': 'Transactions',
                'url': 'payment/transaction/'
              }
            ]
          }, {
            'name': 'Testimonials',
            'url': 'testimonials/testimonial/'
          },  {
            'name': 'Wishlists',
            'url': 'wishlists/wishlist/',
            'models': [{
                'name': 'Wish List Lines',
                'url': 'wishlists/line/'
              },
            ]
          },]
    },  {
        'name': 'MARKETING',
        'icon': 'fas fa-bullhorn',
        'models': [
          {
            'name': 'Analytics',
            'models': [
              {
                'name': 'Product Records',
                'url': 'analytics/productrecord/'
              }, {
                'name': 'User Product Views',
                'url': 'analytics/userproductviews/'
              }, {
                'name': 'User Records',
                'url': 'analytics/userrecord/'
              }, {
                'name': 'User Search Queries',
                'url': 'analytics/usersearch/'
              }
            ]
          }, {
            'name': 'Announcements',
            'models': [
              {
                'name': 'Announcements',
                'url': 'announcements/announcement/'
              }, {
                'name': 'Dismissals',
                'url': 'announcements/dismissals/'
              }
            ]
          }, {
            'name': 'Communication',
            'models': [
              {
                'name': 'Communication Event Types',
                'url': 'communication/communicationeventtype/'
              }, {
                'name': 'Emails',
                'url': 'communication/emails/'
              }
            ]
          }, {
            'name': 'Coupon',
            'models': [
              {
                'name': 'Coupon Applications',
                'url': 'voucher/voucherapplication/'
              }, {
                'name': 'Coupons',
                'url': 'voucher/voucher/'
              }
            ]
          },  {
            'name': 'Rewards',
            'url': 'pinax_badges/badgeaward/'
          }, {
            'name': 'Events',
            'url': 'pinax_events/event/'
          },  {
            'name': 'Messages',
            'models': [
              {
                'name': 'Messages',
                'url': 'pinax_messages/message/'
              }, {
                'name': 'User Threads',
                'url': 'pinax_messages/userthread/'
              }
            ]
          }, {
            'name': 'Newsletter',
            'models': [
              {
                'name': 'Messages',
                'url': 'newsletter/message/'
              }, {
                'name': 'Newsletters',
                'url': 'newsletter/newsletter/'
              },  {
                'name': 'Submissions',
                'url': 'newsletter/submission/'
              },  {
                'name': 'Subscriptions',
                'url': 'newsletter/subscription/'
              }
            ]
          }
        ]}, {
        'name': 'CONTENT',
        'icon': 'fas fa-laptop',
        'models': [
          {
            'name': 'Content Management',
            'models': [
              {
                'name': 'Page Types',
                'url': 'cms/pagetype/'
              }, {
                'name': 'Pages',
                'url': 'cms/page/'
              }, {
                'name': 'Pages Global Permissions',
                'url': 'cms/globalpagepermission/'
              }, {
                'name': 'Static Placeholders',
                'url': 'cms/staticplaceholder/'
              },
               {
                'name': 'User Groups (Pages)',
                'url': 'cms/pageusergroup/'
              },
                {
                'name': 'Users (Pages)',
                'url': 'cms/pageuser/'
              }
            ]
          }, {
            'name': 'Blog',
            'models': [
              {
                'name': 'Articles',
                'url': 'djangocms_blog/post/'
              }, {
                'name': 'Blog Categories',
                'url': 'djangocms_blog/blogcategory/'
              },  {
                'name': 'Blog Configurations',
                'url': 'djangocms_blog/blogconfig/'
              },
                {
                'name': 'Tags',
                'url': 'taggit/tag/'
              }
            ]
          }, {
            'name': 'Photo Gallery',
            'models': [
              {
                'name': 'Galleries',
                'url': 'photologue/gallery/'
              }, {
                'name': 'Photo Effects',
                'url': 'photologue/photoeffect/'
              },  {
                'name': 'Photo Sizes',
                'url': 'photologue/photosize/'
              },  {
                'name': 'Photos',
                'url': 'photologue/photo/'
              },  {
                'name': 'Watermarks',
                'url': 'photologue/watermark/'
              }
            ]
          }, {
            'name': 'File Management',
            'models': [
              {
                'name': 'Folders',
                'url': 'filer/folder/'
              }, {
                'name': 'Thumbnail Options',
                'url': 'filer/thumbnailoption/'
              }
            ]
          }, {
            'name': 'Sites',
            'url': 'sites/site/'
          },]
    }, {
        'name': 'SHOPS',
        'icon': 'fas fa-store',
        'models': [
          {
            'name': 'Cart',
            'models': [
              {
                'name': 'Cart Lines',
                'url': 'basket/line/'
              }, {
                'name': 'Carts',
                'url': 'basket/basket/'
              },  {
                'name': 'Line Attributes',
                'url': 'basket/lineattribute/'
              }
            ]
          }, {
            'name': 'Partners',
            'models': [
              {
                'name': 'Fulfillment Partners',
                'url': 'partner/partner/'
              }, {
                'name': 'Stock Records',
                'url': 'partner/stockrecord/'
              },
            ]
          }, ]
    }, {
        'name': 'SECURITY',
        'icon': 'fas fa-shield-alt',
        'models': [
          {
            'name': 'Authentication and Authorization',
            'models': [
              {
                'name': 'Groups',
                'url': 'auth/group/'
              }, {
                'name': 'Users',
                'url': 'auth/user/'
              }
            ]
          }, {
            'name': 'Two Factor Authentication',
            'url': 'two_factor/phonedevice/'
          }, {
            'name': 'GDPR Compliance',
            'url': 'gdpr_assist/personaldata/'
          }, {
            'name': 'API Keys',
            'url': 'oscarapi/apikey/'
          }, {
            'name': 'OTP Static Devices',
            'url': 'otp_static/staticdevice/'
          }, {
            'name': 'OTP TOTP Devices',
            'url': 'otp_totp/totpdevice/'
          }, {
            'name': 'OTP Yubikey',
            'models': [
              {
                'name': 'Local Yubikey Devices',
                'url': 'otp_yubikey/yubikeydevice/'
              }, {
                'name': 'Remote YubiKey Devices',
                'url': 'otp_yubikey/remoteyubikeydevice/'
              },  {
                'name': 'YubiKey Validation Services',
                'url': 'otp_yubikey/validationservice/'
              },
            ]
          }, ]
    }]
    }
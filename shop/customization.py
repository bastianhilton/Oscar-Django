import os
from .settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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
          }, {
            'name': 'Comments',
            'models': [
              {
                'name': 'Comments',
                'url': 'django_comments_xtd/xtdcomment/'
              }, {
                'name': 'Black Listed Comments',
                'url': 'django_comments_xtd/blacklisteddomain/'
              }, {
                'name': 'Comment Flags',
                'url': 'django_comments/commentflag/'
              },
            ]
          }, {
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
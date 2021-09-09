import graphene
from graphene_django import DjangoObjectType
from .models import *

class AddressCountryType(DjangoObjectType):
    class Meta:
      model = AddressCountry
      fields = (
        "iso_3166_1_a2",
        "iso_3166_1_a3",
        "iso_3166_1_numeric",
        "printable_name",
        "name",
        "display_order",
        "is_shipping_country",
    )

class AddressUseraddressType(DjangoObjectType):
    class Meta:
      model = AddressUseraddress
      fields = (
        "title", 
        "first_name",
        "last_name",
        "line1",
        "line2",
        "line3",
        "line4",
        "state",
        "postcode", 
        "search_text",
        "phone_number",
        "notes",
        "is_default_for_shipping",
        "is_default_for_billing",
        "num_orders_as_shipping_address",
        "hash",
        "date_created",
        "country",
        "user",
        "num_orders_as_billing_address",
    )

class AdvancedFiltersAdvancedfilterType(DjangoObjectType):
    class Meta:
      model = AdvancedFiltersAdvancedfilter
      fields = (
        "title",
        "url",
        "b64_query",
        "model",
        "created_by",
        "created_at",
    )

class AdvancedFiltersAdvancedfilterGroupsType(DjangoObjectType):
    class Meta:
        model = AdvancedFiltersAdvancedfilterGroups
        fields = (
        "advancedfilter",
        "group",
    )

class AdvancedFiltersAdvancedfilterUsersType(DjangoObjectType):
    class Meta:
        model = AdvancedFiltersAdvancedfilterUsers
        fields = (
        "advancedfilter",
        "user",
    )

class AnalyticsProductrecordType(DjangoObjectType):
    class Meta:
        model = AnalyticsProductrecord
        fields = (
        "num_views",
        "num_basket_additions",
        "num_purchases",
        "score",
        "product",
    )


class AnalyticsUserproductviewType(DjangoObjectType):
    class Meta:
        model = AnalyticsUserproductview
        fields = (
        "date_created",
        "product",
        "user",
    )

class AnalyticsUserrecordType(DjangoObjectType):
    class Meta:
      model = AnalyticsUserrecord
      fields = (
        "num_product_views",
        "num_basket_additions",
        "num_orders",
        "num_order_lines",
        "num_order_items",
        "total_spent",
        "date_last_order",
        "user",
)

class AnalyticsUsersearchType(DjangoObjectType):
  class Meta:
      model = AnalyticsUsersearch
      fields = (
        "query",
        "date_created",
        "user",
)


class AnnouncementsAnnouncementType(DjangoObjectType):
  class Meta:
      model = AnnouncementsAnnouncement
      fields = (
    "title",
    "content",
    "creation_date",
    "site_wide",
    "members_only",
    "dismissal_type",
    "publish_start",
    "publish_end",
    "creator",
)

class AnnouncementsDismissalType(DjangoObjectType):
  class Meta:
      model = AnnouncementsDismissal
      fields = (
    "dismissed_at",
    "announcement",
    "user",

)

class AuthGroupType(DjangoObjectType):
  class Meta:
     model = AuthGroup
     fields = (
        "name",
)

class AuthGroupPermissionsType(DjangoObjectType):
  class Meta:
     model = AuthGroupPermissions
     fields = (
        "group",
        "permission",
)

class AuthPermissionType(DjangoObjectType):
  class Meta:
     model = AuthPermission
     fields = (
    "name",
    "content_type",
    "codename",
)

class AuthUserType(DjangoObjectType):
  class Meta:
     model = AuthUser
     fields = (
    "password",
    "last_login",
    "is_superuser",
    "username",
    "first_name",
    "last_name",
    "email",
    "is_staff",
    "is_active",
    "date_joined",
)

class AuthUserGroupsType(DjangoObjectType):
  class Meta:
     model = AuthUserGroups
     fields = (
    "user",
    "group",
)

class AuthUserUserPermissionsType(DjangoObjectType):
  class Meta:
     model = AuthUserUserPermissions
     fields = (
    "user",
    "permission",
)

class BasketBasketType(DjangoObjectType):
  class Meta:
     model = BasketBasket
     fields = (
    "status",
    "date_created",
    "date_merged",
    "date_submitted",
    "owner",
)

class BasketBasketVouchersType(DjangoObjectType):
  class Meta:
     model = BasketBasketVouchers
     fields = (
    "basket",
    "voucher",
)

class BasketLineType(DjangoObjectType):
  class Meta:
     model = BasketLine
     fields = (
    "line_reference",
    "quantity",
    "price_currency",
    "price_excl_tax",
    "price_incl_tax",
    "date_created",
    "basket",
    "product",
    "stockrecord",
    "date_updated",
)

class BasketLineattributeType(DjangoObjectType):
  class Meta:
     model = BasketLineattribute
     fields = (
    "value",
    "line",
    "option",
)

class Bootstrap4AlertsBootstrap4AlertsType(DjangoObjectType):
  class Meta:
     model = Bootstrap4AlertsBootstrap4Alerts
     fields = (
    "cmsplugin_ptr",
    "alert_context",
    "alert_dismissable",
    "tag_type",
    "attributes",
)

class Bootstrap4BadgeBootstrap4BadgeType(DjangoObjectType):
  class Meta:
     model = Bootstrap4BadgeBootstrap4Badge
     fields = (
    "cmsplugin_ptr",
    "badge_text",
    "badge_context",
    "badge_pills",
    "attributes",
)

class Bootstrap4CardBootstrap4CardType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CardBootstrap4Card
     fields = (
    "cmsplugin_ptr",
    "card_type",
    "card_context",
    "card_alignment",
    "card_outline",
    "card_text_color",
    "tag_type",
    "attributes",
)

class Bootstrap4CardBootstrap4CardinnerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CardBootstrap4Cardinner
     fields = (
    "cmsplugin_ptr",
    "inner_type",
    "tag_type",
    "attributes",
)

class Bootstrap4CarouselBootstrap4CarouselType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CarouselBootstrap4Carousel
     fields = (
    "cmsplugin_ptr",
    "template",
    "carousel_interval",
    "carousel_controls",
    "carousel_indicators",
    "carousel_keyboard",
    "carousel_pause",
    "carousel_ride",
    "carousel_wrap",
    "tag_type",
    "attributes",
    "carousel_aspect_ratio",
)

class Bootstrap4CarouselBootstrap4CarouselslideType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CarouselBootstrap4Carouselslide
     fields = (
    "template",
    "name",
    "external_link",
    "anchor",
    "mailto",
    "phone",
    "target",
    "attributes",
    "cmsplugin_ptr",
    "carousel_content",
    "tag_type",
    "carousel_image",
    "internal_link",
    "file_link",
)

class Bootstrap4CollapseBootstrap4CollapseType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CollapseBootstrap4Collapse
     fields = (
    "cmsplugin_ptr",
    "siblings",
    "tag_type",
    "attributes",
    )

class Bootstrap4CollapseBootstrap4CollapsecontainerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CollapseBootstrap4Collapsecontainer
     fields = (
    "cmsplugin_ptr",
    "identifier",
    "tag_type",
    "attributes",
)

class Bootstrap4CollapseBootstrap4CollapsetriggerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CollapseBootstrap4Collapsetrigger
     fields = (
    "cmsplugin_ptr",
    "identifier",
    "tag_type",
    "attributes",
)

class Bootstrap4ContentBootstrap4BlockquoteType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ContentBootstrap4Blockquote
     fields = (
    "cmsplugin_ptr",
    "quote_content",
    "quote_origin",
    "quote_alignment",
    "attributes",
)

class Bootstrap4ContentBootstrap4CodeType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ContentBootstrap4Code
     fields = (
    "cmsplugin_ptr",
    "code_content",
    "tag_type",
    "attributes",
)

class Bootstrap4ContentBootstrap4FigureType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ContentBootstrap4Figure
     fields = (
    "cmsplugin_ptr",
    "figure_caption",
    "figure_alignment",
    "attributes",
)

class Bootstrap4GridBootstrap4GridcolumnType(DjangoObjectType):
  class Meta:
     model = Bootstrap4GridBootstrap4Gridcolumn
     fields = (
    "cmsplugin_ptr",
    "column_type",
    "column_alignment",
    "tag_type",
    "attributes",
    "xs_col",
    "xs_order",
    "xs_ml",
    "xs_mr",
    "sm_col",
    "sm_order",
    "sm_ml",
    "sm_mr",
    "md_col",
    "md_order",
    "md_ml",
    "md_mr",
    "lg_col",
    "lg_order",
    "lg_ml",
    "lg_mr",
    "xl_col",
    "xl_order",
    "xl_ml",
    "xl_mr",
    "lg_offset",
    "md_offset",
    "sm_offset",
    "xl_offset",
    "xs_offset",
)

class Bootstrap4GridBootstrap4GridcontainerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4GridBootstrap4Gridcontainer
     fields = (
    "cmsplugin_ptr",
    "container_type",
    "tag_type",
    "attributes",
)

class Bootstrap4GridBootstrap4GridrowType(DjangoObjectType):
  class Meta:
     model = Bootstrap4GridBootstrap4Gridrow
     fields = (
    "cmsplugin_ptr",
    "vertical_alignment",
    "horizontal_alignment",
    "gutters",
    "tag_type",
    "attributes",
)

class Bootstrap4JumbotronBootstrap4JumbotronType(DjangoObjectType):
  class Meta:
     model = Bootstrap4JumbotronBootstrap4Jumbotron
     fields = (
    "cmsplugin_ptr",
    "fluid",
    "tag_type",
    "attributes",
)

class Bootstrap4LinkBootstrap4LinkType(DjangoObjectType):
  class Meta:
     model = Bootstrap4LinkBootstrap4Link
     fields = (
    "template",
    "name",
    "external_link",
    "anchor",
    "mailto",
    "phone",
    "target",
    "attributes",
    "cmsplugin_ptr",
    "link_type",
    "link_context",
    "link_size",
    "link_outline",
    "link_block",
    "internal_link",
    "icon_left",
    "icon_right",
    "file_link",
)

class Bootstrap4ListgroupBootstrap4ListgroupType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ListgroupBootstrap4Listgroup
     fields = (
    "cmsplugin_ptr",
    "list_group_flush",
    "tag_type",
    "attributes",
)

class Bootstrap4ListgroupBootstrap4ListgroupitemType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ListgroupBootstrap4Listgroupitem
     fields = (
    "cmsplugin_ptr",
    "list_context",
    "list_state",
    "tag_type",
    "attributes",
)

class Bootstrap4MediaBootstrap4MediaType(DjangoObjectType):
  class Meta:
     model = Bootstrap4MediaBootstrap4Media
     fields = (
    "cmsplugin_ptr",
    "tag_type",
    "attributes",
)

class Bootstrap4MediaBootstrap4MediabodyType(DjangoObjectType):
  class Meta:
     model = Bootstrap4MediaBootstrap4Mediabody
     fields = (
    "cmsplugin_ptr",
    "tag_type",
    "attributes",
)

class Bootstrap4PictureBootstrap4PictureType(DjangoObjectType):
  class Meta:
     model = Bootstrap4PictureBootstrap4Picture
     fields = (
    "template",
    "external_picture",
    "width",
    "height",
    "alignment",
    "caption_text",
    "attributes",
    "link_url",
    "link_target",
    "link_attributes",
    "use_automatic_scaling",
    "use_no_cropping",
    "use_crop",
    "use_upscale",
    "cmsplugin_ptr",
    "picture_fluid",
    "picture_rounded",
    "picture_thumbnail",
    "link_page",
    "picture",
    "thumbnail_options",
    "use_responsive_image",
)

class Bootstrap4TabsBootstrap4TabType(DjangoObjectType):
  class Meta:
     model = Bootstrap4TabsBootstrap4Tab
     fields = (
    "cmsplugin_ptr",
    "template",
    "tab_type",
    "tab_alignment",
    "tab_index",
    "tab_effect",
    "tag_type",
    "attributes",
)

class Bootstrap4TabsBootstrap4TabitemType(DjangoObjectType):
  class Meta:
     model = Bootstrap4TabsBootstrap4Tabitem
     fields = (
    "cmsplugin_ptr",
    "tab_title",
    "tag_type",
    "attributes",
)

class Bootstrap4UtilitiesBootstrap4SpacingType(DjangoObjectType):
  class Meta:
     model = Bootstrap4UtilitiesBootstrap4Spacing
     fields = (
    "cmsplugin_ptr",
    "space_property",
    "space_sides",
    "space_size",
    "space_device",
    "tag_type",
    "attributes",
)

class CatalogueAttributeoptionType(DjangoObjectType):
  class Meta:
     model = CatalogueAttributeoption
     fields = (
    "option",
    "group",
)

class CatalogueAttributeoptiongroupType(DjangoObjectType):
  class Meta:
     model = CatalogueAttributeoptiongroup
     fields = (
    "name",
)

class CatalogueCategoryType(DjangoObjectType):
  class Meta:
     model = CatalogueCategory
     fields = (
    "path",
    "depth",
    "numchild",
    "name",
    "description",
    "image",
    "slug",
    "ancestors_are_public",
    "is_public",
    "meta_description",
    "meta_title",
)

class CatalogueOptionType(DjangoObjectType):
  class Meta: 
     model = CatalogueOption
     fields = (
    "name",
    "code",
    "type",
    "required",
)

class CatalogueProductType(DjangoObjectType):
  class Meta:
     model = CatalogueProduct
     fields = (
    "structure",
    "upc",
    "title",
    "slug",
    "description",
    "rating",
    "date_created",
    "date_updated",
    "is_discountable",
    "parent",
    "product_class",
    "is_public",
    "meta_description",
    "meta_title",
)

class CatalogueProductProductOptionsType(DjangoObjectType):
  class Meta:
     model = CatalogueProductProductOptions
     fields = (
    "product",
    "option",
)

class CatalogueProductattributeType(DjangoObjectType):
  class Meta:
     model = CatalogueProductattribute
     fields = (
    "name",
    "code",
    "type",
    "required",
    "option_group",
    "product_class",
)

class CatalogueProductattributevalueType(DjangoObjectType):
  class Meta:
     model = CatalogueProductattributevalue
     fields = (
    "value_text",
    "value_integer",
    "value_boolean",
    "value_float",
    "value_richtext",
    "value_date",
    "value_file",
    "value_image",
    "entity_object_id",
    "attribute",
    "entity_content_type",
    "product",
    "value_option",
    "value_datetime",
)

class CatalogueProductattributevalueValueMultiOptionType(DjangoObjectType):
  class Meta:
     model = CatalogueProductattributevalueValueMultiOption
     fields = (
    "productattributevalue",
    "attributeoption",
)

class CatalogueProductcategoryType(DjangoObjectType):
  class Meta:
     model = CatalogueProductcategory
     fields = (
    "category",
    "product",
)

class CatalogueProductclassType(DjangoObjectType):
    class Meta:
     model = CatalogueProductclass
     fields = (
    "name",
    "slug",
    "requires_shipping",
    "track_stock",
     )

class CatalogueProductclassOptionsType(DjangoObjectType):
    class Meta:
     model = CatalogueProductclassOptions
     fields = (
    "productclass",
    "option",
    )

class CatalogueOptionType(DjangoObjectType):
    class Meta:
     model = CatalogueOption
     fields = (
    "name",
    "code",
    "type",
    "required",
)

class CatalogueProductType(DjangoObjectType):
    class Meta:
     model = CatalogueProduct
     fields = (
    "structure",
    "upc",
    "title",
    "slug",
    "description",
    "rating",
    "date_created",
    "date_updated",
    "is_discountable",
    "parent",
    "product_class",
    "is_public",
    "meta_description",
    "meta_title",
)

class CatalogueProductimageType(DjangoObjectType):
  class Meta:
     model = CatalogueProductimage
     fields = (
    "original",
    "caption",
    "display_order",
    "date_created",
    "product",
)

class CatalogueProductrecommendationType(DjangoObjectType):
  class Meta:
     model = CatalogueProductrecommendation
     fields = (
    "ranking",
    "primary",
    "recommendation",
)

class CmsAliaspluginmodelType(DjangoObjectType):
  class Meta:
     model = CmsAliaspluginmodel
     fields = (
    "cmsplugin_ptr",
    "plugin",
    "alias_placeholder",
)

class CmsCmspluginType(DjangoObjectType):
  class Meta:
     model = CmsCmsplugin
     fields = (
    "position",
    "language",
    "plugin_type",
    "creation_date",
    "changed_date",
    "parent",
    "placeholder",
    "depth",
    "numchild",
    "path",
)

class CmsGlobalpagepermissionType(DjangoObjectType):
  class Meta:
     model = CmsGlobalpagepermission
     fields = (
    "can_change",
    "can_add",
    "can_delete",
    "can_change_advanced_settings",
    "can_publish",
    "can_change_permissions",
    "can_move_page",
    "can_view",
    "can_recover_page",
    "group",
    "user",
)

class CmsGlobalpagepermissionSitesType(DjangoObjectType):
  class Meta:
     model = CmsGlobalpagepermissionSites
     fields = (
    "globalpagepermission",
    "site",
)

class CmsPageType(DjangoObjectType):
  class Meta:
     model = CmsPage
     fields = (
    "created_by",
    "changed_by",
    "creation_date",
    "changed_date",
    "publication_date",
    "publication_end_date",
    "in_navigation",
    "soft_root",
    "reverse_id",
    "navigation_extenders",
    "template",
    "login_required",
    "limit_visibility_in_menu",
    "is_home",
    "application_urls",
    "application_namespace",
    "publisher_is_draft",
    "languages",
    "xframe_options",
    "publisher_public",
    "is_page_type",
    "node",
)

class CmsPagePlaceholdersType(DjangoObjectType):
  class Meta:
     model = CmsPagePlaceholders
     fields = (
    "page",
    "placeholder",
)

class CmsPagepermissionType(DjangoObjectType):
  class Meta:
     model = CmsPagepermission
     fields = (
    "can_change",
    "can_add",
    "can_delete",
    "can_change_advanced_settings",
    "can_publish",
    "can_change_permissions",
    "can_move_page",
    "can_view",
    "grant_on",
    "group",
    "page",
    "user",
)

class CmsPageuserType(DjangoObjectType):
  class Meta:
     model = CmsPageuser
     fields = (
    "user_ptr",
    "created_by",
)

class CmsPageusergroupType(DjangoObjectType):
  class Meta:
     model = CmsPageusergroup
     fields = (
    "group_ptr",
    "created_by",
)

class CmsPlaceholderType(DjangoObjectType):
  class Meta:
     model = CmsPlaceholder
     fields = (
    "slot",
    "default_width",
)

class CmsPlaceholderreferenceType(DjangoObjectType):
  class Meta:
     model = CmsPlaceholderreference
     fields = (
    "cmsplugin_ptr",
    "name",
    "placeholder_ref",
)

class CmsStaticplaceholderType(DjangoObjectType):
  class Meta:
     model = CmsStaticplaceholder
     fields = (
    "name",
    "code",
    "dirty",
    "creation_method",
    "draft",
    "public",
    "site",
)

class CmsTitleType(DjangoObjectType):
  class Meta:
     model = CmsTitle
     fields = (
    "language",
    "title",
    "page_title",
    "menu_title",
    "meta_description",
    "slug",
    "path",
    "has_url_overwrite",
    "redirect",
    "creation_date",
    "published",
    "publisher_is_draft",
    "publisher_state",
    "page",
    "publisher_public",
)

class CmsTreenodeType(DjangoObjectType):
  class Meta:
     model = CmsTreenode
     fields = (
    "path",
    "depth",
    "numchild",
    "parent",
    "site",
)

class CmsUrlconfrevisionType(DjangoObjectType):
  class Meta:
     model = CmsUrlconfrevision
     fields = (
    "revision",
)

class CmsUsersettingsType(DjangoObjectType):
  class Meta:
     model = CmsUsersettings
     fields = (
    "language",
    "clipboard",
    "user",
)

class CommunicationCommunicationeventtypeType(DjangoObjectType):
  class Meta:
     model = CommunicationCommunicationeventtype
     fields = (
    "code",
    "name",
    "category",
    "email_subject_template",
    "email_body_template",
    "email_body_html_template",
    "sms_template",
    "date_created",
    "date_updated",
)

class CommunicationEmailType(DjangoObjectType):
  class Meta:
     model = CommunicationEmail
     fields = (
    "subject",
    "body_text",
    "body_html",
    "date_sent",
    "user",
    "email",
)

class CommunicationNotificationType(DjangoObjectType):
  class Meta:
     model = CommunicationNotification
     fields = (
    "subject",
    "body",
    "location",
    "date_sent",
    "date_read",
    "recipient",
    "sender",
)

class CustomerProductalertType(DjangoObjectType):
  class Meta:
     model = CustomerProductalert
     fields = (
    "email",
    "key",
    "status",
    "date_created",
    "date_confirmed",
    "date_cancelled",
    "date_closed",
    "product",
    "user",
)

class DjangoAdminLogType(DjangoObjectType):
  class Meta:
     model = DjangoAdminLog
     fields = (
    "action_time",
    "object_id",
    "object_repr",
    "action_flag",
    "change_message",
    "content_type",
    "user",
)

class DjangoContentType(DjangoObjectType):
  class Meta:
     model = DjangoContent
     fields = (
    "app_label",
    "model",
)

class DjangoFlatpageType(DjangoObjectType):
  class Meta:
     model = DjangoFlatpage
     fields = (
    "url",
    "title",
    "content",
    "enable_comments",
    "template_name",
    "registration_required",
)

class DjangoFlatpageSitesType(DjangoObjectType):
  class Meta:
     model = DjangoFlatpageSites
     fields = (
    "flatpage",
    "site",
)

class DjangoMigrationsType(DjangoObjectType):
  class Meta:
     model = DjangoMigrations
     fields = (
    "app",
    "name",
    "applied",
)

class DjangoSessionType(DjangoObjectType):
  class Meta:
     model = DjangoSession
     fields = (
    "session_key",
    "session_data",
    "expire_date",
)

class DjangoSiteType(DjangoObjectType):
  class Meta:
     model = DjangoSite
     fields = (
    "domain",
    "name",
)

class DjangocmsBlogAuthorentriespluginType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogAuthorentriesplugin
     fields = (
    "cmsplugin_ptr",
    "latest_posts",
    "app_config",
    "current_site",
    "template_folder",
)

class DjangocmsBlogAuthorentriespluginAuthorsType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogAuthorentriespluginAuthors
     fields = (
    "authorentriesplugin",
    "user",
)

class DjangocmsBlogBlogcategoryType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogcategory
     fields = (
    "date_created",
    "date_modified",
    "parent",
    "app_config",
)

class DjangocmsBlogBlogcategoryTranslationType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogcategoryTranslation
     fields = (
    "language_code",
    "name",
    "slug",
    "master",
    "meta_description",
)

class DjangocmsBlogBlogconfigType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogconfig
     fields = (
    "type",
    "namespace",
    "app_data",
)

class DjangocmsBlogBlogconfigTranslationType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogconfigTranslation
     fields = (
    "language_code",
    "app_title",
    "master",
    "object_name",
)

class DjangocmsBlogGenericblogpluginType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogGenericblogplugin
     fields = (
    "cmsplugin_ptr",
    "app_config",
    "current_site",
    "template_folder",
)

class DjangocmsBlogLatestpostspluginType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogLatestpostsplugin
     fields = (
    "cmsplugin_ptr",
    "latest_posts",
    "app_config",
    "current_site",
    "template_folder",
)

class DjangocmsBlogLatestpostspluginCategoriesType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogLatestpostspluginCategories
     fields = (
    "latestpostsplugin",
    "blogcategory",
)

class DjangocmsBlogPostType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPost
     fields = (
    "date_created",
    "date_modified",
    "date_published",
    "date_published_end",
    "publish",
    "enable_comments",
    "author",
    "content",
    "main_image",
    "app_config",
    "main_image_full",
    "main_image_thumbnail",
    "liveblog",
    "enable_liveblog",
    "date_featured",
    "media",
)

class DjangocmsBlogPostCategoriesType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostCategories
     fields = (
    "post",
    "blogcategory",
)

class DjangocmsBlogPostRelatedType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostRelated
     fields = (
    "from_post",
    "to_post",
    "sort_value",
)

class DjangocmsBlogPostSitesType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostSites
     fields = (
    "post",
    "site",
)

class DjangocmsBlogPostTranslationType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostTranslation
     fields = (
    "language_code",
    "title",
    "slug",
    "abstract",
    "meta_description",
    "meta_keywords",
    "meta_title",
    "post_text",
    "master",
)

class DjangocmsFileFileType(DjangoObjectType):
  class Meta:
     model = DjangocmsFileFile
     fields = (
    "cmsplugin_ptr",
    "file_name",
    "link_target",
    "link_title",
    "file_src",
    "attributes",
    "template",
    "show_file_size",
)

class DjangocmsFileFolderType(DjangoObjectType):
  class Meta: 
     model = DjangocmsFileFolder
     fields = (
    "template",
    "link_target",
    "show_file_size",
    "attributes",
    "cmsplugin_ptr",
    "folder_src",
)

class DjangocmsGooglemapGooglemapType(DjangoObjectType):
  class Meta:
     model = DjangocmsGooglemapGooglemap
     fields = (
    "cmsplugin_ptr",
    "title",
    "zoom",
    "lat",
    "lng",
    "width",
    "height",
    "scrollwheel",
    "double_click_zoom",
    "draggable",
    "keyboard_shortcuts",
    "pan_control",
    "zoom_control",
    "street_view_control",
    "style",
    "fullscreen_control",
    "map_type_control",
    "rotate_control",
    "scale_control",
    "template",
)

class DjangocmsGooglemapGooglemapmarkerType(DjangoObjectType):
  class Meta:
     model = DjangocmsGooglemapGooglemapmarker
     fields = (
    "cmsplugin_ptr",
    "title",
    "address",
    "lat",
    "lng",
    "show_content",
    "info_content",
    "icon",
)

class DjangocmsGooglemapGooglemaprouteType(DjangoObjectType):
  class Meta:
     model = DjangocmsGooglemapGooglemaproute
     fields = (
    "cmsplugin_ptr",
    "title",
    "origin",
    "destination",
    "travel_mode",
)

class DjangocmsHistoryPlaceholderactionType(DjangoObjectType):
  class Meta:
     model = DjangocmsHistoryPlaceholderaction
     fields = (
    "action",
    "pre_action_data",
    "post_action_data",
    "language",
    "order",
    "operation",
    "placeholder",
)

class DjangocmsHistoryPlaceholderoperationType(DjangoObjectType):
  class Meta:
     model = DjangocmsHistoryPlaceholderoperation
     fields = (
    "operation_type",
    "token",
    "origin",
    "language",
    "user_session_key",
    "date_created",
    "is_applied",
    "is_archived",
    "site",
    "user",
)

class DjangocmsIconIconType(DjangoObjectType):
  class Meta:
     model = DjangocmsIconIcon
     fields = (
    "cmsplugin_ptr",
    "icon",
    "template",
    "label",
    "attributes",
)

class DjangocmsLinkLinkType(DjangoObjectType):
  class Meta:
     model = DjangocmsLinkLink
     fields = (
    "cmsplugin_ptr",
    "name",
    "external_link",
    "anchor",
    "mailto",
    "phone",
    "target",
    "internal_link",
    "attributes",
    "template",
    "file_link",
)

class DjangocmsMapsMapsType(DjangoObjectType):
  class Meta:
     model = DjangocmsMapsMaps
     fields = (
    "cmsplugin_ptr",
    "map_provider",
    "title",
    "address",
    "zipcode",
    "city",
    "content",
    "style",
    "zoom",
    "lat",
    "lng",
    "route_planer_title",
    "route_planer",
    "width",
    "height",
    "info_window",
    "scrollwheel",
    "double_click_zoom",
    "draggable",
    "keyboard_shortcuts",
    "pan_control",
    "zoom_control",
    "street_view_control",
    "layers_control",
    "scale_bar",
)

class DjangocmsPicturePictureType(DjangoObjectType):
  class Meta:
     model = DjangocmsPicturePicture
     fields = (
    "cmsplugin_ptr",
    "link_url",
    "alignment",
    "link_page",
    "height",
    "width",
    "picture",
    "attributes",
    "caption_text",
    "link_attributes",
    "link_target",
    "use_automatic_scaling",
    "use_crop",
    "use_no_cropping",
    "use_upscale",
    "thumbnail_options",
    "external_picture",
    "template",
    "use_responsive_image",
)

class DjangocmsStyleStyleType(DjangoObjectType):
  class Meta:
     model = DjangocmsStyleStyle
     fields = (
        "cmsplugin_ptr",
        "class_name",
        "tag_type",
        "padding_left",
        "padding_right",
        "padding_top",
        "padding_bottom",
        "margin_left",
        "margin_right",
        "margin_top",
        "margin_bottom",
        "additional_classes",
        "attributes",
        "id_name",
        "label",
        "template",
)

class DjangocmsTextCkeditorTextType(DjangoObjectType):
  class Meta:
     model = DjangocmsTextCkeditorText
     fields = (
    "cmsplugin_ptr",
    "body",
)

class DjangocmsVideoVideoplayerType(DjangoObjectType):
  class Meta:
     model = DjangocmsVideoVideoplayer
     fields = (
    "cmsplugin_ptr",
    "embed_link",
    "poster",
    "attributes",
    "label",
    "template",
    "parameters",
)

class DjangocmsVideoVideosourceType(DjangoObjectType):
  class Meta:
     model = DjangocmsVideoVideosource
     fields = (
    "cmsplugin_ptr",
    "text_title",
    "text_description",
    "attributes",
    "source_file",
)

class DjangocmsVideoVideotrackType(DjangoObjectType):
  class Meta:
     model = DjangocmsVideoVideotrack
     fields = (
    "cmsplugin_ptr",
    "kind",
    "srclang",
    "label",
    "attributes",
    "src",
)

class EasyThumbnailsSourceType(DjangoObjectType):
  class Meta:
     model = EasyThumbnailsSource
     fields = (
    "storage_hash",
    "name",
    "modified",
)

class EasyThumbnailsThumbnailType(DjangoObjectType):
  class Meta:
     model = EasyThumbnailsThumbnail
     fields = (
    "storage_hash",
    "name",
    "modified",
    "source",
)

class EasyThumbnailsThumbnaildimensionsType(DjangoObjectType):
  class Meta:
     model = EasyThumbnailsThumbnaildimensions
     fields = (
    "thumbnail",
    "width",
    "height",
)

class FilerClipboardType(DjangoObjectType):
  class Meta:
     model = FilerClipboard
     fields = (
    "user",
)

class FilerClipboarditemType(DjangoObjectType):
  class Meta:
     model = FilerClipboarditem
     fields = (
    "clipboard",
    "file",
)

class FilerFileType(DjangoObjectType):
  class Meta:
     model = FilerFile
     fields = (
    "file",
    "field_file_size",
    "sha1",
    "has_all_mandatory_data",
    "original_filename",
    "name",
    "description",
    "uploaded_at",
    "modified_at",
    "is_public",
    "folder",
    "owner",
    "polymorphic_ctype",
    "mime_type",
)

class FilerFolderType(DjangoObjectType):
  class Meta:
     model = FilerFolder
     fields = (
    "name",
    "uploaded_at",
    "created_at",
    "modified_at",
    "lft",
    "rght",
    "tree_id",
    "level",
    "owner",
    "parent",
)

class FilerFolderpermissionType(DjangoObjectType):
  class Meta:
     model = FilerFolderpermission
     fields = (
    "type",
    "everybody",
    "can_edit",
    "can_read",
    "can_add_children",
    "folder",
    "group",
    "user",
)

class FilerImageType(DjangoObjectType):
  class Meta:
     model = FilerImage
     fields = (
    "file_ptr",
    "field_height",
    "field_width",
    "date_taken",
    "default_alt_text",
    "default_caption",
    "author",
    "must_always_publish_author_credit",
    "must_always_publish_copyright",
    "subject_location", 
)

class FilerThumbnailoptionType(DjangoObjectType):
  class Meta:
     model = FilerThumbnailoption
     fields = (
    "name",
    "width",
    "height",
    "crop",
    "upscale",
)

class MenusCachekeyType(DjangoObjectType):
  class Meta:
     model = MenusCachekey
     fields = (
    "language",
    "site",
    "key",
)

class OfferBenefitType(DjangoObjectType):
  class Meta:
     model = OfferBenefit
     fields = (
    "type",
    "value",
    "max_affected_items",
    "proxy_class",
    "range",
)

class OfferConditionType(DjangoObjectType):
  class Meta:
     model = OfferCondition
     fields = (
    "type",
    "value",
    "proxy_class",
)

class OfferConditionalofferType(DjangoObjectType):
  class Meta:
     model = OfferConditionaloffer
     fields = (
    "name",
    "slug",
    "description",
    "offer_type",
    "status", 
    "priority",
    "start_datetime",
    "end_datetime",
    "max_global_applications",
    "max_user_applications",
    "max_basket_applications",
    "max_discount",
    "total_discount",
    "num_applications",
    "num_orders",
    "redirect_url",
    "date_created",
    "benefit",
    "condition",
    "exclusive",
)

class OfferConditionalofferCombinationsType(DjangoObjectType):
  class Meta:
     model = OfferConditionalofferCombinations
     fields = (
    "from_conditionaloffer",
    "to_conditionaloffer",
)

class OfferRangeType(DjangoObjectType):
    class Meta:
     model = OfferRange
     fields = (
    "name",
    "slug",
    "description",
    "is_public",
    "includes_all_products",
    "proxy_class",
    "date_created",
)

class OfferRangeClassesType(DjangoObjectType):
    class Meta:
     model = OfferRangeClasses
     fields = (
    "range",
    "productclass",
)

class OfferRangeExcludedProductsType(DjangoObjectType):
  class Meta:
     model = OfferRangeExcludedProducts
     fields = (
    "range",
)

class OfferRangeIncludedCategoriesType(DjangoObjectType):
  class Meta:
     model = OfferRangeIncludedCategories
     fields = (
    "range",
)

class OfferRangeproductType(DjangoObjectType):
  class Meta:
     model = OfferRangeproduct
     fields = (
    "display_order",
    "product",
    "range", 
)

class OfferRangeproductfileuploadType(DjangoObjectType):
  class Meta:
     model = OfferRangeproductfileupload
     fields = (
    "filepath",
    "size",
    "date_uploaded",
    "status",
    "error_message",
    "date_processed",
    "num_new_skus",
    "num_unknown_skus",
    "num_duplicate_skus",
    "range",
)

class OrderBillingaddressType(DjangoObjectType):
  class Meta:
     model = OrderBillingaddress
     fields = (
    "title", 
    "first_name",
    "last_name",
    "line1",
    "line2",
    "line3",
    "line4",
    "state",
    "postcode", 
    "search_text",
    "country",
)

class OrderCommunicationeventType(DjangoObjectType):
    class Meta:
     model = OrderCommunicationevent
     fields = (
        "date_created",
        "event_type",
        "order",
)

class OrderLineType(DjangoObjectType):
  class Meta:
     model = OrderLine
     fields = (
    "partner_name",
    "partner_sku",
    "partner_line_reference",
    "partner_line_notes",
    "title",
    "upc",
    "quantity",
    "line_price_incl_tax",
    "line_price_excl_tax",
    "line_price_before_discounts_incl_tax",
    "line_price_before_discounts_excl_tax",
    "unit_price_incl_tax",
    "unit_price_excl_tax",
    "status",
    "order",
    "partner",
    "product",
    "stockrecord",
)

class OrderLineattributeType(DjangoObjectType):
  class Meta:
     model = OrderLineattribute
     fields = (
    "type",
    "value",
    "line",
    "option",
)

class OrderLinepriceType(DjangoObjectType):
  class Meta:
     model = OrderLineprice
     fields = (
    "quantity",
    "price_incl_tax",
    "price_excl_tax",
    "shipping_incl_tax",
    "shipping_excl_tax",
    "line",
    "order",
)

class OrderOrderType(DjangoObjectType):
  class Meta:
     model = OrderOrder
     fields = (
    "number",
    "currency",
    "total_incl_tax",
    "total_excl_tax",
    "shipping_incl_tax",
    "shipping_excl_tax",
    "shipping_method",
    "shipping_code",
    "status",
    "guest_email",
    "date_placed",
    "basket",
    "billing_address",
    "shipping_address",
    "site",
    "user",
)

class OrderOrderdiscountType(DjangoObjectType):
  class Meta:
     model = OrderOrderdiscount
     fields = (
    "category", 
    "offer_id",
    "offer_name",
    "voucher_id",
    "voucher_code",
    "frequency",
    "amount",
    "message",
    "order",
)

class OrderOrdernoteType(DjangoObjectType):
  class Meta:
     model = OrderOrdernote
     fields = (
    "note_type",
    "message",
    "date_created",
    "date_updated",
    "order",
    "user",
)

class OrderOrderstatuschangeType(DjangoObjectType):
  class Meta:
     model = OrderOrderstatuschange
     fields = (
    "old_status",
    "new_status",
    "date_created",
    "order",
)

class OrderPaymenteventType(DjangoObjectType):
  class Meta:
     model = OrderPaymentevent
     fields = (
    "amount",
    "reference",
    "date_created",
    "event_type",
    "order",
    "shipping_event",
)

class OrderPaymenteventquantityType(DjangoObjectType):
  class Meta:
     model = OrderPaymenteventquantity
     fields = (
    "quantity",
    "event",
    "line",
)

class OrderPaymenteventtypeType(DjangoObjectType):
  class Meta:
     model = OrderPaymenteventtype
     fields = (
    "name",
    "code",
)

class OrderShippingaddressType(DjangoObjectType):
  class Meta:
     model = OrderShippingaddress
     fields = (
    "title", 
    "first_name",
    "last_name",
    "line1",
    "line2",
    "line3",
    "line4",
    "state",
    "postcode", 
    "search_text",
    "phone_number",
    "notes",
    "country",
)

class OrderShippingeventType(DjangoObjectType):
  class Meta:
     model = OrderShippingevent
     fields = (
    "notes",
    "date_created",
    "event_type",
)

class OrderShippingeventquantityType(DjangoObjectType):
  class Meta:
     model = OrderShippingeventquantity
     fields = (
    "quantity",
    "event",
    "line",
)

class OrderShippingeventtypeType(DjangoObjectType):
  class Meta:
     model = OrderShippingeventtype
     fields = (
    "name",
    "code",
)

class OrderSurchargeType(DjangoObjectType):
  class Meta:
     model = OrderSurcharge
     fields = (
    "name",
    "code",
    "incl_tax",
    "excl_tax",
    "order",
)

class OscarInvoicesInvoiceType(DjangoObjectType):
  class Meta:
     model = OscarInvoicesInvoice
     fields = (
    "number",
    "notes",
    "document",
    "legal_entity",
    "order",
)

class OscarInvoicesLegalentityType(DjangoObjectType):
  class Meta:
     model = OscarInvoicesLegalentity
     fields = (
    "shop_name",
    "business_name",
    "vat_number",
    "logo",
    "email",
    "web_site",
)

class OscarInvoicesLegalentityaddressType(DjangoObjectType):
  class Meta:
     model = OscarInvoicesLegalentityaddress
     fields = (
    "title", 
    "first_name",
    "last_name",
    "line1",
    "line2",
    "line3",
    "line4",
    "state",
    "postcode", 
    "search_text",
    "phone_number",
    "fax_number",
    "country",
    "legal_entity",
)

class OscarapiApikeyType(DjangoObjectType):
  class Meta:
     model = OscarapiApikey
     fields = (
    "key",
)

class PartnerPartnerType(DjangoObjectType):
  class Meta:
     model = PartnerPartner
     fields = (
    "code",
    "name",
)

class PartnerPartnerUsersType(DjangoObjectType):
  class Meta:
     model = PartnerPartnerUsers
     fields = (
    "partner",
    "user",
)

class PartnerPartneraddressType(DjangoObjectType):
  class Meta:
     model = PartnerPartneraddress
     fields = (
    "title", 
    "first_name",
    "last_name",
    "line1",
    "line2",
    "line3",
    "line4",
    "state",
    "postcode", 
    "search_text",
    "country",
    "partner",
)

class PartnerStockalertType(DjangoObjectType):
  class Meta:
     model = PartnerStockalert
     fields = (
    "threshold",
    "status",
    "date_created",
    "date_closed",
    "stockrecord",
)

class PartnerStockrecordType(DjangoObjectType):
  class Meta:
     model = PartnerStockrecord
     fields = (
    "partner_sku",
    "price_currency",
    "price",
    "num_in_stock",
    "num_allocated",
    "low_stock_threshold",
    "date_created",
    "date_updated",
    "partner",
    "product",
)

class PaymentBankcardType(DjangoObjectType):
  class Meta:
     model = PaymentBankcard
     fields = (
    "card_type",
    "name",
    "number",
    "expiry_date",
    "partner_reference",
    "user",
)

class PaymentSourceType(DjangoObjectType):
  class Meta:
     model = PaymentSource
     fields = (
    "currency",
    "amount_allocated",
    "amount_debited",
    "amount_refunded",
    "reference",
    "label",
    "order",
    "source_type",
)

class PaymentSourcetypeType(DjangoObjectType):
  class Meta:
     model = PaymentSourcetype
     fields = (
    "name",
    "code",
)

class PaymentTransactionType(DjangoObjectType):
  class Meta:
     model = PaymentTransaction
     fields = (
    "txn_type",
    "amount",
    "reference",
    "status",
    "date_created",
    "source",
)

class PaypalExpresstransactionType(DjangoObjectType):
  class Meta:
     model = PaypalExpresstransaction
     fields = (
    "raw_request",
    "raw_response",
    "response_time",
    "date_created",
    "method",
    "version",
    "amount",
    "currency",
    "ack",
    "correlation_id",
    "token",
    "error_code",
    "error_message",
)

class PaypalPayflowtransactionType(DjangoObjectType):
  class Meta:
     model = PaypalPayflowtransaction
     fields = (
    "raw_request",
    "raw_response",
    "response_time",
    "date_created",
    "comment1",
    "trxtype",
    "tender",
    "amount",
    "pnref",
    "ppref",
    "result",
    "respmsg",
    "authcode",
    "cvv2match",
    "avsaddr",
    "avszip",
)

class PhotologueGalleryType(DjangoObjectType):
  class Meta:
     model = PhotologueGallery
     fields = (
    "date_added",
    "title",
    "slug",
    "description",
    "is_public",
)

class PhotologueGalleryPhotosType(DjangoObjectType):
  class Meta:
     model = PhotologueGalleryPhotos
     fields = (
    "sort_value",
    "gallery",
    "photo",
)

class PhotologueGallerySitesType(DjangoObjectType):
  class Meta:
     model = PhotologueGallerySites
     fields = (
    "gallery",
    "site",
)

class PhotologuePhotoType(DjangoObjectType):
  class Meta:
     model = PhotologuePhoto
     fields = (
    "image",
    "date_taken",
    "view_count",
    "crop_from",
    "title",
    "slug",
    "caption",
    "date_added",
    "is_public",
    "effect",
)

class PhotologuePhotoSitesType(DjangoObjectType):
  class Meta:
     model = PhotologuePhotoSites
     fields = (
    "photo",
    "site",
)

class PhotologuePhotoeffectType(DjangoObjectType):
  class Meta:
     model = PhotologuePhotoeffect
     fields = (
    "name",
    "description",
    "transpose_method",
    "color",
    "brightness",
    "contrast",
    "sharpness",
    "filters",
    "reflection_size",
    "reflection_strength",
    "background_color",
)

class PhotologuePhotosizeType(DjangoObjectType):
  class Meta:
     model = PhotologuePhotosize
     fields = (
    "name",
    "width",
    "height",
    "quality",
    "upscale",
    "crop",
    "pre_cache",
    "increment_count",
    "effect",
    "watermark",
)

class PhotologueWatermarkType(DjangoObjectType):
  class Meta:
     model = PhotologueWatermark
     fields = (
    "name",
    "description",
    "image",
    "style",
    "opacity",
)

class PinaxBadgesBadgeawardType(DjangoObjectType):
  class Meta:
     model = PinaxBadgesBadgeaward
     fields = (
    "awarded_at",
    "slug",
    "level",
    "user",
)

class PinaxEventsEventType(DjangoObjectType):
  class Meta:
     model = PinaxEventsEvent
     fields = (
    "image",
    "where",
    "what",
    "what_html",
    "start_date",
    "end_date",
    "published_at",
    "created_at",
    "title",
    "url",
    "secondary_image",
)

class PinaxMessagesMessageType(DjangoObjectType):
  class Meta:
     model = PinaxMessagesMessage
     fields = (
    "sent_at",
    "content",
    "sender",
    "thread",
)

class PinaxMessagesThreadType(DjangoObjectType):
  class Meta:
     model = PinaxMessagesThread
     fields = (
    "subject",
)

class PinaxMessagesUserthreadType(DjangoObjectType):
  class Meta:
     model = PinaxMessagesUserthread
     fields = (
    "unread",
    "deleted",
    "thread",
    "user",
)

class ReviewsProductreviewType(DjangoObjectType):
  class Meta:
     model = ReviewsProductreview
     fields = (
    "score",
    "title",
    "body",
    "name",
    "email",
    "homepage",
    "status",
    "total_votes",
    "delta_votes",
    "date_created",
    "product",
    "user",
)

class ReviewsVoteType(DjangoObjectType):
  class Meta:
     model = ReviewsVote
     fields = (
    "delta",
    "date_created",
    "review",
    "user",
)

class ShippingOrderanditemchargesType(DjangoObjectType):
  class Meta:
     model = ShippingOrderanditemcharges
     fields = (
    "code",
    "name",
    "description",
    "price_per_order",
    "price_per_item",
    "free_shipping_threshold",
)

class ShippingOrderanditemchargesCountriesType(DjangoObjectType):
  class Meta:
     model = ShippingOrderanditemchargesCountries
     fields = (
    "orderanditemcharges",
    "country",
)

class ShippingWeightbandType(DjangoObjectType):
  class Meta:
     model = ShippingWeightband
     fields = (
    "upper_limit",
    "method",
)

class ShippingWeightbasedType(DjangoObjectType):
  class Meta:
     model = ShippingWeightbased
     fields = (
    "code",
    "name",
    "description",
    "default_weight",
)

class ShippingWeightbasedCountriesType(DjangoObjectType):
  class Meta:
     model = ShippingWeightbasedCountries
     fields = (
    "weightbased",
    "country",
)

class TaggitTagType(DjangoObjectType):
  class Meta:
     model = TaggitTag
     fields = (
    "name",
    "slug",
)

class TaggitTaggeditemType(DjangoObjectType):
  class Meta:
     model = TaggitTaggeditem
     fields = (
    "object_id",
    "content_type",
    "tag",
)

class TestimonialsTestimonialType(DjangoObjectType):
  class Meta:
     model = TestimonialsTestimonial
     fields = (
    "text",
    "author",
    "affiliation",
    "added",
    "active",
)

class ThumbnailKvstoreType(DjangoObjectType):
  class Meta:
     model = ThumbnailKvstore
     fields = (
    "key",
    "value",
)

class VoucherVoucherType(DjangoObjectType):
  class Meta:
     model = VoucherVoucher
     fields = (
    "name",
    "code",
    "usage",
    "start_datetime",
    "end_datetime",
    "num_basket_additions",
    "num_orders",
    "total_discount",
    "date_created",
    "voucher_set",
)

class VoucherVoucherOffersType(DjangoObjectType):
  class Meta:
     model = VoucherVoucherOffers
     fields = (
    "voucher",
    "conditionaloffer",
)

class VoucherVoucherapplicationType(DjangoObjectType):
  class Meta:
     model = VoucherVoucherapplication
     fields = (
    "date_created",
    "order",
    "user",
    "voucher",
)

class VoucherVouchersetType(DjangoObjectType):
  class Meta:
     model = VoucherVoucherset
     fields = (
    "name",
    "count",
    "code_length",
    "description",
    "date_created",
    "start_datetime",
    "end_datetime",
    "offer",
)

class WishlistsLineType(DjangoObjectType):
  class Meta:
     model = WishlistsLine
     fields = (
    "quantity",
    "title",
    "product",
    "wishlist",
)

class WishlistsWishlistType(DjangoObjectType):
  class Meta:
     model = WishlistsWishlist
     fields = (
        "name",
        "key",
        "visibility",
        "date_created",
        "owner",
    )

class Query(graphene.ObjectType):
  all_AddressCountry = graphene.List(AddressCountryType)
  all_AddressUseraddress = graphene.List(AddressUseraddressType)
  all_AdvancedFiltersAdvancedfilter = graphene.List(AdvancedFiltersAdvancedfilterType)
  all_AdvancedFiltersAdvancedfilterGroups = graphene.List(AdvancedFiltersAdvancedfilterGroupsType)
  all_AdvancedFiltersAdvancedfilterUsers = graphene.List(AdvancedFiltersAdvancedfilterUsersType)
  all_AnalyticsProductrecord = graphene.List(AnalyticsProductrecordType)
  all_AnalyticsUserproductview = graphene.List(AnalyticsUserproductviewType)
  all_AnalyticsUserrecord = graphene.List(AnalyticsUserrecordType)
  all_AnalyticsUsersearch = graphene.List(AnalyticsUsersearchType)
  all_AnnouncementsAnnouncement = graphene.List(AnnouncementsAnnouncementType)
  all_AnnouncementsDismissal = graphene.List(AnnouncementsDismissalType)
  all_AuthGroup = graphene.List(AuthGroupType)
  all_AuthGroupPermissions = graphene.List(AuthGroupPermissionsType)
  all_AuthPermission = graphene.List(AuthPermissionType)
  all_AuthUser = graphene.List(AuthUserType)
  all_AuthUserGroups = graphene.List(AuthUserGroupsType)
  all_AuthUserUserPermissions = graphene.List(AuthUserUserPermissionsType)
  all_BasketBasket = graphene.List(BasketBasketType)
  all_BasketBasketVouchers = graphene.List(BasketBasketVouchersType)
  all_BasketLine = graphene.List(BasketLineType)
  all_BasketLineattribute = graphene.List(BasketLineattributeType)
  all_Bootstrap4AlertsBootstrap4Alerts = graphene.List(Bootstrap4AlertsBootstrap4AlertsType)
  all_Bootstrap4BadgeBootstrap4Badge = graphene.List(Bootstrap4BadgeBootstrap4BadgeType)
  all_Bootstrap4CardBootstrap4Card = graphene.List(Bootstrap4CardBootstrap4CardType)
  all_Bootstrap4CardBootstrap4Cardinner = graphene.List(Bootstrap4CardBootstrap4CardinnerType)
  all_Bootstrap4CarouselBootstrap4Carousel = graphene.List(Bootstrap4CarouselBootstrap4CarouselType)
  all_Bootstrap4CarouselBootstrap4Carouselslide = graphene.List(Bootstrap4CarouselBootstrap4CarouselslideType)
  all_Bootstrap4CollapseBootstrap4Collapse = graphene.List(Bootstrap4CollapseBootstrap4CollapseType)
  all_Bootstrap4CollapseBootstrap4Collapsecontainer = graphene.List(Bootstrap4CollapseBootstrap4CollapsecontainerType)
  all_Bootstrap4CollapseBootstrap4Collapsetrigger = graphene.List(Bootstrap4CollapseBootstrap4CollapsetriggerType)
  all_Bootstrap4ContentBootstrap4Blockquote = graphene.List(Bootstrap4ContentBootstrap4BlockquoteType)
  all_Bootstrap4ContentBootstrap4Code = graphene.List(Bootstrap4ContentBootstrap4CodeType)
  all_Bootstrap4ContentBootstrap4Figure = graphene.List(Bootstrap4ContentBootstrap4FigureType)
  all_Bootstrap4GridBootstrap4Gridcolumn = graphene.List(Bootstrap4GridBootstrap4GridcolumnType)
  all_Bootstrap4GridBootstrap4Gridcontainer = graphene.List(Bootstrap4GridBootstrap4GridcontainerType)
  all_Bootstrap4GridBootstrap4Gridrow = graphene.List(Bootstrap4GridBootstrap4GridrowType)
  all_Bootstrap4JumbotronBootstrap4Jumbotron = graphene.List(Bootstrap4JumbotronBootstrap4JumbotronType)
  all_Bootstrap4LinkBootstrap4Link = graphene.List(Bootstrap4LinkBootstrap4LinkType)
  all_Bootstrap4ListgroupBootstrap4Listgroup = graphene.List(Bootstrap4ListgroupBootstrap4ListgroupType)
  all_Bootstrap4ListgroupBootstrap4Listgroupitem = graphene.List(Bootstrap4ListgroupBootstrap4ListgroupitemType)
  all_Bootstrap4MediaBootstrap4Media = graphene.List(Bootstrap4MediaBootstrap4MediaType)
  all_Bootstrap4MediaBootstrap4Mediabody = graphene.List(Bootstrap4MediaBootstrap4MediabodyType)
  all_Bootstrap4PictureBootstrap4Picture = graphene.List(Bootstrap4PictureBootstrap4PictureType)
  all_Bootstrap4TabsBootstrap4Tab = graphene.List(Bootstrap4TabsBootstrap4TabType)
  all_Bootstrap4TabsBootstrap4Tabitem = graphene.List(Bootstrap4TabsBootstrap4TabitemType)
  all_Bootstrap4UtilitiesBootstrap4Spacing = graphene.List(Bootstrap4UtilitiesBootstrap4SpacingType)
  all_CatalogueAttributeoption = graphene.List(CatalogueAttributeoptionType)
  all_CatalogueAttributeoptiongroup = graphene.List(CatalogueAttributeoptiongroupType)
  all_CatalogueCategory = graphene.List(CatalogueCategoryType)
  all_CatalogueOption = graphene.List(CatalogueOptionType)
  all_CatalogueProduct = graphene.List(CatalogueProductType)
  all_CatalogueProductattribute = graphene.List(CatalogueProductattributeType)
  all_CatalogueProductattributevalue = graphene.List(CatalogueProductattributevalueType)
  all_CatalogueProductattributevalueValueMultiOption = graphene.List(CatalogueProductattributevalueValueMultiOptionType)
  all_CatalogueProductcategory = graphene.List(CatalogueProductcategoryType)
  all_CatalogueProductclass = graphene.List(CatalogueProductclassType)
  all_CatalogueProductclassOptions = graphene.List(CatalogueProductclassOptionsType)
  all_CatalogueProductimage = graphene.List(CatalogueProductimageType)
  all_CatalogueProductProductOptions = graphene.List(CatalogueProductProductOptionsType)
  all_CatalogueProductrecommendation = graphene.List(CatalogueProductrecommendationType)
  all_CmsAliaspluginmodel = graphene.List(CmsAliaspluginmodelType)
  all_CmsCmsplugin = graphene.List(CmsCmspluginType)
  all_CmsGlobalpagepermission = graphene.List(CmsGlobalpagepermissionType)
  all_CmsGlobalpagepermissionSites = graphene.List(CmsGlobalpagepermissionSitesType)
  all_CmsPage = graphene.List(CmsPageType)
  all_CmsPagepermission = graphene.List(CmsPagepermissionType)
  all_CmsPagePlaceholders = graphene.List(CmsPagePlaceholdersType)
  all_CmsPageuser = graphene.List(CmsPageuserType)
  all_CmsPageusergroup = graphene.List(CmsPageusergroupType)
  all_CmsPlaceholder = graphene.List(CmsPlaceholderType)
  all_CmsPlaceholderreference = graphene.List(CmsPlaceholderreferenceType)
  all_CmsStaticplaceholder = graphene.List(CmsStaticplaceholderType)
  all_CmsTitle = graphene.List(CmsTitleType)
  all_CmsTreenode = graphene.List(CmsTreenodeType)
  all_CmsUrlconfrevision = graphene.List(CmsUrlconfrevisionType)
  all_CmsUsersettings = graphene.List(CmsUsersettingsType)
  all_CommunicationCommunicationeventtype = graphene.List(CommunicationCommunicationeventtypeType)
  all_CommunicationEmail = graphene.List(CommunicationEmailType)
  all_CommunicationNotification = graphene.List(CommunicationNotificationType)
  all_CustomerProductalert = graphene.List(CustomerProductalertType)
  all_DjangoAdminLog = graphene.List(DjangoAdminLogType)
  all_DjangocmsBlogAuthorentriesplugin = graphene.List(DjangocmsBlogAuthorentriespluginType)
  all_DjangocmsBlogAuthorentriespluginAuthors = graphene.List(DjangocmsBlogAuthorentriespluginAuthorsType)
  all_DjangocmsBlogBlogcategory = graphene.List(DjangocmsBlogBlogcategoryType)
  all_DjangocmsBlogBlogcategoryTranslation = graphene.List(DjangocmsBlogBlogcategoryTranslationType)
  all_DjangocmsBlogBlogconfig = graphene.List(DjangocmsBlogBlogconfigType)
  all_DjangocmsBlogBlogconfigTranslation = graphene.List(DjangocmsBlogBlogconfigTranslationType)
  all_DjangocmsBlogGenericblogplugin = graphene.List(DjangocmsBlogGenericblogpluginType)
  all_DjangocmsBlogLatestpostsplugin = graphene.List(DjangocmsBlogLatestpostspluginType)
  all_DjangocmsBlogLatestpostspluginCategories = graphene.List(DjangocmsBlogLatestpostspluginCategoriesType)
  all_DjangocmsBlogPost = graphene.List(DjangocmsBlogPostType)
  all_DjangocmsBlogPostCategories = graphene.List(DjangocmsBlogPostCategoriesType)
  all_DjangocmsBlogPostRelated = graphene.List(DjangocmsBlogPostRelatedType)
  all_DjangocmsBlogPostSites = graphene.List(DjangocmsBlogPostSitesType)
  all_DjangocmsBlogPostTranslation = graphene.List(DjangocmsBlogPostTranslationType)
  all_DjangocmsFileFile = graphene.List(DjangocmsFileFileType)
  all_DjangocmsFileFolder = graphene.List(DjangocmsFileFolderType)
  all_DjangocmsGooglemapGooglemap = graphene.List(DjangocmsGooglemapGooglemapType)
  all_DjangocmsGooglemapGooglemapmarker = graphene.List(DjangocmsGooglemapGooglemapmarkerType)
  all_DjangocmsGooglemapGooglemaproute = graphene.List(DjangocmsGooglemapGooglemaprouteType)
  all_DjangocmsHistoryPlaceholderaction = graphene.List(DjangocmsHistoryPlaceholderactionType)
  all_DjangocmsHistoryPlaceholderoperation = graphene.List(DjangocmsHistoryPlaceholderoperationType)
  all_DjangocmsIconIcon = graphene.List(DjangocmsIconIconType)
  all_DjangocmsLinkLink = graphene.List(DjangocmsLinkLinkType)
  all_DjangocmsMapsMaps = graphene.List(DjangocmsMapsMapsType)
  all_DjangocmsPicturePicture = graphene.List(DjangocmsPicturePictureType)
  all_DjangocmsStyleStyle = graphene.List(DjangocmsStyleStyleType)
  all_DjangocmsTextCkeditorText = graphene.List(DjangocmsTextCkeditorTextType)
  all_DjangocmsVideoVideoplayer = graphene.List(DjangocmsVideoVideoplayerType)
  all_DjangocmsVideoVideosource = graphene.List(DjangocmsVideoVideosourceType)
  all_DjangocmsVideoVideotrack = graphene.List(DjangocmsVideoVideotrackType)
  all_DjangoContent = graphene.List(DjangoContentType)
  all_DjangoFlatpage = graphene.List(DjangoFlatpageType)
  all_DjangoFlatpageSites = graphene.List(DjangoFlatpageSitesType)
  all_DjangoMigrations = graphene.List(DjangoMigrationsType)
  all_DjangoSession = graphene.List(DjangoSessionType)
  all_DjangoSite = graphene.List(DjangoSiteType)
  all_EasyThumbnailsSource = graphene.List(EasyThumbnailsSourceType)
  all_EasyThumbnailsThumbnail = graphene.List(EasyThumbnailsThumbnailType)
  all_EasyThumbnailsThumbnaildimensions = graphene.List(EasyThumbnailsThumbnaildimensionsType)
  all_FilerClipboard = graphene.List(FilerClipboardType)
  all_FilerClipboarditem = graphene.List(FilerClipboarditemType)
  all_FilerFile = graphene.List(FilerFileType)
  all_FilerFolder = graphene.List(FilerFolderType)
  all_FilerFolderpermission = graphene.List(FilerFolderpermissionType)
  all_FilerImage = graphene.List(FilerImageType)
  all_FilerThumbnailoption = graphene.List(FilerThumbnailoptionType)
  all_MenusCachekey = graphene.List(MenusCachekeyType)
  all_OfferBenefit = graphene.List(OfferBenefitType)
  all_OfferCondition = graphene.List(OfferConditionType)
  all_OfferConditionaloffer = graphene.List(OfferConditionalofferType)
  all_OfferConditionalofferCombinations = graphene.List(OfferConditionalofferCombinationsType)
  all_OfferRange = graphene.List(OfferRangeType)
  all_OfferRangeClasses = graphene.List(OfferRangeClassesType)
  all_OfferRangeExcludedProducts = graphene.List(OfferRangeExcludedProductsType)
  all_OfferRangeIncludedCategories = graphene.List(OfferRangeIncludedCategoriesType)
  all_OfferRangeproduct = graphene.List(OfferRangeproductType)
  all_OfferRangeproductfileupload = graphene.List(OfferRangeproductfileuploadType)
  all_OrderBillingaddress = graphene.List(OrderBillingaddressType)
  all_OrderCommunicationevent = graphene.List(OrderCommunicationeventType)
  all_OrderLine = graphene.List(OrderLineType)
  all_OrderLineattribute = graphene.List(OrderLineattributeType)
  all_OrderLineprice = graphene.List(OrderLinepriceType)
  all_OrderOrder = graphene.List(OrderOrderType)
  all_OrderOrderdiscount = graphene.List(OrderOrderdiscountType)
  all_OrderOrdernote = graphene.List(OrderOrdernoteType)
  all_OrderOrderstatuschange = graphene.List(OrderOrderstatuschangeType)
  all_OrderPaymentevent = graphene.List(OrderPaymenteventType)
  all_OrderPaymenteventquantity = graphene.List(OrderPaymenteventquantityType)
  all_OrderPaymenteventtype = graphene.List(OrderPaymenteventtypeType)
  all_OrderShippingaddress = graphene.List(OrderShippingaddressType)
  all_OrderShippingevent = graphene.List(OrderShippingeventType)
  all_OrderShippingeventquantity = graphene.List(OrderShippingeventquantityType)
  all_OrderShippingeventtype = graphene.List(OrderShippingeventtypeType)
  all_OrderSurcharge = graphene.List(OrderSurchargeType)
  all_OscarapiApikey = graphene.List(OscarapiApikeyType)
  all_OscarInvoicesInvoice = graphene.List(OscarInvoicesInvoiceType)
  all_OscarInvoicesLegalentity = graphene.List(OscarInvoicesLegalentityType)
  all_OscarInvoicesLegalentityaddress = graphene.List(OscarInvoicesLegalentityaddressType)
  all_PartnerPartner = graphene.List(PartnerPartnerType)
  all_PartnerPartneraddress = graphene.List(PartnerPartneraddressType)
  all_PartnerPartnerUsers = graphene.List(PartnerPartnerUsersType)
  all_PartnerStockalert = graphene.List(PartnerStockalertType)
  all_PartnerStockrecord = graphene.List(PartnerStockrecordType)
  all_PaymentBankcard = graphene.List(PaymentBankcardType)
  all_PaymentSource = graphene.List(PaymentSourceType)
  all_PaymentSourcetype = graphene.List(PaymentSourcetypeType)
  all_PaymentTransaction = graphene.List(PaymentTransactionType)
  all_PaypalExpresstransaction = graphene.List(PaypalExpresstransactionType)
  all_PaypalPayflowtransaction = graphene.List(PaypalPayflowtransactionType)
  all_PhotologueGallery = graphene.List(PhotologueGalleryType)
  all_PhotologueGalleryPhotos = graphene.List(PhotologueGalleryPhotosType)
  all_PhotologueGallerySites = graphene.List(PhotologueGallerySitesType)
  all_PhotologuePhoto = graphene.List(PhotologuePhotoType)
  all_PhotologuePhotoeffect = graphene.List(PhotologuePhotoeffectType)
  all_PhotologuePhotoSites = graphene.List(PhotologuePhotoSitesType)
  all_PhotologuePhotosize = graphene.List(PhotologuePhotosizeType)
  all_PhotologueWatermark = graphene.List(PhotologueWatermarkType)
  all_PinaxBadgesBadgeaward = graphene.List(PinaxBadgesBadgeawardType)
  all_PinaxEventsEvent = graphene.List(PinaxEventsEventType)
  all_PinaxMessagesMessage = graphene.List(PinaxMessagesMessageType)
  all_PinaxMessagesThread = graphene.List(PinaxMessagesThreadType)
  all_PinaxMessagesUserthread = graphene.List(PinaxMessagesUserthreadType)
  all_ReviewsProductreview = graphene.List(ReviewsProductreviewType)
  all_ReviewsVote = graphene.List(ReviewsVoteType)
  all_ShippingOrderanditemcharges = graphene.List(ShippingOrderanditemchargesType)
  all_ShippingOrderanditemchargesCountries = graphene.List(ShippingOrderanditemchargesCountriesType)
  all_ShippingWeightband = graphene.List(ShippingWeightbandType)
  all_ShippingWeightbased = graphene.List(ShippingWeightbasedType)
  all_ShippingWeightbasedCountries = graphene.List(ShippingWeightbasedCountriesType)
  all_TaggitTag = graphene.List(TaggitTagType)
  all_TaggitTaggeditem = graphene.List(TaggitTaggeditemType)
  all_TestimonialsTestimonial = graphene.List(TestimonialsTestimonialType)
  all_ThumbnailKvstore = graphene.List(ThumbnailKvstoreType)
  all_VoucherVoucher = graphene.List(VoucherVoucherType)
  all_VoucherVoucherapplication = graphene.List(VoucherVoucherapplicationType)
  all_VoucherVoucherOffers = graphene.List(VoucherVoucherOffersType)
  all_VoucherVoucherset = graphene.List(VoucherVouchersetType)
  all_WishlistsLine = graphene.List(WishlistsLineType)
  all_WishlistsWishlist = graphene.List(WishlistsWishlistType)

  def resolve_all_AddressCountry(root, info):		
     return AddressCountry.objects.select_related("AddressCountry").all()

  def resolve_all_AddressUseraddress(root, info):		
     return AddressUseraddress.objects.select_related("AddressUseraddress").all()

  def resolve_all_AdvancedFiltersAdvancedfilter(root, info):		
     return AdvancedFiltersAdvancedfilter.objects.select_related("AdvancedFiltersAdvancedfilter").all()

  def resolve_all_AdvancedFiltersAdvancedfilterGroups(root, info):		
     return AdvancedFiltersAdvancedfilterGroups.objects.select_related("AdvancedFiltersAdvancedfilterGroups").all()

  def resolve_all_AdvancedFiltersAdvancedfilterUsers(root, info):		
     return AdvancedFiltersAdvancedfilterUsers.objects.select_related("AdvancedFiltersAdvancedfilterUsers").all()

  def resolve_all_AnalyticsProductrecord(root, info):		
     return AnalyticsProductrecord.objects.select_related("AnalyticsProductrecord").all()

  def resolve_all_AnalyticsUserproductview(root, info):		
     return AnalyticsUserproductview.objects.select_related("AnalyticsUserproductview").all()

  def resolve_all_AnalyticsUserrecord(root, info):		
     return AnalyticsUserrecord.objects.select_related("AnalyticsUserrecord").all()

  def resolve_all_AnalyticsUsersearch(root, info):		
     return AnalyticsUsersearch.objects.select_related("AnalyticsUsersearch").all()

  def resolve_all_AnnouncementsAnnouncement(root, info):		
     return AnnouncementsAnnouncement.objects.select_related("AnnouncementsAnnouncement").all()

  def resolve_all_AnnouncementsDismissal(root, info):		
     return AnnouncementsDismissal.objects.select_related("AnnouncementsDismissal").all()

  def resolve_all_AuthGroup(root, info):		
     return AuthGroup.objects.select_related("AuthGroup").all()

  def resolve_all_AuthGroupPermissions(root, info):		
     return AuthGroupPermissions.objects.select_related("AuthGroupPermissions").all()

  def resolve_all_AuthPermission(root, info):		
     return AuthPermission.objects.select_related("AuthPermission").all()

  def resolve_all_AuthUser(root, info):		
     return AuthUser.objects.select_related("AuthUser").all()

  def resolve_all_AuthUserGroups(root, info):		
     return AuthUserGroups.objects.select_related("AuthUserGroups").all()

  def resolve_all_AuthUserUserPermissions(root, info):		
     return AuthUserUserPermissions.objects.select_related("AuthUserUserPermissions").all()

  def resolve_all_BasketBasket(root, info):		
     return BasketBasket.objects.select_related("BasketBasket").all()

  def resolve_all_BasketBasketVouchers(root, info):		
     return BasketBasketVouchers.objects.select_related("BasketBasketVouchers").all()

  def resolve_all_BasketLine(root, info):		
     return BasketLine.objects.select_related("BasketLine").all()

  def resolve_all_BasketLineattribute(root, info):		
     return BasketLineattribute.objects.select_related("BasketLineattribute").all()

  def resolve_all_Bootstrap4AlertsBootstrap4Alerts(root, info):		
     return Bootstrap4AlertsBootstrap4Alerts.objects.select_related("Bootstrap4AlertsBootstrap4Alerts").all()

  def resolve_all_Bootstrap4BadgeBootstrap4Badge(root, info):		
     return Bootstrap4BadgeBootstrap4Badge.objects.select_related("Bootstrap4BadgeBootstrap4Badge").all()

  def resolve_all_Bootstrap4CardBootstrap4Card(root, info):		
     return Bootstrap4CardBootstrap4Card.objects.select_related("Bootstrap4CardBootstrap4Card").all()

  def resolve_all_Bootstrap4CardBootstrap4Cardinner(root, info):		
     return Bootstrap4CardBootstrap4Cardinner.objects.select_related("Bootstrap4CardBootstrap4Cardinner").all()

  def resolve_all_Bootstrap4CarouselBootstrap4Carousel(root, info):		
     return Bootstrap4CarouselBootstrap4Carousel.objects.select_related("Bootstrap4CarouselBootstrap4Carousel").all()

  def resolve_all_Bootstrap4CarouselBootstrap4Carouselslide(root, info):		
     return Bootstrap4CarouselBootstrap4Carouselslide.objects.select_related("Bootstrap4CarouselBootstrap4Carouselslide").all()

  def resolve_all_Bootstrap4CollapseBootstrap4Collapse(root, info):		
     return Bootstrap4CollapseBootstrap4Collapse.objects.select_related("Bootstrap4CollapseBootstrap4Collapse").all()

  def resolve_all_Bootstrap4CollapseBootstrap4Collapsecontainer(root, info):		
     return Bootstrap4CollapseBootstrap4Collapsecontainer.objects.select_related("Bootstrap4CollapseBootstrap4Collapsecontainer").all()

  def resolve_all_Bootstrap4CollapseBootstrap4Collapsetrigger(root, info):		
     return Bootstrap4CollapseBootstrap4Collapsetrigger.objects.select_related("Bootstrap4CollapseBootstrap4Collapsetrigger").all()

  def resolve_all_Bootstrap4ContentBootstrap4Blockquote(root, info):		
     return Bootstrap4ContentBootstrap4Blockquote.objects.select_related("Bootstrap4ContentBootstrap4Blockquote").all()

  def resolve_all_Bootstrap4ContentBootstrap4Code(root, info):		
     return Bootstrap4ContentBootstrap4Code.objects.select_related("Bootstrap4ContentBootstrap4Code").all()

  def resolve_all_Bootstrap4ContentBootstrap4Figure(root, info):		
     return Bootstrap4ContentBootstrap4Figure.objects.select_related("Bootstrap4ContentBootstrap4Figure").all()

  def resolve_all_Bootstrap4GridBootstrap4Gridcolumn(root, info):		
     return Bootstrap4GridBootstrap4Gridcolumn.objects.select_related("Bootstrap4GridBootstrap4Gridcolumn").all()

  def resolve_all_Bootstrap4GridBootstrap4Gridcontainer(root, info):		
     return Bootstrap4GridBootstrap4Gridcontainer.objects.select_related("Bootstrap4GridBootstrap4Gridcontainer").all()

  def resolve_all_Bootstrap4GridBootstrap4Gridrow(root, info):		
     return Bootstrap4GridBootstrap4Gridrow.objects.select_related("Bootstrap4GridBootstrap4Gridrow").all()

  def resolve_all_Bootstrap4JumbotronBootstrap4Jumbotron(root, info):		
     return Bootstrap4JumbotronBootstrap4Jumbotron.objects.select_related("Bootstrap4JumbotronBootstrap4Jumbotron").all()

  def resolve_all_Bootstrap4LinkBootstrap4Link(root, info):		
     return Bootstrap4LinkBootstrap4Link.objects.select_related("Bootstrap4LinkBootstrap4Link").all()

  def resolve_all_Bootstrap4ListgroupBootstrap4Listgroup(root, info):		
     return Bootstrap4ListgroupBootstrap4Listgroup.objects.select_related("Bootstrap4ListgroupBootstrap4Listgroup").all()

  def resolve_all_Bootstrap4ListgroupBootstrap4Listgroupitem(root, info):		
     return Bootstrap4ListgroupBootstrap4Listgroupitem.objects.select_related("Bootstrap4ListgroupBootstrap4Listgroupitem").all()

  def resolve_all_Bootstrap4MediaBootstrap4Media(root, info):		
     return Bootstrap4MediaBootstrap4Media.objects.select_related("Bootstrap4MediaBootstrap4Media").all()

  def resolve_all_Bootstrap4MediaBootstrap4Mediabody(root, info):		
     return Bootstrap4MediaBootstrap4Mediabody.objects.select_related("Bootstrap4MediaBootstrap4Mediabody").all()

  def resolve_all_Bootstrap4PictureBootstrap4Picture(root, info):		
     return Bootstrap4PictureBootstrap4Picture.objects.select_related("Bootstrap4PictureBootstrap4Picture").all()

  def resolve_all_Bootstrap4TabsBootstrap4Tab(root, info):		
     return Bootstrap4TabsBootstrap4Tab.objects.select_related("Bootstrap4TabsBootstrap4Tab").all()

  def resolve_all_Bootstrap4TabsBootstrap4Tabitem(root, info):		
     return Bootstrap4TabsBootstrap4Tabitem.objects.select_related("Bootstrap4TabsBootstrap4Tabitem").all()

  def resolve_all_Bootstrap4UtilitiesBootstrap4Spacing(root, info):		
     return Bootstrap4UtilitiesBootstrap4Spacing.objects.select_related("Bootstrap4UtilitiesBootstrap4Spacing").all()

  def resolve_all_CatalogueAttributeoption(root, info):		
     return CatalogueAttributeoption.objects.select_related("CatalogueAttributeoption").all()

  def resolve_all_CatalogueAttributeoptiongroup(root, info):		
     return CatalogueAttributeoptiongroup.objects.select_related("CatalogueAttributeoptiongroup").all()

  def resolve_all_CatalogueCategory(root, info):		
     return CatalogueCategory.objects.select_related("CatalogueCategory").all()

  def resolve_all_CatalogueOption(root, info):		
     return CatalogueOption.objects.select_related("CatalogueOption").all()

  def resolve_all_CatalogueProduct(root, info):		
     return CatalogueProduct.objects.select_related("CatalogueProduct").all()

  def resolve_all_CatalogueProductattribute(root, info):		
     return CatalogueProductattribute.objects.select_related("CatalogueProductattribute").all()

  def resolve_all_CatalogueProductattributevalue(root, info):		
     return CatalogueProductattributevalue.objects.select_related("CatalogueProductattributevalue").all()

  def resolve_all_CatalogueProductattributevalueValueMultiOption(root, info):		
     return CatalogueProductattributevalueValueMultiOption.objects.select_related("CatalogueProductattributevalueValueMultiOption").all()

  def resolve_all_CatalogueProductcategory(root, info):		
     return CatalogueProductcategory.objects.select_related("CatalogueProductcategory").all()

  def resolve_all_CatalogueProductclass(root, info):		
     return CatalogueProductclass.objects.select_related("CatalogueProductclass").all()

  def resolve_all_CatalogueProductclassOptions(root, info):		
     return CatalogueProductclassOptions.objects.select_related("CatalogueProductclassOptions").all()

  def resolve_all_CatalogueProductimage(root, info):		
     return CatalogueProductimage.objects.select_related("CatalogueProductimage").all()

  def resolve_all_CatalogueProductProductOptions(root, info):		
     return CatalogueProductProductOptions.objects.select_related("CatalogueProductProductOptions").all()

  def resolve_all_CatalogueProductrecommendation(root, info):		
     return CatalogueProductrecommendation.objects.select_related("CatalogueProductrecommendation").all()

  def resolve_all_Client(root, info):		
     return Client.objects.select_related("Client").all()

  def resolve_all_CmsAliaspluginmodel(root, info):		
     return CmsAliaspluginmodel.objects.select_related("CmsAliaspluginmodel").all()

  def resolve_all_CmsCmsplugin(root, info):		
     return CmsCmsplugin.objects.select_related("CmsCmsplugin").all()

  def resolve_all_CmsGlobalpagepermission(root, info):		
     return CmsGlobalpagepermission.objects.select_related("CmsGlobalpagepermission").all()

  def resolve_all_CmsGlobalpagepermissionSites(root, info):		
     return CmsGlobalpagepermissionSites.objects.select_related("CmsGlobalpagepermissionSites").all()

  def resolve_all_CmsPage(root, info):		
     return CmsPage.objects.select_related("CmsPage").all()

  def resolve_all_CmsPagepermission(root, info):		
     return CmsPagepermission.objects.select_related("CmsPagepermission").all()

  def resolve_all_CmsPagePlaceholders(root, info):		
     return CmsPagePlaceholders.objects.select_related("CmsPagePlaceholders").all()

  def resolve_all_CmsPageuser(root, info):		
     return CmsPageuser.objects.select_related("CmsPageuser").all()

  def resolve_all_CmsPageusergroup(root, info):		
     return CmsPageusergroup.objects.select_related("CmsPageusergroup").all()

  def resolve_all_CmsPlaceholder(root, info):		
     return CmsPlaceholder.objects.select_related("CmsPlaceholder").all()

  def resolve_all_CmsPlaceholderreference(root, info):		
     return CmsPlaceholderreference.objects.select_related("CmsPlaceholderreference").all()

  def resolve_all_CmsStaticplaceholder(root, info):		
     return CmsStaticplaceholder.objects.select_related("CmsStaticplaceholder").all()

  def resolve_all_CmsTitle(root, info):		
     return CmsTitle.objects.select_related("CmsTitle").all()

  def resolve_all_CmsTreenode(root, info):		
     return CmsTreenode.objects.select_related("CmsTreenode").all()

  def resolve_all_CmsUrlconfrevision(root, info):		
     return CmsUrlconfrevision.objects.select_related("CmsUrlconfrevision").all()

  def resolve_all_CmsUsersettings(root, info):		
     return CmsUsersettings.objects.select_related("CmsUsersettings").all()

  def resolve_all_CommunicationCommunicationeventtype(root, info):		
     return CommunicationCommunicationeventtype.objects.select_related("CommunicationCommunicationeventtype").all()

  def resolve_all_CommunicationEmail(root, info):		
     return CommunicationEmail.objects.select_related("CommunicationEmail").all()

  def resolve_all_CommunicationNotification(root, info):		
     return CommunicationNotification.objects.select_related("CommunicationNotification").all()

  def resolve_all_CustomerProductalert(root, info):		
     return CustomerProductalert.objects.select_related("CustomerProductalert").all()

  def resolve_all_DjangoAdminLog(root, info):		
     return DjangoAdminLog.objects.select_related("DjangoAdminLog").all()

  def resolve_all_DjangocmsBlogAuthorentriesplugin(root, info):		
     return DjangocmsBlogAuthorentriesplugin.objects.select_related("DjangocmsBlogAuthorentriesplugin").all()

  def resolve_all_DjangocmsBlogAuthorentriespluginAuthors(root, info):		
     return DjangocmsBlogAuthorentriespluginAuthors.objects.select_related("DjangocmsBlogAuthorentriespluginAuthors").all()

  def resolve_all_DjangocmsBlogBlogcategory(root, info):		
     return DjangocmsBlogBlogcategory.objects.select_related("DjangocmsBlogBlogcategory").all()

  def resolve_all_DjangocmsBlogBlogcategoryTranslation(root, info):		
     return DjangocmsBlogBlogcategoryTranslation.objects.select_related("DjangocmsBlogBlogcategoryTranslation").all()

  def resolve_all_DjangocmsBlogBlogconfig(root, info):		
     return DjangocmsBlogBlogconfig.objects.select_related("DjangocmsBlogBlogconfig").all()

  def resolve_all_DjangocmsBlogBlogconfigTranslation(root, info):		
     return DjangocmsBlogBlogconfigTranslation.objects.select_related("DjangocmsBlogBlogconfigTranslation").all()

  def resolve_all_DjangocmsBlogGenericblogplugin(root, info):		
     return DjangocmsBlogGenericblogplugin.objects.select_related("DjangocmsBlogGenericblogplugin").all()

  def resolve_all_DjangocmsBlogLatestpostsplugin(root, info):		
     return DjangocmsBlogLatestpostsplugin.objects.select_related("DjangocmsBlogLatestpostsplugin").all()

  def resolve_all_DjangocmsBlogLatestpostspluginCategories(root, info):		
     return DjangocmsBlogLatestpostspluginCategories.objects.select_related("DjangocmsBlogLatestpostspluginCategories").all()

  def resolve_all_DjangocmsBlogPost(root, info):		
     return DjangocmsBlogPost.objects.select_related("DjangocmsBlogPost").all()

  def resolve_all_DjangocmsBlogPostCategories(root, info):		
     return DjangocmsBlogPostCategories.objects.select_related("DjangocmsBlogPostCategories").all()

  def resolve_all_DjangocmsBlogPostRelated(root, info):		
     return DjangocmsBlogPostRelated.objects.select_related("DjangocmsBlogPostRelated").all()

  def resolve_all_DjangocmsBlogPostSites(root, info):		
     return DjangocmsBlogPostSites.objects.select_related("DjangocmsBlogPostSites").all()

  def resolve_all_DjangocmsBlogPostTranslation(root, info):		
     return DjangocmsBlogPostTranslation.objects.select_related("DjangocmsBlogPostTranslation").all()

  def resolve_all_DjangocmsFileFile(root, info):		
     return DjangocmsFileFile.objects.select_related("DjangocmsFileFile").all()

  def resolve_all_DjangocmsFileFolder(root, info):		
     return DjangocmsFileFolder.objects.select_related("DjangocmsFileFolder").all()

  def resolve_all_DjangocmsGooglemapGooglemap(root, info):		
     return DjangocmsGooglemapGooglemap.objects.select_related("DjangocmsGooglemapGooglemap").all()

  def resolve_all_DjangocmsGooglemapGooglemapmarker(root, info):		
     return DjangocmsGooglemapGooglemapmarker.objects.select_related("DjangocmsGooglemapGooglemapmarker").all()

  def resolve_all_DjangocmsGooglemapGooglemaproute(root, info):		
     return DjangocmsGooglemapGooglemaproute.objects.select_related("DjangocmsGooglemapGooglemaproute").all()

  def resolve_all_DjangocmsHistoryPlaceholderaction(root, info):		
     return DjangocmsHistoryPlaceholderaction.objects.select_related("DjangocmsHistoryPlaceholderaction").all()

  def resolve_all_DjangocmsHistoryPlaceholderoperation(root, info):		
     return DjangocmsHistoryPlaceholderoperation.objects.select_related("DjangocmsHistoryPlaceholderoperation").all()

  def resolve_all_DjangocmsIconIcon(root, info):		
     return DjangocmsIconIcon.objects.select_related("DjangocmsIconIcon").all()

  def resolve_all_DjangocmsLinkLink(root, info):		
     return DjangocmsLinkLink.objects.select_related("DjangocmsLinkLink").all()

  def resolve_all_DjangocmsMapsMaps(root, info):		
     return DjangocmsMapsMaps.objects.select_related("DjangocmsMapsMaps").all()

  def resolve_all_DjangocmsPicturePicture(root, info):		
     return DjangocmsPicturePicture.objects.select_related("DjangocmsPicturePicture").all()

  def resolve_all_DjangocmsStyleStyle(root, info):		
     return DjangocmsStyleStyle.objects.select_related("DjangocmsStyleStyle").all()

  def resolve_all_DjangocmsTextCkeditorText(root, info):		
     return DjangocmsTextCkeditorText.objects.select_related("DjangocmsTextCkeditorText").all()

  def resolve_all_DjangocmsVideoVideoplayer(root, info):		
     return DjangocmsVideoVideoplayer.objects.select_related("DjangocmsVideoVideoplayer").all()

  def resolve_all_DjangocmsVideoVideosource(root, info):		
     return DjangocmsVideoVideosource.objects.select_related("DjangocmsVideoVideosource").all()

  def resolve_all_DjangocmsVideoVideotrack(root, info):		
     return DjangocmsVideoVideotrack.objects.select_related("DjangocmsVideoVideotrack").all()

  def resolve_all_DjangoContent(root, info):		
     return DjangoContent.objects.select_related("DjangoContent").all()

  def resolve_all_DjangoFlatpage(root, info):		
     return DjangoFlatpage.objects.select_related("DjangoFlatpage").all()

  def resolve_all_DjangoFlatpageSites(root, info):		
     return DjangoFlatpageSites.objects.select_related("DjangoFlatpageSites").all()

  def resolve_all_DjangoMigrations(root, info):		
     return DjangoMigrations.objects.select_related("DjangoMigrations").all()

  def resolve_all_DjangoSession(root, info):		
     return DjangoSession.objects.select_related("DjangoSession").all()

  def resolve_all_DjangoSite(root, info):		
     return DjangoSite.objects.select_related("DjangoSite").all()

  def resolve_all_EasyThumbnailsSource(root, info):		
     return EasyThumbnailsSource.objects.select_related("EasyThumbnailsSource").all()

  def resolve_all_EasyThumbnailsThumbnail(root, info):		
     return EasyThumbnailsThumbnail.objects.select_related("EasyThumbnailsThumbnail").all()

  def resolve_all_EasyThumbnailsThumbnaildimensions(root, info):		
     return EasyThumbnailsThumbnaildimensions.objects.select_related("EasyThumbnailsThumbnaildimensions").all()

  def resolve_all_FilerClipboard(root, info):		
     return FilerClipboard.objects.select_related("FilerClipboard").all()

  def resolve_all_FilerClipboarditem(root, info):		
     return FilerClipboarditem.objects.select_related("FilerClipboarditem").all()

  def resolve_all_FilerFile(root, info):		
     return FilerFile.objects.select_related("FilerFile").all()

  def resolve_all_FilerFolder(root, info):		
     return FilerFolder.objects.select_related("FilerFolder").all()

  def resolve_all_FilerFolderpermission(root, info):		
     return FilerFolderpermission.objects.select_related("FilerFolderpermission").all()

  def resolve_all_FilerImage(root, info):		
     return FilerImage.objects.select_related("FilerImage").all()

  def resolve_all_FilerThumbnailoption(root, info):		
     return FilerThumbnailoption.objects.select_related("FilerThumbnailoption").all()

  def resolve_all_MenusCachekey(root, info):		
     return MenusCachekey.objects.select_related("MenusCachekey").all()

  def resolve_all_OfferBenefit(root, info):		
     return OfferBenefit.objects.select_related("OfferBenefit").all()

  def resolve_all_OfferCondition(root, info):		
     return OfferCondition.objects.select_related("OfferCondition").all()

  def resolve_all_OfferConditionaloffer(root, info):		
     return OfferConditionaloffer.objects.select_related("OfferConditionaloffer").all()

  def resolve_all_OfferConditionalofferCombinations(root, info):		
     return OfferConditionalofferCombinations.objects.select_related("OfferConditionalofferCombinations").all()

  def resolve_all_OfferRange(root, info):		
     return OfferRange.objects.select_related("OfferRange").all()

  def resolve_all_OfferRangeClasses(root, info):		
     return OfferRangeClasses.objects.select_related("OfferRangeClasses").all()

  def resolve_all_OfferRangeExcludedProducts(root, info):		
     return OfferRangeExcludedProducts.objects.select_related("OfferRangeExcludedProducts").all()

  def resolve_all_OfferRangeIncludedCategories(root, info):		
     return OfferRangeIncludedCategories.objects.select_related("OfferRangeIncludedCategories").all()

  def resolve_all_OfferRangeproduct(root, info):		
     return OfferRangeproduct.objects.select_related("OfferRangeproduct").all()

  def resolve_all_OfferRangeproductfileupload(root, info):		
     return OfferRangeproductfileupload.objects.select_related("OfferRangeproductfileupload").all()

  def resolve_all_OrderBillingaddress(root, info):		
     return OrderBillingaddress.objects.select_related("OrderBillingaddress").all()

  def resolve_all_OrderCommunicationevent(root, info):		
     return OrderCommunicationevent.objects.select_related("OrderCommunicationevent").all()

  def resolve_all_OrderLine(root, info):		
     return OrderLine.objects.select_related("OrderLine").all()

  def resolve_all_OrderLineattribute(root, info):		
     return OrderLineattribute.objects.select_related("OrderLineattribute").all()

  def resolve_all_OrderLineprice(root, info):		
     return OrderLineprice.objects.select_related("OrderLineprice").all()

  def resolve_all_OrderOrder(root, info):		
     return OrderOrder.objects.select_related("OrderOrder").all()

  def resolve_all_OrderOrderdiscount(root, info):		
     return OrderOrderdiscount.objects.select_related("OrderOrderdiscount").all()

  def resolve_all_OrderOrdernote(root, info):		
     return OrderOrdernote.objects.select_related("OrderOrdernote").all()

  def resolve_all_OrderOrderstatuschange(root, info):		
     return OrderOrderstatuschange.objects.select_related("OrderOrderstatuschange").all()

  def resolve_all_OrderPaymentevent(root, info):		
     return OrderPaymentevent.objects.select_related("OrderPaymentevent").all()

  def resolve_all_OrderPaymenteventquantity(root, info):		
     return OrderPaymenteventquantity.objects.select_related("OrderPaymenteventquantity").all()

  def resolve_all_OrderPaymenteventtype(root, info):		
     return OrderPaymenteventtype.objects.select_related("OrderPaymenteventtype").all()

  def resolve_all_OrderShippingaddress(root, info):		
     return OrderShippingaddress.objects.select_related("OrderShippingaddress").all()

  def resolve_all_OrderShippingevent(root, info):		
     return OrderShippingevent.objects.select_related("OrderShippingevent").all()

  def resolve_all_OrderShippingeventquantity(root, info):		
     return OrderShippingeventquantity.objects.select_related("OrderShippingeventquantity").all()

  def resolve_all_OrderShippingeventtype(root, info):		
     return OrderShippingeventtype.objects.select_related("OrderShippingeventtype").all()

  def resolve_all_OrderSurcharge(root, info):		
     return OrderSurcharge.objects.select_related("OrderSurcharge").all()

  def resolve_all_OscarapiApikey(root, info):		
     return OscarapiApikey.objects.select_related("OscarapiApikey").all()

  def resolve_all_OscarInvoicesInvoice(root, info):		
     return OscarInvoicesInvoice.objects.select_related("OscarInvoicesInvoice").all()

  def resolve_all_OscarInvoicesLegalentity(root, info):		
     return OscarInvoicesLegalentity.objects.select_related("OscarInvoicesLegalentity").all()

  def resolve_all_OscarInvoicesLegalentityaddress(root, info):		
     return OscarInvoicesLegalentityaddress.objects.select_related("OscarInvoicesLegalentityaddress").all()

  def resolve_all_PartnerPartner(root, info):		
     return PartnerPartner.objects.select_related("PartnerPartner").all()

  def resolve_all_PartnerPartneraddress(root, info):		
     return PartnerPartneraddress.objects.select_related("PartnerPartneraddress").all()

  def resolve_all_PartnerPartnerUsers(root, info):		
     return PartnerPartnerUsers.objects.select_related("PartnerPartnerUsers").all()

  def resolve_all_PartnerStockalert(root, info):		
     return PartnerStockalert.objects.select_related("PartnerStockalert").all()

  def resolve_all_PartnerStockrecord(root, info):		
     return PartnerStockrecord.objects.select_related("PartnerStockrecord").all()

  def resolve_all_Payment(root, info):		
     return Payment.objects.select_related("Payment").all()

  def resolve_all_PaymentBankcard(root, info):		
     return PaymentBankcard.objects.select_related("PaymentBankcard").all()

  def resolve_all_PaymentSource(root, info):		
     return PaymentSource.objects.select_related("PaymentSource").all()

  def resolve_all_PaymentSourcetype(root, info):		
     return PaymentSourcetype.objects.select_related("PaymentSourcetype").all()

  def resolve_all_PaymentTransaction(root, info):		
     return PaymentTransaction.objects.select_related("PaymentTransaction").all()

  def resolve_all_PaypalExpresstransaction(root, info):		
     return PaypalExpresstransaction.objects.select_related("PaypalExpresstransaction").all()

  def resolve_all_PaypalPayflowtransaction(root, info):		
     return PaypalPayflowtransaction.objects.select_related("PaypalPayflowtransaction").all()

  def resolve_all_PhotologueGallery(root, info):		
     return PhotologueGallery.objects.select_related("PhotologueGallery").all()

  def resolve_all_PhotologueGalleryPhotos(root, info):		
     return PhotologueGalleryPhotos.objects.select_related("PhotologueGalleryPhotos").all()

  def resolve_all_PhotologueGallerySites(root, info):		
     return PhotologueGallerySites.objects.select_related("PhotologueGallerySites").all()

  def resolve_all_PhotologuePhoto(root, info):		
     return PhotologuePhoto.objects.select_related("PhotologuePhoto").all()

  def resolve_all_PhotologuePhotoeffect(root, info):		
     return PhotologuePhotoeffect.objects.select_related("PhotologuePhotoeffect").all()

  def resolve_all_PhotologuePhotoSites(root, info):		
     return PhotologuePhotoSites.objects.select_related("PhotologuePhotoSites").all()

  def resolve_all_PhotologuePhotosize(root, info):		
     return PhotologuePhotosize.objects.select_related("PhotologuePhotosize").all()

  def resolve_all_PhotologueWatermark(root, info):		
     return PhotologueWatermark.objects.select_related("PhotologueWatermark").all()

  def resolve_all_PinaxBadgesBadgeaward(root, info):		
     return PinaxBadgesBadgeaward.objects.select_related("PinaxBadgesBadgeaward").all()

  def resolve_all_PinaxEventsEvent(root, info):		
     return PinaxEventsEvent.objects.select_related("PinaxEventsEvent").all()

  def resolve_all_PinaxMessagesMessage(root, info):		
     return PinaxMessagesMessage.objects.select_related("PinaxMessagesMessage").all()

  def resolve_all_PinaxMessagesThread(root, info):		
     return PinaxMessagesThread.objects.select_related("PinaxMessagesThread").all()

  def resolve_all_PinaxMessagesUserthread(root, info):		
     return PinaxMessagesUserthread.objects.select_related("PinaxMessagesUserthread").all()

  def resolve_all_Product(root, info):		
     return Product.objects.select_related("Product").all()

  def resolve_all_ReviewsProductreview(root, info):		
     return ReviewsProductreview.objects.select_related("ReviewsProductreview").all()

  def resolve_all_ReviewsVote(root, info):		
     return ReviewsVote.objects.select_related("ReviewsVote").all()

  def resolve_all_SalesLineTransaction(root, info):		
     return SalesLineTransaction.objects.select_related("SalesLineTransaction").all()

  def resolve_all_ShippingOrderanditemcharges(root, info):		
     return ShippingOrderanditemcharges.objects.select_related("ShippingOrderanditemcharges").all()

  def resolve_all_ShippingOrderanditemchargesCountries(root, info):		
     return ShippingOrderanditemchargesCountries.objects.select_related("ShippingOrderanditemchargesCountries").all()

  def resolve_all_ShippingWeightband(root, info):		
     return ShippingWeightband.objects.select_related("ShippingWeightband").all()

  def resolve_all_ShippingWeightbased(root, info):		
     return ShippingWeightbased.objects.select_related("ShippingWeightbased").all()

  def resolve_all_ShippingWeightbasedCountries(root, info):		
     return ShippingWeightbasedCountries.objects.select_related("ShippingWeightbasedCountries").all()

  def resolve_all_TaggitTag(root, info):		
     return TaggitTag.objects.select_related("TaggitTag").all()

  def resolve_all_TaggitTaggeditem(root, info):		
     return TaggitTaggeditem.objects.select_related("TaggitTaggeditem").all()

  def resolve_all_TestimonialsTestimonial(root, info):		
     return TestimonialsTestimonial.objects.select_related("TestimonialsTestimonial").all()

  def resolve_all_ThumbnailKvstore(root, info):		
     return ThumbnailKvstore.objects.select_related("ThumbnailKvstore").all()

  def resolve_all_VoucherVoucher(root, info):		
     return VoucherVoucher.objects.select_related("VoucherVoucher").all()

  def resolve_all_VoucherVoucherapplication(root, info):		
     return VoucherVoucherapplication.objects.select_related("VoucherVoucherapplication").all()

  def resolve_all_VoucherVoucherOffers(root, info):		
     return VoucherVoucherOffers.objects.select_related("VoucherVoucherOffers").all()

  def resolve_all_VoucherVoucherset(root, info):		
     return VoucherVoucherset.objects.select_related("VoucherVoucherset").all()

  def resolve_all_WishlistsLine(root, info):		
     return WishlistsLine.objects.select_related("WishlistsLine").all()

  def resolve_all_WishlistsWishlist(root, info):		
     return WishlistsWishlist.objects.select_related("WishlistsWishlist").all()

schema = graphene.Schema(query=Query)
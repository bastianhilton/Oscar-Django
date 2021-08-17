import graphene
from graphene_django import DjangoObjectType
from shop.models import *

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

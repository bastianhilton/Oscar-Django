import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *

class AddressCountryType(DjangoObjectType):
  class Meta:
      model = AddressCountry
      filter_fields = {
        "iso_3166_1_a2",
        "iso_3166_1_a3",
        "iso_3166_1_numeric",
        "printable_name",
        "name",
        "display_order",
        "is_shipping_country",
   }
  interfaces = (relay.Node,)

class AddressUseraddressType(DjangoObjectType):
  class Meta:
      model = AddressUseraddress
      filter_fields = {
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
   }
  interfaces = (relay.Node,)

class AdvancedFiltersAdvancedfilterType(DjangoObjectType):
  class Meta:
      model = AdvancedFiltersAdvancedfilter
      filter_fields = {
        "title",
        "url",
        "b64_query",
        "model",
        "created_by",
        "created_at",
   }
  interfaces = (relay.Node,)

class AdvancedFiltersAdvancedfilterGroupsType(DjangoObjectType):
  class Meta:
        model = AdvancedFiltersAdvancedfilterGroups
        filter_fields = {
        "advancedfilter",
        "group",
   }
  interfaces = (relay.Node,)

class AdvancedFiltersAdvancedfilterUsersType(DjangoObjectType):
  class Meta:
        model = AdvancedFiltersAdvancedfilterUsers
        filter_fields = {
        "advancedfilter",
        "user",
   }
  interfaces = (relay.Node,)

class AnalyticsProductrecordType(DjangoObjectType):
  class Meta:
        model = AnalyticsProductrecord
        filter_fields = {
        "num_views",
        "num_basket_additions",
        "num_purchases",
        "score",
        "product",
   }
  interfaces = (relay.Node,)


class AnalyticsUserproductviewType(DjangoObjectType):
  class Meta:
        model = AnalyticsUserproductview
        filter_fields = {
        "date_created",
        "product",
        "user",
   }
  interfaces = (relay.Node,)

class AnalyticsUserrecordType(DjangoObjectType):
  class Meta:
      model = AnalyticsUserrecord
      filter_fields = {
        "num_product_views",
        "num_basket_additions",
        "num_orders",
        "num_order_lines",
        "num_order_items",
        "total_spent",
        "date_last_order",
        "user",
   }
  interfaces = (relay.Node,)

class AnalyticsUsersearchType(DjangoObjectType):
  class Meta:
      model = AnalyticsUsersearch
      filter_fields = {
        "query",
        "date_created",
        "user",
   }
  interfaces = (relay.Node,)


class AnnouncementsAnnouncementType(DjangoObjectType):
  class Meta:
      model = AnnouncementsAnnouncement
      filter_fields = {
    "title",
    "content",
    "creation_date",
    "site_wide",
    "members_only",
    "dismissal_type",
    "publish_start",
    "publish_end",
    "creator",
   }
  interfaces = (relay.Node,)

class AnnouncementsDismissalType(DjangoObjectType):
  class Meta:
      model = AnnouncementsDismissal
      filter_fields = {
    "dismissed_at",
    "announcement",
    "user",
   }
  interfaces = (relay.Node,)

class AuthGroupType(DjangoObjectType):
  class Meta:
     model = AuthGroup
     filter_fields = {
        "name",
   }
  interfaces = (relay.Node,)

class AuthGroupPermissionsType(DjangoObjectType):
  class Meta:
     model = AuthGroupPermissions
     filter_fields = {
        "group",
        "permission",
   }
  interfaces = (relay.Node,)

class AuthPermissionType(DjangoObjectType):
  class Meta:
     model = AuthPermission
     filter_fields = {
    "name",
    "content_type",
    "codename",
   }
  interfaces = (relay.Node,)

class AuthUserType(DjangoObjectType):
  class Meta:
     model = AuthUser
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class AuthUserGroupsType(DjangoObjectType):
  class Meta:
     model = AuthUserGroups
     filter_fields = {
    "user",
    "group",
   }
  interfaces = (relay.Node,)

class AuthUserUserPermissionsType(DjangoObjectType):
  class Meta:
     model = AuthUserUserPermissions
     filter_fields = {
    "user",
    "permission",
   }
  interfaces = (relay.Node,)

class BasketBasketType(DjangoObjectType):
  class Meta:
     model = BasketBasket
     filter_fields = {
    "status",
    "date_created",
    "date_merged",
    "date_submitted",
    "owner",
   }
  interfaces = (relay.Node,)

class BasketBasketVouchersType(DjangoObjectType):
  class Meta:
     model = BasketBasketVouchers
     filter_fields = {
    "basket",
    "voucher",
   }
  interfaces = (relay.Node,)

class BasketLineType(DjangoObjectType):
  class Meta:
     model = BasketLine
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class BasketLineattributeType(DjangoObjectType):
  class Meta:
     model = BasketLineattribute
     filter_fields = {
    "value",
    "line",
    "option",
   }
  interfaces = (relay.Node,)

class Bootstrap4AlertsBootstrap4AlertsType(DjangoObjectType):
  class Meta:
     model = Bootstrap4AlertsBootstrap4Alerts
     filter_fields = {
    "cmsplugin_ptr",
    "alert_context",
    "alert_dismissable",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4BadgeBootstrap4BadgeType(DjangoObjectType):
  class Meta:
     model = Bootstrap4BadgeBootstrap4Badge
     filter_fields = {
    "cmsplugin_ptr",
    "badge_text",
    "badge_context",
    "badge_pills",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4CardBootstrap4CardType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CardBootstrap4Card
     filter_fields = {
    "cmsplugin_ptr",
    "card_type",
    "card_context",
    "card_alignment",
    "card_outline",
    "card_text_color",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4CardBootstrap4CardinnerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CardBootstrap4Cardinner
     filter_fields = {
    "cmsplugin_ptr",
    "inner_type",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4CarouselBootstrap4CarouselType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CarouselBootstrap4Carousel
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class Bootstrap4CarouselBootstrap4CarouselslideType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CarouselBootstrap4Carouselslide
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class Bootstrap4CollapseBootstrap4CollapseType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CollapseBootstrap4Collapse
     filter_fields = {
    "cmsplugin_ptr",
    "siblings",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4CollapseBootstrap4CollapsecontainerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CollapseBootstrap4Collapsecontainer
     filter_fields = {
    "cmsplugin_ptr",
    "identifier",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4CollapseBootstrap4CollapsetriggerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4CollapseBootstrap4Collapsetrigger
     filter_fields = {
    "cmsplugin_ptr",
    "identifier",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4ContentBootstrap4BlockquoteType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ContentBootstrap4Blockquote
     filter_fields = {
    "cmsplugin_ptr",
    "quote_content",
    "quote_origin",
    "quote_alignment",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4ContentBootstrap4CodeType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ContentBootstrap4Code
     filter_fields = {
    "cmsplugin_ptr",
    "code_content",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4ContentBootstrap4FigureType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ContentBootstrap4Figure
     filter_fields = {
    "cmsplugin_ptr",
    "figure_caption",
    "figure_alignment",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4GridBootstrap4GridcolumnType(DjangoObjectType):
  class Meta:
     model = Bootstrap4GridBootstrap4Gridcolumn
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class Bootstrap4GridBootstrap4GridcontainerType(DjangoObjectType):
  class Meta:
     model = Bootstrap4GridBootstrap4Gridcontainer
     filter_fields = {
    "cmsplugin_ptr",
    "container_type",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4GridBootstrap4GridrowType(DjangoObjectType):
  class Meta:
     model = Bootstrap4GridBootstrap4Gridrow
     filter_fields = {
    "cmsplugin_ptr",
    "vertical_alignment",
    "horizontal_alignment",
    "gutters",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4JumbotronBootstrap4JumbotronType(DjangoObjectType):
  class Meta:
     model = Bootstrap4JumbotronBootstrap4Jumbotron
     filter_fields = {
    "cmsplugin_ptr",
    "fluid",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4LinkBootstrap4LinkType(DjangoObjectType):
  class Meta:
     model = Bootstrap4LinkBootstrap4Link
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class Bootstrap4ListgroupBootstrap4ListgroupType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ListgroupBootstrap4Listgroup
     filter_fields = {
    "cmsplugin_ptr",
    "list_group_flush",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4ListgroupBootstrap4ListgroupitemType(DjangoObjectType):
  class Meta:
     model = Bootstrap4ListgroupBootstrap4Listgroupitem
     filter_fields = {
    "cmsplugin_ptr",
    "list_context",
    "list_state",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4MediaBootstrap4MediaType(DjangoObjectType):
  class Meta:
     model = Bootstrap4MediaBootstrap4Media
     filter_fields = {
    "cmsplugin_ptr",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4MediaBootstrap4MediabodyType(DjangoObjectType):
  class Meta:
     model = Bootstrap4MediaBootstrap4Mediabody
     filter_fields = {
    "cmsplugin_ptr",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4PictureBootstrap4PictureType(DjangoObjectType):
  class Meta:
     model = Bootstrap4PictureBootstrap4Picture
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class Bootstrap4TabsBootstrap4TabType(DjangoObjectType):
  class Meta:
     model = Bootstrap4TabsBootstrap4Tab
     filter_fields = {
    "cmsplugin_ptr",
    "template",
    "tab_type",
    "tab_alignment",
    "tab_index",
    "tab_effect",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4TabsBootstrap4TabitemType(DjangoObjectType):
  class Meta:
     model = Bootstrap4TabsBootstrap4Tabitem
     filter_fields = {
    "cmsplugin_ptr",
    "tab_title",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class Bootstrap4UtilitiesBootstrap4SpacingType(DjangoObjectType):
  class Meta:
     model = Bootstrap4UtilitiesBootstrap4Spacing
     filter_fields = {
    "cmsplugin_ptr",
    "space_property",
    "space_sides",
    "space_size",
    "space_device",
    "tag_type",
    "attributes",
   }
  interfaces = (relay.Node,)

class CatalogueAttributeoptionType(DjangoObjectType):
  class Meta:
     model = CatalogueAttributeoption
     filter_fields = {
    "option",
    "group",
   }
  interfaces = (relay.Node,)

class CatalogueAttributeoptiongroupType(DjangoObjectType):
  class Meta:
     model = CatalogueAttributeoptiongroup
     filter_fields = {
    "name",
   }
  interfaces = (relay.Node,)

class CatalogueCategoryType(DjangoObjectType):
  class Meta:
     model = CatalogueCategory
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CatalogueOptionType(DjangoObjectType):
  class Meta: 
     model = CatalogueOption
     filter_fields = {
    "name",
    "code",
    "type",
    "required",
   }
  interfaces = (relay.Node,)

class CatalogueProductType(DjangoObjectType):
  class Meta:
     model = CatalogueProduct
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CatalogueProductProductOptionsType(DjangoObjectType):
  class Meta:
     model = CatalogueProductProductOptions
     filter_fields = {
    "product",
    "option",
   }
  interfaces = (relay.Node,)

class CatalogueProductattributeType(DjangoObjectType):
  class Meta:
     model = CatalogueProductattribute
     filter_fields = {
    "name",
    "code",
    "type",
    "required",
    "option_group",
    "product_class",
   }
  interfaces = (relay.Node,)

class CatalogueProductattributevalueType(DjangoObjectType):
  class Meta:
     model = CatalogueProductattributevalue
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CatalogueProductattributevalueValueMultiOptionType(DjangoObjectType):
  class Meta:
     model = CatalogueProductattributevalueValueMultiOption
     filter_fields = {
    "productattributevalue",
    "attributeoption",
   }
  interfaces = (relay.Node,)

class CatalogueProductcategoryType(DjangoObjectType):
  class Meta:
     model = CatalogueProductcategory
     filter_fields = {
    "category",
    "product",
   }
  interfaces = (relay.Node,)

class CatalogueProductclassType(DjangoObjectType):
  class Meta:
     model = CatalogueProductclass
     filter_fields = {
    "name",
    "slug",
    "requires_shipping",
    "track_stock",
     }

class CatalogueProductclassOptionsType(DjangoObjectType):
  class Meta:
     model = CatalogueProductclassOptions
     filter_fields = {
    "productclass",
    "option",
   }
  interfaces = (relay.Node,)

class CatalogueOptionType(DjangoObjectType):
  class Meta:
     model = CatalogueOption
     filter_fields = {
    "name",
    "code",
    "type",
    "required",
   }
  interfaces = (relay.Node,)

class CatalogueProductType(DjangoObjectType):
  class Meta:
     model = CatalogueProduct
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CatalogueProductimageType(DjangoObjectType):
  class Meta:
     model = CatalogueProductimage
     filter_fields = {
    "original",
    "caption",
    "display_order",
    "date_created",
    "product",
   }
  interfaces = (relay.Node,)

class CatalogueProductrecommendationType(DjangoObjectType):
  class Meta:
     model = CatalogueProductrecommendation
     filter_fields = {
    "ranking",
    "primary",
    "recommendation",
   }
  interfaces = (relay.Node,)

class CmsAliaspluginmodelType(DjangoObjectType):
  class Meta:
     model = CmsAliaspluginmodel
     filter_fields = {
    "cmsplugin_ptr",
    "plugin",
    "alias_placeholder",
   }
  interfaces = (relay.Node,)

class CmsCmspluginType(DjangoObjectType):
  class Meta:
     model = CmsCmsplugin
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CmsGlobalpagepermissionType(DjangoObjectType):
  class Meta:
     model = CmsGlobalpagepermission
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CmsGlobalpagepermissionSitesType(DjangoObjectType):
  class Meta:
     model = CmsGlobalpagepermissionSites
     filter_fields = {
    "globalpagepermission",
    "site",
   }
  interfaces = (relay.Node,)

class CmsPageType(DjangoObjectType):
  class Meta:
     model = CmsPage
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CmsPagePlaceholdersType(DjangoObjectType):
  class Meta:
     model = CmsPagePlaceholders
     filter_fields = {
    "page",
    "placeholder",
   }
  interfaces = (relay.Node,)

class CmsPagepermissionType(DjangoObjectType):
  class Meta:
     model = CmsPagepermission
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CmsPageuserType(DjangoObjectType):
  class Meta:
     model = CmsPageuser
     filter_fields = {
    "user_ptr",
    "created_by",
   }
  interfaces = (relay.Node,)

class CmsPageusergroupType(DjangoObjectType):
  class Meta:
     model = CmsPageusergroup
     filter_fields = {
    "group_ptr",
    "created_by",
   }
  interfaces = (relay.Node,)

class CmsPlaceholderType(DjangoObjectType):
  class Meta:
     model = CmsPlaceholder
     filter_fields = {
    "slot",
    "default_width",
   }
  interfaces = (relay.Node,)

class CmsPlaceholderreferenceType(DjangoObjectType):
  class Meta:
     model = CmsPlaceholderreference
     filter_fields = {
    "cmsplugin_ptr",
    "name",
    "placeholder_ref",
   }
  interfaces = (relay.Node,)

class CmsStaticplaceholderType(DjangoObjectType):
  class Meta:
     model = CmsStaticplaceholder
     filter_fields = {
    "name",
    "code",
    "dirty",
    "creation_method",
    "draft",
    "public",
    "site",
   }
  interfaces = (relay.Node,)

class CmsTitleType(DjangoObjectType):
  class Meta:
     model = CmsTitle
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class CmsTreenodeType(DjangoObjectType):
  class Meta:
     model = CmsTreenode
     filter_fields = {
    "path",
    "depth",
    "numchild",
    "parent",
    "site",
   }
  interfaces = (relay.Node,)

class CmsUrlconfrevisionType(DjangoObjectType):
  class Meta:
     model = CmsUrlconfrevision
     filter_fields = {
    "revision",
   }
  interfaces = (relay.Node,)

class CmsUsersettingsType(DjangoObjectType):
  class Meta:
     model = CmsUsersettings
     filter_fields = {
    "language",
    "clipboard",
    "user",
   }
  interfaces = (relay.Node,)

class CommunicationCommunicationeventtypeType(DjangoObjectType):
  class Meta:
     model = CommunicationCommunicationeventtype
     filter_fields = {
    "code",
    "name",
    "category",
    "email_subject_template",
    "email_body_template",
    "email_body_html_template",
    "sms_template",
    "date_created",
    "date_updated",
   }
  interfaces = (relay.Node,)

class CommunicationEmailType(DjangoObjectType):
  class Meta:
     model = CommunicationEmail
     filter_fields = {
    "subject",
    "body_text",
    "body_html",
    "date_sent",
    "user",
    "email",
   }
  interfaces = (relay.Node,)

class CommunicationNotificationType(DjangoObjectType):
  class Meta:
     model = CommunicationNotification
     filter_fields = {
    "subject",
    "body",
    "location",
    "date_sent",
    "date_read",
    "recipient",
    "sender",
   }
  interfaces = (relay.Node,)

class CustomerProductalertType(DjangoObjectType):
  class Meta:
     model = CustomerProductalert
     filter_fields = {
    "email",
    "key",
    "status",
    "date_created",
    "date_confirmed",
    "date_cancelled",
    "date_closed",
    "product",
    "user",
   }
  interfaces = (relay.Node,)

class DjangoAdminLogType(DjangoObjectType):
  class Meta:
     model = DjangoAdminLog
     filter_fields = {
    "action_time",
    "object_id",
    "object_repr",
    "action_flag",
    "change_message",
    "content_type",
    "user",
   }
  interfaces = (relay.Node,)

class DjangoContentType(DjangoObjectType):
  class Meta:
     model = DjangoContent
     filter_fields = {
    "app_label",
    "model",
   }
  interfaces = (relay.Node,)

class DjangoFlatpageType(DjangoObjectType):
  class Meta:
     model = DjangoFlatpage
     filter_fields = {
    "url",
    "title",
    "content",
    "enable_comments",
    "template_name",
    "registration_required",
   }
  interfaces = (relay.Node,)

class DjangoFlatpageSitesType(DjangoObjectType):
  class Meta:
     model = DjangoFlatpageSites
     filter_fields = {
    "flatpage",
    "site",
   }
  interfaces = (relay.Node,)

class DjangoMigrationsType(DjangoObjectType):
  class Meta:
     model = DjangoMigrations
     filter_fields = {
    "app",
    "name",
    "applied",
   }
  interfaces = (relay.Node,)

class DjangoSessionType(DjangoObjectType):
  class Meta:
     model = DjangoSession
     filter_fields = {
    "session_key",
    "session_data",
    "expire_date",
   }
  interfaces = (relay.Node,)

class DjangoSiteType(DjangoObjectType):
  class Meta:
     model = DjangoSite
     filter_fields = {
    "domain",
    "name",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogAuthorentriespluginType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogAuthorentriesplugin
     filter_fields = {
    "cmsplugin_ptr",
    "latest_posts",
    "app_config",
    "current_site",
    "template_folder",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogAuthorentriespluginAuthorsType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogAuthorentriespluginAuthors
     filter_fields = {
    "authorentriesplugin",
    "user",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogBlogcategoryType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogcategory
     filter_fields = {
    "date_created",
    "date_modified",
    "parent",
    "app_config",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogBlogcategoryTranslationType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogcategoryTranslation
     filter_fields = {
    "language_code",
    "name",
    "slug",
    "master",
    "meta_description",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogBlogconfigType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogconfig
     filter_fields = {
    "type",
    "namespace",
    "app_data",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogBlogconfigTranslationType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogBlogconfigTranslation
     filter_fields = {
    "language_code",
    "app_title",
    "master",
    "object_name",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogGenericblogpluginType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogGenericblogplugin
     filter_fields = {
    "cmsplugin_ptr",
    "app_config",
    "current_site",
    "template_folder",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogLatestpostspluginType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogLatestpostsplugin
     filter_fields = {
    "cmsplugin_ptr",
    "latest_posts",
    "app_config",
    "current_site",
    "template_folder",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogLatestpostspluginCategoriesType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogLatestpostspluginCategories
     filter_fields = {
    "latestpostsplugin",
    "blogcategory",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogPostType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPost
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsBlogPostCategoriesType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostCategories
     filter_fields = {
    "post",
    "blogcategory",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogPostRelatedType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostRelated
     filter_fields = {
    "from_post",
    "to_post",
    "sort_value",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogPostSitesType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostSites
     filter_fields = {
    "post",
    "site",
   }
  interfaces = (relay.Node,)

class DjangocmsBlogPostTranslationType(DjangoObjectType):
  class Meta:
     model = DjangocmsBlogPostTranslation
     filter_fields = {
    "language_code",
    "title",
    "slug",
    "abstract",
    "meta_description",
    "meta_keywords",
    "meta_title",
    "post_text",
    "master",
   }
  interfaces = (relay.Node,)

class DjangocmsFileFileType(DjangoObjectType):
  class Meta:
     model = DjangocmsFileFile
     filter_fields = {
    "cmsplugin_ptr",
    "file_name",
    "link_target",
    "link_title",
    "file_src",
    "attributes",
    "template",
    "show_file_size",
   }
  interfaces = (relay.Node,)

class DjangocmsFileFolderType(DjangoObjectType):
  class Meta: 
     model = DjangocmsFileFolder
     filter_fields = {
    "template",
    "link_target",
    "show_file_size",
    "attributes",
    "cmsplugin_ptr",
    "folder_src",
   }
  interfaces = (relay.Node,)

class DjangocmsGooglemapGooglemapType(DjangoObjectType):
  class Meta:
     model = DjangocmsGooglemapGooglemap
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsGooglemapGooglemapmarkerType(DjangoObjectType):
  class Meta:
     model = DjangocmsGooglemapGooglemapmarker
     filter_fields = {
    "cmsplugin_ptr",
    "title",
    "address",
    "lat",
    "lng",
    "show_content",
    "info_content",
    "icon",
   }
  interfaces = (relay.Node,)

class DjangocmsGooglemapGooglemaprouteType(DjangoObjectType):
  class Meta:
     model = DjangocmsGooglemapGooglemaproute
     filter_fields = {
    "cmsplugin_ptr",
    "title",
    "origin",
    "destination",
    "travel_mode",
   }
  interfaces = (relay.Node,)

class DjangocmsHistoryPlaceholderactionType(DjangoObjectType):
  class Meta:
     model = DjangocmsHistoryPlaceholderaction
     filter_fields = {
    "action",
    "pre_action_data",
    "post_action_data",
    "language",
    "order",
    "operation",
    "placeholder",
   }
  interfaces = (relay.Node,)

class DjangocmsHistoryPlaceholderoperationType(DjangoObjectType):
  class Meta:
     model = DjangocmsHistoryPlaceholderoperation
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsIconIconType(DjangoObjectType):
  class Meta:
     model = DjangocmsIconIcon
     filter_fields = {
    "cmsplugin_ptr",
    "icon",
    "template",
    "label",
    "attributes",
   }
  interfaces = (relay.Node,)

class DjangocmsLinkLinkType(DjangoObjectType):
  class Meta:
     model = DjangocmsLinkLink
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsMapsMapsType(DjangoObjectType):
  class Meta:
     model = DjangocmsMapsMaps
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsPicturePictureType(DjangoObjectType):
  class Meta:
     model = DjangocmsPicturePicture
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsStyleStyleType(DjangoObjectType):
  class Meta:
     model = DjangocmsStyleStyle
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class DjangocmsTextCkeditorTextType(DjangoObjectType):
  class Meta:
     model = DjangocmsTextCkeditorText
     filter_fields = {
    "cmsplugin_ptr",
    "body",
   }
  interfaces = (relay.Node,)

class DjangocmsVideoVideoplayerType(DjangoObjectType):
  class Meta:
     model = DjangocmsVideoVideoplayer
     filter_fields = {
    "cmsplugin_ptr",
    "embed_link",
    "poster",
    "attributes",
    "label",
    "template",
    "parameters",
   }
  interfaces = (relay.Node,)

class DjangocmsVideoVideosourceType(DjangoObjectType):
  class Meta:
     model = DjangocmsVideoVideosource
     filter_fields = {
    "cmsplugin_ptr",
    "text_title",
    "text_description",
    "attributes",
    "source_file",
   }
  interfaces = (relay.Node,)

class DjangocmsVideoVideotrackType(DjangoObjectType):
  class Meta:
     model = DjangocmsVideoVideotrack
     filter_fields = {
    "cmsplugin_ptr",
    "kind",
    "srclang",
    "label",
    "attributes",
    "src",
   }
  interfaces = (relay.Node,)

class EasyThumbnailsSourceType(DjangoObjectType):
  class Meta:
     model = EasyThumbnailsSource
     filter_fields = {
    "storage_hash",
    "name",
    "modified",
   }
  interfaces = (relay.Node,)

class EasyThumbnailsThumbnailType(DjangoObjectType):
  class Meta:
     model = EasyThumbnailsThumbnail
     filter_fields = {
    "storage_hash",
    "name",
    "modified",
    "source",
   }
  interfaces = (relay.Node,)

class EasyThumbnailsThumbnaildimensionsType(DjangoObjectType):
  class Meta:
     model = EasyThumbnailsThumbnaildimensions
     filter_fields = {
    "thumbnail",
    "width",
    "height",
   }
  interfaces = (relay.Node,)

class FilerClipboardType(DjangoObjectType):
  class Meta:
     model = FilerClipboard
     filter_fields = {
    "user",
   }
  interfaces = (relay.Node,)

class FilerClipboarditemType(DjangoObjectType):
  class Meta:
     model = FilerClipboarditem
     filter_fields = {
    "clipboard",
    "file",
   }
  interfaces = (relay.Node,)

class FilerFileType(DjangoObjectType):
  class Meta:
     model = FilerFile
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class FilerFolderType(DjangoObjectType):
  class Meta:
     model = FilerFolder
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class FilerFolderpermissionType(DjangoObjectType):
  class Meta:
     model = FilerFolderpermission
     filter_fields = {
    "type",
    "everybody",
    "can_edit",
    "can_read",
    "can_add_children",
    "folder",
    "group",
    "user",
   }
  interfaces = (relay.Node,)

class FilerImageType(DjangoObjectType):
  class Meta:
     model = FilerImage
     filter_fields = {
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
}
  interfaces = (relay.Node,)

class FilerThumbnailoptionType(DjangoObjectType):
  class Meta:
     model = FilerThumbnailoption
     filter_fields = {
    "name",
    "width",
    "height",
    "crop",
    "upscale",
   }
  interfaces = (relay.Node,)

class MenusCachekeyType(DjangoObjectType):
  class Meta:
     model = MenusCachekey
     filter_fields = {
    "language",
    "site",
    "key",
   }
  interfaces = (relay.Node,)

class OfferBenefitType(DjangoObjectType):
  class Meta:
     model = OfferBenefit
     filter_fields = {
    "type",
    "value",
    "max_affected_items",
    "proxy_class",
    "range",
   }
  interfaces = (relay.Node,)

class OfferConditionType(DjangoObjectType):
  class Meta:
     model = OfferCondition
     filter_fields = {
    "type",
    "value",
    "proxy_class",
   }
  interfaces = (relay.Node,)

class OfferConditionalofferType(DjangoObjectType):
  class Meta:
     model = OfferConditionaloffer
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OfferConditionalofferCombinationsType(DjangoObjectType):
  class Meta:
     model = OfferConditionalofferCombinations
     filter_fields = {
    "from_conditionaloffer",
    "to_conditionaloffer",
   }
  interfaces = (relay.Node,)

class OfferRangeType(DjangoObjectType):
  class Meta:
     model = OfferRange
     filter_fields = {
    "name",
    "slug",
    "description",
    "is_public",
    "includes_all_products",
    "proxy_class",
    "date_created",
   }
  interfaces = (relay.Node,)

class OfferRangeClassesType(DjangoObjectType):
  class Meta:
     model = OfferRangeClasses
     filter_fields = {
    "range",
    "productclass",
   }
  interfaces = (relay.Node,)

class OfferRangeExcludedProductsType(DjangoObjectType):
  class Meta:
     model = OfferRangeExcludedProducts
     filter_fields = {
    "range",
   }
  interfaces = (relay.Node,)

class OfferRangeIncludedCategoriesType(DjangoObjectType):
  class Meta:
     model = OfferRangeIncludedCategories
     filter_fields = {
    "range",
   }
  interfaces = (relay.Node,)

class OfferRangeproductType(DjangoObjectType):
  class Meta:
     model = OfferRangeproduct
     filter_fields = {
    "display_order",
    "product",
    "range", 
}
  interfaces = (relay.Node,)

class OfferRangeproductfileuploadType(DjangoObjectType):
  class Meta:
     model = OfferRangeproductfileupload
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OrderBillingaddressType(DjangoObjectType):
  class Meta:
     model = OrderBillingaddress
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OrderCommunicationeventType(DjangoObjectType):
  class Meta:
     model = OrderCommunicationevent
     filter_fields = {
        "date_created",
        "event_type",
        "order",
   }
  interfaces = (relay.Node,)

class OrderLineType(DjangoObjectType):
  class Meta:
     model = OrderLine
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OrderLineattributeType(DjangoObjectType):
  class Meta:
     model = OrderLineattribute
     filter_fields = {
    "type",
    "value",
    "line",
    "option",
   }
  interfaces = (relay.Node,)

class OrderLinepriceType(DjangoObjectType):
  class Meta:
     model = OrderLineprice
     filter_fields = {
    "quantity",
    "price_incl_tax",
    "price_excl_tax",
    "shipping_incl_tax",
    "shipping_excl_tax",
    "line",
    "order",
   }
  interfaces = (relay.Node,)

class OrderOrderType(DjangoObjectType):
  class Meta:
     model = OrderOrder
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OrderOrderdiscountType(DjangoObjectType):
  class Meta:
     model = OrderOrderdiscount
     filter_fields = {
    "category", 
    "offer_id",
    "offer_name",
    "voucher_id",
    "voucher_code",
    "frequency",
    "amount",
    "message",
    "order",
   }
  interfaces = (relay.Node,)

class OrderOrdernoteType(DjangoObjectType):
  class Meta:
     model = OrderOrdernote
     filter_fields = {
    "note_type",
    "message",
    "date_created",
    "date_updated",
    "order",
    "user",
   }
  interfaces = (relay.Node,)

class OrderOrderstatuschangeType(DjangoObjectType):
  class Meta:
     model = OrderOrderstatuschange
     filter_fields = {
    "old_status",
    "new_status",
    "date_created",
    "order",
   }
  interfaces = (relay.Node,)

class OrderPaymenteventType(DjangoObjectType):
  class Meta:
     model = OrderPaymentevent
     filter_fields = {
    "amount",
    "reference",
    "date_created",
    "event_type",
    "order",
    "shipping_event",
   }
  interfaces = (relay.Node,)

class OrderPaymenteventquantityType(DjangoObjectType):
  class Meta:
     model = OrderPaymenteventquantity
     filter_fields = {
    "quantity",
    "event",
    "line",
   }
  interfaces = (relay.Node,)

class OrderPaymenteventtypeType(DjangoObjectType):
  class Meta:
     model = OrderPaymenteventtype
     filter_fields = {
    "name",
    "code",
   }
  interfaces = (relay.Node,)

class OrderShippingaddressType(DjangoObjectType):
  class Meta:
     model = OrderShippingaddress
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OrderShippingeventType(DjangoObjectType):
  class Meta:
     model = OrderShippingevent
     filter_fields = {
    "notes",
    "date_created",
    "event_type",
   }
  interfaces = (relay.Node,)

class OrderShippingeventquantityType(DjangoObjectType):
  class Meta:
     model = OrderShippingeventquantity
     filter_fields = {
    "quantity",
    "event",
    "line",
   }
  interfaces = (relay.Node,)

class OrderShippingeventtypeType(DjangoObjectType):
  class Meta:
     model = OrderShippingeventtype
     filter_fields = {
    "name",
    "code",
   }
  interfaces = (relay.Node,)

class OrderSurchargeType(DjangoObjectType):
  class Meta:
     model = OrderSurcharge
     filter_fields = {
    "name",
    "code",
    "incl_tax",
    "excl_tax",
    "order",
   }
  interfaces = (relay.Node,)

class OscarInvoicesInvoiceType(DjangoObjectType):
  class Meta:
     model = OscarInvoicesInvoice
     filter_fields = {
    "number",
    "notes",
    "document",
    "legal_entity",
    "order",
   }
  interfaces = (relay.Node,)

class OscarInvoicesLegalentityType(DjangoObjectType):
  class Meta:
     model = OscarInvoicesLegalentity
     filter_fields = {
    "shop_name",
    "business_name",
    "vat_number",
    "logo",
    "email",
    "web_site",
   }
  interfaces = (relay.Node,)

class OscarInvoicesLegalentityaddressType(DjangoObjectType):
  class Meta:
     model = OscarInvoicesLegalentityaddress
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class OscarapiApikeyType(DjangoObjectType):
  class Meta:
     model = OscarapiApikey
     filter_fields = {
    "key",
   }
  interfaces = (relay.Node,)

class PartnerPartnerType(DjangoObjectType):
  class Meta:
     model = PartnerPartner
     filter_fields = {
    "code",
    "name",
   }
  interfaces = (relay.Node,)

class PartnerPartnerUsersType(DjangoObjectType):
  class Meta:
     model = PartnerPartnerUsers
     filter_fields = {
    "partner",
    "user",
   }
  interfaces = (relay.Node,)

class PartnerPartneraddressType(DjangoObjectType):
  class Meta:
     model = PartnerPartneraddress
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PartnerStockalertType(DjangoObjectType):
  class Meta:
     model = PartnerStockalert
     filter_fields = {
    "threshold",
    "status",
    "date_created",
    "date_closed",
    "stockrecord",
   }
  interfaces = (relay.Node,)

class PartnerStockrecordType(DjangoObjectType):
  class Meta:
     model = PartnerStockrecord
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PaymentBankcardType(DjangoObjectType):
  class Meta:
     model = PaymentBankcard
     filter_fields = {
    "card_type",
    "name",
    "number",
    "expiry_date",
    "partner_reference",
    "user",
   }
  interfaces = (relay.Node,)

class PaymentSourceType(DjangoObjectType):
  class Meta:
     model = PaymentSource
     filter_fields = {
    "currency",
    "amount_allocated",
    "amount_debited",
    "amount_refunded",
    "reference",
    "label",
    "order",
    "source_type",
   }
  interfaces = (relay.Node,)

class PaymentSourcetypeType(DjangoObjectType):
  class Meta:
     model = PaymentSourcetype
     filter_fields = {
    "name",
    "code",
   }
  interfaces = (relay.Node,)

class PaymentTransactionType(DjangoObjectType):
  class Meta:
     model = PaymentTransaction
     filter_fields = {
    "txn_type",
    "amount",
    "reference",
    "status",
    "date_created",
    "source",
   }
  interfaces = (relay.Node,)

class PaypalExpresstransactionType(DjangoObjectType):
  class Meta:
     model = PaypalExpresstransaction
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PaypalPayflowtransactionType(DjangoObjectType):
  class Meta:
     model = PaypalPayflowtransaction
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PhotologueGalleryType(DjangoObjectType):
  class Meta:
     model = PhotologueGallery
     filter_fields = {
    "date_added",
    "title",
    "slug",
    "description",
    "is_public",
   }
  interfaces = (relay.Node,)

class PhotologueGalleryPhotosType(DjangoObjectType):
  class Meta:
     model = PhotologueGalleryPhotos
     filter_fields = {
    "sort_value",
    "gallery",
    "photo",
   }
  interfaces = (relay.Node,)

class PhotologueGallerySitesType(DjangoObjectType):
  class Meta:
     model = PhotologueGallerySites
     filter_fields = {
    "gallery",
    "site",
   }
  interfaces = (relay.Node,)

class PhotologuePhotoType(DjangoObjectType):
  class Meta:
     model = PhotologuePhoto
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PhotologuePhotoSitesType(DjangoObjectType):
  class Meta:
     model = PhotologuePhotoSites
     filter_fields = {
    "photo",
    "site",
   }
  interfaces = (relay.Node,)

class PhotologuePhotoeffectType(DjangoObjectType):
  class Meta:
     model = PhotologuePhotoeffect
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PhotologuePhotosizeType(DjangoObjectType):
  class Meta:
     model = PhotologuePhotosize
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PhotologueWatermarkType(DjangoObjectType):
  class Meta:
     model = PhotologueWatermark
     filter_fields = {
    "name",
    "description",
    "image",
    "style",
    "opacity",
   }
  interfaces = (relay.Node,)

class PinaxBadgesBadgeawardType(DjangoObjectType):
  class Meta:
     model = PinaxBadgesBadgeaward
     filter_fields = {
    "awarded_at",
    "slug",
    "level",
    "user",
   }
  interfaces = (relay.Node,)

class PinaxEventsEventType(DjangoObjectType):
  class Meta:
     model = PinaxEventsEvent
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class PinaxMessagesMessageType(DjangoObjectType):
  class Meta:
     model = PinaxMessagesMessage
     filter_fields = {
    "sent_at",
    "content",
    "sender",
    "thread",
   }
  interfaces = (relay.Node,)

class PinaxMessagesThreadType(DjangoObjectType):
  class Meta:
     model = PinaxMessagesThread
     filter_fields = {
    "subject",
   }
  interfaces = (relay.Node,)

class PinaxMessagesUserthreadType(DjangoObjectType):
  class Meta:
     model = PinaxMessagesUserthread
     filter_fields = {
    "unread",
    "deleted",
    "thread",
    "user",
   }
  interfaces = (relay.Node,)

class ReviewsProductreviewType(DjangoObjectType):
  class Meta:
     model = ReviewsProductreview
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class ReviewsVoteType(DjangoObjectType):
  class Meta:
     model = ReviewsVote
     filter_fields = {
    "delta",
    "date_created",
    "review",
    "user",
   }
  interfaces = (relay.Node,)

class ShippingOrderanditemchargesType(DjangoObjectType):
  class Meta:
     model = ShippingOrderanditemcharges
     filter_fields = {
    "code",
    "name",
    "description",
    "price_per_order",
    "price_per_item",
    "free_shipping_threshold",
   }
  interfaces = (relay.Node,)

class ShippingOrderanditemchargesCountriesType(DjangoObjectType):
  class Meta:
     model = ShippingOrderanditemchargesCountries
     filter_fields = {
    "orderanditemcharges",
    "country",
   }
  interfaces = (relay.Node,)

class ShippingWeightbandType(DjangoObjectType):
  class Meta:
     model = ShippingWeightband
     filter_fields = {
    "upper_limit",
    "method",
   }
  interfaces = (relay.Node,)

class ShippingWeightbasedType(DjangoObjectType):
  class Meta:
     model = ShippingWeightbased
     filter_fields = {
    "code",
    "name",
    "description",
    "default_weight",
   }
  interfaces = (relay.Node,)

class ShippingWeightbasedCountriesType(DjangoObjectType):
  class Meta:
     model = ShippingWeightbasedCountries
     filter_fields = {
    "weightbased",
    "country",
   }
  interfaces = (relay.Node,)

class TaggitTagType(DjangoObjectType):
  class Meta:
     model = TaggitTag
     filter_fields = {
    "name",
    "slug",
   }
  interfaces = (relay.Node,)

class TaggitTaggeditemType(DjangoObjectType):
  class Meta:
     model = TaggitTaggeditem
     filter_fields = {
    "object_id",
    "content_type",
    "tag",
   }
  interfaces = (relay.Node,)

class TestimonialsTestimonialType(DjangoObjectType):
  class Meta:
     model = TestimonialsTestimonial
     filter_fields = {
    "text",
    "author",
    "affiliation",
    "added",
    "active",
   }
  interfaces = (relay.Node,)

class ThumbnailKvstoreType(DjangoObjectType):
  class Meta:
     model = ThumbnailKvstore
     filter_fields = {
    "key",
    "value",
   }
  interfaces = (relay.Node,)

class VoucherVoucherType(DjangoObjectType):
  class Meta:
     model = VoucherVoucher
     filter_fields = {
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
   }
  interfaces = (relay.Node,)

class VoucherVoucherOffersType(DjangoObjectType):
  class Meta:
     model = VoucherVoucherOffers
     filter_fields = {
    "voucher",
    "conditionaloffer",
   }
  interfaces = (relay.Node,)

class VoucherVoucherapplicationType(DjangoObjectType):
  class Meta:
     model = VoucherVoucherapplication
     filter_fields = {
    "date_created",
    "order",
    "user",
    "voucher",
   }
  interfaces = (relay.Node,)

class VoucherVouchersetType(DjangoObjectType):
  class Meta:
     model = VoucherVoucherset
     filter_fields = {
    "name",
    "count",
    "code_length",
    "description",
    "date_created",
    "start_datetime",
    "end_datetime",
    "offer",
   }
  interfaces = (relay.Node,)

class WishlistsLineType(DjangoObjectType):
  class Meta:
     model = WishlistsLine
     filter_fields = {
    "quantity",
    "title",
    "product",
    "wishlist",
   }
  interfaces = (relay.Node,)

class WishlistsWishlistType(DjangoObjectType):
  class Meta:
     model = WishlistsWishlist
     filter_fields = {
        "name",
        "key",
        "visibility",
        "date_created",
        "owner",
   }
  interfaces = (relay.Node,)

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
     return AddressCountry.objects.prefetch_related("AddressCountry").all()

  def resolve_all_AddressUseraddress(root, info):		
     return AddressUseraddress.objects.prefetch_related("AddressUseraddress").all()

  def resolve_all_AdvancedFiltersAdvancedfilter(root, info):		
     return AdvancedFiltersAdvancedfilter.objects.prefetch_related("AdvancedFiltersAdvancedfilter").all()

  def resolve_all_AdvancedFiltersAdvancedfilterGroups(root, info):		
     return AdvancedFiltersAdvancedfilterGroups.objects.prefetch_related("AdvancedFiltersAdvancedfilterGroups").all()

  def resolve_all_AdvancedFiltersAdvancedfilterUsers(root, info):		
     return AdvancedFiltersAdvancedfilterUsers.objects.prefetch_related("AdvancedFiltersAdvancedfilterUsers").all()

  def resolve_all_AnalyticsProductrecord(root, info):		
     return AnalyticsProductrecord.objects.prefetch_related("AnalyticsProductrecord").all()

  def resolve_all_AnalyticsUserproductview(root, info):		
     return AnalyticsUserproductview.objects.prefetch_related("AnalyticsUserproductview").all()

  def resolve_all_AnalyticsUserrecord(root, info):		
     return AnalyticsUserrecord.objects.prefetch_related("AnalyticsUserrecord").all()

  def resolve_all_AnalyticsUsersearch(root, info):		
     return AnalyticsUsersearch.objects.prefetch_related("AnalyticsUsersearch").all()

  def resolve_all_AnnouncementsAnnouncement(root, info):		
     return AnnouncementsAnnouncement.objects.prefetch_related("AnnouncementsAnnouncement").all()

  def resolve_all_AnnouncementsDismissal(root, info):		
     return AnnouncementsDismissal.objects.prefetch_related("AnnouncementsDismissal").all()

  def resolve_all_AuthGroup(root, info):		
     return AuthGroup.objects.prefetch_related("AuthGroup").all()

  def resolve_all_AuthGroupPermissions(root, info):		
     return AuthGroupPermissions.objects.prefetch_related("AuthGroupPermissions").all()

  def resolve_all_AuthPermission(root, info):		
     return AuthPermission.objects.prefetch_related("AuthPermission").all()

  def resolve_all_AuthUser(root, info):		
     return AuthUser.objects.prefetch_related("AuthUser").all()

  def resolve_all_AuthUserGroups(root, info):		
     return AuthUserGroups.objects.prefetch_related("AuthUserGroups").all()

  def resolve_all_AuthUserUserPermissions(root, info):		
     return AuthUserUserPermissions.objects.prefetch_related("AuthUserUserPermissions").all()

  def resolve_all_BasketBasket(root, info):		
     return BasketBasket.objects.prefetch_related("BasketBasket").all()

  def resolve_all_BasketBasketVouchers(root, info):		
     return BasketBasketVouchers.objects.prefetch_related("BasketBasketVouchers").all()

  def resolve_all_BasketLine(root, info):		
     return BasketLine.objects.prefetch_related("BasketLine").all()

  def resolve_all_BasketLineattribute(root, info):		
     return BasketLineattribute.objects.prefetch_related("BasketLineattribute").all()

  def resolve_all_Bootstrap4AlertsBootstrap4Alerts(root, info):		
     return Bootstrap4AlertsBootstrap4Alerts.objects.prefetch_related("Bootstrap4AlertsBootstrap4Alerts").all()

  def resolve_all_Bootstrap4BadgeBootstrap4Badge(root, info):		
     return Bootstrap4BadgeBootstrap4Badge.objects.prefetch_related("Bootstrap4BadgeBootstrap4Badge").all()

  def resolve_all_Bootstrap4CardBootstrap4Card(root, info):		
     return Bootstrap4CardBootstrap4Card.objects.prefetch_related("Bootstrap4CardBootstrap4Card").all()

  def resolve_all_Bootstrap4CardBootstrap4Cardinner(root, info):		
     return Bootstrap4CardBootstrap4Cardinner.objects.prefetch_related("Bootstrap4CardBootstrap4Cardinner").all()

  def resolve_all_Bootstrap4CarouselBootstrap4Carousel(root, info):		
     return Bootstrap4CarouselBootstrap4Carousel.objects.prefetch_related("Bootstrap4CarouselBootstrap4Carousel").all()

  def resolve_all_Bootstrap4CarouselBootstrap4Carouselslide(root, info):		
     return Bootstrap4CarouselBootstrap4Carouselslide.objects.prefetch_related("Bootstrap4CarouselBootstrap4Carouselslide").all()

  def resolve_all_Bootstrap4CollapseBootstrap4Collapse(root, info):		
     return Bootstrap4CollapseBootstrap4Collapse.objects.prefetch_related("Bootstrap4CollapseBootstrap4Collapse").all()

  def resolve_all_Bootstrap4CollapseBootstrap4Collapsecontainer(root, info):		
     return Bootstrap4CollapseBootstrap4Collapsecontainer.objects.prefetch_related("Bootstrap4CollapseBootstrap4Collapsecontainer").all()

  def resolve_all_Bootstrap4CollapseBootstrap4Collapsetrigger(root, info):		
     return Bootstrap4CollapseBootstrap4Collapsetrigger.objects.prefetch_related("Bootstrap4CollapseBootstrap4Collapsetrigger").all()

  def resolve_all_Bootstrap4ContentBootstrap4Blockquote(root, info):		
     return Bootstrap4ContentBootstrap4Blockquote.objects.prefetch_related("Bootstrap4ContentBootstrap4Blockquote").all()

  def resolve_all_Bootstrap4ContentBootstrap4Code(root, info):		
     return Bootstrap4ContentBootstrap4Code.objects.prefetch_related("Bootstrap4ContentBootstrap4Code").all()

  def resolve_all_Bootstrap4ContentBootstrap4Figure(root, info):		
     return Bootstrap4ContentBootstrap4Figure.objects.prefetch_related("Bootstrap4ContentBootstrap4Figure").all()

  def resolve_all_Bootstrap4GridBootstrap4Gridcolumn(root, info):		
     return Bootstrap4GridBootstrap4Gridcolumn.objects.prefetch_related("Bootstrap4GridBootstrap4Gridcolumn").all()

  def resolve_all_Bootstrap4GridBootstrap4Gridcontainer(root, info):		
     return Bootstrap4GridBootstrap4Gridcontainer.objects.prefetch_related("Bootstrap4GridBootstrap4Gridcontainer").all()

  def resolve_all_Bootstrap4GridBootstrap4Gridrow(root, info):		
     return Bootstrap4GridBootstrap4Gridrow.objects.prefetch_related("Bootstrap4GridBootstrap4Gridrow").all()

  def resolve_all_Bootstrap4JumbotronBootstrap4Jumbotron(root, info):		
     return Bootstrap4JumbotronBootstrap4Jumbotron.objects.prefetch_related("Bootstrap4JumbotronBootstrap4Jumbotron").all()

  def resolve_all_Bootstrap4LinkBootstrap4Link(root, info):		
     return Bootstrap4LinkBootstrap4Link.objects.prefetch_related("Bootstrap4LinkBootstrap4Link").all()

  def resolve_all_Bootstrap4ListgroupBootstrap4Listgroup(root, info):		
     return Bootstrap4ListgroupBootstrap4Listgroup.objects.prefetch_related("Bootstrap4ListgroupBootstrap4Listgroup").all()

  def resolve_all_Bootstrap4ListgroupBootstrap4Listgroupitem(root, info):		
     return Bootstrap4ListgroupBootstrap4Listgroupitem.objects.prefetch_related("Bootstrap4ListgroupBootstrap4Listgroupitem").all()

  def resolve_all_Bootstrap4MediaBootstrap4Media(root, info):		
     return Bootstrap4MediaBootstrap4Media.objects.prefetch_related("Bootstrap4MediaBootstrap4Media").all()

  def resolve_all_Bootstrap4MediaBootstrap4Mediabody(root, info):		
     return Bootstrap4MediaBootstrap4Mediabody.objects.prefetch_related("Bootstrap4MediaBootstrap4Mediabody").all()

  def resolve_all_Bootstrap4PictureBootstrap4Picture(root, info):		
     return Bootstrap4PictureBootstrap4Picture.objects.prefetch_related("Bootstrap4PictureBootstrap4Picture").all()

  def resolve_all_Bootstrap4TabsBootstrap4Tab(root, info):		
     return Bootstrap4TabsBootstrap4Tab.objects.prefetch_related("Bootstrap4TabsBootstrap4Tab").all()

  def resolve_all_Bootstrap4TabsBootstrap4Tabitem(root, info):		
     return Bootstrap4TabsBootstrap4Tabitem.objects.prefetch_related("Bootstrap4TabsBootstrap4Tabitem").all()

  def resolve_all_Bootstrap4UtilitiesBootstrap4Spacing(root, info):		
     return Bootstrap4UtilitiesBootstrap4Spacing.objects.prefetch_related("Bootstrap4UtilitiesBootstrap4Spacing").all()

  def resolve_all_CatalogueAttributeoption(root, info):		
     return CatalogueAttributeoption.objects.prefetch_related("CatalogueAttributeoption").all()

  def resolve_all_CatalogueAttributeoptiongroup(root, info):		
     return CatalogueAttributeoptiongroup.objects.prefetch_related("CatalogueAttributeoptiongroup").all()

  def resolve_all_CatalogueCategory(root, info):		
     return CatalogueCategory.objects.prefetch_related("CatalogueCategory").all()

  def resolve_all_CatalogueOption(root, info):		
     return CatalogueOption.objects.prefetch_related("CatalogueOption").all()

  def resolve_all_CatalogueProduct(root, info):		
     return CatalogueProduct.objects.prefetch_related("CatalogueProduct").all()

  def resolve_all_CatalogueProductattribute(root, info):		
     return CatalogueProductattribute.objects.prefetch_related("CatalogueProductattribute").all()

  def resolve_all_CatalogueProductattributevalue(root, info):		
     return CatalogueProductattributevalue.objects.prefetch_related("CatalogueProductattributevalue").all()

  def resolve_all_CatalogueProductattributevalueValueMultiOption(root, info):		
     return CatalogueProductattributevalueValueMultiOption.objects.prefetch_related("CatalogueProductattributevalueValueMultiOption").all()

  def resolve_all_CatalogueProductcategory(root, info):		
     return CatalogueProductcategory.objects.prefetch_related("CatalogueProductcategory").all()

  def resolve_all_CatalogueProductclass(root, info):		
     return CatalogueProductclass.objects.prefetch_related("CatalogueProductclass").all()

  def resolve_all_CatalogueProductclassOptions(root, info):		
     return CatalogueProductclassOptions.objects.prefetch_related("CatalogueProductclassOptions").all()

  def resolve_all_CatalogueProductimage(root, info):		
     return CatalogueProductimage.objects.prefetch_related("CatalogueProductimage").all()

  def resolve_all_CatalogueProductProductOptions(root, info):		
     return CatalogueProductProductOptions.objects.prefetch_related("CatalogueProductProductOptions").all()

  def resolve_all_CatalogueProductrecommendation(root, info):		
     return CatalogueProductrecommendation.objects.prefetch_related("CatalogueProductrecommendation").all()

  def resolve_all_Client(root, info):		
     return Client.objects.prefetch_related("Client").all()

  def resolve_all_CmsAliaspluginmodel(root, info):		
     return CmsAliaspluginmodel.objects.prefetch_related("CmsAliaspluginmodel").all()

  def resolve_all_CmsCmsplugin(root, info):		
     return CmsCmsplugin.objects.prefetch_related("CmsCmsplugin").all()

  def resolve_all_CmsGlobalpagepermission(root, info):		
     return CmsGlobalpagepermission.objects.prefetch_related("CmsGlobalpagepermission").all()

  def resolve_all_CmsGlobalpagepermissionSites(root, info):		
     return CmsGlobalpagepermissionSites.objects.prefetch_related("CmsGlobalpagepermissionSites").all()

  def resolve_all_CmsPage(root, info):		
     return CmsPage.objects.prefetch_related("CmsPage").all()

  def resolve_all_CmsPagepermission(root, info):		
     return CmsPagepermission.objects.prefetch_related("CmsPagepermission").all()

  def resolve_all_CmsPagePlaceholders(root, info):		
     return CmsPagePlaceholders.objects.prefetch_related("CmsPagePlaceholders").all()

  def resolve_all_CmsPageuser(root, info):		
     return CmsPageuser.objects.prefetch_related("CmsPageuser").all()

  def resolve_all_CmsPageusergroup(root, info):		
     return CmsPageusergroup.objects.prefetch_related("CmsPageusergroup").all()

  def resolve_all_CmsPlaceholder(root, info):		
     return CmsPlaceholder.objects.prefetch_related("CmsPlaceholder").all()

  def resolve_all_CmsPlaceholderreference(root, info):		
     return CmsPlaceholderreference.objects.prefetch_related("CmsPlaceholderreference").all()

  def resolve_all_CmsStaticplaceholder(root, info):		
     return CmsStaticplaceholder.objects.prefetch_related("CmsStaticplaceholder").all()

  def resolve_all_CmsTitle(root, info):		
     return CmsTitle.objects.prefetch_related("CmsTitle").all()

  def resolve_all_CmsTreenode(root, info):		
     return CmsTreenode.objects.prefetch_related("CmsTreenode").all()

  def resolve_all_CmsUrlconfrevision(root, info):		
     return CmsUrlconfrevision.objects.prefetch_related("CmsUrlconfrevision").all()

  def resolve_all_CmsUsersettings(root, info):		
     return CmsUsersettings.objects.prefetch_related("CmsUsersettings").all()

  def resolve_all_CommunicationCommunicationeventtype(root, info):		
     return CommunicationCommunicationeventtype.objects.prefetch_related("CommunicationCommunicationeventtype").all()

  def resolve_all_CommunicationEmail(root, info):		
     return CommunicationEmail.objects.prefetch_related("CommunicationEmail").all()

  def resolve_all_CommunicationNotification(root, info):		
     return CommunicationNotification.objects.prefetch_related("CommunicationNotification").all()

  def resolve_all_CustomerProductalert(root, info):		
     return CustomerProductalert.objects.prefetch_related("CustomerProductalert").all()

  def resolve_all_DjangoAdminLog(root, info):		
     return DjangoAdminLog.objects.prefetch_related("DjangoAdminLog").all()

  def resolve_all_DjangocmsBlogAuthorentriesplugin(root, info):		
     return DjangocmsBlogAuthorentriesplugin.objects.prefetch_related("DjangocmsBlogAuthorentriesplugin").all()

  def resolve_all_DjangocmsBlogAuthorentriespluginAuthors(root, info):		
     return DjangocmsBlogAuthorentriespluginAuthors.objects.prefetch_related("DjangocmsBlogAuthorentriespluginAuthors").all()

  def resolve_all_DjangocmsBlogBlogcategory(root, info):		
     return DjangocmsBlogBlogcategory.objects.prefetch_related("DjangocmsBlogBlogcategory").all()

  def resolve_all_DjangocmsBlogBlogcategoryTranslation(root, info):		
     return DjangocmsBlogBlogcategoryTranslation.objects.prefetch_related("DjangocmsBlogBlogcategoryTranslation").all()

  def resolve_all_DjangocmsBlogBlogconfig(root, info):		
     return DjangocmsBlogBlogconfig.objects.prefetch_related("DjangocmsBlogBlogconfig").all()

  def resolve_all_DjangocmsBlogBlogconfigTranslation(root, info):		
     return DjangocmsBlogBlogconfigTranslation.objects.prefetch_related("DjangocmsBlogBlogconfigTranslation").all()

  def resolve_all_DjangocmsBlogGenericblogplugin(root, info):		
     return DjangocmsBlogGenericblogplugin.objects.prefetch_related("DjangocmsBlogGenericblogplugin").all()

  def resolve_all_DjangocmsBlogLatestpostsplugin(root, info):		
     return DjangocmsBlogLatestpostsplugin.objects.prefetch_related("DjangocmsBlogLatestpostsplugin").all()

  def resolve_all_DjangocmsBlogLatestpostspluginCategories(root, info):		
     return DjangocmsBlogLatestpostspluginCategories.objects.prefetch_related("DjangocmsBlogLatestpostspluginCategories").all()

  def resolve_all_DjangocmsBlogPost(root, info):		
     return DjangocmsBlogPost.objects.prefetch_related("DjangocmsBlogPost").all()

  def resolve_all_DjangocmsBlogPostCategories(root, info):		
     return DjangocmsBlogPostCategories.objects.prefetch_related("DjangocmsBlogPostCategories").all()

  def resolve_all_DjangocmsBlogPostRelated(root, info):		
     return DjangocmsBlogPostRelated.objects.prefetch_related("DjangocmsBlogPostRelated").all()

  def resolve_all_DjangocmsBlogPostSites(root, info):		
     return DjangocmsBlogPostSites.objects.prefetch_related("DjangocmsBlogPostSites").all()

  def resolve_all_DjangocmsBlogPostTranslation(root, info):		
     return DjangocmsBlogPostTranslation.objects.prefetch_related("DjangocmsBlogPostTranslation").all()

  def resolve_all_DjangocmsFileFile(root, info):		
     return DjangocmsFileFile.objects.prefetch_related("DjangocmsFileFile").all()

  def resolve_all_DjangocmsFileFolder(root, info):		
     return DjangocmsFileFolder.objects.prefetch_related("DjangocmsFileFolder").all()

  def resolve_all_DjangocmsGooglemapGooglemap(root, info):		
     return DjangocmsGooglemapGooglemap.objects.prefetch_related("DjangocmsGooglemapGooglemap").all()

  def resolve_all_DjangocmsGooglemapGooglemapmarker(root, info):		
     return DjangocmsGooglemapGooglemapmarker.objects.prefetch_related("DjangocmsGooglemapGooglemapmarker").all()

  def resolve_all_DjangocmsGooglemapGooglemaproute(root, info):		
     return DjangocmsGooglemapGooglemaproute.objects.prefetch_related("DjangocmsGooglemapGooglemaproute").all()

  def resolve_all_DjangocmsHistoryPlaceholderaction(root, info):		
     return DjangocmsHistoryPlaceholderaction.objects.prefetch_related("DjangocmsHistoryPlaceholderaction").all()

  def resolve_all_DjangocmsHistoryPlaceholderoperation(root, info):		
     return DjangocmsHistoryPlaceholderoperation.objects.prefetch_related("DjangocmsHistoryPlaceholderoperation").all()

  def resolve_all_DjangocmsIconIcon(root, info):		
     return DjangocmsIconIcon.objects.prefetch_related("DjangocmsIconIcon").all()

  def resolve_all_DjangocmsLinkLink(root, info):		
     return DjangocmsLinkLink.objects.prefetch_related("DjangocmsLinkLink").all()

  def resolve_all_DjangocmsMapsMaps(root, info):		
     return DjangocmsMapsMaps.objects.prefetch_related("DjangocmsMapsMaps").all()

  def resolve_all_DjangocmsPicturePicture(root, info):		
     return DjangocmsPicturePicture.objects.prefetch_related("DjangocmsPicturePicture").all()

  def resolve_all_DjangocmsStyleStyle(root, info):		
     return DjangocmsStyleStyle.objects.prefetch_related("DjangocmsStyleStyle").all()

  def resolve_all_DjangocmsTextCkeditorText(root, info):		
     return DjangocmsTextCkeditorText.objects.prefetch_related("DjangocmsTextCkeditorText").all()

  def resolve_all_DjangocmsVideoVideoplayer(root, info):		
     return DjangocmsVideoVideoplayer.objects.prefetch_related("DjangocmsVideoVideoplayer").all()

  def resolve_all_DjangocmsVideoVideosource(root, info):		
     return DjangocmsVideoVideosource.objects.prefetch_related("DjangocmsVideoVideosource").all()

  def resolve_all_DjangocmsVideoVideotrack(root, info):		
     return DjangocmsVideoVideotrack.objects.prefetch_related("DjangocmsVideoVideotrack").all()

  def resolve_all_DjangoContent(root, info):		
     return DjangoContent.objects.prefetch_related("DjangoContent").all()

  def resolve_all_DjangoFlatpage(root, info):		
     return DjangoFlatpage.objects.prefetch_related("DjangoFlatpage").all()

  def resolve_all_DjangoFlatpageSites(root, info):		
     return DjangoFlatpageSites.objects.prefetch_related("DjangoFlatpageSites").all()

  def resolve_all_DjangoMigrations(root, info):		
     return DjangoMigrations.objects.prefetch_related("DjangoMigrations").all()

  def resolve_all_DjangoSession(root, info):		
     return DjangoSession.objects.prefetch_related("DjangoSession").all()

  def resolve_all_DjangoSite(root, info):		
     return DjangoSite.objects.prefetch_related("DjangoSite").all()

  def resolve_all_EasyThumbnailsSource(root, info):		
     return EasyThumbnailsSource.objects.prefetch_related("EasyThumbnailsSource").all()

  def resolve_all_EasyThumbnailsThumbnail(root, info):		
     return EasyThumbnailsThumbnail.objects.prefetch_related("EasyThumbnailsThumbnail").all()

  def resolve_all_EasyThumbnailsThumbnaildimensions(root, info):		
     return EasyThumbnailsThumbnaildimensions.objects.prefetch_related("EasyThumbnailsThumbnaildimensions").all()

  def resolve_all_FilerClipboard(root, info):		
     return FilerClipboard.objects.prefetch_related("FilerClipboard").all()

  def resolve_all_FilerClipboarditem(root, info):		
     return FilerClipboarditem.objects.prefetch_related("FilerClipboarditem").all()

  def resolve_all_FilerFile(root, info):		
     return FilerFile.objects.prefetch_related("FilerFile").all()

  def resolve_all_FilerFolder(root, info):		
     return FilerFolder.objects.prefetch_related("FilerFolder").all()

  def resolve_all_FilerFolderpermission(root, info):		
     return FilerFolderpermission.objects.prefetch_related("FilerFolderpermission").all()

  def resolve_all_FilerImage(root, info):		
     return FilerImage.objects.prefetch_related("FilerImage").all()

  def resolve_all_FilerThumbnailoption(root, info):		
     return FilerThumbnailoption.objects.prefetch_related("FilerThumbnailoption").all()

  def resolve_all_MenusCachekey(root, info):		
     return MenusCachekey.objects.prefetch_related("MenusCachekey").all()

  def resolve_all_OfferBenefit(root, info):		
     return OfferBenefit.objects.prefetch_related("OfferBenefit").all()

  def resolve_all_OfferCondition(root, info):		
     return OfferCondition.objects.prefetch_related("OfferCondition").all()

  def resolve_all_OfferConditionaloffer(root, info):		
     return OfferConditionaloffer.objects.prefetch_related("OfferConditionaloffer").all()

  def resolve_all_OfferConditionalofferCombinations(root, info):		
     return OfferConditionalofferCombinations.objects.prefetch_related("OfferConditionalofferCombinations").all()

  def resolve_all_OfferRange(root, info):		
     return OfferRange.objects.prefetch_related("OfferRange").all()

  def resolve_all_OfferRangeClasses(root, info):		
     return OfferRangeClasses.objects.prefetch_related("OfferRangeClasses").all()

  def resolve_all_OfferRangeExcludedProducts(root, info):		
     return OfferRangeExcludedProducts.objects.prefetch_related("OfferRangeExcludedProducts").all()

  def resolve_all_OfferRangeIncludedCategories(root, info):		
     return OfferRangeIncludedCategories.objects.prefetch_related("OfferRangeIncludedCategories").all()

  def resolve_all_OfferRangeproduct(root, info):		
     return OfferRangeproduct.objects.prefetch_related("OfferRangeproduct").all()

  def resolve_all_OfferRangeproductfileupload(root, info):		
     return OfferRangeproductfileupload.objects.prefetch_related("OfferRangeproductfileupload").all()

  def resolve_all_OrderBillingaddress(root, info):		
     return OrderBillingaddress.objects.prefetch_related("OrderBillingaddress").all()

  def resolve_all_OrderCommunicationevent(root, info):		
     return OrderCommunicationevent.objects.prefetch_related("OrderCommunicationevent").all()

  def resolve_all_OrderLine(root, info):		
     return OrderLine.objects.prefetch_related("OrderLine").all()

  def resolve_all_OrderLineattribute(root, info):		
     return OrderLineattribute.objects.prefetch_related("OrderLineattribute").all()

  def resolve_all_OrderLineprice(root, info):		
     return OrderLineprice.objects.prefetch_related("OrderLineprice").all()

  def resolve_all_OrderOrder(root, info):		
     return OrderOrder.objects.prefetch_related("OrderOrder").all()

  def resolve_all_OrderOrderdiscount(root, info):		
     return OrderOrderdiscount.objects.prefetch_related("OrderOrderdiscount").all()

  def resolve_all_OrderOrdernote(root, info):		
     return OrderOrdernote.objects.prefetch_related("OrderOrdernote").all()

  def resolve_all_OrderOrderstatuschange(root, info):		
     return OrderOrderstatuschange.objects.prefetch_related("OrderOrderstatuschange").all()

  def resolve_all_OrderPaymentevent(root, info):		
     return OrderPaymentevent.objects.prefetch_related("OrderPaymentevent").all()

  def resolve_all_OrderPaymenteventquantity(root, info):		
     return OrderPaymenteventquantity.objects.prefetch_related("OrderPaymenteventquantity").all()

  def resolve_all_OrderPaymenteventtype(root, info):		
     return OrderPaymenteventtype.objects.prefetch_related("OrderPaymenteventtype").all()

  def resolve_all_OrderShippingaddress(root, info):		
     return OrderShippingaddress.objects.prefetch_related("OrderShippingaddress").all()

  def resolve_all_OrderShippingevent(root, info):		
     return OrderShippingevent.objects.prefetch_related("OrderShippingevent").all()

  def resolve_all_OrderShippingeventquantity(root, info):		
     return OrderShippingeventquantity.objects.prefetch_related("OrderShippingeventquantity").all()

  def resolve_all_OrderShippingeventtype(root, info):		
     return OrderShippingeventtype.objects.prefetch_related("OrderShippingeventtype").all()

  def resolve_all_OrderSurcharge(root, info):		
     return OrderSurcharge.objects.prefetch_related("OrderSurcharge").all()

  def resolve_all_OscarapiApikey(root, info):		
     return OscarapiApikey.objects.prefetch_related("OscarapiApikey").all()

  def resolve_all_OscarInvoicesInvoice(root, info):		
     return OscarInvoicesInvoice.objects.prefetch_related("OscarInvoicesInvoice").all()

  def resolve_all_OscarInvoicesLegalentity(root, info):		
     return OscarInvoicesLegalentity.objects.prefetch_related("OscarInvoicesLegalentity").all()

  def resolve_all_OscarInvoicesLegalentityaddress(root, info):		
     return OscarInvoicesLegalentityaddress.objects.prefetch_related("OscarInvoicesLegalentityaddress").all()

  def resolve_all_PartnerPartner(root, info):		
     return PartnerPartner.objects.prefetch_related("PartnerPartner").all()

  def resolve_all_PartnerPartneraddress(root, info):		
     return PartnerPartneraddress.objects.prefetch_related("PartnerPartneraddress").all()

  def resolve_all_PartnerPartnerUsers(root, info):		
     return PartnerPartnerUsers.objects.prefetch_related("PartnerPartnerUsers").all()

  def resolve_all_PartnerStockalert(root, info):		
     return PartnerStockalert.objects.prefetch_related("PartnerStockalert").all()

  def resolve_all_PartnerStockrecord(root, info):		
     return PartnerStockrecord.objects.prefetch_related("PartnerStockrecord").all()

  def resolve_all_Payment(root, info):		
     return Payment.objects.prefetch_related("Payment").all()

  def resolve_all_PaymentBankcard(root, info):		
     return PaymentBankcard.objects.prefetch_related("PaymentBankcard").all()

  def resolve_all_PaymentSource(root, info):		
     return PaymentSource.objects.prefetch_related("PaymentSource").all()

  def resolve_all_PaymentSourcetype(root, info):		
     return PaymentSourcetype.objects.prefetch_related("PaymentSourcetype").all()

  def resolve_all_PaymentTransaction(root, info):		
     return PaymentTransaction.objects.prefetch_related("PaymentTransaction").all()

  def resolve_all_PaypalExpresstransaction(root, info):		
     return PaypalExpresstransaction.objects.prefetch_related("PaypalExpresstransaction").all()

  def resolve_all_PaypalPayflowtransaction(root, info):		
     return PaypalPayflowtransaction.objects.prefetch_related("PaypalPayflowtransaction").all()

  def resolve_all_PhotologueGallery(root, info):		
     return PhotologueGallery.objects.prefetch_related("PhotologueGallery").all()

  def resolve_all_PhotologueGalleryPhotos(root, info):		
     return PhotologueGalleryPhotos.objects.prefetch_related("PhotologueGalleryPhotos").all()

  def resolve_all_PhotologueGallerySites(root, info):		
     return PhotologueGallerySites.objects.prefetch_related("PhotologueGallerySites").all()

  def resolve_all_PhotologuePhoto(root, info):		
     return PhotologuePhoto.objects.prefetch_related("PhotologuePhoto").all()

  def resolve_all_PhotologuePhotoeffect(root, info):		
     return PhotologuePhotoeffect.objects.prefetch_related("PhotologuePhotoeffect").all()

  def resolve_all_PhotologuePhotoSites(root, info):		
     return PhotologuePhotoSites.objects.prefetch_related("PhotologuePhotoSites").all()

  def resolve_all_PhotologuePhotosize(root, info):		
     return PhotologuePhotosize.objects.prefetch_related("PhotologuePhotosize").all()

  def resolve_all_PhotologueWatermark(root, info):		
     return PhotologueWatermark.objects.prefetch_related("PhotologueWatermark").all()

  def resolve_all_PinaxBadgesBadgeaward(root, info):		
     return PinaxBadgesBadgeaward.objects.prefetch_related("PinaxBadgesBadgeaward").all()

  def resolve_all_PinaxEventsEvent(root, info):		
     return PinaxEventsEvent.objects.prefetch_related("PinaxEventsEvent").all()

  def resolve_all_PinaxMessagesMessage(root, info):		
     return PinaxMessagesMessage.objects.prefetch_related("PinaxMessagesMessage").all()

  def resolve_all_PinaxMessagesThread(root, info):		
     return PinaxMessagesThread.objects.prefetch_related("PinaxMessagesThread").all()

  def resolve_all_PinaxMessagesUserthread(root, info):		
     return PinaxMessagesUserthread.objects.prefetch_related("PinaxMessagesUserthread").all()

  def resolve_all_Product(root, info):		
     return Product.objects.prefetch_related("Product").all()

  def resolve_all_ReviewsProductreview(root, info):		
     return ReviewsProductreview.objects.prefetch_related("ReviewsProductreview").all()

  def resolve_all_ReviewsVote(root, info):		
     return ReviewsVote.objects.prefetch_related("ReviewsVote").all()

  def resolve_all_SalesLineTransaction(root, info):		
     return SalesLineTransaction.objects.prefetch_related("SalesLineTransaction").all()

  def resolve_all_ShippingOrderanditemcharges(root, info):		
     return ShippingOrderanditemcharges.objects.prefetch_related("ShippingOrderanditemcharges").all()

  def resolve_all_ShippingOrderanditemchargesCountries(root, info):		
     return ShippingOrderanditemchargesCountries.objects.prefetch_related("ShippingOrderanditemchargesCountries").all()

  def resolve_all_ShippingWeightband(root, info):		
     return ShippingWeightband.objects.prefetch_related("ShippingWeightband").all()

  def resolve_all_ShippingWeightbased(root, info):		
     return ShippingWeightbased.objects.prefetch_related("ShippingWeightbased").all()

  def resolve_all_ShippingWeightbasedCountries(root, info):		
     return ShippingWeightbasedCountries.objects.prefetch_related("ShippingWeightbasedCountries").all()

  def resolve_all_TaggitTag(root, info):		
     return TaggitTag.objects.prefetch_related("TaggitTag").all()

  def resolve_all_TaggitTaggeditem(root, info):		
     return TaggitTaggeditem.objects.prefetch_related("TaggitTaggeditem").all()

  def resolve_all_TestimonialsTestimonial(root, info):		
     return TestimonialsTestimonial.objects.prefetch_related("TestimonialsTestimonial").all()

  def resolve_all_ThumbnailKvstore(root, info):		
     return ThumbnailKvstore.objects.prefetch_related("ThumbnailKvstore").all()

  def resolve_all_VoucherVoucher(root, info):		
     return VoucherVoucher.objects.prefetch_related("VoucherVoucher").all()

  def resolve_all_VoucherVoucherapplication(root, info):		
     return VoucherVoucherapplication.objects.prefetch_related("VoucherVoucherapplication").all()

  def resolve_all_VoucherVoucherOffers(root, info):		
     return VoucherVoucherOffers.objects.prefetch_related("VoucherVoucherOffers").all()

  def resolve_all_VoucherVoucherset(root, info):		
     return VoucherVoucherset.objects.prefetch_related("VoucherVoucherset").all()

  def resolve_all_WishlistsLine(root, info):		
     return WishlistsLine.objects.prefetch_related("WishlistsLine").all()

  def resolve_all_WishlistsWishlist(root, info):		
     return WishlistsWishlist.objects.prefetch_related("WishlistsWishlist").all()

  def resolve_AddressCountry_by_name(root, info, name):
     try:
        return	AddressCountry.objects.get(name=name)
     except AddressCountry.DoesNotExist:
        return None

  def resolve_AddressUseraddress_by_name(root, info, name):
     try:
        return	AddressUseraddress.objects.get(name=name)
     except AddressUseraddress.DoesNotExist:
        return None

  def resolve_AdvancedFiltersAdvancedfilter_by_name(root, info, name):
     try:
        return	AdvancedFiltersAdvancedfilter.objects.get(name=name)
     except AdvancedFiltersAdvancedfilter.DoesNotExist:
        return None

  def resolve_AdvancedFiltersAdvancedfilterGroups_by_name(root, info, name):
     try:
        return	AdvancedFiltersAdvancedfilterGroups.objects.get(name=name)
     except AdvancedFiltersAdvancedfilterGroups.DoesNotExist:
        return None

  def resolve_AdvancedFiltersAdvancedfilterUsers_by_name(root, info, name):
     try:
        return	AdvancedFiltersAdvancedfilterUsers.objects.get(name=name)
     except AdvancedFiltersAdvancedfilterUsers.DoesNotExist:
        return None

  def resolve_AnalyticsProductrecord_by_name(root, info, name):
     try:
        return	AnalyticsProductrecord.objects.get(name=name)
     except AnalyticsProductrecord.DoesNotExist:
        return None

  def resolve_AnalyticsUserproductview_by_name(root, info, name):
     try:
        return	AnalyticsUserproductview.objects.get(name=name)
     except AnalyticsUserproductview.DoesNotExist:
        return None

  def resolve_AnalyticsUserrecord_by_name(root, info, name):
     try:
        return	AnalyticsUserrecord.objects.get(name=name)
     except AnalyticsUserrecord.DoesNotExist:
        return None

  def resolve_AnalyticsUsersearch_by_name(root, info, name):
     try:
        return	AnalyticsUsersearch.objects.get(name=name)
     except AnalyticsUsersearch.DoesNotExist:
        return None

  def resolve_AnnouncementsAnnouncement_by_name(root, info, name):
     try:
        return	AnnouncementsAnnouncement.objects.get(name=name)
     except AnnouncementsAnnouncement.DoesNotExist:
        return None

  def resolve_AnnouncementsDismissal_by_name(root, info, name):
     try:
        return	AnnouncementsDismissal.objects.get(name=name)
     except AnnouncementsDismissal.DoesNotExist:
        return None

  def resolve_AuthGroup_by_name(root, info, name):
     try:
        return	AuthGroup.objects.get(name=name)
     except AuthGroup.DoesNotExist:
        return None

  def resolve_AuthGroupPermissions_by_name(root, info, name):
     try:
        return	AuthGroupPermissions.objects.get(name=name)
     except AuthGroupPermissions.DoesNotExist:
        return None

  def resolve_AuthPermission_by_name(root, info, name):
     try:
        return	AuthPermission.objects.get(name=name)
     except AuthPermission.DoesNotExist:
        return None

  def resolve_AuthUser_by_name(root, info, name):
     try:
        return	AuthUser.objects.get(name=name)
     except AuthUser.DoesNotExist:
        return None

  def resolve_AuthUserGroups_by_name(root, info, name):
     try:
        return	AuthUserGroups.objects.get(name=name)
     except AuthUserGroups.DoesNotExist:
        return None

  def resolve_AuthUserUserPermissions_by_name(root, info, name):
     try:
        return	AuthUserUserPermissions.objects.get(name=name)
     except AuthUserUserPermissions.DoesNotExist:
        return None

  def resolve_BasketBasket_by_name(root, info, name):
     try:
        return	BasketBasket.objects.get(name=name)
     except BasketBasket.DoesNotExist:
        return None

  def resolve_BasketBasketVouchers_by_name(root, info, name):
     try:
        return	BasketBasketVouchers.objects.get(name=name)
     except BasketBasketVouchers.DoesNotExist:
        return None

  def resolve_BasketLine_by_name(root, info, name):
     try:
        return	BasketLine.objects.get(name=name)
     except BasketLine.DoesNotExist:
        return None

  def resolve_BasketLineattribute_by_name(root, info, name):
     try:
        return	BasketLineattribute.objects.get(name=name)
     except BasketLineattribute.DoesNotExist:
        return None

  def resolve_Bootstrap4AlertsBootstrap4Alerts_by_name(root, info, name):
     try:
        return	Bootstrap4AlertsBootstrap4Alerts.objects.get(name=name)
     except Bootstrap4AlertsBootstrap4Alerts.DoesNotExist:
        return None

  def resolve_Bootstrap4BadgeBootstrap4Badge_by_name(root, info, name):
     try:
        return	Bootstrap4BadgeBootstrap4Badge.objects.get(name=name)
     except Bootstrap4BadgeBootstrap4Badge.DoesNotExist:
        return None

  def resolve_Bootstrap4CardBootstrap4Card_by_name(root, info, name):
     try:
        return	Bootstrap4CardBootstrap4Card.objects.get(name=name)
     except Bootstrap4CardBootstrap4Card.DoesNotExist:
        return None

  def resolve_Bootstrap4CardBootstrap4Cardinner_by_name(root, info, name):
     try:
        return	Bootstrap4CardBootstrap4Cardinner.objects.get(name=name)
     except Bootstrap4CardBootstrap4Cardinner.DoesNotExist:
        return None

  def resolve_Bootstrap4CarouselBootstrap4Carousel_by_name(root, info, name):
     try:
        return	Bootstrap4CarouselBootstrap4Carousel.objects.get(name=name)
     except Bootstrap4CarouselBootstrap4Carousel.DoesNotExist:
        return None

  def resolve_Bootstrap4CarouselBootstrap4Carouselslide_by_name(root, info, name):
     try:
        return	Bootstrap4CarouselBootstrap4Carouselslide.objects.get(name=name)
     except Bootstrap4CarouselBootstrap4Carouselslide.DoesNotExist:
        return None

  def resolve_Bootstrap4CollapseBootstrap4Collapse_by_name(root, info, name):
     try:
        return	Bootstrap4CollapseBootstrap4Collapse.objects.get(name=name)
     except Bootstrap4CollapseBootstrap4Collapse.DoesNotExist:
        return None

  def resolve_Bootstrap4CollapseBootstrap4Collapsecontainer_by_name(root, info, name):
     try:
        return	Bootstrap4CollapseBootstrap4Collapsecontainer.objects.get(name=name)
     except Bootstrap4CollapseBootstrap4Collapsecontainer.DoesNotExist:
        return None

  def resolve_Bootstrap4CollapseBootstrap4Collapsetrigger_by_name(root, info, name):
     try:
        return	Bootstrap4CollapseBootstrap4Collapsetrigger.objects.get(name=name)
     except Bootstrap4CollapseBootstrap4Collapsetrigger.DoesNotExist:
        return None

  def resolve_Bootstrap4ContentBootstrap4Blockquote_by_name(root, info, name):
     try:
        return	Bootstrap4ContentBootstrap4Blockquote.objects.get(name=name)
     except Bootstrap4ContentBootstrap4Blockquote.DoesNotExist:
        return None

  def resolve_Bootstrap4ContentBootstrap4Code_by_name(root, info, name):
     try:
        return	Bootstrap4ContentBootstrap4Code.objects.get(name=name)
     except Bootstrap4ContentBootstrap4Code.DoesNotExist:
        return None

  def resolve_Bootstrap4ContentBootstrap4Figure_by_name(root, info, name):
     try:
        return	Bootstrap4ContentBootstrap4Figure.objects.get(name=name)
     except Bootstrap4ContentBootstrap4Figure.DoesNotExist:
        return None

  def resolve_Bootstrap4GridBootstrap4Gridcolumn_by_name(root, info, name):
     try:
        return	Bootstrap4GridBootstrap4Gridcolumn.objects.get(name=name)
     except Bootstrap4GridBootstrap4Gridcolumn.DoesNotExist:
        return None

  def resolve_Bootstrap4GridBootstrap4Gridcontainer_by_name(root, info, name):
     try:
        return	Bootstrap4GridBootstrap4Gridcontainer.objects.get(name=name)
     except Bootstrap4GridBootstrap4Gridcontainer.DoesNotExist:
        return None

  def resolve_Bootstrap4GridBootstrap4Gridrow_by_name(root, info, name):
     try:
        return	Bootstrap4GridBootstrap4Gridrow.objects.get(name=name)
     except Bootstrap4GridBootstrap4Gridrow.DoesNotExist:
        return None

  def resolve_Bootstrap4JumbotronBootstrap4Jumbotron_by_name(root, info, name):
     try:
        return	Bootstrap4JumbotronBootstrap4Jumbotron.objects.get(name=name)
     except Bootstrap4JumbotronBootstrap4Jumbotron.DoesNotExist:
        return None

  def resolve_Bootstrap4LinkBootstrap4Link_by_name(root, info, name):
     try:
        return	Bootstrap4LinkBootstrap4Link.objects.get(name=name)
     except Bootstrap4LinkBootstrap4Link.DoesNotExist:
        return None

  def resolve_Bootstrap4ListgroupBootstrap4Listgroup_by_name(root, info, name):
     try:
        return	Bootstrap4ListgroupBootstrap4Listgroup.objects.get(name=name)
     except Bootstrap4ListgroupBootstrap4Listgroup.DoesNotExist:
        return None

  def resolve_Bootstrap4ListgroupBootstrap4Listgroupitem_by_name(root, info, name):
     try:
        return	Bootstrap4ListgroupBootstrap4Listgroupitem.objects.get(name=name)
     except Bootstrap4ListgroupBootstrap4Listgroupitem.DoesNotExist:
        return None

  def resolve_Bootstrap4MediaBootstrap4Media_by_name(root, info, name):
     try:
        return	Bootstrap4MediaBootstrap4Media.objects.get(name=name)
     except Bootstrap4MediaBootstrap4Media.DoesNotExist:
        return None

  def resolve_Bootstrap4MediaBootstrap4Mediabody_by_name(root, info, name):
     try:
        return	Bootstrap4MediaBootstrap4Mediabody.objects.get(name=name)
     except Bootstrap4MediaBootstrap4Mediabody.DoesNotExist:
        return None

  def resolve_Bootstrap4PictureBootstrap4Picture_by_name(root, info, name):
     try:
        return	Bootstrap4PictureBootstrap4Picture.objects.get(name=name)
     except Bootstrap4PictureBootstrap4Picture.DoesNotExist:
        return None

  def resolve_Bootstrap4TabsBootstrap4Tab_by_name(root, info, name):
     try:
        return	Bootstrap4TabsBootstrap4Tab.objects.get(name=name)
     except Bootstrap4TabsBootstrap4Tab.DoesNotExist:
        return None

  def resolve_Bootstrap4TabsBootstrap4Tabitem_by_name(root, info, name):
     try:
        return	Bootstrap4TabsBootstrap4Tabitem.objects.get(name=name)
     except Bootstrap4TabsBootstrap4Tabitem.DoesNotExist:
        return None

  def resolve_Bootstrap4UtilitiesBootstrap4Spacing_by_name(root, info, name):
     try:
        return	Bootstrap4UtilitiesBootstrap4Spacing.objects.get(name=name)
     except Bootstrap4UtilitiesBootstrap4Spacing.DoesNotExist:
        return None

  def resolve_CatalogueAttributeoption_by_name(root, info, name):
     try:
        return	CatalogueAttributeoption.objects.get(name=name)
     except CatalogueAttributeoption.DoesNotExist:
        return None

  def resolve_CatalogueAttributeoptiongroup_by_name(root, info, name):
     try:
        return	CatalogueAttributeoptiongroup.objects.get(name=name)
     except CatalogueAttributeoptiongroup.DoesNotExist:
        return None

  def resolve_CatalogueCategory_by_name(root, info, name):
     try:
        return	CatalogueCategory.objects.get(name=name)
     except CatalogueCategory.DoesNotExist:
        return None

  def resolve_CatalogueOption_by_name(root, info, name):
     try:
        return	CatalogueOption.objects.get(name=name)
     except CatalogueOption.DoesNotExist:
        return None

  def resolve_CatalogueProduct_by_name(root, info, name):
     try:
        return	CatalogueProduct.objects.get(name=name)
     except CatalogueProduct.DoesNotExist:
        return None

  def resolve_CatalogueProductattribute_by_name(root, info, name):
     try:
        return	CatalogueProductattribute.objects.get(name=name)
     except CatalogueProductattribute.DoesNotExist:
        return None

  def resolve_CatalogueProductattributevalue_by_name(root, info, name):
     try:
        return	CatalogueProductattributevalue.objects.get(name=name)
     except CatalogueProductattributevalue.DoesNotExist:
        return None

  def resolve_CatalogueProductattributevalueValueMultiOption_by_name(root, info, name):
     try:
        return	CatalogueProductattributevalueValueMultiOption.objects.get(name=name)
     except CatalogueProductattributevalueValueMultiOption.DoesNotExist:
        return None

  def resolve_CatalogueProductcategory_by_name(root, info, name):
     try:
        return	CatalogueProductcategory.objects.get(name=name)
     except CatalogueProductcategory.DoesNotExist:
        return None

  def resolve_CatalogueProductclass_by_name(root, info, name):
     try:
        return	CatalogueProductclass.objects.get(name=name)
     except CatalogueProductclass.DoesNotExist:
        return None

  def resolve_CatalogueProductclassOptions_by_name(root, info, name):
     try:
        return	CatalogueProductclassOptions.objects.get(name=name)
     except CatalogueProductclassOptions.DoesNotExist:
        return None

  def resolve_CatalogueProductimage_by_name(root, info, name):
     try:
        return	CatalogueProductimage.objects.get(name=name)
     except CatalogueProductimage.DoesNotExist:
        return None

  def resolve_CatalogueProductProductOptions_by_name(root, info, name):
     try:
        return	CatalogueProductProductOptions.objects.get(name=name)
     except CatalogueProductProductOptions.DoesNotExist:
        return None

  def resolve_CatalogueProductrecommendation_by_name(root, info, name):
     try:
        return	CatalogueProductrecommendation.objects.get(name=name)
     except CatalogueProductrecommendation.DoesNotExist:
        return None

  def resolve_Client_by_name(root, info, name):
     try:
        return	Client.objects.get(name=name)
     except Client.DoesNotExist:
        return None

  def resolve_CmsAliaspluginmodel_by_name(root, info, name):
     try:
        return	CmsAliaspluginmodel.objects.get(name=name)
     except CmsAliaspluginmodel.DoesNotExist:
        return None

  def resolve_CmsCmsplugin_by_name(root, info, name):
     try:
        return	CmsCmsplugin.objects.get(name=name)
     except CmsCmsplugin.DoesNotExist:
        return None

  def resolve_CmsGlobalpagepermission_by_name(root, info, name):
     try:
        return	CmsGlobalpagepermission.objects.get(name=name)
     except CmsGlobalpagepermission.DoesNotExist:
        return None

  def resolve_CmsGlobalpagepermissionSites_by_name(root, info, name):
     try:
        return	CmsGlobalpagepermissionSites.objects.get(name=name)
     except CmsGlobalpagepermissionSites.DoesNotExist:
        return None

  def resolve_CmsPage_by_name(root, info, name):
     try:
        return	CmsPage.objects.get(name=name)
     except CmsPage.DoesNotExist:
        return None

  def resolve_CmsPagepermission_by_name(root, info, name):
     try:
        return	CmsPagepermission.objects.get(name=name)
     except CmsPagepermission.DoesNotExist:
        return None

  def resolve_CmsPagePlaceholders_by_name(root, info, name):
     try:
        return	CmsPagePlaceholders.objects.get(name=name)
     except CmsPagePlaceholders.DoesNotExist:
        return None

  def resolve_CmsPageuser_by_name(root, info, name):
     try:
        return	CmsPageuser.objects.get(name=name)
     except CmsPageuser.DoesNotExist:
        return None

  def resolve_CmsPageusergroup_by_name(root, info, name):
     try:
        return	CmsPageusergroup.objects.get(name=name)
     except CmsPageusergroup.DoesNotExist:
        return None

  def resolve_CmsPlaceholder_by_name(root, info, name):
     try:
        return	CmsPlaceholder.objects.get(name=name)
     except CmsPlaceholder.DoesNotExist:
        return None

  def resolve_CmsPlaceholderreference_by_name(root, info, name):
     try:
        return	CmsPlaceholderreference.objects.get(name=name)
     except CmsPlaceholderreference.DoesNotExist:
        return None

  def resolve_CmsStaticplaceholder_by_name(root, info, name):
     try:
        return	CmsStaticplaceholder.objects.get(name=name)
     except CmsStaticplaceholder.DoesNotExist:
        return None

  def resolve_CmsTitle_by_name(root, info, name):
     try:
        return	CmsTitle.objects.get(name=name)
     except CmsTitle.DoesNotExist:
        return None

  def resolve_CmsTreenode_by_name(root, info, name):
     try:
        return	CmsTreenode.objects.get(name=name)
     except CmsTreenode.DoesNotExist:
        return None

  def resolve_CmsUrlconfrevision_by_name(root, info, name):
     try:
        return	CmsUrlconfrevision.objects.get(name=name)
     except CmsUrlconfrevision.DoesNotExist:
        return None

  def resolve_CmsUsersettings_by_name(root, info, name):
     try:
        return	CmsUsersettings.objects.get(name=name)
     except CmsUsersettings.DoesNotExist:
        return None

  def resolve_CommunicationCommunicationeventtype_by_name(root, info, name):
     try:
        return	CommunicationCommunicationeventtype.objects.get(name=name)
     except CommunicationCommunicationeventtype.DoesNotExist:
        return None

  def resolve_CommunicationEmail_by_name(root, info, name):
     try:
        return	CommunicationEmail.objects.get(name=name)
     except CommunicationEmail.DoesNotExist:
        return None

  def resolve_CommunicationNotification_by_name(root, info, name):
     try:
        return	CommunicationNotification.objects.get(name=name)
     except CommunicationNotification.DoesNotExist:
        return None

  def resolve_CustomerProductalert_by_name(root, info, name):
     try:
        return	CustomerProductalert.objects.get(name=name)
     except CustomerProductalert.DoesNotExist:
        return None

  def resolve_DjangoAdminLog_by_name(root, info, name):
     try:
        return	DjangoAdminLog.objects.get(name=name)
     except DjangoAdminLog.DoesNotExist:
        return None

  def resolve_DjangocmsBlogAuthorentriesplugin_by_name(root, info, name):
     try:
        return	DjangocmsBlogAuthorentriesplugin.objects.get(name=name)
     except DjangocmsBlogAuthorentriesplugin.DoesNotExist:
        return None

  def resolve_DjangocmsBlogAuthorentriespluginAuthors_by_name(root, info, name):
     try:
        return	DjangocmsBlogAuthorentriespluginAuthors.objects.get(name=name)
     except DjangocmsBlogAuthorentriespluginAuthors.DoesNotExist:
        return None

  def resolve_DjangocmsBlogBlogcategory_by_name(root, info, name):
     try:
        return	DjangocmsBlogBlogcategory.objects.get(name=name)
     except DjangocmsBlogBlogcategory.DoesNotExist:
        return None

  def resolve_DjangocmsBlogBlogcategoryTranslation_by_name(root, info, name):
     try:
        return	DjangocmsBlogBlogcategoryTranslation.objects.get(name=name)
     except DjangocmsBlogBlogcategoryTranslation.DoesNotExist:
        return None

  def resolve_DjangocmsBlogBlogconfig_by_name(root, info, name):
     try:
        return	DjangocmsBlogBlogconfig.objects.get(name=name)
     except DjangocmsBlogBlogconfig.DoesNotExist:
        return None

  def resolve_DjangocmsBlogBlogconfigTranslation_by_name(root, info, name):
     try:
        return	DjangocmsBlogBlogconfigTranslation.objects.get(name=name)
     except DjangocmsBlogBlogconfigTranslation.DoesNotExist:
        return None

  def resolve_DjangocmsBlogGenericblogplugin_by_name(root, info, name):
     try:
        return	DjangocmsBlogGenericblogplugin.objects.get(name=name)
     except DjangocmsBlogGenericblogplugin.DoesNotExist:
        return None

  def resolve_DjangocmsBlogLatestpostsplugin_by_name(root, info, name):
     try:
        return	DjangocmsBlogLatestpostsplugin.objects.get(name=name)
     except DjangocmsBlogLatestpostsplugin.DoesNotExist:
        return None

  def resolve_DjangocmsBlogLatestpostspluginCategories_by_name(root, info, name):
     try:
        return	DjangocmsBlogLatestpostspluginCategories.objects.get(name=name)
     except DjangocmsBlogLatestpostspluginCategories.DoesNotExist:
        return None

  def resolve_DjangocmsBlogPost_by_name(root, info, name):
     try:
        return	DjangocmsBlogPost.objects.get(name=name)
     except DjangocmsBlogPost.DoesNotExist:
        return None

  def resolve_DjangocmsBlogPostCategories_by_name(root, info, name):
     try:
        return	DjangocmsBlogPostCategories.objects.get(name=name)
     except DjangocmsBlogPostCategories.DoesNotExist:
        return None

  def resolve_DjangocmsBlogPostRelated_by_name(root, info, name):
     try:
        return	DjangocmsBlogPostRelated.objects.get(name=name)
     except DjangocmsBlogPostRelated.DoesNotExist:
        return None

  def resolve_DjangocmsBlogPostSites_by_name(root, info, name):
     try:
        return	DjangocmsBlogPostSites.objects.get(name=name)
     except DjangocmsBlogPostSites.DoesNotExist:
        return None

  def resolve_DjangocmsBlogPostTranslation_by_name(root, info, name):
     try:
        return	DjangocmsBlogPostTranslation.objects.get(name=name)
     except DjangocmsBlogPostTranslation.DoesNotExist:
        return None

  def resolve_DjangocmsFileFile_by_name(root, info, name):
     try:
        return	DjangocmsFileFile.objects.get(name=name)
     except DjangocmsFileFile.DoesNotExist:
        return None

  def resolve_DjangocmsFileFolder_by_name(root, info, name):
     try:
        return	DjangocmsFileFolder.objects.get(name=name)
     except DjangocmsFileFolder.DoesNotExist:
        return None

  def resolve_DjangocmsGooglemapGooglemap_by_name(root, info, name):
     try:
        return	DjangocmsGooglemapGooglemap.objects.get(name=name)
     except DjangocmsGooglemapGooglemap.DoesNotExist:
        return None

  def resolve_DjangocmsGooglemapGooglemapmarker_by_name(root, info, name):
     try:
        return	DjangocmsGooglemapGooglemapmarker.objects.get(name=name)
     except DjangocmsGooglemapGooglemapmarker.DoesNotExist:
        return None

  def resolve_DjangocmsGooglemapGooglemaproute_by_name(root, info, name):
     try:
        return	DjangocmsGooglemapGooglemaproute.objects.get(name=name)
     except DjangocmsGooglemapGooglemaproute.DoesNotExist:
        return None

  def resolve_DjangocmsHistoryPlaceholderaction_by_name(root, info, name):
     try:
        return	DjangocmsHistoryPlaceholderaction.objects.get(name=name)
     except DjangocmsHistoryPlaceholderaction.DoesNotExist:
        return None

  def resolve_DjangocmsHistoryPlaceholderoperation_by_name(root, info, name):
     try:
        return	DjangocmsHistoryPlaceholderoperation.objects.get(name=name)
     except DjangocmsHistoryPlaceholderoperation.DoesNotExist:
        return None

  def resolve_DjangocmsIconIcon_by_name(root, info, name):
     try:
        return	DjangocmsIconIcon.objects.get(name=name)
     except DjangocmsIconIcon.DoesNotExist:
        return None

  def resolve_DjangocmsLinkLink_by_name(root, info, name):
     try:
        return	DjangocmsLinkLink.objects.get(name=name)
     except DjangocmsLinkLink.DoesNotExist:
        return None

  def resolve_DjangocmsMapsMaps_by_name(root, info, name):
     try:
        return	DjangocmsMapsMaps.objects.get(name=name)
     except DjangocmsMapsMaps.DoesNotExist:
        return None

  def resolve_DjangocmsPicturePicture_by_name(root, info, name):
     try:
        return	DjangocmsPicturePicture.objects.get(name=name)
     except DjangocmsPicturePicture.DoesNotExist:
        return None

  def resolve_DjangocmsStyleStyle_by_name(root, info, name):
     try:
        return	DjangocmsStyleStyle.objects.get(name=name)
     except DjangocmsStyleStyle.DoesNotExist:
        return None

  def resolve_DjangocmsTextCkeditorText_by_name(root, info, name):
     try:
        return	DjangocmsTextCkeditorText.objects.get(name=name)
     except DjangocmsTextCkeditorText.DoesNotExist:
        return None

  def resolve_DjangocmsVideoVideoplayer_by_name(root, info, name):
     try:
        return	DjangocmsVideoVideoplayer.objects.get(name=name)
     except DjangocmsVideoVideoplayer.DoesNotExist:
        return None

  def resolve_DjangocmsVideoVideosource_by_name(root, info, name):
     try:
        return	DjangocmsVideoVideosource.objects.get(name=name)
     except DjangocmsVideoVideosource.DoesNotExist:
        return None

  def resolve_DjangocmsVideoVideotrack_by_name(root, info, name):
     try:
        return	DjangocmsVideoVideotrack.objects.get(name=name)
     except DjangocmsVideoVideotrack.DoesNotExist:
        return None

  def resolve_DjangoContent_by_name(root, info, name):
     try:
        return	DjangoContent.objects.get(name=name)
     except DjangoContent.DoesNotExist:
        return None

  def resolve_DjangoFlatpage_by_name(root, info, name):
     try:
        return	DjangoFlatpage.objects.get(name=name)
     except DjangoFlatpage.DoesNotExist:
        return None

  def resolve_DjangoFlatpageSites_by_name(root, info, name):
     try:
        return	DjangoFlatpageSites.objects.get(name=name)
     except DjangoFlatpageSites.DoesNotExist:
        return None

  def resolve_DjangoMigrations_by_name(root, info, name):
     try:
        return	DjangoMigrations.objects.get(name=name)
     except DjangoMigrations.DoesNotExist:
        return None

  def resolve_DjangoSession_by_name(root, info, name):
     try:
        return	DjangoSession.objects.get(name=name)
     except DjangoSession.DoesNotExist:
        return None

  def resolve_DjangoSite_by_name(root, info, name):
     try:
        return	DjangoSite.objects.get(name=name)
     except DjangoSite.DoesNotExist:
        return None

  def resolve_EasyThumbnailsSource_by_name(root, info, name):
     try:
        return	EasyThumbnailsSource.objects.get(name=name)
     except EasyThumbnailsSource.DoesNotExist:
        return None

  def resolve_EasyThumbnailsThumbnail_by_name(root, info, name):
     try:
        return	EasyThumbnailsThumbnail.objects.get(name=name)
     except EasyThumbnailsThumbnail.DoesNotExist:
        return None

  def resolve_EasyThumbnailsThumbnaildimensions_by_name(root, info, name):
     try:
        return	EasyThumbnailsThumbnaildimensions.objects.get(name=name)
     except EasyThumbnailsThumbnaildimensions.DoesNotExist:
        return None

  def resolve_FilerClipboard_by_name(root, info, name):
     try:
        return	FilerClipboard.objects.get(name=name)
     except FilerClipboard.DoesNotExist:
        return None

  def resolve_FilerClipboarditem_by_name(root, info, name):
     try:
        return	FilerClipboarditem.objects.get(name=name)
     except FilerClipboarditem.DoesNotExist:
        return None

  def resolve_FilerFile_by_name(root, info, name):
     try:
        return	FilerFile.objects.get(name=name)
     except FilerFile.DoesNotExist:
        return None

  def resolve_FilerFolder_by_name(root, info, name):
     try:
        return	FilerFolder.objects.get(name=name)
     except FilerFolder.DoesNotExist:
        return None

  def resolve_FilerFolderpermission_by_name(root, info, name):
     try:
        return	FilerFolderpermission.objects.get(name=name)
     except FilerFolderpermission.DoesNotExist:
        return None

  def resolve_FilerImage_by_name(root, info, name):
     try:
        return	FilerImage.objects.get(name=name)
     except FilerImage.DoesNotExist:
        return None

  def resolve_FilerThumbnailoption_by_name(root, info, name):
     try:
        return	FilerThumbnailoption.objects.get(name=name)
     except FilerThumbnailoption.DoesNotExist:
        return None

  def resolve_MenusCachekey_by_name(root, info, name):
     try:
        return	MenusCachekey.objects.get(name=name)
     except MenusCachekey.DoesNotExist:
        return None

  def resolve_OfferBenefit_by_name(root, info, name):
     try:
        return	OfferBenefit.objects.get(name=name)
     except OfferBenefit.DoesNotExist:
        return None

  def resolve_OfferCondition_by_name(root, info, name):
     try:
        return	OfferCondition.objects.get(name=name)
     except OfferCondition.DoesNotExist:
        return None

  def resolve_OfferConditionaloffer_by_name(root, info, name):
     try:
        return	OfferConditionaloffer.objects.get(name=name)
     except OfferConditionaloffer.DoesNotExist:
        return None

  def resolve_OfferConditionalofferCombinations_by_name(root, info, name):
     try:
        return	OfferConditionalofferCombinations.objects.get(name=name)
     except OfferConditionalofferCombinations.DoesNotExist:
        return None

  def resolve_OfferRange_by_name(root, info, name):
     try:
        return	OfferRange.objects.get(name=name)
     except OfferRange.DoesNotExist:
        return None

  def resolve_OfferRangeClasses_by_name(root, info, name):
     try:
        return	OfferRangeClasses.objects.get(name=name)
     except OfferRangeClasses.DoesNotExist:
        return None

  def resolve_OfferRangeExcludedProducts_by_name(root, info, name):
     try:
        return	OfferRangeExcludedProducts.objects.get(name=name)
     except OfferRangeExcludedProducts.DoesNotExist:
        return None

  def resolve_OfferRangeIncludedCategories_by_name(root, info, name):
     try:
        return	OfferRangeIncludedCategories.objects.get(name=name)
     except OfferRangeIncludedCategories.DoesNotExist:
        return None

  def resolve_OfferRangeproduct_by_name(root, info, name):
     try:
        return	OfferRangeproduct.objects.get(name=name)
     except OfferRangeproduct.DoesNotExist:
        return None

  def resolve_OfferRangeproductfileupload_by_name(root, info, name):
     try:
        return	OfferRangeproductfileupload.objects.get(name=name)
     except OfferRangeproductfileupload.DoesNotExist:
        return None

  def resolve_OrderBillingaddress_by_name(root, info, name):
     try:
        return	OrderBillingaddress.objects.get(name=name)
     except OrderBillingaddress.DoesNotExist:
        return None

  def resolve_OrderCommunicationevent_by_name(root, info, name):
     try:
        return	OrderCommunicationevent.objects.get(name=name)
     except OrderCommunicationevent.DoesNotExist:
        return None

  def resolve_OrderLine_by_name(root, info, name):
     try:
        return	OrderLine.objects.get(name=name)
     except OrderLine.DoesNotExist:
        return None

  def resolve_OrderLineattribute_by_name(root, info, name):
     try:
        return	OrderLineattribute.objects.get(name=name)
     except OrderLineattribute.DoesNotExist:
        return None

  def resolve_OrderLineprice_by_name(root, info, name):
     try:
        return	OrderLineprice.objects.get(name=name)
     except OrderLineprice.DoesNotExist:
        return None

  def resolve_OrderOrder_by_name(root, info, name):
     try:
        return	OrderOrder.objects.get(name=name)
     except OrderOrder.DoesNotExist:
        return None

  def resolve_OrderOrderdiscount_by_name(root, info, name):
     try:
        return	OrderOrderdiscount.objects.get(name=name)
     except OrderOrderdiscount.DoesNotExist:
        return None

  def resolve_OrderOrdernote_by_name(root, info, name):
     try:
        return	OrderOrdernote.objects.get(name=name)
     except OrderOrdernote.DoesNotExist:
        return None

  def resolve_OrderOrderstatuschange_by_name(root, info, name):
     try:
        return	OrderOrderstatuschange.objects.get(name=name)
     except OrderOrderstatuschange.DoesNotExist:
        return None

  def resolve_OrderPaymentevent_by_name(root, info, name):
     try:
        return	OrderPaymentevent.objects.get(name=name)
     except OrderPaymentevent.DoesNotExist:
        return None

  def resolve_OrderPaymenteventquantity_by_name(root, info, name):
     try:
        return	OrderPaymenteventquantity.objects.get(name=name)
     except OrderPaymenteventquantity.DoesNotExist:
        return None

  def resolve_OrderPaymenteventtype_by_name(root, info, name):
     try:
        return	OrderPaymenteventtype.objects.get(name=name)
     except OrderPaymenteventtype.DoesNotExist:
        return None

  def resolve_OrderShippingaddress_by_name(root, info, name):
     try:
        return	OrderShippingaddress.objects.get(name=name)
     except OrderShippingaddress.DoesNotExist:
        return None

  def resolve_OrderShippingevent_by_name(root, info, name):
     try:
        return	OrderShippingevent.objects.get(name=name)
     except OrderShippingevent.DoesNotExist:
        return None

  def resolve_OrderShippingeventquantity_by_name(root, info, name):
     try:
        return	OrderShippingeventquantity.objects.get(name=name)
     except OrderShippingeventquantity.DoesNotExist:
        return None

  def resolve_OrderShippingeventtype_by_name(root, info, name):
     try:
        return	OrderShippingeventtype.objects.get(name=name)
     except OrderShippingeventtype.DoesNotExist:
        return None

  def resolve_OrderSurcharge_by_name(root, info, name):
     try:
        return	OrderSurcharge.objects.get(name=name)
     except OrderSurcharge.DoesNotExist:
        return None

  def resolve_OscarapiApikey_by_name(root, info, name):
     try:
        return	OscarapiApikey.objects.get(name=name)
     except OscarapiApikey.DoesNotExist:
        return None

  def resolve_OscarInvoicesInvoice_by_name(root, info, name):
     try:
        return	OscarInvoicesInvoice.objects.get(name=name)
     except OscarInvoicesInvoice.DoesNotExist:
        return None

  def resolve_OscarInvoicesLegalentity_by_name(root, info, name):
     try:
        return	OscarInvoicesLegalentity.objects.get(name=name)
     except OscarInvoicesLegalentity.DoesNotExist:
        return None

  def resolve_OscarInvoicesLegalentityaddress_by_name(root, info, name):
     try:
        return	OscarInvoicesLegalentityaddress.objects.get(name=name)
     except OscarInvoicesLegalentityaddress.DoesNotExist:
        return None

  def resolve_PartnerPartner_by_name(root, info, name):
     try:
        return	PartnerPartner.objects.get(name=name)
     except PartnerPartner.DoesNotExist:
        return None

  def resolve_PartnerPartneraddress_by_name(root, info, name):
     try:
        return	PartnerPartneraddress.objects.get(name=name)
     except PartnerPartneraddress.DoesNotExist:
        return None

  def resolve_PartnerPartnerUsers_by_name(root, info, name):
     try:
        return	PartnerPartnerUsers.objects.get(name=name)
     except PartnerPartnerUsers.DoesNotExist:
        return None

  def resolve_PartnerStockalert_by_name(root, info, name):
     try:
        return	PartnerStockalert.objects.get(name=name)
     except PartnerStockalert.DoesNotExist:
        return None

  def resolve_PartnerStockrecord_by_name(root, info, name):
     try:
        return	PartnerStockrecord.objects.get(name=name)
     except PartnerStockrecord.DoesNotExist:
        return None

  def resolve_Payment_by_name(root, info, name):
     try:
        return	Payment.objects.get(name=name)
     except Payment.DoesNotExist:
        return None

  def resolve_PaymentBankcard_by_name(root, info, name):
     try:
        return	PaymentBankcard.objects.get(name=name)
     except PaymentBankcard.DoesNotExist:
        return None

  def resolve_PaymentSource_by_name(root, info, name):
     try:
        return	PaymentSource.objects.get(name=name)
     except PaymentSource.DoesNotExist:
        return None

  def resolve_PaymentSourcetype_by_name(root, info, name):
     try:
        return	PaymentSourcetype.objects.get(name=name)
     except PaymentSourcetype.DoesNotExist:
        return None

  def resolve_PaymentTransaction_by_name(root, info, name):
     try:
        return	PaymentTransaction.objects.get(name=name)
     except PaymentTransaction.DoesNotExist:
        return None

  def resolve_PaypalExpresstransaction_by_name(root, info, name):
     try:
        return	PaypalExpresstransaction.objects.get(name=name)
     except PaypalExpresstransaction.DoesNotExist:
        return None

  def resolve_PaypalPayflowtransaction_by_name(root, info, name):
     try:
        return	PaypalPayflowtransaction.objects.get(name=name)
     except PaypalPayflowtransaction.DoesNotExist:
        return None

  def resolve_PhotologueGallery_by_name(root, info, name):
     try:
        return	PhotologueGallery.objects.get(name=name)
     except PhotologueGallery.DoesNotExist:
        return None

  def resolve_PhotologueGalleryPhotos_by_name(root, info, name):
     try:
        return	PhotologueGalleryPhotos.objects.get(name=name)
     except PhotologueGalleryPhotos.DoesNotExist:
        return None

  def resolve_PhotologueGallerySites_by_name(root, info, name):
     try:
        return	PhotologueGallerySites.objects.get(name=name)
     except PhotologueGallerySites.DoesNotExist:
        return None

  def resolve_PhotologuePhoto_by_name(root, info, name):
     try:
        return	PhotologuePhoto.objects.get(name=name)
     except PhotologuePhoto.DoesNotExist:
        return None

  def resolve_PhotologuePhotoeffect_by_name(root, info, name):
     try:
        return	PhotologuePhotoeffect.objects.get(name=name)
     except PhotologuePhotoeffect.DoesNotExist:
        return None

  def resolve_PhotologuePhotoSites_by_name(root, info, name):
     try:
        return	PhotologuePhotoSites.objects.get(name=name)
     except PhotologuePhotoSites.DoesNotExist:
        return None

  def resolve_PhotologuePhotosize_by_name(root, info, name):
     try:
        return	PhotologuePhotosize.objects.get(name=name)
     except PhotologuePhotosize.DoesNotExist:
        return None

  def resolve_PhotologueWatermark_by_name(root, info, name):
     try:
        return	PhotologueWatermark.objects.get(name=name)
     except PhotologueWatermark.DoesNotExist:
        return None

  def resolve_PinaxBadgesBadgeaward_by_name(root, info, name):
     try:
        return	PinaxBadgesBadgeaward.objects.get(name=name)
     except PinaxBadgesBadgeaward.DoesNotExist:
        return None

  def resolve_PinaxEventsEvent_by_name(root, info, name):
     try:
        return	PinaxEventsEvent.objects.get(name=name)
     except PinaxEventsEvent.DoesNotExist:
        return None

  def resolve_PinaxMessagesMessage_by_name(root, info, name):
     try:
        return	PinaxMessagesMessage.objects.get(name=name)
     except PinaxMessagesMessage.DoesNotExist:
        return None

  def resolve_PinaxMessagesThread_by_name(root, info, name):
     try:
        return	PinaxMessagesThread.objects.get(name=name)
     except PinaxMessagesThread.DoesNotExist:
        return None

  def resolve_PinaxMessagesUserthread_by_name(root, info, name):
     try:
        return	PinaxMessagesUserthread.objects.get(name=name)
     except PinaxMessagesUserthread.DoesNotExist:
        return None

  def resolve_Product_by_name(root, info, name):
     try:
        return	Product.objects.get(name=name)
     except Product.DoesNotExist:
        return None

  def resolve_ReviewsProductreview_by_name(root, info, name):
     try:
        return	ReviewsProductreview.objects.get(name=name)
     except ReviewsProductreview.DoesNotExist:
        return None

  def resolve_ReviewsVote_by_name(root, info, name):
     try:
        return	ReviewsVote.objects.get(name=name)
     except ReviewsVote.DoesNotExist:
        return None

  def resolve_SalesLineTransaction_by_name(root, info, name):
     try:
        return	SalesLineTransaction.objects.get(name=name)
     except SalesLineTransaction.DoesNotExist:
        return None

  def resolve_ShippingOrderanditemcharges_by_name(root, info, name):
     try:
        return	ShippingOrderanditemcharges.objects.get(name=name)
     except ShippingOrderanditemcharges.DoesNotExist:
        return None

  def resolve_ShippingOrderanditemchargesCountries_by_name(root, info, name):
     try:
        return	ShippingOrderanditemchargesCountries.objects.get(name=name)
     except ShippingOrderanditemchargesCountries.DoesNotExist:
        return None

  def resolve_ShippingWeightband_by_name(root, info, name):
     try:
        return	ShippingWeightband.objects.get(name=name)
     except ShippingWeightband.DoesNotExist:
        return None

  def resolve_ShippingWeightbased_by_name(root, info, name):
     try:
        return	ShippingWeightbased.objects.get(name=name)
     except ShippingWeightbased.DoesNotExist:
        return None

  def resolve_ShippingWeightbasedCountries_by_name(root, info, name):
     try:
        return	ShippingWeightbasedCountries.objects.get(name=name)
     except ShippingWeightbasedCountries.DoesNotExist:
        return None

  def resolve_TaggitTag_by_name(root, info, name):
     try:
        return	TaggitTag.objects.get(name=name)
     except TaggitTag.DoesNotExist:
        return None

  def resolve_TaggitTaggeditem_by_name(root, info, name):
     try:
        return	TaggitTaggeditem.objects.get(name=name)
     except TaggitTaggeditem.DoesNotExist:
        return None

  def resolve_TestimonialsTestimonial_by_name(root, info, name):
     try:
        return	TestimonialsTestimonial.objects.get(name=name)
     except TestimonialsTestimonial.DoesNotExist:
        return None

  def resolve_ThumbnailKvstore_by_name(root, info, name):
     try:
        return	ThumbnailKvstore.objects.get(name=name)
     except ThumbnailKvstore.DoesNotExist:
        return None

  def resolve_VoucherVoucher_by_name(root, info, name):
     try:
        return	VoucherVoucher.objects.get(name=name)
     except VoucherVoucher.DoesNotExist:
        return None

  def resolve_VoucherVoucherapplication_by_name(root, info, name):
     try:
        return	VoucherVoucherapplication.objects.get(name=name)
     except VoucherVoucherapplication.DoesNotExist:
        return None

  def resolve_VoucherVoucherOffers_by_name(root, info, name):
     try:
        return	VoucherVoucherOffers.objects.get(name=name)
     except VoucherVoucherOffers.DoesNotExist:
        return None

  def resolve_VoucherVoucherset_by_name(root, info, name):
     try:
        return	VoucherVoucherset.objects.get(name=name)
     except VoucherVoucherset.DoesNotExist:
        return None

  def resolve_WishlistsLine_by_name(root, info, name):
     try:
        return	WishlistsLine.objects.get(name=name)
     except WishlistsLine.DoesNotExist:
        return None

  def resolve_WishlistsWishlist_by_name(root, info, name):
     try:
        return	WishlistsWishlist.objects.get(name=name)
     except WishlistsWishlist.DoesNotExist:
        return None


schema = graphene.Schema(query=Query)
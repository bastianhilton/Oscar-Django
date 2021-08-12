# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressCountry(models.Model):
    iso_3166_1_a2 = models.CharField(primary_key=True, max_length=2)
    iso_3166_1_a3 = models.CharField(max_length=3)
    iso_3166_1_numeric = models.CharField(max_length=3)
    printable_name = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    display_order = models.SmallIntegerField()
    is_shipping_country = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'address_country'


class AddressUseraddress(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    phone_number = models.CharField(max_length=128)
    notes = models.TextField()
    is_default_for_shipping = models.BooleanField()
    is_default_for_billing = models.BooleanField()
    num_orders_as_shipping_address = models.IntegerField()
    hash = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    num_orders_as_billing_address = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address_useraddress'
        unique_together = (('user', 'hash'),)


class AdvancedFiltersAdvancedfilter(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    b64_query = models.CharField(max_length=2048)
    model = models.CharField(max_length=64, blank=True, null=True)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advanced_filters_advancedfilter'


class AdvancedFiltersAdvancedfilterGroups(models.Model):
    advancedfilter = models.ForeignKey(AdvancedFiltersAdvancedfilter, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'advanced_filters_advancedfilter_groups'
        unique_together = (('advancedfilter', 'group'),)


class AdvancedFiltersAdvancedfilterUsers(models.Model):
    advancedfilter = models.ForeignKey(AdvancedFiltersAdvancedfilter, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'advanced_filters_advancedfilter_users'
        unique_together = (('advancedfilter', 'user'),)


class AnalyticsProductrecord(models.Model):
    num_views = models.IntegerField()
    num_basket_additions = models.IntegerField()
    num_purchases = models.IntegerField()
    score = models.FloatField()
    product = models.ForeignKey('CatalogueProduct', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'analytics_productrecord'


class AnalyticsUserproductview(models.Model):
    date_created = models.DateTimeField()
    product = models.ForeignKey('CatalogueProduct', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytics_userproductview'


class AnalyticsUserrecord(models.Model):
    num_product_views = models.IntegerField()
    num_basket_additions = models.IntegerField()
    num_orders = models.IntegerField()
    num_order_lines = models.IntegerField()
    num_order_items = models.IntegerField()
    total_spent = models.DecimalField(max_digits=12, decimal_places=2)
    date_last_order = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'analytics_userrecord'


class AnalyticsUsersearch(models.Model):
    query = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'analytics_usersearch'


class AnnouncementsAnnouncement(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    creation_date = models.DateTimeField()
    site_wide = models.BooleanField()
    members_only = models.BooleanField()
    dismissal_type = models.IntegerField()
    publish_start = models.DateTimeField()
    publish_end = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'announcements_announcement'


class AnnouncementsDismissal(models.Model):
    dismissed_at = models.DateTimeField()
    announcement = models.ForeignKey(AnnouncementsAnnouncement, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'announcements_dismissal'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BasketBasket(models.Model):
    status = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    date_merged = models.DateTimeField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket_basket'


class BasketBasketVouchers(models.Model):
    basket = models.ForeignKey(BasketBasket, models.DO_NOTHING)
    voucher = models.ForeignKey('VoucherVoucher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'basket_basket_vouchers'
        unique_together = (('basket', 'voucher'),)


class BasketLine(models.Model):
    line_reference = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price_currency = models.CharField(max_length=12)
    price_excl_tax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField()
    basket = models.ForeignKey(BasketBasket, models.DO_NOTHING)
    product = models.ForeignKey('CatalogueProduct', models.DO_NOTHING)
    stockrecord = models.ForeignKey('PartnerStockrecord', models.DO_NOTHING)
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'basket_line'
        unique_together = (('basket', 'line_reference'),)


class BasketLineattribute(models.Model):
    value = models.CharField(max_length=255)
    line = models.ForeignKey(BasketLine, models.DO_NOTHING)
    option = models.ForeignKey('CatalogueOption', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'basket_lineattribute'


class Bootstrap4AlertsBootstrap4Alerts(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    alert_context = models.CharField(max_length=255)
    alert_dismissable = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_alerts_bootstrap4alerts'


class Bootstrap4BadgeBootstrap4Badge(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    badge_text = models.CharField(max_length=255)
    badge_context = models.CharField(max_length=255)
    badge_pills = models.BooleanField()
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_badge_bootstrap4badge'


class Bootstrap4CardBootstrap4Card(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    card_type = models.CharField(max_length=255)
    card_context = models.CharField(max_length=255)
    card_alignment = models.CharField(max_length=255)
    card_outline = models.BooleanField()
    card_text_color = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_card_bootstrap4card'


class Bootstrap4CardBootstrap4Cardinner(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    inner_type = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_card_bootstrap4cardinner'


class Bootstrap4CarouselBootstrap4Carousel(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    template = models.CharField(max_length=255)
    carousel_interval = models.IntegerField()
    carousel_controls = models.BooleanField()
    carousel_indicators = models.BooleanField()
    carousel_keyboard = models.BooleanField()
    carousel_pause = models.CharField(max_length=255)
    carousel_ride = models.CharField(max_length=255)
    carousel_wrap = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()
    carousel_aspect_ratio = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bootstrap4_carousel_bootstrap4carousel'


class Bootstrap4CarouselBootstrap4Carouselslide(models.Model):
    template = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    external_link = models.CharField(max_length=2040)
    anchor = models.CharField(max_length=255)
    mailto = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    attributes = models.TextField()
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    carousel_content = models.TextField()
    tag_type = models.CharField(max_length=255)
    carousel_image = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    internal_link = models.ForeignKey('CmsPage', models.DO_NOTHING, blank=True, null=True)
    file_link = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootstrap4_carousel_bootstrap4carouselslide'


class Bootstrap4CollapseBootstrap4Collapse(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    siblings = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_collapse_bootstrap4collapse'


class Bootstrap4CollapseBootstrap4Collapsecontainer(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    identifier = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_collapse_bootstrap4collapsecontainer'


class Bootstrap4CollapseBootstrap4Collapsetrigger(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    identifier = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_collapse_bootstrap4collapsetrigger'


class Bootstrap4ContentBootstrap4Blockquote(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    quote_content = models.TextField()
    quote_origin = models.TextField()
    quote_alignment = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_content_bootstrap4blockquote'


class Bootstrap4ContentBootstrap4Code(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    code_content = models.TextField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_content_bootstrap4code'


class Bootstrap4ContentBootstrap4Figure(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    figure_caption = models.CharField(max_length=255)
    figure_alignment = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_content_bootstrap4figure'


class Bootstrap4GridBootstrap4Gridcolumn(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    column_type = models.CharField(max_length=255)
    column_alignment = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()
    xs_col = models.IntegerField(blank=True, null=True)
    xs_order = models.IntegerField(blank=True, null=True)
    xs_ml = models.BooleanField()
    xs_mr = models.BooleanField()
    sm_col = models.IntegerField(blank=True, null=True)
    sm_order = models.IntegerField(blank=True, null=True)
    sm_ml = models.BooleanField()
    sm_mr = models.BooleanField()
    md_col = models.IntegerField(blank=True, null=True)
    md_order = models.IntegerField(blank=True, null=True)
    md_ml = models.BooleanField()
    md_mr = models.BooleanField()
    lg_col = models.IntegerField(blank=True, null=True)
    lg_order = models.IntegerField(blank=True, null=True)
    lg_ml = models.BooleanField()
    lg_mr = models.BooleanField()
    xl_col = models.IntegerField(blank=True, null=True)
    xl_order = models.IntegerField(blank=True, null=True)
    xl_ml = models.BooleanField()
    xl_mr = models.BooleanField()
    lg_offset = models.IntegerField(blank=True, null=True)
    md_offset = models.IntegerField(blank=True, null=True)
    sm_offset = models.IntegerField(blank=True, null=True)
    xl_offset = models.IntegerField(blank=True, null=True)
    xs_offset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootstrap4_grid_bootstrap4gridcolumn'


class Bootstrap4GridBootstrap4Gridcontainer(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    container_type = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_grid_bootstrap4gridcontainer'


class Bootstrap4GridBootstrap4Gridrow(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    vertical_alignment = models.CharField(max_length=255)
    horizontal_alignment = models.CharField(max_length=255)
    gutters = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_grid_bootstrap4gridrow'


class Bootstrap4JumbotronBootstrap4Jumbotron(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    fluid = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_jumbotron_bootstrap4jumbotron'


class Bootstrap4LinkBootstrap4Link(models.Model):
    template = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    external_link = models.CharField(max_length=2040)
    anchor = models.CharField(max_length=255)
    mailto = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    attributes = models.TextField()
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    link_type = models.CharField(max_length=255)
    link_context = models.CharField(max_length=255)
    link_size = models.CharField(max_length=255)
    link_outline = models.BooleanField()
    link_block = models.BooleanField()
    internal_link = models.ForeignKey('CmsPage', models.DO_NOTHING, blank=True, null=True)
    icon_left = models.CharField(max_length=255)
    icon_right = models.CharField(max_length=255)
    file_link = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootstrap4_link_bootstrap4link'


class Bootstrap4ListgroupBootstrap4Listgroup(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    list_group_flush = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_listgroup_bootstrap4listgroup'


class Bootstrap4ListgroupBootstrap4Listgroupitem(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    list_context = models.CharField(max_length=255)
    list_state = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_listgroup_bootstrap4listgroupitem'


class Bootstrap4MediaBootstrap4Media(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_media_bootstrap4media'


class Bootstrap4MediaBootstrap4Mediabody(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_media_bootstrap4mediabody'


class Bootstrap4PictureBootstrap4Picture(models.Model):
    template = models.CharField(max_length=255)
    external_picture = models.CharField(max_length=255, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    alignment = models.CharField(max_length=255)
    caption_text = models.TextField(blank=True, null=True)
    attributes = models.TextField()
    link_url = models.CharField(max_length=2040, blank=True, null=True)
    link_target = models.CharField(max_length=255)
    link_attributes = models.TextField()
    use_automatic_scaling = models.BooleanField()
    use_no_cropping = models.BooleanField()
    use_crop = models.BooleanField()
    use_upscale = models.BooleanField()
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    picture_fluid = models.BooleanField()
    picture_rounded = models.BooleanField()
    picture_thumbnail = models.BooleanField()
    link_page = models.ForeignKey('CmsPage', models.DO_NOTHING, blank=True, null=True)
    picture = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    thumbnail_options = models.ForeignKey('FilerThumbnailoption', models.DO_NOTHING, blank=True, null=True)
    use_responsive_image = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'bootstrap4_picture_bootstrap4picture'


class Bootstrap4TabsBootstrap4Tab(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    template = models.CharField(max_length=255)
    tab_type = models.CharField(max_length=255)
    tab_alignment = models.CharField(max_length=255)
    tab_index = models.IntegerField(blank=True, null=True)
    tab_effect = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_tabs_bootstrap4tab'


class Bootstrap4TabsBootstrap4Tabitem(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    tab_title = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_tabs_bootstrap4tabitem'


class Bootstrap4UtilitiesBootstrap4Spacing(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    space_property = models.CharField(max_length=255)
    space_sides = models.CharField(max_length=255)
    space_size = models.CharField(max_length=255)
    space_device = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_utilities_bootstrap4spacing'


class CatalogueAttributeoption(models.Model):
    option = models.CharField(max_length=255)
    group = models.ForeignKey('CatalogueAttributeoptiongroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_attributeoption'
        unique_together = (('group', 'option'),)


class CatalogueAttributeoptiongroup(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'catalogue_attributeoptiongroup'


class CatalogueCategory(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.IntegerField()
    numchild = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255)
    ancestors_are_public = models.BooleanField()
    is_public = models.BooleanField()
    meta_description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_category'


class CatalogueOption(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(unique=True, max_length=128)
    type = models.CharField(max_length=255)
    required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'catalogue_option'


class CatalogueProduct(models.Model):
    structure = models.CharField(max_length=10)
    upc = models.CharField(unique=True, max_length=64, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    is_discountable = models.BooleanField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    product_class = models.ForeignKey('CatalogueProductclass', models.DO_NOTHING, blank=True, null=True)
    is_public = models.BooleanField()
    meta_description = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_product'


class CatalogueProductProductOptions(models.Model):
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    option = models.ForeignKey(CatalogueOption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_product_product_options'
        unique_together = (('product', 'option'),)


class CatalogueProductattribute(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    type = models.CharField(max_length=20)
    required = models.BooleanField()
    option_group = models.ForeignKey(CatalogueAttributeoptiongroup, models.DO_NOTHING, blank=True, null=True)
    product_class = models.ForeignKey('CatalogueProductclass', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_productattribute'


class CatalogueProductattributevalue(models.Model):
    value_text = models.TextField(blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    value_boolean = models.BooleanField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    value_richtext = models.TextField(blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    value_file = models.CharField(max_length=255, blank=True, null=True)
    value_image = models.CharField(max_length=255, blank=True, null=True)
    entity_object_id = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(CatalogueProductattribute, models.DO_NOTHING)
    entity_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    value_option = models.ForeignKey(CatalogueAttributeoption, models.DO_NOTHING, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue_productattributevalue'
        unique_together = (('attribute', 'product'),)


class CatalogueProductattributevalueValueMultiOption(models.Model):
    productattributevalue = models.ForeignKey(CatalogueProductattributevalue, models.DO_NOTHING)
    attributeoption = models.ForeignKey(CatalogueAttributeoption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productattributevalue_value_multi_option'
        unique_together = (('productattributevalue', 'attributeoption'),)


class CatalogueProductcategory(models.Model):
    category = models.ForeignKey(CatalogueCategory, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productcategory'
        unique_together = (('product', 'category'),)


class CatalogueProductclass(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(unique=True, max_length=128)
    requires_shipping = models.BooleanField()
    track_stock = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'catalogue_productclass'


class CatalogueProductclassOptions(models.Model):
    productclass = models.ForeignKey(CatalogueProductclass, models.DO_NOTHING)
    option = models.ForeignKey(CatalogueOption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productclass_options'
        unique_together = (('productclass', 'option'),)


class CatalogueProductimage(models.Model):
    original = models.CharField(max_length=255)
    caption = models.CharField(max_length=200)
    display_order = models.IntegerField()
    date_created = models.DateTimeField()
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productimage'


class CatalogueProductrecommendation(models.Model):
    ranking = models.SmallIntegerField()
    primary = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    recommendation = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogue_productrecommendation'
        unique_together = (('primary', 'recommendation'),)


class CmsAliaspluginmodel(models.Model):
    cmsplugin_ptr = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    plugin = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, blank=True, null=True)
    alias_placeholder = models.ForeignKey('CmsPlaceholder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_aliaspluginmodel'


class CmsCmsplugin(models.Model):
    position = models.SmallIntegerField()
    language = models.CharField(max_length=15)
    plugin_type = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
    changed_date = models.DateTimeField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    placeholder = models.ForeignKey('CmsPlaceholder', models.DO_NOTHING, blank=True, null=True)
    depth = models.IntegerField()
    numchild = models.IntegerField()
    path = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'cms_cmsplugin'


class CmsGlobalpagepermission(models.Model):
    can_change = models.BooleanField()
    can_add = models.BooleanField()
    can_delete = models.BooleanField()
    can_change_advanced_settings = models.BooleanField()
    can_publish = models.BooleanField()
    can_change_permissions = models.BooleanField()
    can_move_page = models.BooleanField()
    can_view = models.BooleanField()
    can_recover_page = models.BooleanField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission'


class CmsGlobalpagepermissionSites(models.Model):
    globalpagepermission = models.ForeignKey(CmsGlobalpagepermission, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission_sites'
        unique_together = (('globalpagepermission', 'site'),)


class CmsPage(models.Model):
    created_by = models.CharField(max_length=255)
    changed_by = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    changed_date = models.DateTimeField()
    publication_date = models.DateTimeField(blank=True, null=True)
    publication_end_date = models.DateTimeField(blank=True, null=True)
    in_navigation = models.BooleanField()
    soft_root = models.BooleanField()
    reverse_id = models.CharField(max_length=40, blank=True, null=True)
    navigation_extenders = models.CharField(max_length=80, blank=True, null=True)
    template = models.CharField(max_length=100)
    login_required = models.BooleanField()
    limit_visibility_in_menu = models.SmallIntegerField(blank=True, null=True)
    is_home = models.BooleanField()
    application_urls = models.CharField(max_length=200, blank=True, null=True)
    application_namespace = models.CharField(max_length=200, blank=True, null=True)
    publisher_is_draft = models.BooleanField()
    languages = models.CharField(max_length=255, blank=True, null=True)
    xframe_options = models.IntegerField()
    publisher_public = models.ForeignKey('self', models.DO_NOTHING, unique=True, blank=True, null=True)
    is_page_type = models.BooleanField()
    node = models.ForeignKey('CmsTreenode', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_page'
        unique_together = (('node', 'publisher_is_draft'),)


class CmsPagePlaceholders(models.Model):
    page = models.ForeignKey(CmsPage, models.DO_NOTHING)
    placeholder = models.ForeignKey('CmsPlaceholder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_page_placeholders'
        unique_together = (('page', 'placeholder'),)


class CmsPagepermission(models.Model):
    can_change = models.BooleanField()
    can_add = models.BooleanField()
    can_delete = models.BooleanField()
    can_change_advanced_settings = models.BooleanField()
    can_publish = models.BooleanField()
    can_change_permissions = models.BooleanField()
    can_move_page = models.BooleanField()
    can_view = models.BooleanField()
    grant_on = models.IntegerField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_pagepermission'


class CmsPageuser(models.Model):
    user_ptr = models.ForeignKey(AuthUser, models.DO_NOTHING, primary_key=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_pageuser'


class CmsPageusergroup(models.Model):
    group_ptr = models.ForeignKey(AuthGroup, models.DO_NOTHING, primary_key=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_pageusergroup'


class CmsPlaceholder(models.Model):
    slot = models.CharField(max_length=255)
    default_width = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_placeholder'


class CmsPlaceholderreference(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255)
    placeholder_ref = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_placeholderreference'


class CmsStaticplaceholder(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    dirty = models.BooleanField()
    creation_method = models.CharField(max_length=20)
    draft = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    public = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_staticplaceholder'
        unique_together = (('code', 'site'),)


class CmsTitle(models.Model):
    language = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255, blank=True, null=True)
    menu_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    has_url_overwrite = models.BooleanField()
    redirect = models.CharField(max_length=2048, blank=True, null=True)
    creation_date = models.DateTimeField()
    published = models.BooleanField()
    publisher_is_draft = models.BooleanField()
    publisher_state = models.SmallIntegerField()
    page = models.ForeignKey(CmsPage, models.DO_NOTHING)
    publisher_public = models.ForeignKey('self', models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_title'
        unique_together = (('language', 'page'),)


class CmsTreenode(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.IntegerField()
    numchild = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_treenode'


class CmsUrlconfrevision(models.Model):
    revision = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cms_urlconfrevision'


class CmsUsersettings(models.Model):
    language = models.CharField(max_length=10)
    clipboard = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'cms_usersettings'


class CommunicationCommunicationeventtype(models.Model):
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    email_subject_template = models.CharField(max_length=255, blank=True, null=True)
    email_body_template = models.TextField(blank=True, null=True)
    email_body_html_template = models.TextField(blank=True, null=True)
    sms_template = models.CharField(max_length=170, blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'communication_communicationeventtype'


class CommunicationEmail(models.Model):
    subject = models.TextField()
    body_text = models.TextField()
    body_html = models.TextField()
    date_sent = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_email'


class CommunicationNotification(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    location = models.CharField(max_length=32)
    date_sent = models.DateTimeField()
    date_read = models.DateTimeField(blank=True, null=True)
    recipient = models.ForeignKey(AuthUser, models.DO_NOTHING)
    sender = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_notification'


class CustomerProductalert(models.Model):
    email = models.CharField(max_length=254)
    key = models.CharField(max_length=128)
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    date_confirmed = models.DateTimeField(blank=True, null=True)
    date_cancelled = models.DateTimeField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_productalert'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoFlatpage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_flatpage'


class DjangoFlatpageSites(models.Model):
    flatpage = models.ForeignKey(DjangoFlatpage, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_flatpage_sites'
        unique_together = (('flatpage', 'site'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjangocmsBlogAuthorentriesplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    latest_posts = models.IntegerField()
    app_config = models.ForeignKey('DjangocmsBlogBlogconfig', models.DO_NOTHING, blank=True, null=True)
    current_site = models.BooleanField()
    template_folder = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_authorentriesplugin'


class DjangocmsBlogAuthorentriespluginAuthors(models.Model):
    authorentriesplugin = models.ForeignKey(DjangocmsBlogAuthorentriesplugin, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_authorentriesplugin_authors'
        unique_together = (('authorentriesplugin', 'user'),)


class DjangocmsBlogBlogcategory(models.Model):
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    app_config = models.ForeignKey('DjangocmsBlogBlogconfig', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_blogcategory'


class DjangocmsBlogBlogcategoryTranslation(models.Model):
    language_code = models.CharField(max_length=15)
    name = models.CharField(max_length=752)
    slug = models.CharField(max_length=752)
    master = models.ForeignKey(DjangocmsBlogBlogcategory, models.DO_NOTHING, blank=True, null=True)
    meta_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_blog_blogcategory_translation'
        unique_together = (('language_code', 'master'), ('language_code', 'slug'),)


class DjangocmsBlogBlogconfig(models.Model):
    type = models.CharField(max_length=100)
    namespace = models.CharField(unique=True, max_length=100)
    app_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_blog_blogconfig'


class DjangocmsBlogBlogconfigTranslation(models.Model):
    language_code = models.CharField(max_length=15)
    app_title = models.CharField(max_length=234)
    master = models.ForeignKey(DjangocmsBlogBlogconfig, models.DO_NOTHING, blank=True, null=True)
    object_name = models.CharField(max_length=234)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_blogconfig_translation'
        unique_together = (('language_code', 'master'),)


class DjangocmsBlogGenericblogplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    app_config = models.ForeignKey(DjangocmsBlogBlogconfig, models.DO_NOTHING, blank=True, null=True)
    current_site = models.BooleanField()
    template_folder = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_genericblogplugin'


class DjangocmsBlogLatestpostsplugin(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    latest_posts = models.IntegerField()
    app_config = models.ForeignKey(DjangocmsBlogBlogconfig, models.DO_NOTHING, blank=True, null=True)
    current_site = models.BooleanField()
    template_folder = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_latestpostsplugin'


class DjangocmsBlogLatestpostspluginCategories(models.Model):
    latestpostsplugin = models.ForeignKey(DjangocmsBlogLatestpostsplugin, models.DO_NOTHING)
    blogcategory = models.ForeignKey(DjangocmsBlogBlogcategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_latestpostsplugin_categories'
        unique_together = (('latestpostsplugin', 'blogcategory'),)


class DjangocmsBlogPost(models.Model):
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_published = models.DateTimeField(blank=True, null=True)
    date_published_end = models.DateTimeField(blank=True, null=True)
    publish = models.BooleanField()
    enable_comments = models.BooleanField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    content = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    main_image = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    app_config = models.ForeignKey(DjangocmsBlogBlogconfig, models.DO_NOTHING, blank=True, null=True)
    main_image_full = models.ForeignKey('FilerThumbnailoption', models.DO_NOTHING, blank=True, null=True)
    main_image_thumbnail = models.ForeignKey('FilerThumbnailoption', models.DO_NOTHING, blank=True, null=True)
    liveblog = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    enable_liveblog = models.BooleanField()
    date_featured = models.DateTimeField(blank=True, null=True)
    media = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_post'


class DjangocmsBlogPostCategories(models.Model):
    post = models.ForeignKey(DjangocmsBlogPost, models.DO_NOTHING)
    blogcategory = models.ForeignKey(DjangocmsBlogBlogcategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_post_categories'
        unique_together = (('post', 'blogcategory'),)


class DjangocmsBlogPostRelated(models.Model):
    from_post = models.ForeignKey(DjangocmsBlogPost, models.DO_NOTHING)
    to_post = models.ForeignKey(DjangocmsBlogPost, models.DO_NOTHING)
    sort_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'djangocms_blog_post_related'
        unique_together = (('from_post', 'to_post'),)


class DjangocmsBlogPostSites(models.Model):
    post = models.ForeignKey(DjangocmsBlogPost, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_post_sites'
        unique_together = (('post', 'site'),)


class DjangocmsBlogPostTranslation(models.Model):
    language_code = models.CharField(max_length=15)
    title = models.CharField(max_length=752)
    slug = models.CharField(max_length=752)
    abstract = models.TextField()
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    meta_title = models.CharField(max_length=2000)
    post_text = models.TextField()
    master = models.ForeignKey(DjangocmsBlogPost, models.DO_NOTHING, blank=True, null=True)
    subtitle = models.CharField(max_length=767)

    class Meta:
        managed = False
        db_table = 'djangocms_blog_post_translation'
        unique_together = (('language_code', 'master'), ('language_code', 'slug'),)


class DjangocmsFileFile(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    file_name = models.CharField(max_length=255)
    link_target = models.CharField(max_length=255)
    link_title = models.CharField(max_length=255)
    file_src = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    template = models.CharField(max_length=255)
    show_file_size = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'djangocms_file_file'


class DjangocmsFileFolder(models.Model):
    template = models.CharField(max_length=255)
    link_target = models.CharField(max_length=255)
    show_file_size = models.BooleanField()
    attributes = models.TextField()
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    folder_src = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_file_folder'


class DjangocmsGooglemapGooglemap(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=255)
    zoom = models.SmallIntegerField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    width = models.CharField(max_length=6)
    height = models.CharField(max_length=6)
    scrollwheel = models.BooleanField()
    double_click_zoom = models.BooleanField()
    draggable = models.BooleanField()
    keyboard_shortcuts = models.BooleanField()
    pan_control = models.BooleanField()
    zoom_control = models.BooleanField()
    street_view_control = models.BooleanField()
    style = models.TextField()
    fullscreen_control = models.BooleanField()
    map_type_control = models.CharField(max_length=255)
    rotate_control = models.BooleanField()
    scale_control = models.BooleanField()
    template = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_googlemap_googlemap'


class DjangocmsGooglemapGooglemapmarker(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    show_content = models.BooleanField()
    info_content = models.TextField()
    icon = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_googlemap_googlemapmarker'


class DjangocmsGooglemapGooglemaproute(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_mode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_googlemap_googlemaproute'


class DjangocmsHistoryPlaceholderaction(models.Model):
    action = models.CharField(max_length=30)
    pre_action_data = models.TextField()
    post_action_data = models.TextField()
    language = models.CharField(max_length=15)
    order = models.IntegerField()
    operation = models.ForeignKey('DjangocmsHistoryPlaceholderoperation', models.DO_NOTHING)
    placeholder = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djangocms_history_placeholderaction'
        unique_together = (('operation', 'order'),)


class DjangocmsHistoryPlaceholderoperation(models.Model):
    operation_type = models.CharField(max_length=30)
    token = models.CharField(max_length=120)
    origin = models.CharField(max_length=255)
    language = models.CharField(max_length=15)
    user_session_key = models.CharField(max_length=120)
    date_created = models.DateTimeField()
    is_applied = models.BooleanField()
    is_archived = models.BooleanField()
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'djangocms_history_placeholderoperation'


class DjangocmsIconIcon(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    icon = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_icon_icon'


class DjangocmsLinkLink(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255)
    external_link = models.CharField(max_length=2040)
    anchor = models.CharField(max_length=255)
    mailto = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    internal_link = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    template = models.CharField(max_length=255)
    file_link = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_link_link'


class DjangocmsMapsMaps(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    map_provider = models.CharField(max_length=16)
    title = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    style = models.TextField()
    zoom = models.SmallIntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    route_planer_title = models.CharField(max_length=150, blank=True, null=True)
    route_planer = models.BooleanField()
    width = models.CharField(max_length=6)
    height = models.CharField(max_length=6)
    info_window = models.BooleanField()
    scrollwheel = models.BooleanField()
    double_click_zoom = models.BooleanField()
    draggable = models.BooleanField()
    keyboard_shortcuts = models.BooleanField()
    pan_control = models.BooleanField()
    zoom_control = models.BooleanField()
    street_view_control = models.BooleanField()
    layers_control = models.BooleanField()
    scale_bar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'djangocms_maps_maps'


class DjangocmsPicturePicture(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    link_url = models.CharField(max_length=2040, blank=True, null=True)
    alignment = models.CharField(max_length=255)
    link_page = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    picture = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    caption_text = models.TextField(blank=True, null=True)
    link_attributes = models.TextField()
    link_target = models.CharField(max_length=255)
    use_automatic_scaling = models.BooleanField()
    use_crop = models.BooleanField()
    use_no_cropping = models.BooleanField()
    use_upscale = models.BooleanField()
    thumbnail_options = models.ForeignKey('FilerThumbnailoption', models.DO_NOTHING, blank=True, null=True)
    external_picture = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255)
    use_responsive_image = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'djangocms_picture_picture'


class DjangocmsStyleStyle(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    class_name = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    padding_left = models.SmallIntegerField(blank=True, null=True)
    padding_right = models.SmallIntegerField(blank=True, null=True)
    padding_top = models.SmallIntegerField(blank=True, null=True)
    padding_bottom = models.SmallIntegerField(blank=True, null=True)
    margin_left = models.SmallIntegerField(blank=True, null=True)
    margin_right = models.SmallIntegerField(blank=True, null=True)
    margin_top = models.SmallIntegerField(blank=True, null=True)
    margin_bottom = models.SmallIntegerField(blank=True, null=True)
    additional_classes = models.CharField(max_length=255)
    attributes = models.TextField()
    id_name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    template = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_style_style'


class DjangocmsTextCkeditorText(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_text_ckeditor_text'


class DjangocmsVideoVideoplayer(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    embed_link = models.CharField(max_length=255)
    poster = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    label = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    parameters = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_video_videoplayer'


class DjangocmsVideoVideosource(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    text_title = models.CharField(max_length=255)
    text_description = models.TextField()
    attributes = models.TextField()
    source_file = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_video_videosource'


class DjangocmsVideoVideotrack(models.Model):
    cmsplugin_ptr = models.ForeignKey(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    kind = models.CharField(max_length=255)
    srclang = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    attributes = models.TextField()
    src = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_video_videotrack'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.ForeignKey(EasyThumbnailsThumbnail, models.DO_NOTHING, unique=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class FilerClipboard(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboard'


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, models.DO_NOTHING)
    file = models.ForeignKey('FilerFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboarditem'


class FilerFile(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    field_file_size = models.BigIntegerField(db_column='_file_size', blank=True, null=True)  # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40)
    has_all_mandatory_data = models.BooleanField()
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    is_public = models.BooleanField()
    folder = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    polymorphic_ctype = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    mime_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'filer_file'


class FilerFolder(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folder'
        unique_together = (('parent', 'name'),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField()
    everybody = models.BooleanField()
    can_edit = models.SmallIntegerField(blank=True, null=True)
    can_read = models.SmallIntegerField(blank=True, null=True)
    can_add_children = models.SmallIntegerField(blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folderpermission'


class FilerImage(models.Model):
    file_ptr = models.ForeignKey(FilerFile, models.DO_NOTHING, primary_key=True)
    field_height = models.IntegerField(db_column='_height', blank=True, null=True)  # Field renamed because it started with '_'.
    field_width = models.IntegerField(db_column='_width', blank=True, null=True)  # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, blank=True, null=True)
    default_caption = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField()
    must_always_publish_copyright = models.BooleanField()
    subject_location = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filer_image'


class FilerThumbnailoption(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    crop = models.BooleanField()
    upscale = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'filer_thumbnailoption'


class MenusCachekey(models.Model):
    language = models.CharField(max_length=255)
    site = models.IntegerField()
    key = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'menus_cachekey'


class OfferBenefit(models.Model):
    type = models.CharField(max_length=128)
    value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    max_affected_items = models.IntegerField(blank=True, null=True)
    proxy_class = models.CharField(max_length=255, blank=True, null=True)
    range = models.ForeignKey('OfferRange', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_benefit'


class OfferCondition(models.Model):
    type = models.CharField(max_length=128)
    value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    proxy_class = models.CharField(max_length=255, blank=True, null=True)
    range = models.ForeignKey('OfferRange', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer_condition'


class OfferConditionaloffer(models.Model):
    name = models.CharField(unique=True, max_length=128)
    slug = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    offer_type = models.CharField(max_length=128)
    status = models.CharField(max_length=64)
    priority = models.IntegerField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    max_global_applications = models.IntegerField(blank=True, null=True)
    max_user_applications = models.IntegerField(blank=True, null=True)
    max_basket_applications = models.IntegerField(blank=True, null=True)
    max_discount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_discount = models.DecimalField(max_digits=12, decimal_places=2)
    num_applications = models.IntegerField()
    num_orders = models.IntegerField()
    redirect_url = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    benefit = models.ForeignKey(OfferBenefit, models.DO_NOTHING)
    condition = models.ForeignKey(OfferCondition, models.DO_NOTHING)
    exclusive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'offer_conditionaloffer'


class OfferConditionalofferCombinations(models.Model):
    from_conditionaloffer = models.ForeignKey(OfferConditionaloffer, models.DO_NOTHING)
    to_conditionaloffer = models.ForeignKey(OfferConditionaloffer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_conditionaloffer_combinations'
        unique_together = (('from_conditionaloffer', 'to_conditionaloffer'),)


class OfferRange(models.Model):
    name = models.CharField(unique=True, max_length=128)
    slug = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    is_public = models.BooleanField()
    includes_all_products = models.BooleanField()
    proxy_class = models.CharField(unique=True, max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'offer_range'


class OfferRangeClasses(models.Model):
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    productclass = models.ForeignKey(CatalogueProductclass, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_range_classes'
        unique_together = (('range', 'productclass'),)


class OfferRangeExcludedProducts(models.Model):
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_range_excluded_products'
        unique_together = (('range', 'product'),)


class OfferRangeIncludedCategories(models.Model):
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    category = models.ForeignKey(CatalogueCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_range_included_categories'
        unique_together = (('range', 'category'),)


class OfferRangeproduct(models.Model):
    display_order = models.IntegerField()
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_rangeproduct'
        unique_together = (('range', 'product'),)


class OfferRangeproductfileupload(models.Model):
    filepath = models.CharField(max_length=255)
    size = models.IntegerField()
    date_uploaded = models.DateTimeField()
    status = models.CharField(max_length=32)
    error_message = models.CharField(max_length=255)
    date_processed = models.DateTimeField(blank=True, null=True)
    num_new_skus = models.IntegerField(blank=True, null=True)
    num_unknown_skus = models.IntegerField(blank=True, null=True)
    num_duplicate_skus = models.IntegerField(blank=True, null=True)
    range = models.ForeignKey(OfferRange, models.DO_NOTHING)
    uploaded_by = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offer_rangeproductfileupload'


class OrderBillingaddress(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_billingaddress'


class OrderCommunicationevent(models.Model):
    date_created = models.DateTimeField()
    event_type = models.ForeignKey(CommunicationCommunicationeventtype, models.DO_NOTHING)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_communicationevent'


class OrderLine(models.Model):
    partner_name = models.CharField(max_length=128)
    partner_sku = models.CharField(max_length=128)
    partner_line_reference = models.CharField(max_length=128)
    partner_line_notes = models.TextField()
    title = models.CharField(max_length=255)
    upc = models.CharField(max_length=128, blank=True, null=True)
    quantity = models.IntegerField()
    line_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    line_price_excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    line_price_before_discounts_incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    line_price_before_discounts_excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    unit_price_excl_tax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=255)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)
    partner = models.ForeignKey('PartnerPartner', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING, blank=True, null=True)
    stockrecord = models.ForeignKey('PartnerStockrecord', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_line'


class OrderLineattribute(models.Model):
    type = models.CharField(max_length=128)
    value = models.CharField(max_length=255)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)
    option = models.ForeignKey(CatalogueOption, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_lineattribute'


class OrderLineprice(models.Model):
    quantity = models.IntegerField()
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    price_excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)
    order = models.ForeignKey('OrderOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_lineprice'


class OrderOrder(models.Model):
    number = models.CharField(unique=True, max_length=128)
    currency = models.CharField(max_length=12)
    total_incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    total_excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    status = models.CharField(max_length=100)
    guest_email = models.CharField(max_length=254)
    date_placed = models.DateTimeField()
    basket = models.ForeignKey(BasketBasket, models.DO_NOTHING, blank=True, null=True)
    billing_address = models.ForeignKey(OrderBillingaddress, models.DO_NOTHING, blank=True, null=True)
    shipping_address = models.ForeignKey('OrderShippingaddress', models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_order'


class OrderOrderdiscount(models.Model):
    category = models.CharField(max_length=64)
    offer_id = models.IntegerField(blank=True, null=True)
    offer_name = models.CharField(max_length=128)
    voucher_id = models.IntegerField(blank=True, null=True)
    voucher_code = models.CharField(max_length=128)
    frequency = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    message = models.TextField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_orderdiscount'


class OrderOrdernote(models.Model):
    note_type = models.CharField(max_length=128)
    message = models.TextField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_ordernote'


class OrderOrderstatuschange(models.Model):
    old_status = models.CharField(max_length=100)
    new_status = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_orderstatuschange'


class OrderPaymentevent(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    event_type = models.ForeignKey('OrderPaymenteventtype', models.DO_NOTHING)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    shipping_event = models.ForeignKey('OrderShippingevent', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_paymentevent'


class OrderPaymenteventquantity(models.Model):
    quantity = models.IntegerField()
    event = models.ForeignKey(OrderPaymentevent, models.DO_NOTHING)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_paymenteventquantity'
        unique_together = (('event', 'line'),)


class OrderPaymenteventtype(models.Model):
    name = models.CharField(unique=True, max_length=128)
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'order_paymenteventtype'


class OrderShippingaddress(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    phone_number = models.CharField(max_length=128)
    notes = models.TextField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_shippingaddress'


class OrderShippingevent(models.Model):
    notes = models.TextField()
    date_created = models.DateTimeField()
    event_type = models.ForeignKey('OrderShippingeventtype', models.DO_NOTHING)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_shippingevent'


class OrderShippingeventquantity(models.Model):
    quantity = models.IntegerField()
    event = models.ForeignKey(OrderShippingevent, models.DO_NOTHING)
    line = models.ForeignKey(OrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_shippingeventquantity'
        unique_together = (('event', 'line'),)


class OrderShippingeventtype(models.Model):
    name = models.CharField(unique=True, max_length=255)
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'order_shippingeventtype'


class OrderSurcharge(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    incl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    excl_tax = models.DecimalField(max_digits=12, decimal_places=2)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_surcharge'


class OscarInvoicesInvoice(models.Model):
    number = models.CharField(unique=True, max_length=128)
    notes = models.TextField(blank=True, null=True)
    document = models.CharField(max_length=255, blank=True, null=True)
    legal_entity = models.ForeignKey('OscarInvoicesLegalentity', models.DO_NOTHING)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oscar_invoices_invoice'


class OscarInvoicesLegalentity(models.Model):
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    business_name = models.CharField(max_length=255)
    vat_number = models.CharField(max_length=20)
    logo = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    web_site = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oscar_invoices_legalentity'


class OscarInvoicesLegalentityaddress(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    phone_number = models.CharField(max_length=128)
    fax_number = models.CharField(max_length=128)
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    legal_entity = models.ForeignKey(OscarInvoicesLegalentity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'oscar_invoices_legalentityaddress'


class OscarapiApikey(models.Model):
    key = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'oscarapi_apikey'


class PartnerPartner(models.Model):
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'partner_partner'


class PartnerPartnerUsers(models.Model):
    partner = models.ForeignKey(PartnerPartner, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_partner_users'
        unique_together = (('partner', 'user'),)


class PartnerPartneraddress(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255)
    line3 = models.CharField(max_length=255)
    line4 = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=64)
    search_text = models.TextField()
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)
    partner = models.ForeignKey(PartnerPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_partneraddress'


class PartnerStockalert(models.Model):
    threshold = models.IntegerField()
    status = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    date_closed = models.DateTimeField(blank=True, null=True)
    stockrecord = models.ForeignKey('PartnerStockrecord', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_stockalert'


class PartnerStockrecord(models.Model):
    partner_sku = models.CharField(max_length=128)
    price_currency = models.CharField(max_length=12)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    num_in_stock = models.IntegerField(blank=True, null=True)
    num_allocated = models.IntegerField(blank=True, null=True)
    low_stock_threshold = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    partner = models.ForeignKey(PartnerPartner, models.DO_NOTHING)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'partner_stockrecord'
        unique_together = (('partner', 'partner_sku'),)


class PaymentBankcard(models.Model):
    card_type = models.CharField(max_length=128)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=32)
    expiry_date = models.DateField()
    partner_reference = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_bankcard'


class PaymentSource(models.Model):
    currency = models.CharField(max_length=12)
    amount_allocated = models.DecimalField(max_digits=12, decimal_places=2)
    amount_debited = models.DecimalField(max_digits=12, decimal_places=2)
    amount_refunded = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=255)
    label = models.CharField(max_length=128)
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    source_type = models.ForeignKey('PaymentSourcetype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_source'


class PaymentSourcetype(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(unique=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'payment_sourcetype'


class PaymentTransaction(models.Model):
    txn_type = models.CharField(max_length=128)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    source = models.ForeignKey(PaymentSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PaypalExpresstransaction(models.Model):
    raw_request = models.TextField()
    raw_response = models.TextField()
    response_time = models.FloatField()
    date_created = models.DateTimeField()
    method = models.CharField(max_length=32)
    version = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=8, blank=True, null=True)
    ack = models.CharField(max_length=32)
    correlation_id = models.CharField(max_length=32, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)
    error_code = models.CharField(max_length=32, blank=True, null=True)
    error_message = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_expresstransaction'


class PaypalPayflowtransaction(models.Model):
    raw_request = models.TextField()
    raw_response = models.TextField()
    response_time = models.FloatField()
    date_created = models.DateTimeField()
    comment1 = models.CharField(max_length=128)
    trxtype = models.CharField(max_length=12)
    tender = models.CharField(max_length=12, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pnref = models.CharField(unique=True, max_length=32, blank=True, null=True)
    ppref = models.CharField(max_length=32, blank=True, null=True)
    result = models.CharField(max_length=32, blank=True, null=True)
    respmsg = models.CharField(max_length=512)
    authcode = models.CharField(max_length=32, blank=True, null=True)
    cvv2match = models.CharField(max_length=12, blank=True, null=True)
    avsaddr = models.CharField(max_length=1, blank=True, null=True)
    avszip = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_payflowtransaction'


class PhotologueGallery(models.Model):
    date_added = models.DateTimeField()
    title = models.CharField(unique=True, max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    description = models.TextField()
    is_public = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'photologue_gallery'


class PhotologueGalleryPhotos(models.Model):
    sort_value = models.IntegerField()
    gallery = models.ForeignKey(PhotologueGallery, models.DO_NOTHING)
    photo = models.ForeignKey('PhotologuePhoto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photologue_gallery_photos'
        unique_together = (('gallery', 'photo'),)


class PhotologueGallerySites(models.Model):
    gallery = models.ForeignKey(PhotologueGallery, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photologue_gallery_sites'
        unique_together = (('gallery', 'site'),)


class PhotologuePhoto(models.Model):
    image = models.CharField(max_length=100)
    date_taken = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField()
    crop_from = models.CharField(max_length=10)
    title = models.CharField(unique=True, max_length=250)
    slug = models.CharField(unique=True, max_length=250)
    caption = models.TextField()
    date_added = models.DateTimeField()
    is_public = models.BooleanField()
    effect = models.ForeignKey('PhotologuePhotoeffect', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photologue_photo'


class PhotologuePhotoSites(models.Model):
    photo = models.ForeignKey(PhotologuePhoto, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photologue_photo_sites'
        unique_together = (('photo', 'site'),)


class PhotologuePhotoeffect(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    transpose_method = models.CharField(max_length=15)
    color = models.FloatField()
    brightness = models.FloatField()
    contrast = models.FloatField()
    sharpness = models.FloatField()
    filters = models.CharField(max_length=200)
    reflection_size = models.FloatField()
    reflection_strength = models.FloatField()
    background_color = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'photologue_photoeffect'


class PhotologuePhotosize(models.Model):
    name = models.CharField(unique=True, max_length=40)
    width = models.IntegerField()
    height = models.IntegerField()
    quality = models.IntegerField()
    upscale = models.BooleanField()
    crop = models.BooleanField()
    pre_cache = models.BooleanField()
    increment_count = models.BooleanField()
    effect = models.ForeignKey(PhotologuePhotoeffect, models.DO_NOTHING, blank=True, null=True)
    watermark = models.ForeignKey('PhotologueWatermark', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photologue_photosize'


class PhotologueWatermark(models.Model):
    name = models.CharField(unique=True, max_length=30)
    description = models.TextField()
    image = models.CharField(max_length=100)
    style = models.CharField(max_length=5)
    opacity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'photologue_watermark'


class PinaxBadgesBadgeaward(models.Model):
    awarded_at = models.DateTimeField()
    slug = models.CharField(max_length=255)
    level = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pinax_badges_badgeaward'


class PinaxEventsEvent(models.Model):
    image = models.CharField(max_length=100)
    where = models.CharField(max_length=200)
    what = models.TextField()
    what_html = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    published_at = models.DateTimeField()
    created_at = models.DateTimeField()
    title = models.CharField(max_length=200)
    url = models.TextField()
    secondary_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pinax_events_event'


class PinaxMessagesMessage(models.Model):
    sent_at = models.DateTimeField()
    content = models.TextField()
    sender = models.ForeignKey(AuthUser, models.DO_NOTHING)
    thread = models.ForeignKey('PinaxMessagesThread', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pinax_messages_message'


class PinaxMessagesThread(models.Model):
    subject = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'pinax_messages_thread'


class PinaxMessagesUserthread(models.Model):
    unread = models.BooleanField()
    deleted = models.BooleanField()
    thread = models.ForeignKey(PinaxMessagesThread, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pinax_messages_userthread'


class ReviewsProductreview(models.Model):
    score = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    homepage = models.CharField(max_length=200)
    status = models.SmallIntegerField()
    total_votes = models.IntegerField()
    delta_votes = models.IntegerField()
    date_created = models.DateTimeField()
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews_productreview'
        unique_together = (('product', 'user'),)


class ReviewsVote(models.Model):
    delta = models.SmallIntegerField()
    date_created = models.DateTimeField()
    review = models.ForeignKey(ReviewsProductreview, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_vote'
        unique_together = (('user', 'review'),)


class ShippingOrderanditemcharges(models.Model):
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    price_per_order = models.DecimalField(max_digits=12, decimal_places=2)
    price_per_item = models.DecimalField(max_digits=12, decimal_places=2)
    free_shipping_threshold = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_orderanditemcharges'


class ShippingOrderanditemchargesCountries(models.Model):
    orderanditemcharges = models.ForeignKey(ShippingOrderanditemcharges, models.DO_NOTHING)
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_orderanditemcharges_countries'
        unique_together = (('orderanditemcharges', 'country'),)


class ShippingWeightband(models.Model):
    upper_limit = models.DecimalField(max_digits=12, decimal_places=3)
    charge = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.ForeignKey('ShippingWeightbased', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_weightband'


class ShippingWeightbased(models.Model):
    code = models.CharField(unique=True, max_length=128)
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    default_weight = models.DecimalField(max_digits=12, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'shipping_weightbased'


class ShippingWeightbasedCountries(models.Model):
    weightbased = models.ForeignKey(ShippingWeightbased, models.DO_NOTHING)
    country = models.ForeignKey(AddressCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipping_weightbased_countries'
        unique_together = (('weightbased', 'country'),)


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class TestimonialsTestimonial(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    added = models.DateTimeField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'testimonials_testimonial'


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'


class VoucherVoucher(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(unique=True, max_length=128)
    usage = models.CharField(max_length=128)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    num_basket_additions = models.IntegerField()
    num_orders = models.IntegerField()
    total_discount = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateTimeField()
    voucher_set = models.ForeignKey('VoucherVoucherset', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_voucher'


class VoucherVoucherOffers(models.Model):
    voucher = models.ForeignKey(VoucherVoucher, models.DO_NOTHING)
    conditionaloffer = models.ForeignKey(OfferConditionaloffer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'voucher_voucher_offers'
        unique_together = (('voucher', 'conditionaloffer'),)


class VoucherVoucherapplication(models.Model):
    date_created = models.DateTimeField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    voucher = models.ForeignKey(VoucherVoucher, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'voucher_voucherapplication'


class VoucherVoucherset(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    code_length = models.IntegerField()
    description = models.TextField()
    date_created = models.DateTimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    offer = models.ForeignKey(OfferConditionaloffer, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_voucherset'


class WishlistsLine(models.Model):
    quantity = models.IntegerField()
    title = models.CharField(max_length=255)
    product = models.ForeignKey(CatalogueProduct, models.DO_NOTHING, blank=True, null=True)
    wishlist = models.ForeignKey('WishlistsWishlist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlists_line'
        unique_together = (('wishlist', 'product'),)


class WishlistsWishlist(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=6)
    visibility = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlists_wishlist'

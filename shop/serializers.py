from rest_framework.serializers import ModelSerializer
from shop.models import AddressCountry, AddressUseraddress, AldrynFormsEmailfieldplugin, AldrynFormsFieldplugin, AldrynFormsFieldsetplugin, AldrynFormsFileuploadfieldplugin, AldrynFormsFormbuttonplugin, AldrynFormsFormplugin, AldrynFormsFormpluginRecipients, AldrynFormsFormsubmission, AldrynFormsImageuploadfieldplugin, AldrynFormsOption, AldrynFormsTextareafieldplugin, AdvancedFiltersAdvancedfilter, AdvancedFiltersAdvancedfilterGroups, AdvancedFiltersAdvancedfilterUsers, AnalyticsProductrecord, AnalyticsUserproductview, AnalyticsUserrecord, AnalyticsUsersearch, AnnouncementsAnnouncement, AnnouncementsDismissal, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, BasketBasket, BasketBasketVouchers, BasketLine, BasketLineattribute, Bootstrap4AlertsBootstrap4Alerts, Bootstrap4BadgeBootstrap4Badge, Bootstrap4CardBootstrap4Card, Bootstrap4CardBootstrap4Cardinner, Bootstrap4CarouselBootstrap4Carousel, Bootstrap4CarouselBootstrap4Carouselslide, Bootstrap4CollapseBootstrap4Collapse, Bootstrap4CollapseBootstrap4Collapsecontainer, Bootstrap4CollapseBootstrap4Collapsetrigger, Bootstrap4ContentBootstrap4Blockquote, Bootstrap4ContentBootstrap4Code, Bootstrap4ContentBootstrap4Figure, Bootstrap4GridBootstrap4Gridcolumn, Bootstrap4GridBootstrap4Gridcontainer, Bootstrap4GridBootstrap4Gridrow, Bootstrap4JumbotronBootstrap4Jumbotron, Bootstrap4LinkBootstrap4Link, Bootstrap4ListgroupBootstrap4Listgroup, Bootstrap4ListgroupBootstrap4Listgroupitem, Bootstrap4MediaBootstrap4Media, Bootstrap4MediaBootstrap4Mediabody, Bootstrap4PictureBootstrap4Picture, Bootstrap4TabsBootstrap4Tab, Bootstrap4TabsBootstrap4Tabitem, Bootstrap4UtilitiesBootstrap4Spacing, CatalogueAttributeoption, CatalogueAttributeoptiongroup, CatalogueCategory, CatalogueOption, CatalogueProduct, CatalogueProductProductOptions, CatalogueProductattribute, CatalogueProductattributevalue, CatalogueProductattributevalueValueMultiOption, CatalogueProductcategory, CatalogueProductclass, CatalogueProductclassOptions, CatalogueProductimage, CatalogueProductrecommendation, CmsAliaspluginmodel, CmsCmsplugin, CmsGlobalpagepermission, CmsGlobalpagepermissionSites, CmsPage, CmsPagePlaceholders, CmsPagepermission, CmsPageuser, CmsPageusergroup, CmsPlaceholder, CmsPlaceholderreference, CmsStaticplaceholder, CmsTitle, CmsTreenode, CmsUrlconfrevision, CmsUsersettings, CommunicationCommunicationeventtype, CommunicationEmail, CommunicationNotification, CustomerProductalert, DjangoAdminLog, DjangoContent, DjangoFlatpage, DjangoFlatpageSites, DjangoMigrations, DjangoSession, DjangoSite, DjangocmsBlogAuthorentriesplugin, DjangocmsBlogAuthorentriespluginAuthors, DjangocmsBlogBlogcategory, DjangocmsBlogBlogcategoryTranslation, DjangocmsBlogBlogconfig, DjangocmsBlogBlogconfigTranslation, DjangocmsBlogGenericblogplugin, DjangocmsBlogLatestpostsplugin, DjangocmsBlogLatestpostspluginCategories, DjangocmsBlogPost, DjangocmsBlogPostCategories, DjangocmsBlogPostRelated, DjangocmsBlogPostSites, DjangocmsBlogPostTranslation, DjangocmsFileFile, DjangocmsFileFolder, DjangocmsGooglemapGooglemap, DjangocmsGooglemapGooglemapmarker, DjangocmsGooglemapGooglemaproute, DjangocmsHistoryPlaceholderaction, DjangocmsHistoryPlaceholderoperation, DjangocmsIconIcon, DjangocmsLinkLink, DjangocmsMapsMaps, DjangocmsPicturePicture, DjangocmsStyleStyle, DjangocmsTextCkeditorText, DjangocmsVideoVideoplayer, DjangocmsVideoVideosource, DjangocmsVideoVideotrack, EasyThumbnailsSource, EasyThumbnailsThumbnail, EasyThumbnailsThumbnaildimensions, FilerClipboard, FilerClipboarditem, FilerFile, FilerFolder, FilerFolderpermission, FilerImage, FilerThumbnailoption, MenusCachekey, OfferBenefit, OfferCondition, OfferConditionaloffer, OfferConditionalofferCombinations, OfferRange, OfferRangeClasses, OfferRangeExcludedProducts, OfferRangeIncludedCategories, OfferRangeproduct, OfferRangeproductfileupload, OrderBillingaddress, OrderCommunicationevent, OrderLine, OrderLineattribute, OrderLineprice, OrderOrder, OrderOrderdiscount, OrderOrdernote, OrderOrderstatuschange, OrderPaymentevent, OrderPaymenteventquantity, OrderPaymenteventtype, OrderShippingaddress, OrderShippingevent, OrderShippingeventquantity, OrderShippingeventtype, OrderSurcharge, OscarInvoicesInvoice, OscarInvoicesLegalentity, OscarInvoicesLegalentityaddress, OscarapiApikey, PartnerPartner, PartnerPartnerUsers, PartnerPartneraddress, PartnerStockalert, PartnerStockrecord, Payment, PaymentBankcard, PaymentSource, PaymentSourcetype, PaymentTransaction, PaypalExpresstransaction, PaypalPayflowtransaction, PhotologueGallery, PhotologueGalleryPhotos, PhotologueGallerySites, PhotologuePhoto, PhotologuePhotoSites, PhotologuePhotoeffect, PhotologuePhotosize, PhotologueWatermark, PinaxBadgesBadgeaward, PinaxEventsEvent, PinaxMessagesMessage, PinaxMessagesThread, PinaxMessagesUserthread, ReviewsProductreview, ReviewsVote, Client, Product, SalesLineTransaction, ShippingOrderanditemcharges, ShippingOrderanditemchargesCountries, ShippingWeightband, ShippingWeightbased, ShippingWeightbasedCountries, TaggitTag, TaggitTaggeditem, TestimonialsTestimonial, ThumbnailKvstore, VoucherVoucher, VoucherVoucherOffers, VoucherVoucherapplication, VoucherVoucherset, WishlistsLine, WishlistsWishlist


class AddressCountrySerializer(ModelSerializer):

    class Meta:
        model = AddressCountry
        depth = 0
        fields = '__all__'


class AddressUseraddressSerializer(ModelSerializer):

    class Meta:
        model = AddressUseraddress
        depth = 0
        fields = '__all__'


class AldrynFormsEmailfieldpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsEmailfieldplugin
        depth = 0
        fields = '__all__'


class AldrynFormsFieldpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFieldplugin
        depth = 0
        fields = '__all__'


class AldrynFormsFieldsetpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFieldsetplugin
        depth = 0
        fields = '__all__'


class AldrynFormsFileuploadfieldpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFileuploadfieldplugin
        depth = 0
        fields = '__all__'


class AldrynFormsFormbuttonpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFormbuttonplugin
        depth = 0
        fields = '__all__'


class AldrynFormsFormpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFormplugin
        depth = 0
        fields = '__all__'


class AldrynFormsFormpluginRecipientsSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFormpluginRecipients
        depth = 0
        fields = '__all__'


class AldrynFormsFormsubmissionSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsFormsubmission
        depth = 0
        fields = '__all__'


class AldrynFormsImageuploadfieldpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsImageuploadfieldplugin
        depth = 0
        fields = '__all__'


class AldrynFormsOptionSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsOption
        depth = 0
        fields = '__all__'


class AldrynFormsTextareafieldpluginSerializer(ModelSerializer):

    class Meta:
        model = AldrynFormsTextareafieldplugin
        depth = 0
        fields = '__all__'


class AdvancedFiltersAdvancedfilterSerializer(ModelSerializer):

    class Meta:
        model = AdvancedFiltersAdvancedfilter
        depth = 0
        fields = '__all__'


class AdvancedFiltersAdvancedfilterGroupsSerializer(ModelSerializer):

    class Meta:
        model = AdvancedFiltersAdvancedfilterGroups
        depth = 0
        fields = '__all__'


class AdvancedFiltersAdvancedfilterUsersSerializer(ModelSerializer):

    class Meta:
        model = AdvancedFiltersAdvancedfilterUsers
        depth = 0
        fields = '__all__'


class AnalyticsProductrecordSerializer(ModelSerializer):

    class Meta:
        model = AnalyticsProductrecord
        depth = 0
        fields = '__all__'


class AnalyticsUserproductviewSerializer(ModelSerializer):

    class Meta:
        model = AnalyticsUserproductview
        depth = 0
        fields = '__all__'


class AnalyticsUserrecordSerializer(ModelSerializer):

    class Meta:
        model = AnalyticsUserrecord
        depth = 0
        fields = '__all__'


class AnalyticsUsersearchSerializer(ModelSerializer):

    class Meta:
        model = AnalyticsUsersearch
        depth = 0
        fields = '__all__'


class AnnouncementsAnnouncementSerializer(ModelSerializer):

    class Meta:
        model = AnnouncementsAnnouncement
        depth = 0
        fields = '__all__'


class AnnouncementsDismissalSerializer(ModelSerializer):

    class Meta:
        model = AnnouncementsDismissal
        depth = 0
        fields = '__all__'


class AuthGroupSerializer(ModelSerializer):

    class Meta:
        model = AuthGroup
        depth = 0
        fields = '__all__'


class AuthGroupPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthGroupPermissions
        depth = 0
        fields = '__all__'


class AuthPermissionSerializer(ModelSerializer):

    class Meta:
        model = AuthPermission
        depth = 0
        fields = '__all__'


class AuthUserSerializer(ModelSerializer):

    class Meta:
        model = AuthUser
        depth = 0
        fields = '__all__'


class AuthUserGroupsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserGroups
        depth = 0
        fields = '__all__'


class AuthUserUserPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserUserPermissions
        depth = 0
        fields = '__all__'


class BasketBasketSerializer(ModelSerializer):

    class Meta:
        model = BasketBasket
        depth = 0
        fields = '__all__'


class BasketBasketVouchersSerializer(ModelSerializer):

    class Meta:
        model = BasketBasketVouchers
        depth = 0
        fields = '__all__'


class BasketLineSerializer(ModelSerializer):

    class Meta:
        model = BasketLine
        depth = 0
        fields = '__all__'


class BasketLineattributeSerializer(ModelSerializer):

    class Meta:
        model = BasketLineattribute
        depth = 0
        fields = '__all__'


class Bootstrap4AlertsBootstrap4AlertsSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4AlertsBootstrap4Alerts
        depth = 0
        fields = '__all__'


class Bootstrap4BadgeBootstrap4BadgeSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4BadgeBootstrap4Badge
        depth = 0
        fields = '__all__'


class Bootstrap4CardBootstrap4CardSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CardBootstrap4Card
        depth = 0
        fields = '__all__'


class Bootstrap4CardBootstrap4CardinnerSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CardBootstrap4Cardinner
        depth = 0
        fields = '__all__'


class Bootstrap4CarouselBootstrap4CarouselSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CarouselBootstrap4Carousel
        depth = 0
        fields = '__all__'


class Bootstrap4CarouselBootstrap4CarouselslideSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CarouselBootstrap4Carouselslide
        depth = 0
        fields = '__all__'


class Bootstrap4CollapseBootstrap4CollapseSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CollapseBootstrap4Collapse
        depth = 0
        fields = '__all__'


class Bootstrap4CollapseBootstrap4CollapsecontainerSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CollapseBootstrap4Collapsecontainer
        depth = 0
        fields = '__all__'


class Bootstrap4CollapseBootstrap4CollapsetriggerSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4CollapseBootstrap4Collapsetrigger
        depth = 0
        fields = '__all__'


class Bootstrap4ContentBootstrap4BlockquoteSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4ContentBootstrap4Blockquote
        depth = 0
        fields = '__all__'


class Bootstrap4ContentBootstrap4CodeSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4ContentBootstrap4Code
        depth = 0
        fields = '__all__'


class Bootstrap4ContentBootstrap4FigureSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4ContentBootstrap4Figure
        depth = 0
        fields = '__all__'


class Bootstrap4GridBootstrap4GridcolumnSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4GridBootstrap4Gridcolumn
        depth = 0
        fields = '__all__'


class Bootstrap4GridBootstrap4GridcontainerSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4GridBootstrap4Gridcontainer
        depth = 0
        fields = '__all__'


class Bootstrap4GridBootstrap4GridrowSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4GridBootstrap4Gridrow
        depth = 0
        fields = '__all__'


class Bootstrap4JumbotronBootstrap4JumbotronSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4JumbotronBootstrap4Jumbotron
        depth = 0
        fields = '__all__'


class Bootstrap4LinkBootstrap4LinkSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4LinkBootstrap4Link
        depth = 0
        fields = '__all__'


class Bootstrap4ListgroupBootstrap4ListgroupSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4ListgroupBootstrap4Listgroup
        depth = 0
        fields = '__all__'


class Bootstrap4ListgroupBootstrap4ListgroupitemSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4ListgroupBootstrap4Listgroupitem
        depth = 0
        fields = '__all__'


class Bootstrap4MediaBootstrap4MediaSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4MediaBootstrap4Media
        depth = 0
        fields = '__all__'


class Bootstrap4MediaBootstrap4MediabodySerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4MediaBootstrap4Mediabody
        depth = 0
        fields = '__all__'


class Bootstrap4PictureBootstrap4PictureSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4PictureBootstrap4Picture
        depth = 0
        fields = '__all__'


class Bootstrap4TabsBootstrap4TabSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4TabsBootstrap4Tab
        depth = 0
        fields = '__all__'


class Bootstrap4TabsBootstrap4TabitemSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4TabsBootstrap4Tabitem
        depth = 0
        fields = '__all__'


class Bootstrap4UtilitiesBootstrap4SpacingSerializer(ModelSerializer):

    class Meta:
        model = Bootstrap4UtilitiesBootstrap4Spacing
        depth = 0
        fields = '__all__'


class CatalogueAttributeoptionSerializer(ModelSerializer):

    class Meta:
        model = CatalogueAttributeoption
        depth = 0
        fields = '__all__'


class CatalogueAttributeoptiongroupSerializer(ModelSerializer):

    class Meta:
        model = CatalogueAttributeoptiongroup
        depth = 0
        fields = '__all__'


class CatalogueCategorySerializer(ModelSerializer):

    class Meta:
        model = CatalogueCategory
        depth = 0
        fields = '__all__'


class CatalogueOptionSerializer(ModelSerializer):

    class Meta:
        model = CatalogueOption
        depth = 0
        fields = '__all__'


class CatalogueProductSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProduct
        depth = 0
        fields = '__all__'


class CatalogueProductProductOptionsSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductProductOptions
        depth = 0
        fields = '__all__'


class CatalogueProductattributeSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductattribute
        depth = 0
        fields = '__all__'


class CatalogueProductattributevalueSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductattributevalue
        depth = 0
        fields = '__all__'


class CatalogueProductattributevalueValueMultiOptionSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductattributevalueValueMultiOption
        depth = 0
        fields = '__all__'


class CatalogueProductcategorySerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductcategory
        depth = 0
        fields = '__all__'


class CatalogueProductclassSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductclass
        depth = 0
        fields = '__all__'


class CatalogueProductclassOptionsSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductclassOptions
        depth = 0
        fields = '__all__'


class CatalogueProductimageSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductimage
        depth = 0
        fields = '__all__'


class CatalogueProductrecommendationSerializer(ModelSerializer):

    class Meta:
        model = CatalogueProductrecommendation
        depth = 0
        fields = '__all__'


class CmsAliaspluginmodelSerializer(ModelSerializer):

    class Meta:
        model = CmsAliaspluginmodel
        depth = 0
        fields = '__all__'


class CmsCmspluginSerializer(ModelSerializer):

    class Meta:
        model = CmsCmsplugin
        depth = 0
        fields = '__all__'


class CmsGlobalpagepermissionSerializer(ModelSerializer):

    class Meta:
        model = CmsGlobalpagepermission
        depth = 0
        fields = '__all__'


class CmsGlobalpagepermissionSitesSerializer(ModelSerializer):

    class Meta:
        model = CmsGlobalpagepermissionSites
        depth = 0
        fields = '__all__'


class CmsPageSerializer(ModelSerializer):

    class Meta:
        model = CmsPage
        depth = 0
        fields = '__all__'


class CmsPagePlaceholdersSerializer(ModelSerializer):

    class Meta:
        model = CmsPagePlaceholders
        depth = 0
        fields = '__all__'


class CmsPagepermissionSerializer(ModelSerializer):

    class Meta:
        model = CmsPagepermission
        depth = 0
        fields = '__all__'


class CmsPageuserSerializer(ModelSerializer):

    class Meta:
        model = CmsPageuser
        depth = 0
        fields = '__all__'


class CmsPageusergroupSerializer(ModelSerializer):

    class Meta:
        model = CmsPageusergroup
        depth = 0
        fields = '__all__'


class CmsPlaceholderSerializer(ModelSerializer):

    class Meta:
        model = CmsPlaceholder
        depth = 0
        fields = '__all__'


class CmsPlaceholderreferenceSerializer(ModelSerializer):

    class Meta:
        model = CmsPlaceholderreference
        depth = 0
        fields = '__all__'


class CmsStaticplaceholderSerializer(ModelSerializer):

    class Meta:
        model = CmsStaticplaceholder
        depth = 0
        fields = '__all__'


class CmsTitleSerializer(ModelSerializer):

    class Meta:
        model = CmsTitle
        depth = 0
        fields = '__all__'


class CmsTreenodeSerializer(ModelSerializer):

    class Meta:
        model = CmsTreenode
        depth = 0
        fields = '__all__'


class CmsUrlconfrevisionSerializer(ModelSerializer):

    class Meta:
        model = CmsUrlconfrevision
        depth = 0
        fields = '__all__'


class CmsUsersettingsSerializer(ModelSerializer):

    class Meta:
        model = CmsUsersettings
        depth = 0
        fields = '__all__'


class CommunicationCommunicationeventtypeSerializer(ModelSerializer):

    class Meta:
        model = CommunicationCommunicationeventtype
        depth = 0
        fields = '__all__'


class CommunicationEmailSerializer(ModelSerializer):

    class Meta:
        model = CommunicationEmail
        depth = 0
        fields = '__all__'


class CommunicationNotificationSerializer(ModelSerializer):

    class Meta:
        model = CommunicationNotification
        depth = 0
        fields = '__all__'


class CustomerProductalertSerializer(ModelSerializer):

    class Meta:
        model = CustomerProductalert
        depth = 0
        fields = '__all__'


class DjangoAdminLogSerializer(ModelSerializer):

    class Meta:
        model = DjangoAdminLog
        depth = 0
        fields = '__all__'


class DjangoContentSerializer(ModelSerializer):

    class Meta:
        model = DjangoContent
        depth = 0
        fields = '__all__'


class DjangoFlatpageSerializer(ModelSerializer):

    class Meta:
        model = DjangoFlatpage
        depth = 0
        fields = '__all__'


class DjangoFlatpageSitesSerializer(ModelSerializer):

    class Meta:
        model = DjangoFlatpageSites
        depth = 0
        fields = '__all__'


class DjangoMigrationsSerializer(ModelSerializer):

    class Meta:
        model = DjangoMigrations
        depth = 0
        fields = '__all__'


class DjangoSessionSerializer(ModelSerializer):

    class Meta:
        model = DjangoSession
        depth = 0
        fields = '__all__'


class DjangoSiteSerializer(ModelSerializer):

    class Meta:
        model = DjangoSite
        depth = 0
        fields = '__all__'


class DjangocmsBlogAuthorentriespluginSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogAuthorentriesplugin
        depth = 0
        fields = '__all__'


class DjangocmsBlogAuthorentriespluginAuthorsSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogAuthorentriespluginAuthors
        depth = 0
        fields = '__all__'


class DjangocmsBlogBlogcategorySerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogBlogcategory
        depth = 0
        fields = '__all__'


class DjangocmsBlogBlogcategoryTranslationSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogBlogcategoryTranslation
        depth = 0
        fields = '__all__'


class DjangocmsBlogBlogconfigSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogBlogconfig
        depth = 0
        fields = '__all__'


class DjangocmsBlogBlogconfigTranslationSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogBlogconfigTranslation
        depth = 0
        fields = '__all__'


class DjangocmsBlogGenericblogpluginSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogGenericblogplugin
        depth = 0
        fields = '__all__'


class DjangocmsBlogLatestpostspluginSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogLatestpostsplugin
        depth = 0
        fields = '__all__'


class DjangocmsBlogLatestpostspluginCategoriesSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogLatestpostspluginCategories
        depth = 0
        fields = '__all__'


class DjangocmsBlogPostSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogPost
        depth = 0
        fields = '__all__'


class DjangocmsBlogPostCategoriesSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogPostCategories
        depth = 0
        fields = '__all__'


class DjangocmsBlogPostRelatedSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogPostRelated
        depth = 0
        fields = '__all__'


class DjangocmsBlogPostSitesSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogPostSites
        depth = 0
        fields = '__all__'


class DjangocmsBlogPostTranslationSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsBlogPostTranslation
        depth = 0
        fields = '__all__'


class DjangocmsFileFileSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsFileFile
        depth = 0
        fields = '__all__'


class DjangocmsFileFolderSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsFileFolder
        depth = 0
        fields = '__all__'


class DjangocmsGooglemapGooglemapSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsGooglemapGooglemap
        depth = 0
        fields = '__all__'


class DjangocmsGooglemapGooglemapmarkerSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsGooglemapGooglemapmarker
        depth = 0
        fields = '__all__'


class DjangocmsGooglemapGooglemaprouteSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsGooglemapGooglemaproute
        depth = 0
        fields = '__all__'


class DjangocmsHistoryPlaceholderactionSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsHistoryPlaceholderaction
        depth = 0
        fields = '__all__'


class DjangocmsHistoryPlaceholderoperationSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsHistoryPlaceholderoperation
        depth = 0
        fields = '__all__'


class DjangocmsIconIconSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsIconIcon
        depth = 0
        fields = '__all__'


class DjangocmsLinkLinkSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsLinkLink
        depth = 0
        fields = '__all__'


class DjangocmsMapsMapsSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsMapsMaps
        depth = 0
        fields = '__all__'


class DjangocmsPicturePictureSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsPicturePicture
        depth = 0
        fields = '__all__'


class DjangocmsStyleStyleSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsStyleStyle
        depth = 0
        fields = '__all__'


class DjangocmsTextCkeditorTextSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsTextCkeditorText
        depth = 0
        fields = '__all__'


class DjangocmsVideoVideoplayerSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsVideoVideoplayer
        depth = 0
        fields = '__all__'


class DjangocmsVideoVideosourceSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsVideoVideosource
        depth = 0
        fields = '__all__'


class DjangocmsVideoVideotrackSerializer(ModelSerializer):

    class Meta:
        model = DjangocmsVideoVideotrack
        depth = 0
        fields = '__all__'


class EasyThumbnailsSourceSerializer(ModelSerializer):

    class Meta:
        model = EasyThumbnailsSource
        depth = 0
        fields = '__all__'


class EasyThumbnailsThumbnailSerializer(ModelSerializer):

    class Meta:
        model = EasyThumbnailsThumbnail
        depth = 0
        fields = '__all__'


class EasyThumbnailsThumbnaildimensionsSerializer(ModelSerializer):

    class Meta:
        model = EasyThumbnailsThumbnaildimensions
        depth = 0
        fields = '__all__'


class FilerClipboardSerializer(ModelSerializer):

    class Meta:
        model = FilerClipboard
        depth = 0
        fields = '__all__'


class FilerClipboarditemSerializer(ModelSerializer):

    class Meta:
        model = FilerClipboarditem
        depth = 0
        fields = '__all__'


class FilerFileSerializer(ModelSerializer):

    class Meta:
        model = FilerFile
        depth = 0
        fields = '__all__'


class FilerFolderSerializer(ModelSerializer):

    class Meta:
        model = FilerFolder
        depth = 0
        fields = '__all__'


class FilerFolderpermissionSerializer(ModelSerializer):

    class Meta:
        model = FilerFolderpermission
        depth = 0
        fields = '__all__'


class FilerImageSerializer(ModelSerializer):

    class Meta:
        model = FilerImage
        depth = 0
        fields = '__all__'


class FilerThumbnailoptionSerializer(ModelSerializer):

    class Meta:
        model = FilerThumbnailoption
        depth = 0
        fields = '__all__'


class MenusCachekeySerializer(ModelSerializer):

    class Meta:
        model = MenusCachekey
        depth = 0
        fields = '__all__'


class OfferBenefitSerializer(ModelSerializer):

    class Meta:
        model = OfferBenefit
        depth = 0
        fields = '__all__'


class OfferConditionSerializer(ModelSerializer):

    class Meta:
        model = OfferCondition
        depth = 0
        fields = '__all__'


class OfferConditionalofferSerializer(ModelSerializer):

    class Meta:
        model = OfferConditionaloffer
        depth = 0
        fields = '__all__'


class OfferConditionalofferCombinationsSerializer(ModelSerializer):

    class Meta:
        model = OfferConditionalofferCombinations
        depth = 0
        fields = '__all__'


class OfferRangeSerializer(ModelSerializer):

    class Meta:
        model = OfferRange
        depth = 0
        fields = '__all__'


class OfferRangeClassesSerializer(ModelSerializer):

    class Meta:
        model = OfferRangeClasses
        depth = 0
        fields = '__all__'


class OfferRangeExcludedProductsSerializer(ModelSerializer):

    class Meta:
        model = OfferRangeExcludedProducts
        depth = 0
        fields = '__all__'


class OfferRangeIncludedCategoriesSerializer(ModelSerializer):

    class Meta:
        model = OfferRangeIncludedCategories
        depth = 0
        fields = '__all__'


class OfferRangeproductSerializer(ModelSerializer):

    class Meta:
        model = OfferRangeproduct
        depth = 0
        fields = '__all__'


class OfferRangeproductfileuploadSerializer(ModelSerializer):

    class Meta:
        model = OfferRangeproductfileupload
        depth = 0
        fields = '__all__'


class OrderBillingaddressSerializer(ModelSerializer):

    class Meta:
        model = OrderBillingaddress
        depth = 0
        fields = '__all__'


class OrderCommunicationeventSerializer(ModelSerializer):

    class Meta:
        model = OrderCommunicationevent
        depth = 0
        fields = '__all__'


class OrderLineSerializer(ModelSerializer):

    class Meta:
        model = OrderLine
        depth = 0
        fields = '__all__'


class OrderLineattributeSerializer(ModelSerializer):

    class Meta:
        model = OrderLineattribute
        depth = 0
        fields = '__all__'


class OrderLinepriceSerializer(ModelSerializer):

    class Meta:
        model = OrderLineprice
        depth = 0
        fields = '__all__'


class OrderOrderSerializer(ModelSerializer):

    class Meta:
        model = OrderOrder
        depth = 0
        fields = '__all__'


class OrderOrderdiscountSerializer(ModelSerializer):

    class Meta:
        model = OrderOrderdiscount
        depth = 0
        fields = '__all__'


class OrderOrdernoteSerializer(ModelSerializer):

    class Meta:
        model = OrderOrdernote
        depth = 0
        fields = '__all__'


class OrderOrderstatuschangeSerializer(ModelSerializer):

    class Meta:
        model = OrderOrderstatuschange
        depth = 0
        fields = '__all__'


class OrderPaymenteventSerializer(ModelSerializer):

    class Meta:
        model = OrderPaymentevent
        depth = 0
        fields = '__all__'


class OrderPaymenteventquantitySerializer(ModelSerializer):

    class Meta:
        model = OrderPaymenteventquantity
        depth = 0
        fields = '__all__'


class OrderPaymenteventtypeSerializer(ModelSerializer):

    class Meta:
        model = OrderPaymenteventtype
        depth = 0
        fields = '__all__'


class OrderShippingaddressSerializer(ModelSerializer):

    class Meta:
        model = OrderShippingaddress
        depth = 0
        fields = '__all__'


class OrderShippingeventSerializer(ModelSerializer):

    class Meta:
        model = OrderShippingevent
        depth = 0
        fields = '__all__'


class OrderShippingeventquantitySerializer(ModelSerializer):

    class Meta:
        model = OrderShippingeventquantity
        depth = 0
        fields = '__all__'


class OrderShippingeventtypeSerializer(ModelSerializer):

    class Meta:
        model = OrderShippingeventtype
        depth = 0
        fields = '__all__'


class OrderSurchargeSerializer(ModelSerializer):

    class Meta:
        model = OrderSurcharge
        depth = 0
        fields = '__all__'


class OscarInvoicesInvoiceSerializer(ModelSerializer):

    class Meta:
        model = OscarInvoicesInvoice
        depth = 0
        fields = '__all__'


class OscarInvoicesLegalentitySerializer(ModelSerializer):

    class Meta:
        model = OscarInvoicesLegalentity
        depth = 0
        fields = '__all__'


class OscarInvoicesLegalentityaddressSerializer(ModelSerializer):

    class Meta:
        model = OscarInvoicesLegalentityaddress
        depth = 0
        fields = '__all__'


class OscarapiApikeySerializer(ModelSerializer):

    class Meta:
        model = OscarapiApikey
        depth = 0
        fields = '__all__'


class PartnerPartnerSerializer(ModelSerializer):

    class Meta:
        model = PartnerPartner
        depth = 0
        fields = '__all__'


class PartnerPartnerUsersSerializer(ModelSerializer):

    class Meta:
        model = PartnerPartnerUsers
        depth = 0
        fields = '__all__'


class PartnerPartneraddressSerializer(ModelSerializer):

    class Meta:
        model = PartnerPartneraddress
        depth = 0
        fields = '__all__'


class PartnerStockalertSerializer(ModelSerializer):

    class Meta:
        model = PartnerStockalert
        depth = 0
        fields = '__all__'


class PartnerStockrecordSerializer(ModelSerializer):

    class Meta:
        model = PartnerStockrecord
        depth = 0
        fields = '__all__'


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        depth = 0
        fields = '__all__'


class PaymentBankcardSerializer(ModelSerializer):

    class Meta:
        model = PaymentBankcard
        depth = 0
        fields = '__all__'


class PaymentSourceSerializer(ModelSerializer):

    class Meta:
        model = PaymentSource
        depth = 0
        fields = '__all__'


class PaymentSourcetypeSerializer(ModelSerializer):

    class Meta:
        model = PaymentSourcetype
        depth = 0
        fields = '__all__'


class PaymentTransactionSerializer(ModelSerializer):

    class Meta:
        model = PaymentTransaction
        depth = 0
        fields = '__all__'


class PaypalExpresstransactionSerializer(ModelSerializer):

    class Meta:
        model = PaypalExpresstransaction
        depth = 0
        fields = '__all__'


class PaypalPayflowtransactionSerializer(ModelSerializer):

    class Meta:
        model = PaypalPayflowtransaction
        depth = 0
        fields = '__all__'


class PhotologueGallerySerializer(ModelSerializer):

    class Meta:
        model = PhotologueGallery
        depth = 0
        fields = '__all__'


class PhotologueGalleryPhotosSerializer(ModelSerializer):

    class Meta:
        model = PhotologueGalleryPhotos
        depth = 0
        fields = '__all__'


class PhotologueGallerySitesSerializer(ModelSerializer):

    class Meta:
        model = PhotologueGallerySites
        depth = 0
        fields = '__all__'


class PhotologuePhotoSerializer(ModelSerializer):

    class Meta:
        model = PhotologuePhoto
        depth = 0
        fields = '__all__'


class PhotologuePhotoSitesSerializer(ModelSerializer):

    class Meta:
        model = PhotologuePhotoSites
        depth = 0
        fields = '__all__'


class PhotologuePhotoeffectSerializer(ModelSerializer):

    class Meta:
        model = PhotologuePhotoeffect
        depth = 0
        fields = '__all__'


class PhotologuePhotosizeSerializer(ModelSerializer):

    class Meta:
        model = PhotologuePhotosize
        depth = 0
        fields = '__all__'


class PhotologueWatermarkSerializer(ModelSerializer):

    class Meta:
        model = PhotologueWatermark
        depth = 0
        fields = '__all__'


class PinaxBadgesBadgeawardSerializer(ModelSerializer):

    class Meta:
        model = PinaxBadgesBadgeaward
        depth = 0
        fields = '__all__'


class PinaxEventsEventSerializer(ModelSerializer):

    class Meta:
        model = PinaxEventsEvent
        depth = 0
        fields = '__all__'


class PinaxMessagesMessageSerializer(ModelSerializer):

    class Meta:
        model = PinaxMessagesMessage
        depth = 0
        fields = '__all__'


class PinaxMessagesThreadSerializer(ModelSerializer):

    class Meta:
        model = PinaxMessagesThread
        depth = 0
        fields = '__all__'


class PinaxMessagesUserthreadSerializer(ModelSerializer):

    class Meta:
        model = PinaxMessagesUserthread
        depth = 0
        fields = '__all__'


class ReviewsProductreviewSerializer(ModelSerializer):

    class Meta:
        model = ReviewsProductreview
        depth = 0
        fields = '__all__'


class ReviewsVoteSerializer(ModelSerializer):

    class Meta:
        model = ReviewsVote
        depth = 0
        fields = '__all__'


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        depth = 0
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        depth = 0
        fields = '__all__'


class SalesLineTransactionSerializer(ModelSerializer):

    class Meta:
        model = SalesLineTransaction
        depth = 0
        fields = '__all__'


class ShippingOrderanditemchargesSerializer(ModelSerializer):

    class Meta:
        model = ShippingOrderanditemcharges
        depth = 0
        fields = '__all__'


class ShippingOrderanditemchargesCountriesSerializer(ModelSerializer):

    class Meta:
        model = ShippingOrderanditemchargesCountries
        depth = 0
        fields = '__all__'


class ShippingWeightbandSerializer(ModelSerializer):

    class Meta:
        model = ShippingWeightband
        depth = 0
        fields = '__all__'


class ShippingWeightbasedSerializer(ModelSerializer):

    class Meta:
        model = ShippingWeightbased
        depth = 0
        fields = '__all__'


class ShippingWeightbasedCountriesSerializer(ModelSerializer):

    class Meta:
        model = ShippingWeightbasedCountries
        depth = 0
        fields = '__all__'


class TaggitTagSerializer(ModelSerializer):

    class Meta:
        model = TaggitTag
        depth = 0
        fields = '__all__'


class TaggitTaggeditemSerializer(ModelSerializer):

    class Meta:
        model = TaggitTaggeditem
        depth = 0
        fields = '__all__'


class TestimonialsTestimonialSerializer(ModelSerializer):

    class Meta:
        model = TestimonialsTestimonial
        depth = 0
        fields = '__all__'


class ThumbnailKvstoreSerializer(ModelSerializer):

    class Meta:
        model = ThumbnailKvstore
        depth = 0
        fields = '__all__'


class VoucherVoucherSerializer(ModelSerializer):

    class Meta:
        model = VoucherVoucher
        depth = 0
        fields = '__all__'


class VoucherVoucherOffersSerializer(ModelSerializer):

    class Meta:
        model = VoucherVoucherOffers
        depth = 0
        fields = '__all__'


class VoucherVoucherapplicationSerializer(ModelSerializer):

    class Meta:
        model = VoucherVoucherapplication
        depth = 0
        fields = '__all__'


class VoucherVouchersetSerializer(ModelSerializer):

    class Meta:
        model = VoucherVoucherset
        depth = 0
        fields = '__all__'


class WishlistsLineSerializer(ModelSerializer):

    class Meta:
        model = WishlistsLine
        depth = 0
        fields = '__all__'


class WishlistsWishlistSerializer(ModelSerializer):

    class Meta:
        model = WishlistsWishlist
        depth = 0
        fields = '__all__'

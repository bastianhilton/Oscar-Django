from ariadne_django import QueryType, make_executable_schema


type_defs = """
    
       type Query { all_AuthPermission = ariadne.List(AuthPermissionType)}
    
       type Query { all_AuthGroup = ariadne.List(AuthGroupType)}
    
       type Query { all_AuthGroupPermissions = ariadne.List(AuthGroupPermissionsType)}
    
       type Query { all_AuthUserGroups = ariadne.List(AuthUserGroupsType)}
    
       type Query { all_AuthUser = ariadne.List(AuthUserType)}
    
       type Query { all_DjangocmsMapsMaps = ariadne.List(DjangocmsMapsMapsType)}
    
       type Query { all_AuthUserUserPermissions = ariadne.List(AuthUserUserPermissionsType)}
    
       type Query { all_AddressCountry = ariadne.List(AddressCountryType)}
    
       type Query { all_AddressUseraddress = ariadne.List(AddressUseraddressType)}
    
       type Query { all_DjangoAdminLog = ariadne.List(DjangoAdminLogType)}
    
       type Query { all_DjangocmsStyleStyle = ariadne.List(DjangocmsStyleStyleType)}
    
       type Query { all_DjangocmsTextCkeditorText = ariadne.List(DjangocmsTextCkeditorTextType)}
    
       type Query { all_DjangocmsVideoVideoplayer = ariadne.List(DjangocmsVideoVideoplayerType)}
    
       type Query { all_CatalogueAttributeoptiongroup = ariadne.List(CatalogueAttributeoptiongroupType)}
    
       type Query { all_CatalogueProductattribute = ariadne.List(CatalogueProductattributeType)}
    
       type Query { all_CatalogueAttributeoption = ariadne.List(CatalogueAttributeoptionType)}
    
       type Query { all_CatalogueProductcategory = ariadne.List(CatalogueProductcategoryType)}
    
       type Query { all_CatalogueProductclass = ariadne.List(CatalogueProductclassType)}
    
       type Query { all_CatalogueProductclassOptions = ariadne.List(CatalogueProductclassOptionsType)}
    
       type Query { all_CatalogueProductimage = ariadne.List(CatalogueProductimageType)}
    
       type Query { all_CatalogueProductrecommendation = ariadne.List(CatalogueProductrecommendationType)}
    
       type Query { all_CatalogueProductProductOptions = ariadne.List(CatalogueProductProductOptionsType)}
    
       type Query { all_CatalogueProductattributevalue = ariadne.List(CatalogueProductattributevalueType)}
    
       type Query { all_CatalogueOption = ariadne.List(CatalogueOptionType)}
    
       type Query { all_CatalogueCategory = ariadne.List(CatalogueCategoryType)}
    
       type Query { all_AnalyticsUserrecord = ariadne.List(AnalyticsUserrecordType)}
    
       type Query { all_AnalyticsUsersearch = ariadne.List(AnalyticsUsersearchType)}
    
       type Query { all_AnnouncementsAnnouncement = ariadne.List(AnnouncementsAnnouncementType)}
    
       type Query { all_AnalyticsUserproductview = ariadne.List(AnalyticsUserproductviewType)}
    
       type Query { all_AnalyticsProductrecord = ariadne.List(AnalyticsProductrecordType)}
    
       type Query { all_AnnouncementsDismissal = ariadne.List(AnnouncementsDismissalType)}
    
       type Query { all_DjangocmsVideoVideosource = ariadne.List(DjangocmsVideoVideosourceType)}
    
       type Query { all_CommunicationCommunicationeventtype = ariadne.List(CommunicationCommunicationeventtypeType)}
    
       type Query { all_PartnerPartner = ariadne.List(PartnerPartnerType)}
    
       type Query { all_PartnerPartnerUsers = ariadne.List(PartnerPartnerUsersType)}
    
       type Query { all_PartnerPartneraddress = ariadne.List(PartnerPartneraddressType)}
    
       type Query { all_PartnerStockrecord = ariadne.List(PartnerStockrecordType)}
    
       type Query { all_PartnerStockalert = ariadne.List(PartnerStockalertType)}
    
       type Query { all_DjangocmsVideoVideotrack = ariadne.List(DjangocmsVideoVideotrackType)}
    
       type Query { all_BasketLine = ariadne.List(BasketLineType)}
    
       type Query { all_CustomerProductalert = ariadne.List(CustomerProductalertType)}
    
       type Query { all_CommunicationEmail = ariadne.List(CommunicationEmailType)}
    
       type Query { all_BasketLineattribute = ariadne.List(BasketLineattributeType)}
    
       type Query { all_CommunicationNotification = ariadne.List(CommunicationNotificationType)}
    
       type Query { all_BasketBasket = ariadne.List(BasketBasketType)}
    
       type Query { all_EasyThumbnailsSource = ariadne.List(EasyThumbnailsSourceType)}
    
       type Query { all_EasyThumbnailsThumbnail = ariadne.List(EasyThumbnailsThumbnailType)}
    
       type Query { all_EasyThumbnailsThumbnaildimensions = ariadne.List(EasyThumbnailsThumbnaildimensionsType)}
    
       type Query { all_DjangoFlatpage = ariadne.List(DjangoFlatpageType)}
    
       type Query { all_DjangoFlatpageSites = ariadne.List(DjangoFlatpageSitesType)}
    
       type Query { all_MenusCachekey = ariadne.List(MenusCachekeyType)}
    
       type Query { all_OrderBillingaddress = ariadne.List(OrderBillingaddressType)}
    
       type Query { all_OfferConditionalofferCombinations = ariadne.List(OfferConditionalofferCombinationsType)}
    
       type Query { all_OrderCommunicationevent = ariadne.List(OrderCommunicationeventType)}
    
       type Query { all_OrderLine = ariadne.List(OrderLineType)}
    
       type Query { all_OrderLineattribute = ariadne.List(OrderLineattributeType)}
    
       type Query { all_OrderLineprice = ariadne.List(OrderLinepriceType)}
    
       type Query { all_OrderOrder = ariadne.List(OrderOrderType)}
    
       type Query { all_OrderOrderdiscount = ariadne.List(OrderOrderdiscountType)}
    
       type Query { all_OrderOrdernote = ariadne.List(OrderOrdernoteType)}
    
       type Query { all_OrderPaymentevent = ariadne.List(OrderPaymenteventType)}
    
       type Query { all_OrderPaymenteventquantity = ariadne.List(OrderPaymenteventquantityType)}
    
       type Query { all_OrderShippingaddress = ariadne.List(OrderShippingaddressType)}
    
       type Query { all_OrderShippingevent = ariadne.List(OrderShippingeventType)}
    
       type Query { all_OrderShippingeventquantity = ariadne.List(OrderShippingeventquantityType)}
    
       type Query { all_OrderShippingeventtype = ariadne.List(OrderShippingeventtypeType)}
    
       type Query { all_OrderPaymenteventtype = ariadne.List(OrderPaymenteventtypeType)}
    
       type Query { all_DjangoSite = ariadne.List(DjangoSiteType)}
    
       type Query { all_OrderSurcharge = ariadne.List(OrderSurchargeType)}
    
       type Query { all_OfferConditionaloffer = ariadne.List(OfferConditionalofferType)}
    
       type Query { all_OfferBenefit = ariadne.List(OfferBenefitType)}
    
       type Query { all_OfferCondition = ariadne.List(OfferConditionType)}
    
       type Query { all_OfferRange = ariadne.List(OfferRangeType)}
    
       type Query { all_OfferRangeClasses = ariadne.List(OfferRangeClassesType)}
    
       type Query { all_OfferRangeExcludedProducts = ariadne.List(OfferRangeExcludedProductsType)}
    
       type Query { all_OfferRangeIncludedCategories = ariadne.List(OfferRangeIncludedCategoriesType)}
    
       type Query { all_OfferRangeproduct = ariadne.List(OfferRangeproductType)}
    
       type Query { all_OfferRangeproductfileupload = ariadne.List(OfferRangeproductfileuploadType)}
    
       type Query { all_VoucherVoucher = ariadne.List(VoucherVoucherType)}
    
       type Query { all_VoucherVoucherOffers = ariadne.List(VoucherVoucherOffersType)}
    
       type Query { all_BasketBasketVouchers = ariadne.List(BasketBasketVouchersType)}
    
       type Query { all_OscarInvoicesLegalentityaddress = ariadne.List(OscarInvoicesLegalentityaddressType)}
    
       type Query { all_OscarInvoicesLegalentity = ariadne.List(OscarInvoicesLegalentityType)}
    
       type Query { all_OscarInvoicesInvoice = ariadne.List(OscarInvoicesInvoiceType)}
    
       type Query { all_CmsGlobalpagepermission = ariadne.List(CmsGlobalpagepermissionType)}
    
       type Query { all_CmsGlobalpagepermissionSites = ariadne.List(CmsGlobalpagepermissionSitesType)}
    
       type Query { all_OscarapiApikey = ariadne.List(OscarapiApikeyType)}
    
       type Query { all_CmsAliaspluginmodel = ariadne.List(CmsAliaspluginmodelType)}
    
       type Query { all_CmsPagepermission = ariadne.List(CmsPagepermissionType)}
    
       type Query { all_CmsPageuser = ariadne.List(CmsPageuserType)}
    
       type Query { all_CmsPageusergroup = ariadne.List(CmsPageusergroupType)}
    
       type Query { all_CmsPagePlaceholders = ariadne.List(CmsPagePlaceholdersType)}
    
       type Query { all_CmsPlaceholder = ariadne.List(CmsPlaceholderType)}
    
       type Query { all_CmsPlaceholderreference = ariadne.List(CmsPlaceholderreferenceType)}
    
       type Query { all_CmsStaticplaceholder = ariadne.List(CmsStaticplaceholderType)}
    
       type Query { all_CmsTitle = ariadne.List(CmsTitleType)}
    
       type Query { all_CmsUsersettings = ariadne.List(CmsUsersettingsType)}
    
       type Query { all_CmsUrlconfrevision = ariadne.List(CmsUrlconfrevisionType)}
    
       type Query { all_CmsCmsplugin = ariadne.List(CmsCmspluginType)}
    
       type Query { all_Bootstrap4AlertsBootstrap4Alerts = ariadne.List(Bootstrap4AlertsBootstrap4AlertsType)}
    
       type Query { all_Bootstrap4BadgeBootstrap4Badge = ariadne.List(Bootstrap4BadgeBootstrap4BadgeType)}
    
       type Query { all_Bootstrap4CardBootstrap4Card = ariadne.List(Bootstrap4CardBootstrap4CardType)}
    
       type Query { all_Bootstrap4CardBootstrap4Cardinner = ariadne.List(Bootstrap4CardBootstrap4CardinnerType)}
    
       type Query { all_PaymentBankcard = ariadne.List(PaymentBankcardType)}
    
       type Query { all_PaymentSource = ariadne.List(PaymentSourceType)}
    
       type Query { all_PaymentTransaction = ariadne.List(PaymentTransactionType)}
    
       type Query { all_PaymentSourcetype = ariadne.List(PaymentSourcetypeType)}
    
       type Query { all_FilerClipboard = ariadne.List(FilerClipboardType)}
    
       type Query { all_FilerClipboarditem = ariadne.List(FilerClipboarditemType)}
    
       type Query { all_FilerFolder = ariadne.List(FilerFolderType)}
    
       type Query { all_PaypalExpresstransaction = ariadne.List(PaypalExpresstransactionType)}
    
       type Query { all_FilerFile = ariadne.List(FilerFileType)}
    
       type Query { all_FilerFolderpermission = ariadne.List(FilerFolderpermissionType)}
    
       type Query { all_FilerImage = ariadne.List(FilerImageType)}
    
       type Query { all_PaypalPayflowtransaction = ariadne.List(PaypalPayflowtransactionType)}
    
       type Query { all_Bootstrap4CarouselBootstrap4Carousel = ariadne.List(Bootstrap4CarouselBootstrap4CarouselType)}
    
       type Query { all_Bootstrap4CarouselBootstrap4Carouselslide = ariadne.List(Bootstrap4CarouselBootstrap4CarouselslideType)}
    
       type Query { all_FilerThumbnailoption = ariadne.List(FilerThumbnailoptionType)}
    
       type Query { all_Bootstrap4CollapseBootstrap4Collapse = ariadne.List(Bootstrap4CollapseBootstrap4CollapseType)}
    
       type Query { all_Bootstrap4CollapseBootstrap4Collapsecontainer = ariadne.List(Bootstrap4CollapseBootstrap4CollapsecontainerType)}
    
       type Query { all_Bootstrap4CollapseBootstrap4Collapsetrigger = ariadne.List(Bootstrap4CollapseBootstrap4CollapsetriggerType)}
    
       type Query { all_Bootstrap4GridBootstrap4Gridcontainer = ariadne.List(Bootstrap4GridBootstrap4GridcontainerType)}
    
       type Query { all_Bootstrap4ContentBootstrap4Blockquote = ariadne.List(Bootstrap4ContentBootstrap4BlockquoteType)}
    
       type Query { all_Bootstrap4ContentBootstrap4Code = ariadne.List(Bootstrap4ContentBootstrap4CodeType)}
    
       type Query { all_Bootstrap4GridBootstrap4Gridrow = ariadne.List(Bootstrap4GridBootstrap4GridrowType)}
    
       type Query { all_Bootstrap4ContentBootstrap4Figure = ariadne.List(Bootstrap4ContentBootstrap4FigureType)}
    
       type Query { all_Bootstrap4JumbotronBootstrap4Jumbotron = ariadne.List(Bootstrap4JumbotronBootstrap4JumbotronType)}
    
       type Query { all_Bootstrap4GridBootstrap4Gridcolumn = ariadne.List(Bootstrap4GridBootstrap4GridcolumnType)}
    
       type Query { all_Bootstrap4LinkBootstrap4Link = ariadne.List(Bootstrap4LinkBootstrap4LinkType)}
    
       type Query { all_Bootstrap4ListgroupBootstrap4Listgroup = ariadne.List(Bootstrap4ListgroupBootstrap4ListgroupType)}
    
       type Query { all_Bootstrap4ListgroupBootstrap4Listgroupitem = ariadne.List(Bootstrap4ListgroupBootstrap4ListgroupitemType)}
    
       type Query { all_Bootstrap4MediaBootstrap4Media = ariadne.List(Bootstrap4MediaBootstrap4MediaType)}
    
       type Query { all_Bootstrap4MediaBootstrap4Mediabody = ariadne.List(Bootstrap4MediaBootstrap4MediabodyType)}
    
       type Query { all_DjangocmsPicturePicture = ariadne.List(DjangocmsPicturePictureType)}
    
       type Query { all_Bootstrap4PictureBootstrap4Picture = ariadne.List(Bootstrap4PictureBootstrap4PictureType)}
    
       type Query { all_Bootstrap4TabsBootstrap4Tab = ariadne.List(Bootstrap4TabsBootstrap4TabType)}
    
       type Query { all_Bootstrap4TabsBootstrap4Tabitem = ariadne.List(Bootstrap4TabsBootstrap4TabitemType)}
    
       type Query { all_Bootstrap4UtilitiesBootstrap4Spacing = ariadne.List(Bootstrap4UtilitiesBootstrap4SpacingType)}
    
       type Query { all_CatalogueProductattributevalueValueMultiOption = ariadne.List(CatalogueProductattributevalueValueMultiOptionType)}
    
       type Query { all_CatalogueProduct = ariadne.List(CatalogueProductType)}
    
       type Query { all_CmsTreenode = ariadne.List(CmsTreenodeType)}
    
       type Query { all_CmsPage = ariadne.List(CmsPageType)}
    
       type Query { all_OrderOrderstatuschange = ariadne.List(OrderOrderstatuschangeType)}
    
       type Query { all_TaggitTaggeditem = ariadne.List(TaggitTaggeditemType)}
    
       type Query { all_TaggitTag = ariadne.List(TaggitTagType)}
    
       type Query { all_DjangocmsBlogAuthorentriespluginAuthors = ariadne.List(DjangocmsBlogAuthorentriespluginAuthorsType)}
    
       type Query { all_DjangocmsBlogLatestpostspluginCategories = ariadne.List(DjangocmsBlogLatestpostspluginCategoriesType)}
    
       type Query { all_DjangocmsBlogPostCategories = ariadne.List(DjangocmsBlogPostCategoriesType)}
    
       type Query { all_DjangocmsBlogPostSites = ariadne.List(DjangocmsBlogPostSitesType)}
    
       type Query { all_DjangocmsBlogBlogcategory = ariadne.List(DjangocmsBlogBlogcategoryType)}
    
       type Query { all_DjangocmsBlogAuthorentriesplugin = ariadne.List(DjangocmsBlogAuthorentriespluginType)}
    
       type Query { all_DjangocmsBlogLatestpostsplugin = ariadne.List(DjangocmsBlogLatestpostspluginType)}
    
       type Query { all_DjangocmsBlogBlogcategoryTranslation = ariadne.List(DjangocmsBlogBlogcategoryTranslationType)}
    
       type Query { all_DjangocmsBlogPostTranslation = ariadne.List(DjangocmsBlogPostTranslationType)}
    
       type Query { all_DjangocmsBlogPost = ariadne.List(DjangocmsBlogPostType)}
    
       type Query { all_DjangocmsBlogBlogconfig = ariadne.List(DjangocmsBlogBlogconfigType)}
    
       type Query { all_DjangocmsBlogBlogconfigTranslation = ariadne.List(DjangocmsBlogBlogconfigTranslationType)}
    
       type Query { all_DjangocmsBlogGenericblogplugin = ariadne.List(DjangocmsBlogGenericblogpluginType)}
    
       type Query { all_DjangocmsBlogPostRelated = ariadne.List(DjangocmsBlogPostRelatedType)}
    
       type Query { all_DjangocmsFileFile = ariadne.List(DjangocmsFileFileType)}
    
       type Query { all_DjangocmsFileFolder = ariadne.List(DjangocmsFileFolderType)}
    
       type Query { all_DjangocmsGooglemapGooglemap = ariadne.List(DjangocmsGooglemapGooglemapType)}
    
       type Query { all_DjangocmsGooglemapGooglemaproute = ariadne.List(DjangocmsGooglemapGooglemaprouteType)}
    
       type Query { all_DjangocmsLinkLink = ariadne.List(DjangocmsLinkLinkType)}
    
       type Query { all_PhotologueGallery = ariadne.List(PhotologueGalleryType)}
    
       type Query { all_PhotologueGallerySites = ariadne.List(PhotologueGallerySitesType)}
    
       type Query { all_DjangocmsGooglemapGooglemapmarker = ariadne.List(DjangocmsGooglemapGooglemapmarkerType)}
    
       type Query { all_PhotologuePhoto = ariadne.List(PhotologuePhotoType)}
    
       type Query { all_DjangocmsIconIcon = ariadne.List(DjangocmsIconIconType)}
    
       type Query { all_PhotologuePhotoSites = ariadne.List(PhotologuePhotoSitesType)}
    
       type Query { all_PhotologueGalleryPhotos = ariadne.List(PhotologueGalleryPhotosType)}
    
       type Query { all_PhotologuePhotoeffect = ariadne.List(PhotologuePhotoeffectType)}
    
       type Query { all_PhotologuePhotosize = ariadne.List(PhotologuePhotosizeType)}
    
       type Query { all_PhotologueWatermark = ariadne.List(PhotologueWatermarkType)}
    
       type Query { all_PinaxBadgesBadgeaward = ariadne.List(PinaxBadgesBadgeawardType)}
    
       type Query { all_PinaxEventsEvent = ariadne.List(PinaxEventsEventType)}
    
       type Query { all_PinaxMessagesMessage = ariadne.List(PinaxMessagesMessageType)}
    
       type Query { all_PinaxMessagesThread = ariadne.List(PinaxMessagesThreadType)}
    
       type Query { all_PinaxMessagesUserthread = ariadne.List(PinaxMessagesUserthreadType)}
    
       type Query { all_ReviewsProductreview = ariadne.List(ReviewsProductreviewType)}
    
       type Query { all_ReviewsVote = ariadne.List(ReviewsVoteType)}
    
       type Query { all_DjangoSession = ariadne.List(DjangoSessionType)}
    
       type Query { all_ShippingOrderanditemcharges = ariadne.List(ShippingOrderanditemchargesType)}
    
       type Query { all_ShippingOrderanditemchargesCountries = ariadne.List(ShippingOrderanditemchargesCountriesType)}
    
       type Query { all_ShippingWeightbased = ariadne.List(ShippingWeightbasedType)}
    
       type Query { all_ShippingWeightbasedCountries = ariadne.List(ShippingWeightbasedCountriesType)}
    
       type Query { all_ShippingWeightband = ariadne.List(ShippingWeightbandType)}
    
       type Query { all_TestimonialsTestimonial = ariadne.List(TestimonialsTestimonialType)}
    
       type Query { all_ThumbnailKvstore = ariadne.List(ThumbnailKvstoreType)}
    
       type Query { all_VoucherVoucherapplication = ariadne.List(VoucherVoucherapplicationType)}
    
       type Query { all_VoucherVoucherset = ariadne.List(VoucherVouchersetType)}
    
       type Query { all_WishlistsLine = ariadne.List(WishlistsLineType)}
    
       type Query { all_WishlistsWishlist = ariadne.List(WishlistsWishlistType)}
    
       type Query { all_DjangocmsHistoryPlaceholderoperation = ariadne.List(DjangocmsHistoryPlaceholderoperationType)}
    
       type Query { all_DjangocmsHistoryPlaceholderaction = ariadne.List(DjangocmsHistoryPlaceholderactionType)}
    
       type Query { all_AdvancedFiltersAdvancedfilter = ariadne.List(AdvancedFiltersAdvancedfilterType)}
    
       type Query { all_AdvancedFiltersAdvancedfilterGroups = ariadne.List(AdvancedFiltersAdvancedfilterGroupsType)}
    
       type Query { all_AdvancedFiltersAdvancedfilterUsers = ariadne.List(AdvancedFiltersAdvancedfilterUsersType)}	

"""

query = QueryType()

@query.field("AddressCountry")	
def resolve_AddressCountry(root, info, **kwargs):
   return  AddressCountry.objects.all()

@query.field("AddressUseraddress")
def resolve_AddressUseraddress(root, info, **kwargs):
   return  AddressUseraddress.objects.all()

@query.field("AdvancedFiltersAdvancedfilter")
def resolve_AdvancedFiltersAdvancedfilter(root, info, **kwargs):
   return  AdvancedFiltersAdvancedfilter.objects.all()

@query.field("AdvancedFiltersAdvancedfilterGroups")
def resolve_AdvancedFiltersAdvancedfilterGroups(root, info, **kwargs):
   return  AdvancedFiltersAdvancedfilterGroups.objects.all()

@query.field("AdvancedFiltersAdvancedfilterUsers")
def resolve_AdvancedFiltersAdvancedfilterUsers(root, info, **kwargs):
   return  AdvancedFiltersAdvancedfilterUsers.objects.all()

@query.field("AnalyticsProductrecord")
def resolve_AnalyticsProductrecord(root, info, **kwargs):
   return  AnalyticsProductrecord.objects.all()

@query.field("AnalyticsUserproductview")
def resolve_AnalyticsUserproductview(root, info, **kwargs):
   return  AnalyticsUserproductview.objects.all()

@query.field("AnalyticsUserrecord")
def resolve_AnalyticsUserrecord(root, info, **kwargs):
   return  AnalyticsUserrecord.objects.all()

@query.field("AnalyticsUsersearch")
def resolve_AnalyticsUsersearch(root, info, **kwargs):
   return  AnalyticsUsersearch.objects.all()

@query.field("AnnouncementsAnnouncement")
def resolve_AnnouncementsAnnouncement(root, info, **kwargs):
   return  AnnouncementsAnnouncement.objects.all()

@query.field("AnnouncementsDismissal")
def resolve_AnnouncementsDismissal(root, info, **kwargs):
   return  AnnouncementsDismissal.objects.all()

@query.field("AuthGroup")
def resolve_AuthGroup(root, info, **kwargs):
   return  AuthGroup.objects.all()

@query.field("AuthGroupPermissions")
def resolve_AuthGroupPermissions(root, info, **kwargs):
   return  AuthGroupPermissions.objects.all()

@query.field("AuthPermission")
def resolve_AuthPermission(root, info, **kwargs):
   return  AuthPermission.objects.all()

@query.field("AuthUser")
def resolve_AuthUser(root, info, **kwargs):
   return  AuthUser.objects.all()

@query.field("AuthUserGroups")
def resolve_AuthUserGroups(root, info, **kwargs):
   return  AuthUserGroups.objects.all()

@query.field("AuthUserUserPermissions")
def resolve_AuthUserUserPermissions(root, info, **kwargs):
   return  AuthUserUserPermissions.objects.all()

@query.field("BasketBasket")
def resolve_BasketBasket(root, info, **kwargs):
   return  BasketBasket.objects.all()

@query.field("BasketBasketVouchers")
def resolve_BasketBasketVouchers(root, info, **kwargs):
   return  BasketBasketVouchers.objects.all()

@query.field("BasketLine")
def resolve_BasketLine(root, info, **kwargs):
   return  BasketLine.objects.all()

@query.field("BasketLineattribute")
def resolve_BasketLineattribute(root, info, **kwargs):
   return  BasketLineattribute.objects.all()

@query.field("Bootstrap4AlertsBootstrap4Alerts")
def resolve_Bootstrap4AlertsBootstrap4Alerts(root, info, **kwargs):
   return  Bootstrap4AlertsBootstrap4Alerts.objects.all()

@query.field("Bootstrap4BadgeBootstrap4Badge")
def resolve_Bootstrap4BadgeBootstrap4Badge(root, info, **kwargs):
   return  Bootstrap4BadgeBootstrap4Badge.objects.all()

@query.field("Bootstrap4CardBootstrap4Card")
def resolve_Bootstrap4CardBootstrap4Card(root, info, **kwargs):
   return  Bootstrap4CardBootstrap4Card.objects.all()

@query.field("Bootstrap4CardBootstrap4Cardinner")
def resolve_Bootstrap4CardBootstrap4Cardinner(root, info, **kwargs):
   return  Bootstrap4CardBootstrap4Cardinner.objects.all()

@query.field("Bootstrap4CarouselBootstrap4Carousel")
def resolve_Bootstrap4CarouselBootstrap4Carousel(root, info, **kwargs):
   return  Bootstrap4CarouselBootstrap4Carousel.objects.all()

@query.field("Bootstrap4CarouselBootstrap4Carouselslide")
def resolve_Bootstrap4CarouselBootstrap4Carouselslide(root, info, **kwargs):
   return  Bootstrap4CarouselBootstrap4Carouselslide.objects.all()

@query.field("Bootstrap4CollapseBootstrap4Collapse")
def resolve_Bootstrap4CollapseBootstrap4Collapse(root, info, **kwargs):
   return  Bootstrap4CollapseBootstrap4Collapse.objects.all()

@query.field("Bootstrap4CollapseBootstrap4Collapsecontainer")
def resolve_Bootstrap4CollapseBootstrap4Collapsecontainer(root, info, **kwargs):
   return  Bootstrap4CollapseBootstrap4Collapsecontainer.objects.all()

@query.field("Bootstrap4CollapseBootstrap4Collapsetrigger")
def resolve_Bootstrap4CollapseBootstrap4Collapsetrigger(root, info, **kwargs):
   return  Bootstrap4CollapseBootstrap4Collapsetrigger.objects.all()

@query.field("Bootstrap4ContentBootstrap4Blockquote")
def resolve_Bootstrap4ContentBootstrap4Blockquote(root, info, **kwargs):
   return  Bootstrap4ContentBootstrap4Blockquote.objects.all()

@query.field("Bootstrap4ContentBootstrap4Code")
def resolve_Bootstrap4ContentBootstrap4Code(root, info, **kwargs):
   return  Bootstrap4ContentBootstrap4Code.objects.all()

@query.field("Bootstrap4ContentBootstrap4Figure")
def resolve_Bootstrap4ContentBootstrap4Figure(root, info, **kwargs):
   return  Bootstrap4ContentBootstrap4Figure.objects.all()

@query.field("Bootstrap4GridBootstrap4Gridcolumn")
def resolve_Bootstrap4GridBootstrap4Gridcolumn(root, info, **kwargs):
   return  Bootstrap4GridBootstrap4Gridcolumn.objects.all()

@query.field("Bootstrap4GridBootstrap4Gridcontainer")
def resolve_Bootstrap4GridBootstrap4Gridcontainer(root, info, **kwargs):
   return  Bootstrap4GridBootstrap4Gridcontainer.objects.all()

@query.field("Bootstrap4GridBootstrap4Gridrow")
def resolve_Bootstrap4GridBootstrap4Gridrow(root, info, **kwargs):
   return  Bootstrap4GridBootstrap4Gridrow.objects.all()

@query.field("Bootstrap4JumbotronBootstrap4Jumbotron")
def resolve_Bootstrap4JumbotronBootstrap4Jumbotron(root, info, **kwargs):
   return  Bootstrap4JumbotronBootstrap4Jumbotron.objects.all()

@query.field("Bootstrap4LinkBootstrap4Link")
def resolve_Bootstrap4LinkBootstrap4Link(root, info, **kwargs):
   return  Bootstrap4LinkBootstrap4Link.objects.all()

@query.field("Bootstrap4ListgroupBootstrap4Listgroup")
def resolve_Bootstrap4ListgroupBootstrap4Listgroup(root, info, **kwargs):
   return  Bootstrap4ListgroupBootstrap4Listgroup.objects.all()

@query.field("Bootstrap4ListgroupBootstrap4Listgroupitem")
def resolve_Bootstrap4ListgroupBootstrap4Listgroupitem(root, info, **kwargs):
   return  Bootstrap4ListgroupBootstrap4Listgroupitem.objects.all()

@query.field("Bootstrap4MediaBootstrap4Media")
def resolve_Bootstrap4MediaBootstrap4Media(root, info, **kwargs):
   return  Bootstrap4MediaBootstrap4Media.objects.all()

@query.field("Bootstrap4MediaBootstrap4Mediabody")
def resolve_Bootstrap4MediaBootstrap4Mediabody(root, info, **kwargs):
   return  Bootstrap4MediaBootstrap4Mediabody.objects.all()

@query.field("Bootstrap4PictureBootstrap4Picture")
def resolve_Bootstrap4PictureBootstrap4Picture(root, info, **kwargs):
   return  Bootstrap4PictureBootstrap4Picture.objects.all()

@query.field("Bootstrap4TabsBootstrap4Tab")
def resolve_Bootstrap4TabsBootstrap4Tab(root, info, **kwargs):
   return  Bootstrap4TabsBootstrap4Tab.objects.all()

@query.field("Bootstrap4TabsBootstrap4Tabitem")
def resolve_Bootstrap4TabsBootstrap4Tabitem(root, info, **kwargs):
   return  Bootstrap4TabsBootstrap4Tabitem.objects.all()

@query.field("Bootstrap4UtilitiesBootstrap4Spacing")
def resolve_Bootstrap4UtilitiesBootstrap4Spacing(root, info, **kwargs):
   return  Bootstrap4UtilitiesBootstrap4Spacing.objects.all()

@query.field("CatalogueAttributeoption")
def resolve_CatalogueAttributeoption(root, info, **kwargs):
   return  CatalogueAttributeoption.objects.all()

@query.field("CatalogueAttributeoptiongroup")
def resolve_CatalogueAttributeoptiongroup(root, info, **kwargs):
   return  CatalogueAttributeoptiongroup.objects.all()

@query.field("CatalogueCategory")
def resolve_CatalogueCategory(root, info, **kwargs):
   return  CatalogueCategory.objects.all()

@query.field("CatalogueOption")
def resolve_CatalogueOption(root, info, **kwargs):
   return  CatalogueOption.objects.all()

@query.field("CatalogueProduct")
def resolve_CatalogueProduct(root, info, **kwargs):
   return  CatalogueProduct.objects.all()

@query.field("CatalogueProductattribute")
def resolve_CatalogueProductattribute(root, info, **kwargs):
   return  CatalogueProductattribute.objects.all()

@query.field("CatalogueProductattributevalue")
def resolve_CatalogueProductattributevalue(root, info, **kwargs):
   return  CatalogueProductattributevalue.objects.all()

@query.field("CatalogueProductattributevalueValueMultiOption")
def resolve_CatalogueProductattributevalueValueMultiOption(root, info, **kwargs):
   return  CatalogueProductattributevalueValueMultiOption.objects.all()

@query.field("CatalogueProductcategory")
def resolve_CatalogueProductcategory(root, info, **kwargs):
   return  CatalogueProductcategory.objects.all()

@query.field("CatalogueProductclass")
def resolve_CatalogueProductclass(root, info, **kwargs):
   return  CatalogueProductclass.objects.all()

@query.field("CatalogueProductclassOptions")
def resolve_CatalogueProductclassOptions(root, info, **kwargs):
   return  CatalogueProductclassOptions.objects.all()

@query.field("CatalogueProductimage")
def resolve_CatalogueProductimage(root, info, **kwargs):
   return  CatalogueProductimage.objects.all()

@query.field("CatalogueProductProductOptions")
def resolve_CatalogueProductProductOptions(root, info, **kwargs):
   return  CatalogueProductProductOptions.objects.all()

@query.field("CatalogueProductrecommendation")
def resolve_CatalogueProductrecommendation(root, info, **kwargs):
   return  CatalogueProductrecommendation.objects.all()

@query.field("CmsAliaspluginmodel")
def resolve_CmsAliaspluginmodel(root, info, **kwargs):
   return  CmsAliaspluginmodel.objects.all()

@query.field("CmsCmsplugin")
def resolve_CmsCmsplugin(root, info, **kwargs):
   return  CmsCmsplugin.objects.all()

@query.field("CmsGlobalpagepermission")
def resolve_CmsGlobalpagepermission(root, info, **kwargs):
   return  CmsGlobalpagepermission.objects.all()

@query.field("CmsGlobalpagepermissionSites")
def resolve_CmsGlobalpagepermissionSites(root, info, **kwargs):
   return  CmsGlobalpagepermissionSites.objects.all()

@query.field("CmsPage")
def resolve_CmsPage(root, info, **kwargs):
   return  CmsPage.objects.all()

@query.field("CmsPagepermission")
def resolve_CmsPagepermission(root, info, **kwargs):
   return  CmsPagepermission.objects.all()

@query.field("CmsPagePlaceholders")
def resolve_CmsPagePlaceholders(root, info, **kwargs):
   return  CmsPagePlaceholders.objects.all()

@query.field("CmsPageuser")
def resolve_CmsPageuser(root, info, **kwargs):
   return  CmsPageuser.objects.all()

@query.field("CmsPageusergroup")
def resolve_CmsPageusergroup(root, info, **kwargs):
   return  CmsPageusergroup.objects.all()

@query.field("CmsPlaceholder")
def resolve_CmsPlaceholder(root, info, **kwargs):
   return  CmsPlaceholder.objects.all()

@query.field("CmsPlaceholderreference")
def resolve_CmsPlaceholderreference(root, info, **kwargs):
   return  CmsPlaceholderreference.objects.all()

@query.field("CmsStaticplaceholder")
def resolve_CmsStaticplaceholder(root, info, **kwargs):
   return  CmsStaticplaceholder.objects.all()

@query.field("CmsTitle")
def resolve_CmsTitle(root, info, **kwargs):
   return  CmsTitle.objects.all()

@query.field("CmsTreenode")
def resolve_CmsTreenode(root, info, **kwargs):
   return  CmsTreenode.objects.all()

@query.field("CmsUrlconfrevision")
def resolve_CmsUrlconfrevision(root, info, **kwargs):
   return  CmsUrlconfrevision.objects.all()

@query.field("CmsUsersettings")
def resolve_CmsUsersettings(root, info, **kwargs):
   return  CmsUsersettings.objects.all()

@query.field("CommunicationCommunicationeventtype")
def resolve_CommunicationCommunicationeventtype(root, info, **kwargs):
   return  CommunicationCommunicationeventtype.objects.all()

@query.field("CommunicationEmail")
def resolve_CommunicationEmail(root, info, **kwargs):
   return  CommunicationEmail.objects.all()

@query.field("CommunicationNotification")
def resolve_CommunicationNotification(root, info, **kwargs):
   return  CommunicationNotification.objects.all()

@query.field("CustomerProductalert")
def resolve_CustomerProductalert(root, info, **kwargs):
   return  CustomerProductalert.objects.all()

@query.field("DjangoAdminLog")
def resolve_DjangoAdminLog(root, info, **kwargs):
   return  DjangoAdminLog.objects.all()

@query.field("DjangocmsBlogAuthorentriesplugin")
def resolve_DjangocmsBlogAuthorentriesplugin(root, info, **kwargs):
   return  DjangocmsBlogAuthorentriesplugin.objects.all()

@query.field("DjangocmsBlogAuthorentriespluginAuthors")
def resolve_DjangocmsBlogAuthorentriespluginAuthors(root, info, **kwargs):
   return  DjangocmsBlogAuthorentriespluginAuthors.objects.all()

@query.field("DjangocmsBlogBlogcategory")
def resolve_DjangocmsBlogBlogcategory(root, info, **kwargs):
   return  DjangocmsBlogBlogcategory.objects.all()

@query.field("DjangocmsBlogBlogcategoryTranslation")
def resolve_DjangocmsBlogBlogcategoryTranslation(root, info, **kwargs):
   return  DjangocmsBlogBlogcategoryTranslation.objects.all()

@query.field("DjangocmsBlogBlogconfig")
def resolve_DjangocmsBlogBlogconfig(root, info, **kwargs):
   return  DjangocmsBlogBlogconfig.objects.all()

@query.field("DjangocmsBlogBlogconfigTranslation")
def resolve_DjangocmsBlogBlogconfigTranslation(root, info, **kwargs):
   return  DjangocmsBlogBlogconfigTranslation.objects.all()

@query.field("DjangocmsBlogGenericblogplugin")
def resolve_DjangocmsBlogGenericblogplugin(root, info, **kwargs):
   return  DjangocmsBlogGenericblogplugin.objects.all()

@query.field("DjangocmsBlogLatestpostsplugin")
def resolve_DjangocmsBlogLatestpostsplugin(root, info, **kwargs):
   return  DjangocmsBlogLatestpostsplugin.objects.all()

@query.field("DjangocmsBlogLatestpostspluginCategories")
def resolve_DjangocmsBlogLatestpostspluginCategories(root, info, **kwargs):
   return  DjangocmsBlogLatestpostspluginCategories.objects.all()

@query.field("DjangocmsBlogPost")
def resolve_DjangocmsBlogPost(root, info, **kwargs):
   return  DjangocmsBlogPost.objects.all()

@query.field("DjangocmsBlogPostCategories")
def resolve_DjangocmsBlogPostCategories(root, info, **kwargs):
   return  DjangocmsBlogPostCategories.objects.all()

@query.field("DjangocmsBlogPostRelated")
def resolve_DjangocmsBlogPostRelated(root, info, **kwargs):
   return  DjangocmsBlogPostRelated.objects.all()

@query.field("DjangocmsBlogPostSites")
def resolve_DjangocmsBlogPostSites(root, info, **kwargs):
   return  DjangocmsBlogPostSites.objects.all()

@query.field("DjangocmsBlogPostTranslation")
def resolve_DjangocmsBlogPostTranslation(root, info, **kwargs):
   return  DjangocmsBlogPostTranslation.objects.all()

@query.field("DjangocmsFileFile")
def resolve_DjangocmsFileFile(root, info, **kwargs):
   return  DjangocmsFileFile.objects.all()

@query.field("DjangocmsFileFolder")
def resolve_DjangocmsFileFolder(root, info, **kwargs):
   return  DjangocmsFileFolder.objects.all()

@query.field("DjangocmsGooglemapGooglemap")
def resolve_DjangocmsGooglemapGooglemap(root, info, **kwargs):
   return  DjangocmsGooglemapGooglemap.objects.all()

@query.field("DjangocmsGooglemapGooglemapmarker")
def resolve_DjangocmsGooglemapGooglemapmarker(root, info, **kwargs):
   return  DjangocmsGooglemapGooglemapmarker.objects.all()

@query.field("DjangocmsGooglemapGooglemaproute")
def resolve_DjangocmsGooglemapGooglemaproute(root, info, **kwargs):
   return  DjangocmsGooglemapGooglemaproute.objects.all()

@query.field("DjangocmsHistoryPlaceholderaction")
def resolve_DjangocmsHistoryPlaceholderaction(root, info, **kwargs):
   return  DjangocmsHistoryPlaceholderaction.objects.all()

@query.field("DjangocmsHistoryPlaceholderoperation")
def resolve_DjangocmsHistoryPlaceholderoperation(root, info, **kwargs):
   return  DjangocmsHistoryPlaceholderoperation.objects.all()

@query.field("DjangocmsIconIcon")
def resolve_DjangocmsIconIcon(root, info, **kwargs):
   return  DjangocmsIconIcon.objects.all()

@query.field("DjangocmsLinkLink")
def resolve_DjangocmsLinkLink(root, info, **kwargs):
   return  DjangocmsLinkLink.objects.all()

@query.field("DjangocmsMapsMaps")
def resolve_DjangocmsMapsMaps(root, info, **kwargs):
   return  DjangocmsMapsMaps.objects.all()

@query.field("DjangocmsPicturePicture")
def resolve_DjangocmsPicturePicture(root, info, **kwargs):
   return  DjangocmsPicturePicture.objects.all()

@query.field("DjangocmsStyleStyle")
def resolve_DjangocmsStyleStyle(root, info, **kwargs):
   return  DjangocmsStyleStyle.objects.all()

@query.field("DjangocmsTextCkeditorText")
def resolve_DjangocmsTextCkeditorText(root, info, **kwargs):
   return  DjangocmsTextCkeditorText.objects.all()

@query.field("DjangocmsVideoVideoplayer")
def resolve_DjangocmsVideoVideoplayer(root, info, **kwargs):
   return  DjangocmsVideoVideoplayer.objects.all()

@query.field("DjangocmsVideoVideosource")
def resolve_DjangocmsVideoVideosource(root, info, **kwargs):
   return  DjangocmsVideoVideosource.objects.all()

@query.field("DjangocmsVideoVideotrack")
def resolve_DjangocmsVideoVideotrack(root, info, **kwargs):
   return  DjangocmsVideoVideotrack.objects.all()

@query.field("DjangoFlatpage")
def resolve_DjangoFlatpage(root, info, **kwargs):
   return  DjangoFlatpage.objects.all()

@query.field("DjangoFlatpageSites")
def resolve_DjangoFlatpageSites(root, info, **kwargs):
   return  DjangoFlatpageSites.objects.all()

@query.field("DjangoSession")
def resolve_DjangoSession(root, info, **kwargs):
   return  DjangoSession.objects.all()

@query.field("DjangoSite")
def resolve_DjangoSite(root, info, **kwargs):
   return  DjangoSite.objects.all()

@query.field("EasyThumbnailsSource")
def resolve_EasyThumbnailsSource(root, info, **kwargs):
   return  EasyThumbnailsSource.objects.all()

@query.field("EasyThumbnailsThumbnail")
def resolve_EasyThumbnailsThumbnail(root, info, **kwargs):
   return  EasyThumbnailsThumbnail.objects.all()

@query.field("EasyThumbnailsThumbnaildimensions")
def resolve_EasyThumbnailsThumbnaildimensions(root, info, **kwargs):
   return  EasyThumbnailsThumbnaildimensions.objects.all()

@query.field("FilerClipboard")
def resolve_FilerClipboard(root, info, **kwargs):
   return  FilerClipboard.objects.all()

@query.field("FilerClipboarditem")
def resolve_FilerClipboarditem(root, info, **kwargs):
   return  FilerClipboarditem.objects.all()

@query.field("FilerFile")
def resolve_FilerFile(root, info, **kwargs):
   return  FilerFile.objects.all()

@query.field("FilerFolder")
def resolve_FilerFolder(root, info, **kwargs):
   return  FilerFolder.objects.all()

@query.field("FilerFolderpermission")
def resolve_FilerFolderpermission(root, info, **kwargs):
   return  FilerFolderpermission.objects.all()

@query.field("FilerImage")
def resolve_FilerImage(root, info, **kwargs):
   return  FilerImage.objects.all()

@query.field("FilerThumbnailoption")
def resolve_FilerThumbnailoption(root, info, **kwargs):
   return  FilerThumbnailoption.objects.all()

@query.field("MenusCachekey")
def resolve_MenusCachekey(root, info, **kwargs):
   return  MenusCachekey.objects.all()

@query.field("OfferBenefit")
def resolve_OfferBenefit(root, info, **kwargs):
   return  OfferBenefit.objects.all()

@query.field("OfferCondition")
def resolve_OfferCondition(root, info, **kwargs):
   return  OfferCondition.objects.all()

@query.field("OfferConditionaloffer")
def resolve_OfferConditionaloffer(root, info, **kwargs):
   return  OfferConditionaloffer.objects.all()

@query.field("OfferConditionalofferCombinations")
def resolve_OfferConditionalofferCombinations(root, info, **kwargs):
   return  OfferConditionalofferCombinations.objects.all()

@query.field("OfferRange")
def resolve_OfferRange(root, info, **kwargs):
   return  OfferRange.objects.all()

@query.field("OfferRangeClasses")
def resolve_OfferRangeClasses(root, info, **kwargs):
   return  OfferRangeClasses.objects.all()

@query.field("OfferRangeExcludedProducts")
def resolve_OfferRangeExcludedProducts(root, info, **kwargs):
   return  OfferRangeExcludedProducts.objects.all()

@query.field("OfferRangeIncludedCategories")
def resolve_OfferRangeIncludedCategories(root, info, **kwargs):
   return  OfferRangeIncludedCategories.objects.all()

@query.field("OfferRangeproduct")
def resolve_OfferRangeproduct(root, info, **kwargs):
   return  OfferRangeproduct.objects.all()

@query.field("OfferRangeproductfileupload")
def resolve_OfferRangeproductfileupload(root, info, **kwargs):
   return  OfferRangeproductfileupload.objects.all()

@query.field("OrderBillingaddress")
def resolve_OrderBillingaddress(root, info, **kwargs):
   return  OrderBillingaddress.objects.all()

@query.field("OrderCommunicationevent")
def resolve_OrderCommunicationevent(root, info, **kwargs):
   return  OrderCommunicationevent.objects.all()

@query.field("OrderLine")
def resolve_OrderLine(root, info, **kwargs):
   return  OrderLine.objects.all()

@query.field("OrderLineattribute")
def resolve_OrderLineattribute(root, info, **kwargs):
   return  OrderLineattribute.objects.all()

@query.field("OrderLineprice")
def resolve_OrderLineprice(root, info, **kwargs):
   return  OrderLineprice.objects.all()

@query.field("OrderOrder")
def resolve_OrderOrder(root, info, **kwargs):
   return  OrderOrder.objects.all()

@query.field("OrderOrderdiscount")
def resolve_OrderOrderdiscount(root, info, **kwargs):
   return  OrderOrderdiscount.objects.all()

@query.field("OrderOrdernote")
def resolve_OrderOrdernote(root, info, **kwargs):
   return  OrderOrdernote.objects.all()

@query.field("OrderOrderstatuschange")
def resolve_OrderOrderstatuschange(root, info, **kwargs):
   return  OrderOrderstatuschange.objects.all()

@query.field("OrderPaymentevent")
def resolve_OrderPaymentevent(root, info, **kwargs):
   return  OrderPaymentevent.objects.all()

@query.field("OrderPaymenteventquantity")
def resolve_OrderPaymenteventquantity(root, info, **kwargs):
   return  OrderPaymenteventquantity.objects.all()

@query.field("OrderPaymenteventtype")
def resolve_OrderPaymenteventtype(root, info, **kwargs):
   return  OrderPaymenteventtype.objects.all()

@query.field("OrderShippingaddress")
def resolve_OrderShippingaddress(root, info, **kwargs):
   return  OrderShippingaddress.objects.all()

@query.field("OrderShippingevent")
def resolve_OrderShippingevent(root, info, **kwargs):
   return  OrderShippingevent.objects.all()

@query.field("OrderShippingeventquantity")
def resolve_OrderShippingeventquantity(root, info, **kwargs):
   return  OrderShippingeventquantity.objects.all()

@query.field("OrderShippingeventtype")
def resolve_OrderShippingeventtype(root, info, **kwargs):
   return  OrderShippingeventtype.objects.all()

@query.field("OrderSurcharge")
def resolve_OrderSurcharge(root, info, **kwargs):
   return  OrderSurcharge.objects.all()

@query.field("OscarapiApikey")
def resolve_OscarapiApikey(root, info, **kwargs):
   return  OscarapiApikey.objects.all()

@query.field("OscarInvoicesInvoice")
def resolve_OscarInvoicesInvoice(root, info, **kwargs):
   return  OscarInvoicesInvoice.objects.all()

@query.field("OscarInvoicesLegalentity")
def resolve_OscarInvoicesLegalentity(root, info, **kwargs):
   return  OscarInvoicesLegalentity.objects.all()

@query.field("OscarInvoicesLegalentityaddress")
def resolve_OscarInvoicesLegalentityaddress(root, info, **kwargs):
   return  OscarInvoicesLegalentityaddress.objects.all()

@query.field("PartnerPartner")
def resolve_PartnerPartner(root, info, **kwargs):
   return  PartnerPartner.objects.all()

@query.field("PartnerPartneraddress")
def resolve_PartnerPartneraddress(root, info, **kwargs):
   return  PartnerPartneraddress.objects.all()

@query.field("PartnerPartnerUsers")
def resolve_PartnerPartnerUsers(root, info, **kwargs):
   return  PartnerPartnerUsers.objects.all()

@query.field("PartnerStockalert")
def resolve_PartnerStockalert(root, info, **kwargs):
   return  PartnerStockalert.objects.all()

@query.field("PartnerStockrecord")
def resolve_PartnerStockrecord(root, info, **kwargs):
   return  PartnerStockrecord.objects.all()

@query.field("PaymentBankcard")
def resolve_PaymentBankcard(root, info, **kwargs):
   return  PaymentBankcard.objects.all()

@query.field("PaymentSource")
def resolve_PaymentSource(root, info, **kwargs):
   return  PaymentSource.objects.all()

@query.field("PaymentSourcetype")
def resolve_PaymentSourcetype(root, info, **kwargs):
   return  PaymentSourcetype.objects.all()

@query.field("PaymentTransaction")
def resolve_PaymentTransaction(root, info, **kwargs):
   return  PaymentTransaction.objects.all()

@query.field("PaypalExpresstransaction")
def resolve_PaypalExpresstransaction(root, info, **kwargs):
   return  PaypalExpresstransaction.objects.all()

@query.field("PaypalPayflowtransaction")
def resolve_PaypalPayflowtransaction(root, info, **kwargs):
   return  PaypalPayflowtransaction.objects.all()

@query.field("PhotologueGallery")
def resolve_PhotologueGallery(root, info, **kwargs):
   return  PhotologueGallery.objects.all()

@query.field("PhotologueGalleryPhotos")
def resolve_PhotologueGalleryPhotos(root, info, **kwargs):
   return  PhotologueGalleryPhotos.objects.all()

@query.field("PhotologueGallerySites")
def resolve_PhotologueGallerySites(root, info, **kwargs):
   return  PhotologueGallerySites.objects.all()

@query.field("PhotologuePhoto")
def resolve_PhotologuePhoto(root, info, **kwargs):
   return  PhotologuePhoto.objects.all()

@query.field("PhotologuePhotoeffect")
def resolve_PhotologuePhotoeffect(root, info, **kwargs):
   return  PhotologuePhotoeffect.objects.all()

@query.field("PhotologuePhotoSites")
def resolve_PhotologuePhotoSites(root, info, **kwargs):
   return  PhotologuePhotoSites.objects.all()

@query.field("PhotologuePhotosize")
def resolve_PhotologuePhotosize(root, info, **kwargs):
   return  PhotologuePhotosize.objects.all()

@query.field("PhotologueWatermark")
def resolve_PhotologueWatermark(root, info, **kwargs):
   return  PhotologueWatermark.objects.all()

@query.field("PinaxBadgesBadgeaward")
def resolve_PinaxBadgesBadgeaward(root, info, **kwargs):
   return  PinaxBadgesBadgeaward.objects.all()

@query.field("PinaxEventsEvent")
def resolve_PinaxEventsEvent(root, info, **kwargs):
   return  PinaxEventsEvent.objects.all()

@query.field("PinaxMessagesMessage")
def resolve_PinaxMessagesMessage(root, info, **kwargs):
   return  PinaxMessagesMessage.objects.all()

@query.field("PinaxMessagesThread")
def resolve_PinaxMessagesThread(root, info, **kwargs):
   return  PinaxMessagesThread.objects.all()

@query.field("PinaxMessagesUserthread")
def resolve_PinaxMessagesUserthread(root, info, **kwargs):
   return  PinaxMessagesUserthread.objects.all()

@query.field("ReviewsProductreview")
def resolve_ReviewsProductreview(root, info, **kwargs):
   return  ReviewsProductreview.objects.all()

@query.field("ReviewsVote")
def resolve_ReviewsVote(root, info, **kwargs):
   return  ReviewsVote.objects.all()

@query.field("ShippingOrderanditemcharges")
def resolve_ShippingOrderanditemcharges(root, info, **kwargs):
   return  ShippingOrderanditemcharges.objects.all()

@query.field("ShippingOrderanditemchargesCountries")
def resolve_ShippingOrderanditemchargesCountries(root, info, **kwargs):
   return  ShippingOrderanditemchargesCountries.objects.all()

@query.field("ShippingWeightband")
def resolve_ShippingWeightband(root, info, **kwargs):
   return  ShippingWeightband.objects.all()

@query.field("ShippingWeightbased")
def resolve_ShippingWeightbased(root, info, **kwargs):
   return  ShippingWeightbased.objects.all()

@query.field("ShippingWeightbasedCountries")
def resolve_ShippingWeightbasedCountries(root, info, **kwargs):
   return  ShippingWeightbasedCountries.objects.all()

@query.field("TaggitTag")
def resolve_TaggitTag(root, info, **kwargs):
   return  TaggitTag.objects.all()

@query.field("TaggitTaggeditem")
def resolve_TaggitTaggeditem(root, info, **kwargs):
   return  TaggitTaggeditem.objects.all()

@query.field("TestimonialsTestimonial")
def resolve_TestimonialsTestimonial(root, info, **kwargs):
   return  TestimonialsTestimonial.objects.all()

@query.field("ThumbnailKvstore")
def resolve_ThumbnailKvstore(root, info, **kwargs):
   return  ThumbnailKvstore.objects.all()

@query.field("VoucherVoucher")
def resolve_VoucherVoucher(root, info, **kwargs):
   return  VoucherVoucher.objects.all()

@query.field("VoucherVoucherapplication")
def resolve_VoucherVoucherapplication(root, info, **kwargs):
   return  VoucherVoucherapplication.objects.all()

@query.field("VoucherVoucherOffers")
def resolve_VoucherVoucherOffers(root, info, **kwargs):
   return  VoucherVoucherOffers.objects.all()

@query.field("VoucherVoucherset")
def resolve_VoucherVoucherset(root, info, **kwargs):
   return  VoucherVoucherset.objects.all()

@query.field("WishlistsLine")
def resolve_WishlistsLine(root, info, **kwargs):
   return  WishlistsLine.objects.all()

@query.field("WishlistsWishlist")
def resolve_WishlistsWishlist(root, info, **kwargs):
   return  WishlistsWishlist.objects.all()
from ariadne import QueryType, make_executable_schema
from .models import *

type_defs = """
    type Query {
       AddressCountry: String!
       AddressUseraddress: String!
       AdvancedFiltersAdvancedfilter: String!
       AdvancedFiltersAdvancedfilterGroups: String!
       AdvancedFiltersAdvancedfilterUsers: String!
       AnalyticsProductrecord: String!
       AnalyticsUserproductview: String!
       AnalyticsUserrecord: String!
       AnalyticsUsersearch: String!
       AnnouncementsAnnouncement: String!
       AnnouncementsDismissal: String!
       AuthGroup: String!
       AuthGroupPermissions: String!
       AuthPermission: String!
       AuthUser: String!
       AuthUserGroups: String!
       AuthUserUserPermissions: String!
       BasketBasket: String!
       BasketBasketVouchers: String!
       BasketLine: String!
       BasketLineattribute: String!
       Bootstrap4AlertsBootstrap4Alerts: String!
       Bootstrap4BadgeBootstrap4Badge: String!
       Bootstrap4CardBootstrap4Card: String!
       Bootstrap4CardBootstrap4Cardinner: String!
       Bootstrap4CarouselBootstrap4Carousel: String!
       Bootstrap4CarouselBootstrap4Carouselslide: String!
       Bootstrap4CollapseBootstrap4Collapse: String!
       Bootstrap4CollapseBootstrap4Collapsecontainer: String!
       Bootstrap4CollapseBootstrap4Collapsetrigger: String!
       Bootstrap4ContentBootstrap4Blockquote: String!
       Bootstrap4ContentBootstrap4Code: String!
       Bootstrap4ContentBootstrap4Figure: String!
       Bootstrap4GridBootstrap4Gridcolumn: String!
       Bootstrap4GridBootstrap4Gridcontainer: String!
       Bootstrap4GridBootstrap4Gridrow: String!
       Bootstrap4JumbotronBootstrap4Jumbotron: String!
       Bootstrap4LinkBootstrap4Link: String!
       Bootstrap4ListgroupBootstrap4Listgroup: String!
       Bootstrap4ListgroupBootstrap4Listgroupitem: String!
       Bootstrap4MediaBootstrap4Media: String!
       Bootstrap4MediaBootstrap4Mediabody: String!
       Bootstrap4PictureBootstrap4Picture: String!
       Bootstrap4TabsBootstrap4Tab: String!
       Bootstrap4TabsBootstrap4Tabitem: String!
       Bootstrap4UtilitiesBootstrap4Spacing: String!
       CatalogueAttributeoption: String!
       CatalogueAttributeoptiongroup: String!
       CatalogueCategory: String!
       CatalogueOption: String!
       CatalogueProduct: String!
       CatalogueProductattribute: String!
       CatalogueProductattributevalue: String!
       CatalogueProductattributevalueValueMultiOption: String!
       CatalogueProductcategory: String!
       CatalogueProductclass: String!
       CatalogueProductclassOptions: String!
       CatalogueProductimage: String!
       CatalogueProductProductOptions: String!
       CatalogueProductrecommendation: String!
       CmsAliaspluginmodel: String!
       CmsCmsplugin: String!
       CmsGlobalpagepermission: String!
       CmsGlobalpagepermissionSites: String!
       CmsPage: String!
       CmsPagepermission: String!
       CmsPagePlaceholders: String!
       CmsPageuser: String!
       CmsPageusergroup: String!
       CmsPlaceholder: String!
       CmsPlaceholderreference: String!
       CmsStaticplaceholder: String!
       CmsTitle: String!
       CmsTreenode: String!
       CmsUrlconfrevision: String!
       CmsUsersettings: String!
       CommunicationCommunicationeventtype: String!
       CommunicationEmail: String!
       CommunicationNotification: String!
       CustomerProductalert: String!
       DjangoAdminLog: String!
       DjangocmsBlogAuthorentriesplugin: String!
       DjangocmsBlogAuthorentriespluginAuthors: String!
       DjangocmsBlogBlogcategory: String!
       DjangocmsBlogBlogcategoryTranslation: String!
       DjangocmsBlogBlogconfig: String!
       DjangocmsBlogBlogconfigTranslation: String!
       DjangocmsBlogGenericblogplugin: String!
       DjangocmsBlogLatestpostsplugin: String!
       DjangocmsBlogLatestpostspluginCategories: String!
       DjangocmsBlogPost: String!
       DjangocmsBlogPostCategories: String!
       DjangocmsBlogPostRelated: String!
       DjangocmsBlogPostSites: String!
       DjangocmsBlogPostTranslation: String!
       DjangocmsFileFile: String!
       DjangocmsFileFolder: String!
       DjangocmsGooglemapGooglemap: String!
       DjangocmsGooglemapGooglemapmarker: String!
       DjangocmsGooglemapGooglemaproute: String!
       DjangocmsHistoryPlaceholderaction: String!
       DjangocmsHistoryPlaceholderoperation: String!
       DjangocmsIconIcon: String!
       DjangocmsLinkLink: String!
       DjangocmsMapsMaps: String!
       DjangocmsPicturePicture: String!
       DjangocmsStyleStyle: String!
       DjangocmsTextCkeditorText: String!
       DjangocmsVideoVideoplayer: String!
       DjangocmsVideoVideosource: String!
       DjangocmsVideoVideotrack: String!
       DjangoFlatpage: String!
       DjangoFlatpageSites: String!
       DjangoSession: String!
       DjangoSite: String!
       EasyThumbnailsSource: String!
       EasyThumbnailsThumbnail: String!
       EasyThumbnailsThumbnaildimensions: String!
       FilerClipboard: String!
       FilerClipboarditem: String!
       FilerFile: String!
       FilerFolder: String!
       FilerFolderpermission: String!
       FilerImage: String!
       FilerThumbnailoption: String!
       MenusCachekey: String!
       OfferBenefit: String!
       OfferCondition: String!
       OfferConditionaloffer: String!
       OfferConditionalofferCombinations: String!
       OfferRange: String!
       OfferRangeClasses: String!
       OfferRangeExcludedProducts: String!
       OfferRangeIncludedCategories: String!
       OfferRangeproduct: String!
       OfferRangeproductfileupload: String!
       OrderBillingaddress: String!
       OrderCommunicationevent: String!
       OrderLine: String!
       OrderLineattribute: String!
       OrderLineprice: String!
       OrderOrder: String!
       OrderOrderdiscount: String!
       OrderOrdernote: String!
       OrderOrderstatuschange: String!
       OrderPaymentevent: String!
       OrderPaymenteventquantity: String!
       OrderPaymenteventtype: String!
       OrderShippingaddress: String!
       OrderShippingevent: String!
       OrderShippingeventquantity: String!
       OrderShippingeventtype: String!
       OrderSurcharge: String!
       OscarapiApikey: String!
       OscarInvoicesInvoice: String!
       OscarInvoicesLegalentity: String!
       OscarInvoicesLegalentityaddress: String!
       PartnerPartner: String!
       PartnerPartneraddress: String!
       PartnerPartnerUsers: String!
       PartnerStockalert: String!
       PartnerStockrecord: String!
       PaymentBankcard: String!
       PaymentSource: String!
       PaymentSourcetype: String!
       PaymentTransaction: String!
       PaypalExpresstransaction: String!
       PaypalPayflowtransaction: String!
       PhotologueGallery: String!
       PhotologueGalleryPhotos: String!
       PhotologueGallerySites: String!
       PhotologuePhoto: String!
       PhotologuePhotoeffect: String!
       PhotologuePhotoSites: String!
       PhotologuePhotosize: String!
       PhotologueWatermark: String!
       PinaxBadgesBadgeaward: String!
       PinaxEventsEvent: String!
       PinaxMessagesMessage: String!
       PinaxMessagesThread: String!
       PinaxMessagesUserthread: String!
       ReviewsProductreview: String!
       ReviewsVote: String!
       ShippingOrderanditemcharges: String!
       ShippingOrderanditemchargesCountries: String!
       ShippingWeightband: String!
       ShippingWeightbased: String!
       ShippingWeightbasedCountries: String!
       TaggitTag: String!
       TaggitTaggeditem: String!
       TestimonialsTestimonial: String!
       ThumbnailKvstore: String!
       VoucherVoucher: String!
       VoucherVoucherapplication: String!
       VoucherVoucherOffers: String!
       VoucherVoucherset: String!
       WishlistsLine: String!
       WishlistsWishlist: String!
	}
"""

query = QueryType()

@query.field("AddressCountry")	
def resolve_AddressCountry(self, info, **kwargs):
   return  AddressCountry.objects.all()

@query.field("AddressUseraddress")
def resolve_AddressUseraddress(self, info, **kwargs):
   return  AddressUseraddress.objects.all()

@query.field("AdvancedFiltersAdvancedfilter")
def resolve_AdvancedFiltersAdvancedfilter(self, info, **kwargs):
   return  AdvancedFiltersAdvancedfilter.objects.all()

@query.field("AdvancedFiltersAdvancedfilterGroups")
def resolve_AdvancedFiltersAdvancedfilterGroups(self, info, **kwargs):
   return  AdvancedFiltersAdvancedfilterGroups.objects.all()

@query.field("AdvancedFiltersAdvancedfilterUsers")
def resolve_AdvancedFiltersAdvancedfilterUsers(self, info, **kwargs):
   return  AdvancedFiltersAdvancedfilterUsers.objects.all()

@query.field("AnalyticsProductrecord")
def resolve_AnalyticsProductrecord(self, info, **kwargs):
   return  AnalyticsProductrecord.objects.all()

@query.field("AnalyticsUserproductview")
def resolve_AnalyticsUserproductview(self, info, **kwargs):
   return  AnalyticsUserproductview.objects.all()

@query.field("AnalyticsUserrecord")
def resolve_AnalyticsUserrecord(self, info, **kwargs):
   return  AnalyticsUserrecord.objects.all()

@query.field("AnalyticsUsersearch")
def resolve_AnalyticsUsersearch(self, info, **kwargs):
   return  AnalyticsUsersearch.objects.all()

@query.field("AnnouncementsAnnouncement")
def resolve_AnnouncementsAnnouncement(self, info, **kwargs):
   return  AnnouncementsAnnouncement.objects.all()

@query.field("AnnouncementsDismissal")
def resolve_AnnouncementsDismissal(self, info, **kwargs):
   return  AnnouncementsDismissal.objects.all()

@query.field("AuthGroup")
def resolve_AuthGroup(self, info, **kwargs):
   return  AuthGroup.objects.all()

@query.field("AuthGroupPermissions")
def resolve_AuthGroupPermissions(self, info, **kwargs):
   return  AuthGroupPermissions.objects.all()

@query.field("AuthPermission")
def resolve_AuthPermission(self, info, **kwargs):
   return  AuthPermission.objects.all()

@query.field("AuthUser")
def resolve_AuthUser(self, info, **kwargs):
   return  AuthUser.objects.all()

@query.field("AuthUserGroups")
def resolve_AuthUserGroups(self, info, **kwargs):
   return  AuthUserGroups.objects.all()

@query.field("AuthUserUserPermissions")
def resolve_AuthUserUserPermissions(self, info, **kwargs):
   return  AuthUserUserPermissions.objects.all()

@query.field("BasketBasket")
def resolve_BasketBasket(self, info, **kwargs):
   return  BasketBasket.objects.all()

@query.field("BasketBasketVouchers")
def resolve_BasketBasketVouchers(self, info, **kwargs):
   return  BasketBasketVouchers.objects.all()

@query.field("BasketLine")
def resolve_BasketLine(self, info, **kwargs):
   return  BasketLine.objects.all()

@query.field("BasketLineattribute")
def resolve_BasketLineattribute(self, info, **kwargs):
   return  BasketLineattribute.objects.all()

@query.field("Bootstrap4AlertsBootstrap4Alerts")
def resolve_Bootstrap4AlertsBootstrap4Alerts(self, info, **kwargs):
   return  Bootstrap4AlertsBootstrap4Alerts.objects.all()

@query.field("Bootstrap4BadgeBootstrap4Badge")
def resolve_Bootstrap4BadgeBootstrap4Badge(self, info, **kwargs):
   return  Bootstrap4BadgeBootstrap4Badge.objects.all()

@query.field("Bootstrap4CardBootstrap4Card")
def resolve_Bootstrap4CardBootstrap4Card(self, info, **kwargs):
   return  Bootstrap4CardBootstrap4Card.objects.all()

@query.field("Bootstrap4CardBootstrap4Cardinner")
def resolve_Bootstrap4CardBootstrap4Cardinner(self, info, **kwargs):
   return  Bootstrap4CardBootstrap4Cardinner.objects.all()

@query.field("Bootstrap4CarouselBootstrap4Carousel")
def resolve_Bootstrap4CarouselBootstrap4Carousel(self, info, **kwargs):
   return  Bootstrap4CarouselBootstrap4Carousel.objects.all()

@query.field("Bootstrap4CarouselBootstrap4Carouselslide")
def resolve_Bootstrap4CarouselBootstrap4Carouselslide(self, info, **kwargs):
   return  Bootstrap4CarouselBootstrap4Carouselslide.objects.all()

@query.field("Bootstrap4CollapseBootstrap4Collapse")
def resolve_Bootstrap4CollapseBootstrap4Collapse(self, info, **kwargs):
   return  Bootstrap4CollapseBootstrap4Collapse.objects.all()

@query.field("Bootstrap4CollapseBootstrap4Collapsecontainer")
def resolve_Bootstrap4CollapseBootstrap4Collapsecontainer(self, info, **kwargs):
   return  Bootstrap4CollapseBootstrap4Collapsecontainer.objects.all()

@query.field("Bootstrap4CollapseBootstrap4Collapsetrigger")
def resolve_Bootstrap4CollapseBootstrap4Collapsetrigger(self, info, **kwargs):
   return  Bootstrap4CollapseBootstrap4Collapsetrigger.objects.all()

@query.field("Bootstrap4ContentBootstrap4Blockquote")
def resolve_Bootstrap4ContentBootstrap4Blockquote(self, info, **kwargs):
   return  Bootstrap4ContentBootstrap4Blockquote.objects.all()

@query.field("Bootstrap4ContentBootstrap4Code")
def resolve_Bootstrap4ContentBootstrap4Code(self, info, **kwargs):
   return  Bootstrap4ContentBootstrap4Code.objects.all()

@query.field("Bootstrap4ContentBootstrap4Figure")
def resolve_Bootstrap4ContentBootstrap4Figure(self, info, **kwargs):
   return  Bootstrap4ContentBootstrap4Figure.objects.all()

@query.field("Bootstrap4GridBootstrap4Gridcolumn")
def resolve_Bootstrap4GridBootstrap4Gridcolumn(self, info, **kwargs):
   return  Bootstrap4GridBootstrap4Gridcolumn.objects.all()

@query.field("Bootstrap4GridBootstrap4Gridcontainer")
def resolve_Bootstrap4GridBootstrap4Gridcontainer(self, info, **kwargs):
   return  Bootstrap4GridBootstrap4Gridcontainer.objects.all()

@query.field("Bootstrap4GridBootstrap4Gridrow")
def resolve_Bootstrap4GridBootstrap4Gridrow(self, info, **kwargs):
   return  Bootstrap4GridBootstrap4Gridrow.objects.all()

@query.field("Bootstrap4JumbotronBootstrap4Jumbotron")
def resolve_Bootstrap4JumbotronBootstrap4Jumbotron(self, info, **kwargs):
   return  Bootstrap4JumbotronBootstrap4Jumbotron.objects.all()

@query.field("Bootstrap4LinkBootstrap4Link")
def resolve_Bootstrap4LinkBootstrap4Link(self, info, **kwargs):
   return  Bootstrap4LinkBootstrap4Link.objects.all()

@query.field("Bootstrap4ListgroupBootstrap4Listgroup")
def resolve_Bootstrap4ListgroupBootstrap4Listgroup(self, info, **kwargs):
   return  Bootstrap4ListgroupBootstrap4Listgroup.objects.all()

@query.field("Bootstrap4ListgroupBootstrap4Listgroupitem")
def resolve_Bootstrap4ListgroupBootstrap4Listgroupitem(self, info, **kwargs):
   return  Bootstrap4ListgroupBootstrap4Listgroupitem.objects.all()

@query.field("Bootstrap4MediaBootstrap4Media")
def resolve_Bootstrap4MediaBootstrap4Media(self, info, **kwargs):
   return  Bootstrap4MediaBootstrap4Media.objects.all()

@query.field("Bootstrap4MediaBootstrap4Mediabody")
def resolve_Bootstrap4MediaBootstrap4Mediabody(self, info, **kwargs):
   return  Bootstrap4MediaBootstrap4Mediabody.objects.all()

@query.field("Bootstrap4PictureBootstrap4Picture")
def resolve_Bootstrap4PictureBootstrap4Picture(self, info, **kwargs):
   return  Bootstrap4PictureBootstrap4Picture.objects.all()

@query.field("Bootstrap4TabsBootstrap4Tab")
def resolve_Bootstrap4TabsBootstrap4Tab(self, info, **kwargs):
   return  Bootstrap4TabsBootstrap4Tab.objects.all()

@query.field("Bootstrap4TabsBootstrap4Tabitem")
def resolve_Bootstrap4TabsBootstrap4Tabitem(self, info, **kwargs):
   return  Bootstrap4TabsBootstrap4Tabitem.objects.all()

@query.field("Bootstrap4UtilitiesBootstrap4Spacing")
def resolve_Bootstrap4UtilitiesBootstrap4Spacing(self, info, **kwargs):
   return  Bootstrap4UtilitiesBootstrap4Spacing.objects.all()

@query.field("CatalogueAttributeoption")
def resolve_CatalogueAttributeoption(self, info, **kwargs):
   return  CatalogueAttributeoption.objects.all()

@query.field("CatalogueAttributeoptiongroup")
def resolve_CatalogueAttributeoptiongroup(self, info, **kwargs):
   return  CatalogueAttributeoptiongroup.objects.all()

@query.field("CatalogueCategory")
def resolve_CatalogueCategory(self, info, **kwargs):
   return  CatalogueCategory.objects.all()

@query.field("CatalogueOption")
def resolve_CatalogueOption(self, info, **kwargs):
   return  CatalogueOption.objects.all()

@query.field("CatalogueProduct")
def resolve_CatalogueProduct(self, info, **kwargs):
   return  CatalogueProduct.objects.all()

@query.field("CatalogueProductattribute")
def resolve_CatalogueProductattribute(self, info, **kwargs):
   return  CatalogueProductattribute.objects.all()

@query.field("CatalogueProductattributevalue")
def resolve_CatalogueProductattributevalue(self, info, **kwargs):
   return  CatalogueProductattributevalue.objects.all()

@query.field("CatalogueProductattributevalueValueMultiOption")
def resolve_CatalogueProductattributevalueValueMultiOption(self, info, **kwargs):
   return  CatalogueProductattributevalueValueMultiOption.objects.all()

@query.field("CatalogueProductcategory")
def resolve_CatalogueProductcategory(self, info, **kwargs):
   return  CatalogueProductcategory.objects.all()

@query.field("CatalogueProductclass")
def resolve_CatalogueProductclass(self, info, **kwargs):
   return  CatalogueProductclass.objects.all()

@query.field("CatalogueProductclassOptions")
def resolve_CatalogueProductclassOptions(self, info, **kwargs):
   return  CatalogueProductclassOptions.objects.all()

@query.field("CatalogueProductimage")
def resolve_CatalogueProductimage(self, info, **kwargs):
   return  CatalogueProductimage.objects.all()

@query.field("CatalogueProductProductOptions")
def resolve_CatalogueProductProductOptions(self, info, **kwargs):
   return  CatalogueProductProductOptions.objects.all()

@query.field("CatalogueProductrecommendation")
def resolve_CatalogueProductrecommendation(self, info, **kwargs):
   return  CatalogueProductrecommendation.objects.all()

@query.field("CmsAliaspluginmodel")
def resolve_CmsAliaspluginmodel(self, info, **kwargs):
   return  CmsAliaspluginmodel.objects.all()

@query.field("CmsCmsplugin")
def resolve_CmsCmsplugin(self, info, **kwargs):
   return  CmsCmsplugin.objects.all()

@query.field("CmsGlobalpagepermission")
def resolve_CmsGlobalpagepermission(self, info, **kwargs):
   return  CmsGlobalpagepermission.objects.all()

@query.field("CmsGlobalpagepermissionSites")
def resolve_CmsGlobalpagepermissionSites(self, info, **kwargs):
   return  CmsGlobalpagepermissionSites.objects.all()

@query.field("CmsPage")
def resolve_CmsPage(self, info, **kwargs):
   return  CmsPage.objects.all()

@query.field("CmsPagepermission")
def resolve_CmsPagepermission(self, info, **kwargs):
   return  CmsPagepermission.objects.all()

@query.field("CmsPagePlaceholders")
def resolve_CmsPagePlaceholders(self, info, **kwargs):
   return  CmsPagePlaceholders.objects.all()

@query.field("CmsPageuser")
def resolve_CmsPageuser(self, info, **kwargs):
   return  CmsPageuser.objects.all()

@query.field("CmsPageusergroup")
def resolve_CmsPageusergroup(self, info, **kwargs):
   return  CmsPageusergroup.objects.all()

@query.field("CmsPlaceholder")
def resolve_CmsPlaceholder(self, info, **kwargs):
   return  CmsPlaceholder.objects.all()

@query.field("CmsPlaceholderreference")
def resolve_CmsPlaceholderreference(self, info, **kwargs):
   return  CmsPlaceholderreference.objects.all()

@query.field("CmsStaticplaceholder")
def resolve_CmsStaticplaceholder(self, info, **kwargs):
   return  CmsStaticplaceholder.objects.all()

@query.field("CmsTitle")
def resolve_CmsTitle(self, info, **kwargs):
   return  CmsTitle.objects.all()

@query.field("CmsTreenode")
def resolve_CmsTreenode(self, info, **kwargs):
   return  CmsTreenode.objects.all()

@query.field("CmsUrlconfrevision")
def resolve_CmsUrlconfrevision(self, info, **kwargs):
   return  CmsUrlconfrevision.objects.all()

@query.field("CmsUsersettings")
def resolve_CmsUsersettings(self, info, **kwargs):
   return  CmsUsersettings.objects.all()

@query.field("CommunicationCommunicationeventtype")
def resolve_CommunicationCommunicationeventtype(self, info, **kwargs):
   return  CommunicationCommunicationeventtype.objects.all()

@query.field("CommunicationEmail")
def resolve_CommunicationEmail(self, info, **kwargs):
   return  CommunicationEmail.objects.all()

@query.field("CommunicationNotification")
def resolve_CommunicationNotification(self, info, **kwargs):
   return  CommunicationNotification.objects.all()

@query.field("CustomerProductalert")
def resolve_CustomerProductalert(self, info, **kwargs):
   return  CustomerProductalert.objects.all()

@query.field("DjangoAdminLog")
def resolve_DjangoAdminLog(self, info, **kwargs):
   return  DjangoAdminLog.objects.all()

@query.field("DjangocmsBlogAuthorentriesplugin")
def resolve_DjangocmsBlogAuthorentriesplugin(self, info, **kwargs):
   return  DjangocmsBlogAuthorentriesplugin.objects.all()

@query.field("DjangocmsBlogAuthorentriespluginAuthors")
def resolve_DjangocmsBlogAuthorentriespluginAuthors(self, info, **kwargs):
   return  DjangocmsBlogAuthorentriespluginAuthors.objects.all()

@query.field("DjangocmsBlogBlogcategory")
def resolve_DjangocmsBlogBlogcategory(self, info, **kwargs):
   return  DjangocmsBlogBlogcategory.objects.all()

@query.field("DjangocmsBlogBlogcategoryTranslation")
def resolve_DjangocmsBlogBlogcategoryTranslation(self, info, **kwargs):
   return  DjangocmsBlogBlogcategoryTranslation.objects.all()

@query.field("DjangocmsBlogBlogconfig")
def resolve_DjangocmsBlogBlogconfig(self, info, **kwargs):
   return  DjangocmsBlogBlogconfig.objects.all()

@query.field("DjangocmsBlogBlogconfigTranslation")
def resolve_DjangocmsBlogBlogconfigTranslation(self, info, **kwargs):
   return  DjangocmsBlogBlogconfigTranslation.objects.all()

@query.field("DjangocmsBlogGenericblogplugin")
def resolve_DjangocmsBlogGenericblogplugin(self, info, **kwargs):
   return  DjangocmsBlogGenericblogplugin.objects.all()

@query.field("DjangocmsBlogLatestpostsplugin")
def resolve_DjangocmsBlogLatestpostsplugin(self, info, **kwargs):
   return  DjangocmsBlogLatestpostsplugin.objects.all()

@query.field("DjangocmsBlogLatestpostspluginCategories")
def resolve_DjangocmsBlogLatestpostspluginCategories(self, info, **kwargs):
   return  DjangocmsBlogLatestpostspluginCategories.objects.all()

@query.field("DjangocmsBlogPost")
def resolve_DjangocmsBlogPost(self, info, **kwargs):
   return  DjangocmsBlogPost.objects.all()

@query.field("DjangocmsBlogPostCategories")
def resolve_DjangocmsBlogPostCategories(self, info, **kwargs):
   return  DjangocmsBlogPostCategories.objects.all()

@query.field("DjangocmsBlogPostRelated")
def resolve_DjangocmsBlogPostRelated(self, info, **kwargs):
   return  DjangocmsBlogPostRelated.objects.all()

@query.field("DjangocmsBlogPostSites")
def resolve_DjangocmsBlogPostSites(self, info, **kwargs):
   return  DjangocmsBlogPostSites.objects.all()

@query.field("DjangocmsBlogPostTranslation")
def resolve_DjangocmsBlogPostTranslation(self, info, **kwargs):
   return  DjangocmsBlogPostTranslation.objects.all()

@query.field("DjangocmsFileFile")
def resolve_DjangocmsFileFile(self, info, **kwargs):
   return  DjangocmsFileFile.objects.all()

@query.field("DjangocmsFileFolder")
def resolve_DjangocmsFileFolder(self, info, **kwargs):
   return  DjangocmsFileFolder.objects.all()

@query.field("DjangocmsGooglemapGooglemap")
def resolve_DjangocmsGooglemapGooglemap(self, info, **kwargs):
   return  DjangocmsGooglemapGooglemap.objects.all()

@query.field("DjangocmsGooglemapGooglemapmarker")
def resolve_DjangocmsGooglemapGooglemapmarker(self, info, **kwargs):
   return  DjangocmsGooglemapGooglemapmarker.objects.all()

@query.field("DjangocmsGooglemapGooglemaproute")
def resolve_DjangocmsGooglemapGooglemaproute(self, info, **kwargs):
   return  DjangocmsGooglemapGooglemaproute.objects.all()

@query.field("DjangocmsHistoryPlaceholderaction")
def resolve_DjangocmsHistoryPlaceholderaction(self, info, **kwargs):
   return  DjangocmsHistoryPlaceholderaction.objects.all()

@query.field("DjangocmsHistoryPlaceholderoperation")
def resolve_DjangocmsHistoryPlaceholderoperation(self, info, **kwargs):
   return  DjangocmsHistoryPlaceholderoperation.objects.all()

@query.field("DjangocmsIconIcon")
def resolve_DjangocmsIconIcon(self, info, **kwargs):
   return  DjangocmsIconIcon.objects.all()

@query.field("DjangocmsLinkLink")
def resolve_DjangocmsLinkLink(self, info, **kwargs):
   return  DjangocmsLinkLink.objects.all()

@query.field("DjangocmsMapsMaps")
def resolve_DjangocmsMapsMaps(self, info, **kwargs):
   return  DjangocmsMapsMaps.objects.all()

@query.field("DjangocmsPicturePicture")
def resolve_DjangocmsPicturePicture(self, info, **kwargs):
   return  DjangocmsPicturePicture.objects.all()

@query.field("DjangocmsStyleStyle")
def resolve_DjangocmsStyleStyle(self, info, **kwargs):
   return  DjangocmsStyleStyle.objects.all()

@query.field("DjangocmsTextCkeditorText")
def resolve_DjangocmsTextCkeditorText(self, info, **kwargs):
   return  DjangocmsTextCkeditorText.objects.all()

@query.field("DjangocmsVideoVideoplayer")
def resolve_DjangocmsVideoVideoplayer(self, info, **kwargs):
   return  DjangocmsVideoVideoplayer.objects.all()

@query.field("DjangocmsVideoVideosource")
def resolve_DjangocmsVideoVideosource(self, info, **kwargs):
   return  DjangocmsVideoVideosource.objects.all()

@query.field("DjangocmsVideoVideotrack")
def resolve_DjangocmsVideoVideotrack(self, info, **kwargs):
   return  DjangocmsVideoVideotrack.objects.all()

@query.field("DjangoFlatpage")
def resolve_DjangoFlatpage(self, info, **kwargs):
   return  DjangoFlatpage.objects.all()

@query.field("DjangoFlatpageSites")
def resolve_DjangoFlatpageSites(self, info, **kwargs):
   return  DjangoFlatpageSites.objects.all()

@query.field("DjangoSession")
def resolve_DjangoSession(self, info, **kwargs):
   return  DjangoSession.objects.all()

@query.field("DjangoSite")
def resolve_DjangoSite(self, info, **kwargs):
   return  DjangoSite.objects.all()

@query.field("EasyThumbnailsSource")
def resolve_EasyThumbnailsSource(self, info, **kwargs):
   return  EasyThumbnailsSource.objects.all()

@query.field("EasyThumbnailsThumbnail")
def resolve_EasyThumbnailsThumbnail(self, info, **kwargs):
   return  EasyThumbnailsThumbnail.objects.all()

@query.field("EasyThumbnailsThumbnaildimensions")
def resolve_EasyThumbnailsThumbnaildimensions(self, info, **kwargs):
   return  EasyThumbnailsThumbnaildimensions.objects.all()

@query.field("FilerClipboard")
def resolve_FilerClipboard(self, info, **kwargs):
   return  FilerClipboard.objects.all()

@query.field("FilerClipboarditem")
def resolve_FilerClipboarditem(self, info, **kwargs):
   return  FilerClipboarditem.objects.all()

@query.field("FilerFile")
def resolve_FilerFile(self, info, **kwargs):
   return  FilerFile.objects.all()

@query.field("FilerFolder")
def resolve_FilerFolder(self, info, **kwargs):
   return  FilerFolder.objects.all()

@query.field("FilerFolderpermission")
def resolve_FilerFolderpermission(self, info, **kwargs):
   return  FilerFolderpermission.objects.all()

@query.field("FilerImage")
def resolve_FilerImage(self, info, **kwargs):
   return  FilerImage.objects.all()

@query.field("FilerThumbnailoption")
def resolve_FilerThumbnailoption(self, info, **kwargs):
   return  FilerThumbnailoption.objects.all()

@query.field("MenusCachekey")
def resolve_MenusCachekey(self, info, **kwargs):
   return  MenusCachekey.objects.all()

@query.field("OfferBenefit")
def resolve_OfferBenefit(self, info, **kwargs):
   return  OfferBenefit.objects.all()

@query.field("OfferCondition")
def resolve_OfferCondition(self, info, **kwargs):
   return  OfferCondition.objects.all()

@query.field("OfferConditionaloffer")
def resolve_OfferConditionaloffer(self, info, **kwargs):
   return  OfferConditionaloffer.objects.all()

@query.field("OfferConditionalofferCombinations")
def resolve_OfferConditionalofferCombinations(self, info, **kwargs):
   return  OfferConditionalofferCombinations.objects.all()

@query.field("OfferRange")
def resolve_OfferRange(self, info, **kwargs):
   return  OfferRange.objects.all()

@query.field("OfferRangeClasses")
def resolve_OfferRangeClasses(self, info, **kwargs):
   return  OfferRangeClasses.objects.all()

@query.field("OfferRangeExcludedProducts")
def resolve_OfferRangeExcludedProducts(self, info, **kwargs):
   return  OfferRangeExcludedProducts.objects.all()

@query.field("OfferRangeIncludedCategories")
def resolve_OfferRangeIncludedCategories(self, info, **kwargs):
   return  OfferRangeIncludedCategories.objects.all()

@query.field("OfferRangeproduct")
def resolve_OfferRangeproduct(self, info, **kwargs):
   return  OfferRangeproduct.objects.all()

@query.field("OfferRangeproductfileupload")
def resolve_OfferRangeproductfileupload(self, info, **kwargs):
   return  OfferRangeproductfileupload.objects.all()

@query.field("OrderBillingaddress")
def resolve_OrderBillingaddress(self, info, **kwargs):
   return  OrderBillingaddress.objects.all()

@query.field("OrderCommunicationevent")
def resolve_OrderCommunicationevent(self, info, **kwargs):
   return  OrderCommunicationevent.objects.all()

@query.field("OrderLine")
def resolve_OrderLine(self, info, **kwargs):
   return  OrderLine.objects.all()

@query.field("OrderLineattribute")
def resolve_OrderLineattribute(self, info, **kwargs):
   return  OrderLineattribute.objects.all()

@query.field("OrderLineprice")
def resolve_OrderLineprice(self, info, **kwargs):
   return  OrderLineprice.objects.all()

@query.field("OrderOrder")
def resolve_OrderOrder(self, info, **kwargs):
   return  OrderOrder.objects.all()

@query.field("OrderOrderdiscount")
def resolve_OrderOrderdiscount(self, info, **kwargs):
   return  OrderOrderdiscount.objects.all()

@query.field("OrderOrdernote")
def resolve_OrderOrdernote(self, info, **kwargs):
   return  OrderOrdernote.objects.all()

@query.field("OrderOrderstatuschange")
def resolve_OrderOrderstatuschange(self, info, **kwargs):
   return  OrderOrderstatuschange.objects.all()

@query.field("OrderPaymentevent")
def resolve_OrderPaymentevent(self, info, **kwargs):
   return  OrderPaymentevent.objects.all()

@query.field("OrderPaymenteventquantity")
def resolve_OrderPaymenteventquantity(self, info, **kwargs):
   return  OrderPaymenteventquantity.objects.all()

@query.field("OrderPaymenteventtype")
def resolve_OrderPaymenteventtype(self, info, **kwargs):
   return  OrderPaymenteventtype.objects.all()

@query.field("OrderShippingaddress")
def resolve_OrderShippingaddress(self, info, **kwargs):
   return  OrderShippingaddress.objects.all()

@query.field("OrderShippingevent")
def resolve_OrderShippingevent(self, info, **kwargs):
   return  OrderShippingevent.objects.all()

@query.field("OrderShippingeventquantity")
def resolve_OrderShippingeventquantity(self, info, **kwargs):
   return  OrderShippingeventquantity.objects.all()

@query.field("OrderShippingeventtype")
def resolve_OrderShippingeventtype(self, info, **kwargs):
   return  OrderShippingeventtype.objects.all()

@query.field("OrderSurcharge")
def resolve_OrderSurcharge(self, info, **kwargs):
   return  OrderSurcharge.objects.all()

@query.field("OscarapiApikey")
def resolve_OscarapiApikey(self, info, **kwargs):
   return  OscarapiApikey.objects.all()

@query.field("OscarInvoicesInvoice")
def resolve_OscarInvoicesInvoice(self, info, **kwargs):
   return  OscarInvoicesInvoice.objects.all()

@query.field("OscarInvoicesLegalentity")
def resolve_OscarInvoicesLegalentity(self, info, **kwargs):
   return  OscarInvoicesLegalentity.objects.all()

@query.field("OscarInvoicesLegalentityaddress")
def resolve_OscarInvoicesLegalentityaddress(self, info, **kwargs):
   return  OscarInvoicesLegalentityaddress.objects.all()

@query.field("PartnerPartner")
def resolve_PartnerPartner(self, info, **kwargs):
   return  PartnerPartner.objects.all()

@query.field("PartnerPartneraddress")
def resolve_PartnerPartneraddress(self, info, **kwargs):
   return  PartnerPartneraddress.objects.all()

@query.field("PartnerPartnerUsers")
def resolve_PartnerPartnerUsers(self, info, **kwargs):
   return  PartnerPartnerUsers.objects.all()

@query.field("PartnerStockalert")
def resolve_PartnerStockalert(self, info, **kwargs):
   return  PartnerStockalert.objects.all()

@query.field("PartnerStockrecord")
def resolve_PartnerStockrecord(self, info, **kwargs):
   return  PartnerStockrecord.objects.all()

@query.field("PaymentBankcard")
def resolve_PaymentBankcard(self, info, **kwargs):
   return  PaymentBankcard.objects.all()

@query.field("PaymentSource")
def resolve_PaymentSource(self, info, **kwargs):
   return  PaymentSource.objects.all()

@query.field("PaymentSourcetype")
def resolve_PaymentSourcetype(self, info, **kwargs):
   return  PaymentSourcetype.objects.all()

@query.field("PaymentTransaction")
def resolve_PaymentTransaction(self, info, **kwargs):
   return  PaymentTransaction.objects.all()

@query.field("PaypalExpresstransaction")
def resolve_PaypalExpresstransaction(self, info, **kwargs):
   return  PaypalExpresstransaction.objects.all()

@query.field("PaypalPayflowtransaction")
def resolve_PaypalPayflowtransaction(self, info, **kwargs):
   return  PaypalPayflowtransaction.objects.all()

@query.field("PhotologueGallery")
def resolve_PhotologueGallery(self, info, **kwargs):
   return  PhotologueGallery.objects.all()

@query.field("PhotologueGalleryPhotos")
def resolve_PhotologueGalleryPhotos(self, info, **kwargs):
   return  PhotologueGalleryPhotos.objects.all()

@query.field("PhotologueGallerySites")
def resolve_PhotologueGallerySites(self, info, **kwargs):
   return  PhotologueGallerySites.objects.all()

@query.field("PhotologuePhoto")
def resolve_PhotologuePhoto(self, info, **kwargs):
   return  PhotologuePhoto.objects.all()

@query.field("PhotologuePhotoeffect")
def resolve_PhotologuePhotoeffect(self, info, **kwargs):
   return  PhotologuePhotoeffect.objects.all()

@query.field("PhotologuePhotoSites")
def resolve_PhotologuePhotoSites(self, info, **kwargs):
   return  PhotologuePhotoSites.objects.all()

@query.field("PhotologuePhotosize")
def resolve_PhotologuePhotosize(self, info, **kwargs):
   return  PhotologuePhotosize.objects.all()

@query.field("PhotologueWatermark")
def resolve_PhotologueWatermark(self, info, **kwargs):
   return  PhotologueWatermark.objects.all()

@query.field("PinaxBadgesBadgeaward")
def resolve_PinaxBadgesBadgeaward(self, info, **kwargs):
   return  PinaxBadgesBadgeaward.objects.all()

@query.field("PinaxEventsEvent")
def resolve_PinaxEventsEvent(self, info, **kwargs):
   return  PinaxEventsEvent.objects.all()

@query.field("PinaxMessagesMessage")
def resolve_PinaxMessagesMessage(self, info, **kwargs):
   return  PinaxMessagesMessage.objects.all()

@query.field("PinaxMessagesThread")
def resolve_PinaxMessagesThread(self, info, **kwargs):
   return  PinaxMessagesThread.objects.all()

@query.field("PinaxMessagesUserthread")
def resolve_PinaxMessagesUserthread(self, info, **kwargs):
   return  PinaxMessagesUserthread.objects.all()

@query.field("ReviewsProductreview")
def resolve_ReviewsProductreview(self, info, **kwargs):
   return  ReviewsProductreview.objects.all()

@query.field("ReviewsVote")
def resolve_ReviewsVote(self, info, **kwargs):
   return  ReviewsVote.objects.all()

@query.field("ShippingOrderanditemcharges")
def resolve_ShippingOrderanditemcharges(self, info, **kwargs):
   return  ShippingOrderanditemcharges.objects.all()

@query.field("ShippingOrderanditemchargesCountries")
def resolve_ShippingOrderanditemchargesCountries(self, info, **kwargs):
   return  ShippingOrderanditemchargesCountries.objects.all()

@query.field("ShippingWeightband")
def resolve_ShippingWeightband(self, info, **kwargs):
   return  ShippingWeightband.objects.all()

@query.field("ShippingWeightbased")
def resolve_ShippingWeightbased(self, info, **kwargs):
   return  ShippingWeightbased.objects.all()

@query.field("ShippingWeightbasedCountries")
def resolve_ShippingWeightbasedCountries(self, info, **kwargs):
   return  ShippingWeightbasedCountries.objects.all()

@query.field("TaggitTag")
def resolve_TaggitTag(self, info, **kwargs):
   return  TaggitTag.objects.all()

@query.field("TaggitTaggeditem")
def resolve_TaggitTaggeditem(self, info, **kwargs):
   return  TaggitTaggeditem.objects.all()

@query.field("TestimonialsTestimonial")
def resolve_TestimonialsTestimonial(self, info, **kwargs):
   return  TestimonialsTestimonial.objects.all()

@query.field("ThumbnailKvstore")
def resolve_ThumbnailKvstore(self, info, **kwargs):
   return  ThumbnailKvstore.objects.all()

@query.field("VoucherVoucher")
def resolve_VoucherVoucher(self, info, **kwargs):
   return  VoucherVoucher.objects.all()

@query.field("VoucherVoucherapplication")
def resolve_VoucherVoucherapplication(self, info, **kwargs):
   return  VoucherVoucherapplication.objects.all()

@query.field("VoucherVoucherOffers")
def resolve_VoucherVoucherOffers(self, info, **kwargs):
   return  VoucherVoucherOffers.objects.all()

@query.field("VoucherVoucherset")
def resolve_VoucherVoucherset(self, info, **kwargs):
   return  VoucherVoucherset.objects.all()

@query.field("WishlistsLine")
def resolve_WishlistsLine(self, info, **kwargs):
   return  WishlistsLine.objects.all()

@query.field("WishlistsWishlist")
def resolve_WishlistsWishlist(self, info, **kwargs):
   return  WishlistsWishlist.objects.all()

schema = make_executable_schema(type_defs, query)
from django.shortcuts import get_object_or_404, redirect
from rest_framework.viewsets import ModelViewSet
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from shop.serializers import *
from shop.models import *

class AddressCountryViewSet(ModelViewSet):
    queryset = AddressCountry.objects.all()
    serializer_class = AddressCountrySerializer
    
class AddressUseraddressViewSet(ModelViewSet):
    queryset = AddressUseraddress.objects.all()
    serializer_class = AddressUseraddressSerializer
    
class AdvancedFiltersAdvancedfilterViewSet(ModelViewSet):
    queryset = AdvancedFiltersAdvancedfilter.objects.all()
    serializer_class = AdvancedFiltersAdvancedfilterSerializer
    
class AdvancedFiltersAdvancedfilterGroupsViewSet(ModelViewSet):
    queryset = AdvancedFiltersAdvancedfilterGroups.objects.all()
    serializer_class = AdvancedFiltersAdvancedfilterGroupsSerializer
    
class AdvancedFiltersAdvancedfilterUsersViewSet(ModelViewSet):
    queryset = AdvancedFiltersAdvancedfilterUsers.objects.all()
    serializer_class = AdvancedFiltersAdvancedfilterUsersSerializer
        
class AldrynFormsEmailfieldpluginViewSet(ModelViewSet):
    queryset = AldrynFormsEmailfieldplugin.objects.all()
    serializer_class = AldrynFormsEmailfieldpluginSerializer
    
class AldrynFormsFieldpluginViewSet(ModelViewSet):
    queryset = AldrynFormsFieldplugin.objects.all()
    serializer_class = AldrynFormsFieldpluginSerializer
    
class AldrynFormsFieldsetpluginViewSet(ModelViewSet):
    queryset = AldrynFormsFieldsetplugin.objects.all()
    serializer_class = AldrynFormsFieldsetpluginSerializer
    
class AldrynFormsFileuploadfieldpluginViewSet(ModelViewSet):
    queryset = AldrynFormsFileuploadfieldplugin.objects.all()
    serializer_class = AldrynFormsFileuploadfieldpluginSerializer
    
class AldrynFormsFormbuttonpluginViewSet(ModelViewSet):
    queryset = AldrynFormsFormbuttonplugin.objects.all()
    serializer_class = AldrynFormsFormbuttonpluginSerializer
    
class AldrynFormsFormpluginViewSet(ModelViewSet):
    queryset = AldrynFormsFormplugin.objects.all()
    serializer_class = AldrynFormsFormpluginSerializer
    
class AldrynFormsFormpluginRecipientsViewSet(ModelViewSet):
    queryset = AldrynFormsFormpluginRecipients.objects.all()
    serializer_class = AldrynFormsFormpluginRecipientsSerializer
    
class AldrynFormsFormsubmissionViewSet(ModelViewSet):
    queryset = AldrynFormsFormsubmission.objects.all()
    serializer_class = AldrynFormsFormsubmissionSerializer
    
class AldrynFormsImageuploadfieldpluginViewSet(ModelViewSet):
    queryset = AldrynFormsImageuploadfieldplugin.objects.all()
    serializer_class = AldrynFormsImageuploadfieldpluginSerializer
    
class AldrynFormsOptionViewSet(ModelViewSet):
    queryset = AldrynFormsOption.objects.all()
    serializer_class = AldrynFormsOptionSerializer
    
class AldrynFormsTextareafieldpluginViewSet(ModelViewSet):
    queryset = AldrynFormsTextareafieldplugin.objects.all()
    serializer_class = AldrynFormsTextareafieldpluginSerializer
    
class AnalyticsProductrecordViewSet(ModelViewSet):
    queryset = AnalyticsProductrecord.objects.all()
    serializer_class = AnalyticsProductrecordSerializer
    
class AnalyticsUserproductviewViewSet(ModelViewSet):
    queryset = AnalyticsUserproductview.objects.all()
    serializer_class = AnalyticsUserproductviewSerializer
    
class AnalyticsUserrecordViewSet(ModelViewSet):
    queryset = AnalyticsUserrecord.objects.all()
    serializer_class = AnalyticsUserrecordSerializer
    
class AnalyticsUsersearchViewSet(ModelViewSet):
    queryset = AnalyticsUsersearch.objects.all()
    serializer_class = AnalyticsUsersearchSerializer
    
class AnnouncementsAnnouncementViewSet(ModelViewSet):
    queryset = AnnouncementsAnnouncement.objects.all()
    serializer_class = AnnouncementsAnnouncementSerializer
    
class AnnouncementsDismissalViewSet(ModelViewSet):
    queryset = AnnouncementsDismissal.objects.all()
    serializer_class = AnnouncementsDismissalSerializer
    
class AuthGroupViewSet(ModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer
    
class AuthGroupPermissionsViewSet(ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer
    
class AuthPermissionViewSet(ModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer
    
class AuthUserViewSet(ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer
    
class AuthUserGroupsViewSet(ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer
    
class AuthUserUserPermissionsViewSet(ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer
    
class BasketBasketViewSet(ModelViewSet):
    queryset = BasketBasket.objects.all()
    serializer_class = BasketBasketSerializer
    
class BasketBasketVouchersViewSet(ModelViewSet):
    queryset = BasketBasketVouchers.objects.all()
    serializer_class = BasketBasketVouchersSerializer
    
class BasketLineViewSet(ModelViewSet):
    queryset = BasketLine.objects.all()
    serializer_class = BasketLineSerializer
    
class BasketLineattributeViewSet(ModelViewSet):
    queryset = BasketLineattribute.objects.all()
    serializer_class = BasketLineattributeSerializer
    
class Bootstrap4AlertsBootstrap4AlertsViewSet(ModelViewSet):
    queryset = Bootstrap4AlertsBootstrap4Alerts.objects.all()
    serializer_class = Bootstrap4AlertsBootstrap4AlertsSerializer
    
class Bootstrap4BadgeBootstrap4BadgeViewSet(ModelViewSet):
    queryset = Bootstrap4BadgeBootstrap4Badge.objects.all()
    serializer_class = Bootstrap4BadgeBootstrap4BadgeSerializer
    
class Bootstrap4CardBootstrap4CardViewSet(ModelViewSet):
    queryset = Bootstrap4CardBootstrap4Card.objects.all()
    serializer_class = Bootstrap4CardBootstrap4CardSerializer
    
class Bootstrap4CardBootstrap4CardinnerViewSet(ModelViewSet):
    queryset = Bootstrap4CardBootstrap4Cardinner.objects.all()
    serializer_class = Bootstrap4CardBootstrap4CardinnerSerializer
    
class Bootstrap4CarouselBootstrap4CarouselViewSet(ModelViewSet):
    queryset = Bootstrap4CarouselBootstrap4Carousel.objects.all()
    serializer_class = Bootstrap4CarouselBootstrap4CarouselSerializer
    
class Bootstrap4CarouselBootstrap4CarouselslideViewSet(ModelViewSet):
    queryset = Bootstrap4CarouselBootstrap4Carouselslide.objects.all()
    serializer_class = Bootstrap4CarouselBootstrap4CarouselslideSerializer
    
class Bootstrap4CollapseBootstrap4CollapseViewSet(ModelViewSet):
    queryset = Bootstrap4CollapseBootstrap4Collapse.objects.all()
    serializer_class = Bootstrap4CollapseBootstrap4CollapseSerializer
    
class Bootstrap4CollapseBootstrap4CollapsecontainerViewSet(ModelViewSet):
    queryset = Bootstrap4CollapseBootstrap4Collapsecontainer.objects.all()
    serializer_class = Bootstrap4CollapseBootstrap4CollapsecontainerSerializer
    
class Bootstrap4CollapseBootstrap4CollapsetriggerViewSet(ModelViewSet):
    queryset = Bootstrap4CollapseBootstrap4Collapsetrigger.objects.all()
    serializer_class = Bootstrap4CollapseBootstrap4CollapsetriggerSerializer
    
class Bootstrap4ContentBootstrap4BlockquoteViewSet(ModelViewSet):
    queryset = Bootstrap4ContentBootstrap4Blockquote.objects.all()
    serializer_class = Bootstrap4ContentBootstrap4BlockquoteSerializer
    
class Bootstrap4ContentBootstrap4CodeViewSet(ModelViewSet):
    queryset = Bootstrap4ContentBootstrap4Code.objects.all()
    serializer_class = Bootstrap4ContentBootstrap4CodeSerializer
    
class Bootstrap4ContentBootstrap4FigureViewSet(ModelViewSet):
    queryset = Bootstrap4ContentBootstrap4Figure.objects.all()
    serializer_class = Bootstrap4ContentBootstrap4FigureSerializer
    
class Bootstrap4GridBootstrap4GridcolumnViewSet(ModelViewSet):
    queryset = Bootstrap4GridBootstrap4Gridcolumn.objects.all()
    serializer_class = Bootstrap4GridBootstrap4GridcolumnSerializer
    
class Bootstrap4GridBootstrap4GridcontainerViewSet(ModelViewSet):
    queryset = Bootstrap4GridBootstrap4Gridcontainer.objects.all()
    serializer_class = Bootstrap4GridBootstrap4GridcontainerSerializer
    
class Bootstrap4GridBootstrap4GridrowViewSet(ModelViewSet):
    queryset = Bootstrap4GridBootstrap4Gridrow.objects.all()
    serializer_class = Bootstrap4GridBootstrap4GridrowSerializer
    
class Bootstrap4JumbotronBootstrap4JumbotronViewSet(ModelViewSet):
    queryset = Bootstrap4JumbotronBootstrap4Jumbotron.objects.all()
    serializer_class = Bootstrap4JumbotronBootstrap4JumbotronSerializer
    
class Bootstrap4LinkBootstrap4LinkViewSet(ModelViewSet):
    queryset = Bootstrap4LinkBootstrap4Link.objects.all()
    serializer_class = Bootstrap4LinkBootstrap4LinkSerializer
    
class Bootstrap4ListgroupBootstrap4ListgroupViewSet(ModelViewSet):
    queryset = Bootstrap4ListgroupBootstrap4Listgroup.objects.all()
    serializer_class = Bootstrap4ListgroupBootstrap4ListgroupSerializer
    
class Bootstrap4ListgroupBootstrap4ListgroupitemViewSet(ModelViewSet):
    queryset = Bootstrap4ListgroupBootstrap4Listgroupitem.objects.all()
    serializer_class = Bootstrap4ListgroupBootstrap4ListgroupitemSerializer
    
class Bootstrap4MediaBootstrap4MediaViewSet(ModelViewSet):
    queryset = Bootstrap4MediaBootstrap4Media.objects.all()
    serializer_class = Bootstrap4MediaBootstrap4MediaSerializer
    
class Bootstrap4MediaBootstrap4MediabodyViewSet(ModelViewSet):
    queryset = Bootstrap4MediaBootstrap4Mediabody.objects.all()
    serializer_class = Bootstrap4MediaBootstrap4MediabodySerializer
    
class Bootstrap4PictureBootstrap4PictureViewSet(ModelViewSet):
    queryset = Bootstrap4PictureBootstrap4Picture.objects.all()
    serializer_class = Bootstrap4PictureBootstrap4PictureSerializer
    
class Bootstrap4TabsBootstrap4TabViewSet(ModelViewSet):
    queryset = Bootstrap4TabsBootstrap4Tab.objects.all()
    serializer_class = Bootstrap4TabsBootstrap4TabSerializer
    
class Bootstrap4TabsBootstrap4TabitemViewSet(ModelViewSet):
    queryset = Bootstrap4TabsBootstrap4Tabitem.objects.all()
    serializer_class = Bootstrap4TabsBootstrap4TabitemSerializer
    
class Bootstrap4UtilitiesBootstrap4SpacingViewSet(ModelViewSet):
    queryset = Bootstrap4UtilitiesBootstrap4Spacing.objects.all()
    serializer_class = Bootstrap4UtilitiesBootstrap4SpacingSerializer
    
class CatalogueAttributeoptionViewSet(ModelViewSet):
    queryset = CatalogueAttributeoption.objects.all()
    serializer_class = CatalogueAttributeoptionSerializer
    
class CatalogueAttributeoptiongroupViewSet(ModelViewSet):
    queryset = CatalogueAttributeoptiongroup.objects.all()
    serializer_class = CatalogueAttributeoptiongroupSerializer
    
class CatalogueCategoryViewSet(ModelViewSet):
    queryset = CatalogueCategory.objects.all()
    serializer_class = CatalogueCategorySerializer
    
class CatalogueOptionViewSet(ModelViewSet):
    queryset = CatalogueOption.objects.all()
    serializer_class = CatalogueOptionSerializer
    
class CatalogueProductViewSet(ModelViewSet):
    queryset = CatalogueProduct.objects.all()
    serializer_class = CatalogueProductSerializer
    
class CatalogueProductattributeViewSet(ModelViewSet):
    queryset = CatalogueProductattribute.objects.all()
    serializer_class = CatalogueProductattributeSerializer
    
class CatalogueProductattributevalueViewSet(ModelViewSet):
    queryset = CatalogueProductattributevalue.objects.all()
    serializer_class = CatalogueProductattributevalueSerializer
    
class CatalogueProductattributevalueValueMultiOptionViewSet(ModelViewSet):
    queryset = CatalogueProductattributevalueValueMultiOption.objects.all()
    serializer_class = CatalogueProductattributevalueValueMultiOptionSerializer
    
class CatalogueProductcategoryViewSet(ModelViewSet):
    queryset = CatalogueProductcategory.objects.all()
    serializer_class = CatalogueProductcategorySerializer
    
class CatalogueProductclassViewSet(ModelViewSet):
    queryset = CatalogueProductclass .objects.all()
    serializer_class = CatalogueProductclassSerializer
    
class CatalogueProductclassOptionsViewSet(ModelViewSet):
    queryset = CatalogueProductclassOptions.objects.all()
    serializer_class = CatalogueProductclassOptionsSerializer
    
class CatalogueProductimageViewSet(ModelViewSet):
    queryset = CatalogueProductimage.objects.all()
    serializer_class = CatalogueProductimageSerializer
    
class CatalogueProductProductOptionsViewSet(ModelViewSet):
    queryset = CatalogueProductProductOptions.objects.all()
    serializer_class = CatalogueProductProductOptionsSerializer
    
class CatalogueProductrecommendationViewSet(ModelViewSet):
    queryset = CatalogueProductrecommendation.objects.all()
    serializer_class = CatalogueProductrecommendationSerializer
    
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class CmsAliaspluginmodelViewSet(ModelViewSet):
    queryset = CmsAliaspluginmodel.objects.all()
    serializer_class = CmsAliaspluginmodelSerializer
    
class CmsCmspluginViewSet(ModelViewSet):
    queryset = CmsCmsplugin.objects.all()
    serializer_class = CmsCmspluginSerializer
    
class CmsGlobalpagepermissionViewSet(ModelViewSet):
    queryset = CmsGlobalpagepermission.objects.all()
    serializer_class = CmsGlobalpagepermissionSerializer
    
class CmsGlobalpagepermissionSitesViewSet(ModelViewSet):
    queryset = CmsGlobalpagepermissionSites.objects.all()
    serializer_class = CmsGlobalpagepermissionSitesSerializer
    
class CmsPageViewSet(ModelViewSet):
    queryset = CmsPage.objects.all()
    serializer_class = CmsPageSerializer
    
class CmsPagepermissionViewSet(ModelViewSet):
    queryset = CmsPagepermission.objects.all()
    serializer_class = CmsPagepermissionSerializer
    
class CmsPagePlaceholdersViewSet(ModelViewSet):
    queryset = CmsPagePlaceholders.objects.all()
    serializer_class = CmsPagePlaceholdersSerializer
    
class CmsPageuserViewSet(ModelViewSet):
    queryset = CmsPageuser.objects.all()
    serializer_class = CmsPageuserSerializer
    
class CmsPageusergroupViewSet(ModelViewSet):
    queryset = CmsPageusergroup.objects.all()
    serializer_class = CmsPageusergroupSerializer
    
class CmsPlaceholderViewSet(ModelViewSet):
    queryset = CmsPlaceholder.objects.all()
    serializer_class = CmsPlaceholderSerializer
    
class CmsPlaceholderreferenceViewSet(ModelViewSet):
    queryset = CmsPlaceholderreference.objects.all()
    serializer_class = CmsPlaceholderreferenceSerializer
    
class CmsStaticplaceholderViewSet(ModelViewSet):
    queryset = CmsStaticplaceholder.objects.all()
    serializer_class = CmsStaticplaceholderSerializer
    
class CmsTitleViewSet(ModelViewSet):
    queryset = CmsTitle.objects.all()
    serializer_class = CmsTitleSerializer
    
class CmsTreenodeViewSet(ModelViewSet):
    queryset = CmsTreenode.objects.all()
    serializer_class = CmsTreenodeSerializer
    
class CmsUrlconfrevisionViewSet(ModelViewSet):
    queryset = CmsUrlconfrevision.objects.all()
    serializer_class = CmsUrlconfrevisionSerializer
    
class CmsUsersettingsViewSet(ModelViewSet):
    queryset = CmsUsersettings.objects.all()
    serializer_class = CmsUsersettingsSerializer
    
class CommunicationCommunicationeventtypeViewSet(ModelViewSet):
    queryset = CommunicationCommunicationeventtype.objects.all()
    serializer_class = CommunicationCommunicationeventtypeSerializer
    
class CommunicationEmailViewSet(ModelViewSet):
    queryset = CommunicationEmail.objects.all()
    serializer_class = CommunicationEmailSerializer
    
class CommunicationNotificationViewSet(ModelViewSet):
    queryset = CommunicationNotification.objects.all()
    serializer_class = CommunicationNotificationSerializer
    
class CustomerProductalertViewSet(ModelViewSet):
    queryset = CustomerProductalert.objects.all()
    serializer_class = CustomerProductalertSerializer
    
class DjangoAdminLogViewSet(ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer
    
class DjangocmsBlogAuthorentriespluginViewSet(ModelViewSet):
    queryset = DjangocmsBlogAuthorentriesplugin.objects.all()
    serializer_class = DjangocmsBlogAuthorentriespluginSerializer
    
class DjangocmsBlogAuthorentriespluginAuthorsViewSet(ModelViewSet):
    queryset = DjangocmsBlogAuthorentriespluginAuthors.objects.all()
    serializer_class = DjangocmsBlogAuthorentriespluginAuthorsSerializer
    
class DjangocmsBlogBlogcategoryViewSet(ModelViewSet):
    queryset = DjangocmsBlogBlogcategory.objects.all()
    serializer_class = DjangocmsBlogBlogcategorySerializer
    
class DjangocmsBlogBlogcategoryTranslationViewSet(ModelViewSet):
    queryset = DjangocmsBlogBlogcategoryTranslation.objects.all()
    serializer_class = DjangocmsBlogBlogcategoryTranslationSerializer
    
class DjangocmsBlogBlogconfigViewSet(ModelViewSet):
    queryset = DjangocmsBlogBlogconfig.objects.all()
    serializer_class = DjangocmsBlogBlogconfigSerializer
    
class DjangocmsBlogBlogconfigTranslationViewSet(ModelViewSet):
    queryset = DjangocmsBlogBlogconfigTranslation.objects.all()
    serializer_class = DjangocmsBlogBlogconfigTranslationSerializer
    
class DjangocmsBlogGenericblogpluginViewSet(ModelViewSet):
    queryset = DjangocmsBlogGenericblogplugin.objects.all()
    serializer_class = DjangocmsBlogGenericblogpluginSerializer
    
class DjangocmsBlogLatestpostspluginViewSet(ModelViewSet):
    queryset = DjangocmsBlogLatestpostsplugin.objects.all()
    serializer_class = DjangocmsBlogLatestpostspluginSerializer
    
class DjangocmsBlogLatestpostspluginCategoriesViewSet(ModelViewSet):
    queryset = DjangocmsBlogLatestpostspluginCategories.objects.all()
    serializer_class = DjangocmsBlogLatestpostspluginCategoriesSerializer
    
class DjangocmsBlogPostViewSet(ModelViewSet):
    queryset = DjangocmsBlogPost.objects.all()
    serializer_class = DjangocmsBlogPostSerializer
    
class DjangocmsBlogPostCategoriesViewSet(ModelViewSet):
    queryset = DjangocmsBlogPostCategories.objects.all()
    serializer_class = DjangocmsBlogPostCategoriesSerializer
    
class DjangocmsBlogPostRelatedViewSet(ModelViewSet):
    queryset = DjangocmsBlogPostRelated.objects.all()
    serializer_class = DjangocmsBlogPostRelatedSerializer
    
class DjangocmsBlogPostSitesViewSet(ModelViewSet):
    queryset = DjangocmsBlogPostSites.objects.all()
    serializer_class = DjangocmsBlogPostSitesSerializer
    
class DjangocmsBlogPostTranslationViewSet(ModelViewSet):
    queryset = DjangocmsBlogPostTranslation.objects.all()
    serializer_class = DjangocmsBlogPostTranslationSerializer
    
class DjangocmsFileFileViewSet(ModelViewSet):
    queryset = DjangocmsFileFile.objects.all()
    serializer_class = DjangocmsFileFileSerializer
    
class DjangocmsFileFolderViewSet(ModelViewSet):
    queryset = DjangocmsFileFolder.objects.all()
    serializer_class = DjangocmsFileFolderSerializer
    
class DjangocmsGooglemapGooglemapViewSet(ModelViewSet):
    queryset = DjangocmsGooglemapGooglemap.objects.all()
    serializer_class = DjangocmsGooglemapGooglemapSerializer
    
class DjangocmsGooglemapGooglemapmarkerViewSet(ModelViewSet):
    queryset = DjangocmsGooglemapGooglemapmarker.objects.all()
    serializer_class = DjangocmsGooglemapGooglemapmarkerSerializer
    
class DjangocmsGooglemapGooglemaprouteViewSet(ModelViewSet):
    queryset = DjangocmsGooglemapGooglemaproute.objects.all()
    serializer_class = DjangocmsGooglemapGooglemaprouteSerializer
    
class DjangocmsHistoryPlaceholderactionViewSet(ModelViewSet):
    queryset = DjangocmsHistoryPlaceholderaction.objects.all()
    serializer_class = DjangocmsHistoryPlaceholderactionSerializer
    
class DjangocmsHistoryPlaceholderoperationViewSet(ModelViewSet):
    queryset = DjangocmsHistoryPlaceholderoperation.objects.all()
    serializer_class = DjangocmsHistoryPlaceholderoperationSerializer
    
class DjangocmsIconIconViewSet(ModelViewSet):
    queryset = DjangocmsIconIcon.objects.all()
    serializer_class = DjangocmsIconIconSerializer
    
class DjangocmsLinkLinkViewSet(ModelViewSet):
    queryset = DjangocmsLinkLink.objects.all()
    serializer_class = DjangocmsLinkLinkSerializer
    
class DjangocmsMapsMapsViewSet(ModelViewSet):
    queryset = DjangocmsMapsMaps.objects.all()
    serializer_class = DjangocmsMapsMapsSerializer
    
class DjangocmsPicturePictureViewSet(ModelViewSet):
    queryset = DjangocmsPicturePicture.objects.all()
    serializer_class = DjangocmsPicturePictureSerializer
    
class DjangocmsStyleStyleViewSet(ModelViewSet):
    queryset = DjangocmsStyleStyle.objects.all()
    serializer_class = DjangocmsStyleStyleSerializer
    
class DjangocmsTextCkeditorTextViewSet(ModelViewSet):
    queryset = DjangocmsTextCkeditorText.objects.all()
    serializer_class = DjangocmsTextCkeditorTextSerializer
    
class DjangocmsVideoVideoplayerViewSet(ModelViewSet):
    queryset = DjangocmsVideoVideoplayer.objects.all()
    serializer_class = DjangocmsVideoVideoplayerSerializer
    
class DjangocmsVideoVideosourceViewSet(ModelViewSet):
    queryset = DjangocmsVideoVideosource.objects.all()
    serializer_class = DjangocmsVideoVideosourceSerializer
    
class DjangocmsVideoVideotrackViewSet(ModelViewSet):
    queryset = DjangocmsVideoVideotrack.objects.all()
    serializer_class = DjangocmsVideoVideotrackSerializer
    
class DjangoContentViewSet(ModelViewSet):
    queryset = DjangoContent.objects.all()
    serializer_class = DjangoContentSerializer
    
class DjangoFlatpageViewSet(ModelViewSet):
    queryset = DjangoFlatpage.objects.all()
    serializer_class = DjangoFlatpageSerializer
    
class DjangoFlatpageSitesViewSet(ModelViewSet):
    queryset = DjangoFlatpageSites.objects.all()
    serializer_class = DjangoFlatpageSitesSerializer
    
class DjangoMigrationsViewSet(ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer
    
class DjangoSessionViewSet(ModelViewSet):
    queryset = DjangoSession.objects.all()
    serializer_class = DjangoSessionSerializer
    
class DjangoSiteViewSet(ModelViewSet):
    queryset = DjangoSite.objects.all()
    serializer_class = DjangoSiteSerializer
    
class EasyThumbnailsSourceViewSet(ModelViewSet):
    queryset = EasyThumbnailsSource.objects.all()
    serializer_class = EasyThumbnailsSourceSerializer
    
class EasyThumbnailsThumbnailViewSet(ModelViewSet):
    queryset = EasyThumbnailsThumbnail.objects.all()
    serializer_class = EasyThumbnailsThumbnailSerializer
    
class EasyThumbnailsThumbnaildimensionsViewSet(ModelViewSet):
    queryset = EasyThumbnailsThumbnaildimensions.objects.all()
    serializer_class = EasyThumbnailsThumbnaildimensionsSerializer
    
class FilerClipboardViewSet(ModelViewSet):
    queryset = FilerClipboard.objects.all()
    serializer_class = FilerClipboardSerializer
    
class FilerClipboarditemViewSet(ModelViewSet):
    queryset = FilerClipboarditem.objects.all()
    serializer_class = FilerClipboarditemSerializer
    
class FilerFileViewSet(ModelViewSet):
    queryset = FilerFile.objects.all()
    serializer_class = FilerFileSerializer
    
class FilerFolderViewSet(ModelViewSet):
    queryset = FilerFolder.objects.all()
    serializer_class = FilerFolderSerializer
    
class FilerFolderpermissionViewSet(ModelViewSet):
    queryset = FilerFolderpermission.objects.all()
    serializer_class = FilerFolderpermissionSerializer
    
class FilerImageViewSet(ModelViewSet):
    queryset = FilerImage.objects.all()
    serializer_class = FilerImageSerializer
    
class FilerThumbnailoptionViewSet(ModelViewSet):
    queryset = FilerThumbnailoption.objects.all()
    serializer_class = FilerThumbnailoptionSerializer
    
class MenusCachekeyViewSet(ModelViewSet):
    queryset = MenusCachekey.objects.all()
    serializer_class = MenusCachekeySerializer
    
class OfferBenefitViewSet(ModelViewSet):
    queryset = OfferBenefit.objects.all()
    serializer_class = OfferBenefitSerializer
    
class OfferConditionViewSet(ModelViewSet):
    queryset = OfferCondition.objects.all()
    serializer_class = OfferConditionSerializer
    
class OfferConditionalofferViewSet(ModelViewSet):
    queryset = OfferConditionaloffer.objects.all()
    serializer_class = OfferConditionalofferSerializer
    
class OfferConditionalofferCombinationsViewSet(ModelViewSet):
    queryset = OfferConditionalofferCombinations.objects.all()
    serializer_class = OfferConditionalofferCombinationsSerializer
    
class OfferRangeViewSet(ModelViewSet):
    queryset = OfferRange.objects.all()
    serializer_class = OfferRangeSerializer
    
class OfferRangeClassesViewSet(ModelViewSet):
    queryset = OfferRangeClasses.objects.all()
    serializer_class = OfferRangeClassesSerializer
    
class OfferRangeExcludedProductsViewSet(ModelViewSet):
    queryset = OfferRangeExcludedProducts.objects.all()
    serializer_class = OfferRangeExcludedProductsSerializer
    
class OfferRangeIncludedCategoriesViewSet(ModelViewSet):
    queryset = OfferRangeIncludedCategories.objects.all()
    serializer_class = OfferRangeIncludedCategoriesSerializer
    
class OfferRangeproductViewSet(ModelViewSet):
    queryset = OfferRangeproduct.objects.all()
    serializer_class = OfferRangeproductSerializer
    
class OfferRangeproductfileuploadViewSet(ModelViewSet):
    queryset = OfferRangeproductfileupload.objects.all()
    serializer_class = OfferRangeproductfileuploadSerializer
    
class OrderBillingaddressViewSet(ModelViewSet):
    queryset = OrderBillingaddress.objects.all()
    serializer_class = OrderBillingaddressSerializer
    
class OrderCommunicationeventViewSet(ModelViewSet):
    queryset = OrderCommunicationevent.objects.all()
    serializer_class = OrderCommunicationeventSerializer
    
class OrderLineViewSet(ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    
class OrderLineattributeViewSet(ModelViewSet):
    queryset = OrderLineattribute.objects.all()
    serializer_class = OrderLineattributeSerializer
    
class OrderLinepriceViewSet(ModelViewSet):
    queryset = OrderLineprice.objects.all()
    serializer_class = OrderLinepriceSerializer
    
class OrderOrderViewSet(ModelViewSet):
    queryset = OrderOrder.objects.all()
    serializer_class = OrderOrderSerializer
    
class OrderOrderdiscountViewSet(ModelViewSet):
    queryset = OrderOrderdiscount.objects.all()
    serializer_class = OrderOrderdiscountSerializer
    
class OrderOrdernoteViewSet(ModelViewSet):
    queryset = OrderOrdernote.objects.all()
    serializer_class = OrderOrdernoteSerializer
    
class OrderOrderstatuschangeViewSet(ModelViewSet):
    queryset = OrderOrderstatuschange.objects.all()
    serializer_class = OrderOrderstatuschangeSerializer
    
class OrderPaymenteventViewSet(ModelViewSet):
    queryset = OrderPaymentevent.objects.all()
    serializer_class = OrderPaymenteventSerializer
    
class OrderPaymenteventquantityViewSet(ModelViewSet):
    queryset = OrderPaymenteventquantity.objects.all()
    serializer_class = OrderPaymenteventquantitySerializer
    
class OrderPaymenteventtypeViewSet(ModelViewSet):
    queryset = OrderPaymenteventtype.objects.all()
    serializer_class = OrderPaymenteventtypeSerializer
    
class OrderShippingaddressViewSet(ModelViewSet):
    queryset = OrderShippingaddress.objects.all()
    serializer_class = OrderShippingaddressSerializer
    
class OrderShippingeventViewSet(ModelViewSet):
    queryset = OrderShippingevent.objects.all()
    serializer_class = OrderShippingeventSerializer
    
class OrderShippingeventquantityViewSet(ModelViewSet):
    queryset = OrderShippingeventquantity.objects.all()
    serializer_class = OrderShippingeventquantitySerializer
    
class OrderShippingeventtypeViewSet(ModelViewSet):
    queryset = OrderShippingeventtype.objects.all()
    serializer_class = OrderShippingeventtypeSerializer
    
class OrderSurchargeViewSet(ModelViewSet):
    queryset = OrderSurcharge.objects.all()
    serializer_class = OrderSurchargeSerializer
    
class OscarapiApikeyViewSet(ModelViewSet):
    queryset = OscarapiApikey.objects.all()
    serializer_class = OscarapiApikeySerializer
    
class OscarInvoicesInvoiceViewSet(ModelViewSet):
    queryset = OscarInvoicesInvoice.objects.all()
    serializer_class = OscarInvoicesInvoiceSerializer
    
class OscarInvoicesLegalentityViewSet(ModelViewSet):
    queryset = OscarInvoicesLegalentity.objects.all()
    serializer_class = OscarInvoicesLegalentitySerializer
    
class OscarInvoicesLegalentityaddressViewSet(ModelViewSet):
    queryset = OscarInvoicesLegalentityaddress.objects.all()
    serializer_class = OscarInvoicesLegalentityaddressSerializer
    
class PartnerPartnerViewSet(ModelViewSet):
    queryset = PartnerPartner.objects.all()
    serializer_class = PartnerPartnerSerializer
    
class PartnerPartneraddressViewSet(ModelViewSet):
    queryset = PartnerPartneraddress.objects.all()
    serializer_class = PartnerPartneraddressSerializer
    
class PartnerPartnerUsersViewSet(ModelViewSet):
    queryset = PartnerPartnerUsers.objects.all()
    serializer_class = PartnerPartnerUsersSerializer
    
class PartnerStockalertViewSet(ModelViewSet):
    queryset = PartnerStockalert.objects.all()
    serializer_class = PartnerStockalertSerializer
    
class PartnerStockrecordViewSet(ModelViewSet):
    queryset = PartnerStockrecord.objects.all()
    serializer_class = PartnerStockrecordSerializer
    
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class PaymentBankcardViewSet(ModelViewSet):
    queryset = PaymentBankcard.objects.all()
    serializer_class = PaymentBankcardSerializer
    
class PaymentSourceViewSet(ModelViewSet):
    queryset = PaymentSource.objects.all()
    serializer_class = PaymentSourceSerializer
    
class PaymentSourcetypeViewSet(ModelViewSet):
    queryset = PaymentSourcetype.objects.all()
    serializer_class = PaymentSourcetypeSerializer
    
class PaymentTransactionViewSet(ModelViewSet):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    
class PaypalExpresstransactionViewSet(ModelViewSet):
    queryset = PaypalExpresstransaction.objects.all()
    serializer_class = PaypalExpresstransactionSerializer
    
class PaypalPayflowtransactionViewSet(ModelViewSet):
    queryset = PaypalPayflowtransaction.objects.all()
    serializer_class = PaypalPayflowtransactionSerializer
    
class PhotologueGalleryViewSet(ModelViewSet):
    queryset = PhotologueGallery.objects.all()
    serializer_class = PhotologueGallerySerializer
    
class PhotologueGalleryPhotosViewSet(ModelViewSet):
    queryset = PhotologueGalleryPhotos.objects.all()
    serializer_class = PhotologueGalleryPhotosSerializer
    
class PhotologueGallerySitesViewSet(ModelViewSet):
    queryset = PhotologueGallerySites.objects.all()
    serializer_class = PhotologueGallerySitesSerializer
    
class PhotologuePhotoViewSet(ModelViewSet):
    queryset = PhotologuePhoto.objects.all()
    serializer_class = PhotologuePhotoSerializer
    
class PhotologuePhotoeffectViewSet(ModelViewSet):
    queryset = PhotologuePhotoeffect.objects.all()
    serializer_class = PhotologuePhotoeffectSerializer
    
class PhotologuePhotoSitesViewSet(ModelViewSet):
    queryset = PhotologuePhotoSites.objects.all()
    serializer_class = PhotologuePhotoSitesSerializer
    
class PhotologuePhotosizeViewSet(ModelViewSet):
    queryset = PhotologuePhotosize.objects.all()
    serializer_class = PhotologuePhotosizeSerializer
    
class PhotologueWatermarkViewSet(ModelViewSet):
    queryset = PhotologueWatermark.objects.all()
    serializer_class = PhotologueWatermarkSerializer
    
class PinaxBadgesBadgeawardViewSet(ModelViewSet):
    queryset = PinaxBadgesBadgeaward.objects.all()
    serializer_class = PinaxBadgesBadgeawardSerializer
    
class PinaxEventsEventViewSet(ModelViewSet):
    queryset = PinaxEventsEvent.objects.all()
    serializer_class = PinaxEventsEventSerializer
    
class PinaxMessagesMessageViewSet(ModelViewSet):
    queryset = PinaxMessagesMessage.objects.all()
    serializer_class = PinaxMessagesMessageSerializer
    
class PinaxMessagesThreadViewSet(ModelViewSet):
    queryset = PinaxMessagesThread.objects.all()
    serializer_class = PinaxMessagesThreadSerializer
    
class PinaxMessagesUserthreadViewSet(ModelViewSet):
    queryset = PinaxMessagesUserthread.objects.all()
    serializer_class = PinaxMessagesUserthreadSerializer
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ReviewsProductreviewViewSet(ModelViewSet):
    queryset = ReviewsProductreview.objects.all()
    serializer_class = ReviewsProductreviewSerializer
    
class ReviewsVoteViewSet(ModelViewSet):
    queryset = ReviewsVote.objects.all()
    serializer_class = ReviewsVoteSerializer
    
class SalesLineTransactionViewSet(ModelViewSet):
    queryset = SalesLineTransaction.objects.all()
    serializer_class = SalesLineTransactionSerializer
    
class ShippingOrderanditemchargesViewSet(ModelViewSet):
    queryset = ShippingOrderanditemcharges.objects.all()
    serializer_class = ShippingOrderanditemchargesSerializer
    
class ShippingOrderanditemchargesCountriesViewSet(ModelViewSet):
    queryset = ShippingOrderanditemchargesCountries.objects.all()
    serializer_class = ShippingOrderanditemchargesCountriesSerializer
    
class ShippingWeightbandViewSet(ModelViewSet):
    queryset = ShippingWeightband.objects.all()
    serializer_class = ShippingWeightbandSerializer
    
class ShippingWeightbasedViewSet(ModelViewSet):
    queryset = ShippingWeightbased.objects.all()
    serializer_class = ShippingWeightbasedSerializer
    
class ShippingWeightbasedCountriesViewSet(ModelViewSet):
    queryset = ShippingWeightbasedCountries.objects.all()
    serializer_class = ShippingWeightbasedCountriesSerializer
    
class TaggitTagViewSet(ModelViewSet):
    queryset = TaggitTag.objects.all()
    serializer_class = TaggitTagSerializer
    
class TaggitTaggeditemViewSet(ModelViewSet):
    queryset = TaggitTaggeditem.objects.all()
    serializer_class = TaggitTaggeditemSerializer
    
    
class TestimonialsTestimonialViewSet(ModelViewSet):
    queryset = TestimonialsTestimonial.objects.all()
    serializer_class = TestimonialsTestimonialSerializer
    
class ThumbnailKvstoreViewSet(ModelViewSet):
    queryset = ThumbnailKvstore.objects.all()
    serializer_class = ThumbnailKvstoreSerializer
    
class VoucherVoucherViewSet(ModelViewSet):
    queryset = VoucherVoucher.objects.all()
    serializer_class = VoucherVoucherSerializer
    
class VoucherVoucherapplicationViewSet(ModelViewSet):
    queryset = VoucherVoucherapplication.objects.all()
    serializer_class = VoucherVoucherapplicationSerializer
    
class VoucherVoucherOffersViewSet(ModelViewSet):
    queryset = VoucherVoucherOffers.objects.all()
    serializer_class = VoucherVoucherOffersSerializer
    
class VoucherVouchersetViewSet(ModelViewSet):
    queryset = VoucherVoucherset.objects.all()
    serializer_class = VoucherVouchersetSerializer
    
class WishlistsLineViewSet(ModelViewSet):
    queryset = WishlistsLine.objects.all()
    serializer_class = WishlistsLineSerializer
    
class WishlistsWishlistViewSet(ModelViewSet):
    queryset = WishlistsWishlist.objects.all()
    serializer_class = WishlistsWishlistSerializer

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, 'payment.html',
                            {'form': form, 'payment': payment})

django.jQuery(document).on('formset:added', function(event, $row, formsetName) {
    // On Inline Row added
    // NB: this is using the jQuery not within the django.jQuery namespace, i.e. $row > $($row)
    // https://docs.djangoproject.com/en/2.2/ref/contrib/admin/javascript/

    // For some reason an additional input is added on first new row... so we remove
    $row.find('span.select2').remove();
    // Sets other django-select2 inputs
    $($row).find('.django-select2').select2();
});

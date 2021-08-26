from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from slick_reporting.views import SlickReportView
from slick_reporting.fields import SlickReportField
from .models import MySalesItems

class MonthlyProductSales(SlickReportView):
    # The model where you have the data
    report_model = MySalesItems

    # the main date field used for the model.
    date_field = 'date_placed' # or 'order__date_placed'
    # this support traversing, like so
    # date_field = 'order__date_placed'

    # A foreign key to group calculation on
    group_by = 'product'

    # The columns you want to display
    columns = ['title',
                SlickReportField.create(method=Sum, field='value', name='value__sum', verbose_name=_('Total sold $'))
                ]

    # Charts
    charts_settings = [
     {
        'type': 'bar',
        'data_source': 'value__sum',
        'title_source': 'title',
     },
    ]
    
def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, 'payment.html',
                            {'form': form, 'payment': payment})

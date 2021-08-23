/**
 * Created by Michael on 25-Feb-16.
 */

//Chart Color Types
CHART_TYPES = {
    LINE: 'line',
    BAR: 'bar',
    HORIZONTAL_BAR: 'horizontalBar',
    RADAR: 'radar',
    POLAR: 'polarArea',
    PIE: 'pie',
    DOUGHNUT: 'doughnut',
    BUBBLE: 'bubble',
    SCATTER: 'scatter',
};


function get_color_types(chart_type) {
    switch (chart_type) {
        case CHART_TYPES.LINE:
        case CHART_TYPES.SCATTER:
        case CHART_TYPES.RADAR:
            return ['backgroundColor', 'borderColor', 'hoverBackgroundColor', 'hoverBorderColor',
                'pointBackgroundColor', 'pointBorderColor', 'pointHoverBackgroundColor', 'pointHoverBorderColor']
        case CHART_TYPES.BAR:
        case CHART_TYPES.HORIZONTAL_BAR:
        case CHART_TYPES.PIE:
        case CHART_TYPES.DOUGHNUT:
        case CHART_TYPES.POLAR:
        case CHART_TYPES.BUBBLE:
            return ['backgroundColor', 'borderColor', 'hoverBackgroundColor', 'hoverBorderColor',];

    }
}

function get_color_by_dataset(chart_type, color_by_dataset) {
    if(typeof(color_by_dataset) === 'undefined') {
        switch (chart_type) {
            case CHART_TYPES.LINE:
            case CHART_TYPES.RADAR:
            case CHART_TYPES.SCATTER:
            case CHART_TYPES.BUBBLE:
                return true;
            case CHART_TYPES.BAR:
            case CHART_TYPES.HORIZONTAL_BAR:
            case CHART_TYPES.DOUGHNUT:
            case CHART_TYPES.PIE:
            case CHART_TYPES.POLAR:
                return false;
        }
    }
    return color_by_dataset;
}

function get_color_from_class(chartElement, theClass){
    //Add the Class, get the computed colors, then remove the class
    var theColor = "";
    var tempClass = chartElement.attr('class');
    chartElement
        .addClass(theClass)
        .removeClass(function (idx) {
            theColor = $(this).css('color');
            return theClass;
        });
    chartElement.attr('class', tempClass);
    return theColor;
}


//Parse the Data and return colors
function parse_css_colors(chart_id, chart_type, chart_data, color_by_dataset) {

    //Parse if string, otherwise assume a json data object
    var dataIsString = (typeof (chart_data) == 'string');
    chart_data = dataIsString ? JSON.parse(chart_data) : chart_data;

    //Get Chart Canvas Id, i.e. canvas.#chart_id
    chart_selector = String(chart_id).startsWith('#') ? chart_id : '#' + chart_id;
    chart_selector = 'canvas' + chart_selector;

    //Clear inline color on existing canvas object
    $(chart_selector).css('color', '');

    var theDatasets = chart_data.data.datasets;

    //For each dataset
    $.each(theDatasets, function (dataset_idx, dataset) {

        // Get Chart type for each dataset if set
        chart_type = ('type' in dataset) ? dataset.type : chart_type;

        //Get Color Types for this chart type
        var chart_color_types = get_color_types(chart_type);

        //Get datasets - may need to create a switch in future if more data structures are used in ChartJS
        var do_color_by_dataset = get_color_by_dataset(chart_type, color_by_dataset);

        // For each name: backgroundColor, pointColor...
        $.each(chart_color_types, function (idx, theColorType) {

            // Continue if color already set
            if (theColorType in dataset) return;

            if (do_color_by_dataset) {
                // Color by Dataset
                // ---------------------------------------
                // For each  dataset_idx and each name: backgroundColor, pointColor...
                var theClass = chart_type + ' ' + theColorType + '_' + (dataset_idx + 1);
                //Add/change the computed color to the data
                dataset[theColorType] = get_color_from_class($(chart_selector), theClass);

            } else {
                // Color by Series
                // ---------------------------------------
                // Create an Array of colors and append to each dataset by type
                var color_list = [];
                for (i = 0; i < dataset.data.length; i++) {
                    // For each  dataset_idx and each name: backgroundColor, pointColor...
                    var theClass = chart_type + ' ' + theColorType + '_' + (i + 1);
                    //Add/change the computed color to the data
                    color_list.push(get_color_from_class($(chart_selector), theClass));
                }
                dataset[theColorType] = color_list;
            }
        });
    });

    //If the data was orginally a string - then return as one
    return dataIsString ? JSON.stringify(chart_data) : chart_data;

}

//Fix for IE not having the startsWith Function.
if (!String.prototype.startsWith) {
    String.prototype.startsWith = function (searchString, position) {
        position = position || 0;
        return this.indexOf(searchString, position) === position;
    };
}

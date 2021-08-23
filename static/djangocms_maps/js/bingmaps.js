/*
 * Bing map for djangocms_maps, https://github.com/Organice/djangocms-maps
 *
 * Copyright (c) 2016 Peter Bittner <django@bittner.it>
 * Copyright (c) 2016 Divio (original author for Google Maps implementation)
 *
 * documentation: https://msdn.microsoft.com/en-us/library/mt712552.aspx
 */

var djangocms = window.djangocms || {};

/**
 * Bing map instances from plugins.
 *
 * @class Maps
 * @namespace djangocms
 */

djangocms.Maps = {

    options: {
        container: ".djangocms-maps-container"
    },

    /**
     * Initializes all Map instances.
     *
     * @method init
     * @private
     * @param {Object} opts overwrite default options
     */
    init: function init(opts) {
        var that = this;
        var options = $.extend(true, {}, this.options, opts);

        // loop through every instance
        var containers = $(options.container);
        containers.each(function (index, container) {
            that._loadMap($(container));
        });
    },

    /**
     * Loads a single Map instance provided by ``init``.
     *
     * @method _loadMap
     * @private
     * @param {jQuery} instance jQuery element used for initialization
     */
    _loadMap: function _loadMap(instance) {
        var that = this;
        var container = instance;
        var data = container.data();

        var options = {
            credentials: data.api_key,
            navigationBarMode: Microsoft.Maps.NavigationBarMode.compact,
            showLocateMeButton: false,
            zoom: data.zoom,
            disableScrollWheelZoom: !data.scrollwheel,
            disableZooming: !data.double_click_zoom && !data.scrollwheel,
            disablePanning: !data.draggable,
            showZoomButtons: data.zoom_control,
            showMapTypeSelector: data.layers_control,
            showScalebar: data.scale_bar,
            styles: data.style,
            center: new Microsoft.Maps.Location(46.94708, 7.445975) // default to switzerland;
        };

        var map = new Microsoft.Maps.Map(container[0], options);

        // latitute or longitute have precedence over the address when provided
        // inside the plugin form
        data.lat = data.lat.toString();
        data.lng = data.lng.toString();
        if (data.lat.length && data.lng.length) {
            var coords = {
                lat: parseFloat(data.lat.replace(",", ".")),
                lng: parseFloat(data.lng.replace(",", "."))
            };
            var location = new Microsoft.Maps.Location(coords.lat, coords.lng);
            this.addMarker(map, location, data);
        } else {
            // load latlng from given address
            Microsoft.Maps.loadModule("Microsoft.Maps.Search", function () {
                var searchManager = new Microsoft.Maps.Search.SearchManager(map);
                var requestOptions = {
                    bounds: map.getBounds(),
                    where: data.address,
                    callback: function (answer, userData) {
                        map.setView({ bounds: answer.results[0].bestView });
                        that.addMarker(map, answer.results[0].location, data);

                        // use user-set zoom level for displaying result
                        var options = map.getOptions();
                        options.zoom = data.zoom;
                        map.setView(options);
                    }
                };
                searchManager.geocode(requestOptions);
            });
        }
    },

    /**
     * Adds a marker to a Map instance.
     *
     * @method addMarker
     * @param {jQuery} map ``Microsoft.Maps.Map`` instance
     * @param {jQuery} location ``Microsoft.Maps.Location`` instance
     * @param {jQuery} data the data objects from a Map instance
     */
    addMarker: function addMarker(map, location, data) {
        var pushpin = new Microsoft.Maps.Pushpin(location, null);

        if (data.show_infowindow) {
            // prepare info window
            var windowContent = data.address;
            if (data.info_content) {
                windowContent += "<br /><em>" + data.info_content + "</em>";
            }

            var infobox = new Microsoft.Maps.Infobox(map.getCenter(), {
                title: data.title,
                description: windowContent
            });
            infobox.setMap(map);

            Microsoft.Maps.Events.addHandler(pushpin, "click", function () {
                infobox.setOptions({ visible: true });
            });
        }

        map.entities.push(pushpin);
    }

};

// callback function, initializes all occurring Maps plugins at once
function djangocms_Maps_init() {
    djangocms.Maps.init();
}

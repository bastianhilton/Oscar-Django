/*
 * ViaMichelin map for djangocms_maps, https://github.com/Organice/djangocms-maps
 *
 * Copyright (c) 2016 Peter Bittner <django@bittner.it>
 * Copyright (c) 2016 Divio (original author for Google Maps implementation)
 *
 * documentation: http://dev.viamichelin.com/map-service.html
 */

var djangocms = window.djangocms || {};

/**
 * ViaMichelin map instances from plugins.
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
            container: $_id(container.attr("id")),
            geolocationControl: false,
            menuPoiControl: false,
            mapMenuControl: true,
            mapToolsControl: true,
            mapTypeControl: data.layers_control,
            markerControl: data.show_infowindow,
            situationMapControl: false,
            weatherControl: false,
            navigationMode: data.draggable ? ViaMichelin.Api.Constants.Map.NAVIGATION.DRAG
                                           : ViaMichelin.Api.Constants.Map.NAVIGATION.STATIC,
            scrollwheel: data.scrollwheel,
            zoom: data.zoom
        };

        // latitute or longitute have precedence over the address when provided
        // inside the plugin form
        data.lat = data.lat.toString();
        data.lng = data.lng.toString();
        if (data.lat.length && data.lng.length) {
            options.center = {
                coords: {
                    lat: parseFloat(data.lat.replace(",", ".")),
                    lng: parseFloat(data.lng.replace(",", "."))
                }
            };
        } else {
            // load latlng from given address
            options.center = {address: {singleFieldSearch: data.address}};
            // alternatively {address: {address: data.address, city: data.city, zipcode: data.zipcode}}
        }

        var map = null;

        VMLaunch("ViaMichelin.Api.Map", options, {
            onInit: function(serviceMap) {
                that.map = serviceMap;
            },
            onInitError: function(component, error) {
                console.error(error);
            }
        });
    }

};

// initializes all occurring Maps plugins at once.
djangocms.Maps.init();

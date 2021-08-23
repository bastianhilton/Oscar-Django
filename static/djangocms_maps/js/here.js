/*
 * HERE map for djangocms_maps, https://github.com/Organice/djangocms-maps
 *
 * Copyright (c) 2016 Peter Bittner <django@bittner.it>
 * Copyright (c) 2016 Divio (original author for Google Maps implementation)
 *
 * documentation: https://developer.here.com/develop/javascript-api
 */

var djangocms = window.djangocms || {};

/**
 * HERE map instances from plugins.
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
            apiKey: data.api_key,
            zoom: data.zoom,
            scrollWheelZoom: data.scrollwheel ? H.mapevents.Behavior.WHEELZOOM : 0,
            doubleClickZoom: data.double_click_zoom ? H.mapevents.Behavior.DBLTAPZOOM : 0,
            dragging: data.draggable ? H.mapevents.Behavior.DRAGGING : 0,
            keyboardShortcuts: data.keyboard_shortcuts,
            panControl: data.pan_control,
            zoomControl: data.zoom_control,
            streetViewControl: data.street_view_control,
            layersControl: data.layers_control,
            scaleBar: data.scale_bar,
            uiLanguage: this.getSupportedLanguage(data.lang_code),
            useHTTPS: true,
            styles: data.style,
            center: { lat: 46.94708, lng: 7.445975 } // default to switzerland;
        };

        var platform = new H.service.Platform({
            app_id: options.apiKey.app_id,
            app_code: options.apiKey.app_code,
            useHTTPS: options.useHTTPS
        });
        var defaultLayers = platform.createDefaultLayers();
        var map = new H.Map(container[0], defaultLayers.normal.map, options);

        map.behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
        map.behavior.disable();
        map.behavior.enable(options.scrollWheelZoom | options.doubleClickZoom | options.dragging);

        map.ui = H.ui.UI.createDefault(map, defaultLayers, options.uiLanguage);
        map.ui.getControl("zoom").setDisabled(!options.zoomControl);
        map.ui.getControl("mapsettings").setDisabled(!options.layersControl);
        map.ui.getControl("scalebar").setDisabled(!options.scaleBar);
        // map.ui.getControl("panorama").setDisabled(!options.streetViewControl);

        // latitute or longitute have precedence over the address when provided
        // inside the plugin form
        data.lat = data.lat.toString();
        data.lng = data.lng.toString();
        if (data.lat.length && data.lng.length) {
            var latlng = {
                lat: parseFloat(data.lat.replace(",", ".")),
                lng: parseFloat(data.lng.replace(",", "."))
            };
            this.addMarker(map, latlng, data);
        } else {
            // load latlng from given address
            var geocoder = platform.getGeocodingService();
            geocoder.geocode({ searchText: data.address }, function(result) {
                var locations = result.Response.View[0].Result;
                if (locations.length) {
                    var latlng = {
                        lat: locations[0].Location.DisplayPosition.Latitude,
                        lng: locations[0].Location.DisplayPosition.Longitude
                    };
                    that.addMarker(map, latlng, data);
                }
            }, function(e) { console.log(e); });
        }
    },

    /**
     * Adds a marker to a Map instance.
     *
     * @method addMarker
     * @param {jQuery} map ``H.Map`` instance
     * @param {jQuery} latlng proper formatted lat/lng coordinates
     * @param {jQuery} data the data objects from a Map instance
     */
    addMarker: function addMarker(map, latlng, data) {
        var windowContent = "";
        var marker = new H.map.Marker(latlng);

        map.addObject(marker);
        map.setCenter(latlng);

        if (data.show_infowindow) {
            // prepare info window
            if (data.title) {
                windowContent += "<h2>" + data.title + "</h2>";
            }

            windowContent += data.address;

            if (data.info_content) {
                windowContent += "<br /><em>" + data.info_content + "</em>";
            }

            marker.bubble = new H.ui.InfoBubble(latlng, { content: windowContent });
            marker.addEventListener("tap", function(ev) {
                this.bubble.open();
            });
            map.ui.addBubble(marker.bubble);
        }
    },

    /**
     * Returns a supported UI language for a specified language code.
     * Supported UI langages are listed at
     * https://developer.here.com/javascript-apis/documentation/v3/maps/topics/map-controls.html
     *
     * @method getSupportedLanguage
     * @return String
     */
    getSupportedLanguage: function getSupportedLanguage(lang_code) {
        var supported_languages = [
            "en-US",
            "de-DE",
            "es-ES",
            "fi-FI",
            "fr-FR",
            "it-IT",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ru-RU",
            "tr-TR",
            "zh-CN"
        ];
        if (lang_code in supported_languages) {
            return lang_code;
        }
        for (var i = 0; i < supported_languages.length; i++) {
            if (supported_languages[i].slice(0, 2) == lang_code.slice(0, 2)) {
                return supported_languages[i];
            }
        }
        return supported_languages[0];  // default
    }
};

// initializes all occurring Maps plugins at once.
djangocms.Maps.init();

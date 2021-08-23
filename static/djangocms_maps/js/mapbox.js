/*
 * Mapbox OSM map for djangocms_maps, https://github.com/Organice/djangocms-maps
 *
 * Copyright (c) 2016 Peter Bittner <django@bittner.it>
 * Copyright (c) 2016 Divio (original author for Google Maps implementation)
 *
 * documentation: https://www.mapbox.com/mapbox.js/api/
 */

var djangocms = window.djangocms || {};

/**
 * Mapbox OSM map instances from plugins.
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
            scrollWheelZoom: data.scrollwheel,
            doubleClickZoom: data.double_click_zoom,
            dragging: data.draggable,
            keyboard: data.keyboard_shortcuts,
            panControl: data.pan_control,
            zoomControl: data.zoom_control,
            layersControl: data.layers_control,
            scaleBar: data.scale_bar,
            styles: data.style,
            center: { lat: 46.94708, lng: 7.445975 } // default to switzerland;
        };

        L.mapbox.accessToken = options.apiKey;

        var map = L.mapbox.map(container[0], "mapbox.streets", options);

        if (options.layersControl) {
            L.control.layers({
                "Streets": L.mapbox.tileLayer("mapbox.streets").addTo(map),
                "Satellite": L.mapbox.tileLayer("mapbox.satellite"),
                "Hybrid": L.mapbox.tileLayer("mapbox.streets-satellite")
            }).addTo(map);
        }
        if (options.scaleBar) {
            L.control.scale().addTo(map);
        }

        // latitute or longitute have precedence over the address when provided
        // inside the plugin form
        data.lat = data.lat.toString();
        data.lng = data.lng.toString();
        if (data.lat.length && data.lng.length) {
            var latlng = {
                lat: parseFloat(data.lat.replace(",", ".")),
                lng: parseFloat(data.lng.replace(",", "."))
            };
            map.setView(latlng, data.zoom);
            this.addMarker(map, latlng, data);
        } else {
            // load latlng from given address
            L.mapbox.geocoder("mapbox.places").query(data.address, function(err, geodata) {
                if (geodata.lbounds) {
                    map.fitBounds(geodata.lbounds);
                } else if (geodata.latlng) {
                    var latlng = [geodata.latlng[0], geodata.latlng[1]];
                    map.setView(latlng, 13);
                    that.addMarker(map, latlng, data);
                }
            });
        }
    },

    /**
     * Adds a marker to a Map instance.
     *
     * @method _loadMap
     * @param {jQuery} map ``L.Map`` instance
     * @param {jQuery} latlng proper formatted lat/lng coordinates
     * @param {jQuery} data the data objects from a Map instance
     */
    addMarker: function addMarker(map, latlng, data) {
        var windowContent = "";
        var marker = L.marker(latlng).addTo(map);

        if (data.show_infowindow) {
            // prepare info window
            if (data.title) {
                windowContent += "<h2>" + data.title + "</h2>";
            }

            windowContent += data.address;

            if (data.info_content) {
                windowContent += "<br /><em>" + data.info_content + "</em>";
            }

            marker.bindPopup(windowContent).openPopup();
        }

        // reposition map
        map.panTo(latlng);
    }

};

// initializes all occurring Maps plugins at once.
djangocms.Maps.init();

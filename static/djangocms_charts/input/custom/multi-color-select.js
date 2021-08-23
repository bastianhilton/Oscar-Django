/*
*   Multiple Color Select Widget
*
*/

function MultipleColorWidget(widget_elem) {
    // Get the input widget elements
    const input_text = widget_elem.getElementsByClassName("mutiple-color-input")[0];
    const color_list = widget_elem.getElementsByClassName("multiple-color-list")[0];
    const add_color_btn = widget_elem.getElementsByClassName("multiple-color-add-button")[0];
    const input_template = widget_elem.getElementsByClassName("multiple-color-template")[0];

    // Append Colour inputs
    function append_color_input(default_color) {
        default_color = typeof default_color  === 'undefined' ? '#FF0000' : default_color;
        var item, col_input;
        item = input_template.content.querySelector("li");
        col_input = document.importNode(item, true);
        col_input.getElementsByClassName("multiple-color-input")[0].value = default_color;
        color_list.appendChild(col_input);
    }

    // Init starting values
    function initValues() {
        var i, init_colors;
        color_list.innerHTML = "";
        if (input_text.value === "") return;
        init_colors = input_text.value.split(',');
        color_list.innerHTML = "";
        for (i = 0; i < init_colors.length; i++) {
            append_color_input(init_colors[i]);
        }
        updateSortableList();
    }

    initValues();

    // Add New Button
    add_color_btn.addEventListener("click", function (event) {
        event.preventDefault();
        append_color_input();
        updateSortableList();
    });

    // Remove Buttons
    function removeButtonsClick() {
        const removeButtons = color_list.getElementsByClassName('multiple-color-remove-button');
        Array.from(removeButtons).forEach((removeButton) => {
            removeButton.addEventListener('click', function (event) {
                event.preventDefault();
                removeButton.parentNode.remove();
                serializeItemsToTextInput();
            });
        });
    }

    // On Change Event for Input box (copy, paste, manual edit)
    input_text.addEventListener('change', function (event) {
        input_text.value = input_text.value.replaceAll(" ", "");
        initValues();
    });

    // Color Inputs on change
    function colorInputChange() {
        const colorInputs = color_list.getElementsByClassName('multiple-color-input');
        Array.from(colorInputs).forEach((colorInput) => {
            colorInput.addEventListener('change', function (event) {
                serializeItemsToTextInput();
            });
        });
    }

    // Serialise to text input
    function serializeItemsToTextInput() {
        var serialised = sortable(color_list, 'serialize');
        var col_arr = [];
        Array.from(serialised[0].items).forEach((item) => {
            col = item.node.getElementsByClassName('multiple-color-input')[0].value;
            col_arr.push(col);
        })
        input_text.value = col_arr.join(',');
    }

    // Update and create sortable list
    sortable_list = null;

    function updateSortableList() {
        // Set the sort list
        sortable_list = sortable(color_list);
        // Update the remove buttons
        removeButtonsClick();
        // Update on colour change
        colorInputChange();
        // Add event listener
        sortable_list[0].addEventListener('sortupdate', function (e) {
            serializeItemsToTextInput();
        });
        // Update the text string
        serializeItemsToTextInput();
    }
}

// Create Multiple Widgets here
function LoadMultipleColorWidgets(cls = "multiple-color-widget") {
    var els = document.getElementsByClassName(cls);
    Array.prototype.forEach.call(els, function (el) {
        MultipleColorWidget(el);
    });
}


// On Document load - run above
if (
    document.readyState === "complete" ||
    (document.readyState !== "loading" && !document.documentElement.doScroll)
) {
    LoadMultipleColorWidgets();
} else {
    document.addEventListener("DOMContentLoaded", function () {
        LoadMultipleColorWidgets();
    });
}

// On Django CMS formset added event - for inline forms
django.jQuery(document).on('formset:added', function (event, $row, formsetName) {
    MultipleColorWidget($row.find(".multiple-color-widget")[0]);
});

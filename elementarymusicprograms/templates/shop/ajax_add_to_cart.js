
var AJAX = {
    // handle a form submission including updating the cart quantity
    updatestatus : function(json, result_target, count_target) {
        var result = json.results;
        if (result == "Success") {
            result = 'Added To Cart!';
        }

        // tell jQuery to update the page
        $(result_target).html(result).addClass("status-updated");
        errors = json.errors;
        if (errors.length > 0) {
            for (var i = 0; i < errors.length; i++) {
                wich = errors[i][0];
                err = errors[i][1];
                if (wich == 'quantity') {
                    $(result_target).html(err);
                } else if (wich == 'product') {
                    var t = $(result_target).html();
                    $(result_target).html(t + '<br />' + err);
                }
            }
        }
        else
        {
          $('.basketTotal').html('<b>Total: $' + parseFloat(json.cart_total).toFixed(2) + '</b>');
          $('.basketItems').html('( ' + json.cart_count + ' ) item(s) in basket');
          {% include 'shop/ajax_add_to_cart_success.js' %}
            $(result_target).closest('form').find('.cart_qty').html(parseFloat(json.item_count).toFixed(0)).parent().show();
			// Load quickcart script to show items in cart, if they have the app installed
          if ($('#quickcart').length > 0) {
          	update_cart();
          }
        }
    },

    validate : function(formArray, jqForm, target) {
        var qty = 0;
        for (var i = 0; i < formArray.length; i++) {
            var element = formArray[i];
            if (element.name == 'quantity') {
                qty = element.value;
            }
        }

        if (!parseInt(qty) > 0) {
            $(target).html('Choose a valid quantity');
            return false;
        }
        return true;
    }
};

// Hook the submit to the add to cart form.  Degrades to a standard submit
// if no javascript
$(function() {
    $('form[action="{% url satchmo_smart_add %}"] input[name=addcart]').click(function(){
        var f =  $(this).closest('form');
        var s = f.find('.statusupdate');
        f.ajaxSubmit({
            url : '{% url satchmo_cart_add_ajax %}',
            type : 'POST',
            beforeSubmit : function(formArray, jqForm) {
                s.html('Please wait....');
                return AJAX.validate(formArray, jqForm, s);
            },
            dataType : 'json',
            success : function(json) {
                AJAX.updatestatus(json, s, '#more-cart-info .cartcount');
            }
        });
        return false;
    });
});

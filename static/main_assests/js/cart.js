//add to cart
$(document).on('click', '#add-cart', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "cart_add" %}',
        data: {
            product_id: $('#add-cart').val(),
            product_qty: $('#qty-cart').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },

        success: function (json) {
            //console.log(json)
            document.getElementById("cart_quantity").
                textContent = json.qty
            location.reload()
        },
        error: function (xhr, errmsg, err) {

        }
    });
})

// script to update cart
$(document).on('click', '.update-cart', function (e) {
    e.preventDefault();
    //grab the product id
    var productid = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: '{% url "cart_update" %}',
        data: {
            product_id: $(this).data('index'),
            product_qty: $('#select' + productid).val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },

        success: function (json) {
            //console.log(json)
            //document.getElementById("cart_quantity").textContent = json.qty
            location.reload()
        },
        error: function (xhr, errmsg, err) {

        }
    });
})

// script to delete item from cart
$(document).on('click', '.delete-cart-item', function (e) {
    e.preventDefault();
    //grab the product id
    //var productid = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: '{% url "cart_delete" %}',
        data: {
            product_id: $(this).data('index'),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },

        success: function (json) {
            //console.log(json)
            //document.getElementById("cart_quantity").textContent = json.qty
            location.reload()
        },
        error: function (xhr, errmsg, err) {

        }
    });
})
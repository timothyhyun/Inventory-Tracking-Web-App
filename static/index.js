$(function() {
    $('#addItem').bind('click', function() {
        var adddate = document.getElementById("addDate")
        var valueDate = adddate.value
        adddate.value = ""

        var addsku = document.getElementById("addSKU")
        var valueSKU = addsku.value
        addsku.value = ""

        var addquantity = document.getElementById("addQuantity")
        var valuequantity = addquantity.value
        addquantity.value = ""

        var addcomments = document.getElementById("addComments")
        var valuecomment = addcomments.value
        addcomments.value = ""

        $.getJSON('/addInventory',
            {date:valueDate, sku: valueSKU, quantity:valuequantity, comments:valuecomment},
            function(data) {

            });
    });
});

$(function() {
    $('#editItem').bind('click', function() {
        var editdate = document.getElementById("editDate")
        var valueDate = editdate.value
        editdate.value = ""

        var editsku = document.getElementById("editSKU")
        var valueSKU = editsku.value
        editsku.value = ""

        var editquantity = document.getElementById("editQuantity")
        var valuequantity = editquantity.value
        editquantity.value = ""

        var editcomments = document.getElementById("editComments")
        var valuecomment = editcomments.value
        editcomments.value = ""

        $.getJSON('/editInventory',
            {date:valueDate, sku: valueSKU, quantity:valuequantity, comments:valuecomment},
            function(data) {

            });
    });
});

$(function() {
    $('#deleteItem').bind('click', function() {

        var deletesku = document.getElementById("deleteSKU")
        var valueSKU = deletesku.value
        deletesku.value = ""

        $.getJSON('/addInventory',
            {sku: valueSKU},
            function(data) {

            });
    });
});






window.onload = function (){
    var update_loop = setInterval(update, 100);
    updateTable()
};

function updateTable(){
    fetch('/get_inventory')
             .then(function (response) {
                return response.json();
            }).then(function (text) {
                var table = document.getElementById("inventory")
                // somehow clear entire table except head
                inventory = text["inventory"]
                
            });
};
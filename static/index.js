$(function() {
    $('#addItem').bind('click', function() {
        var addname = document.getElementById("addName")
        var valueName = addname.value
        addname.value = ""

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
            {name:valueName, sku: valueSKU, quantity:valuequantity, comments:valuecomment},
            function(data) {

            });
    });
});

$(function() {
    $('#editItem').bind('click', function() {
        var editname = document.getElementById("editName")
        var valueName = editname.value
        editname.value = ""

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
            {name:valueName, sku: valueSKU, quantity:valuequantity, comments:valuecomment},
            function(data) {

            });
    });
});

$(function() {
    $('#deleteItem').bind('click', function() {

        var deletesku = document.getElementById("deleteSKU")
        var valueSKU = deletesku.value
        deletesku.value = ""

        $.getJSON('/deleteInventory',
            {sku: valueSKU},
            function(data) {

            });
    });
});






window.onload = function (){
    var update_loop = setInterval(updateTable, 100);
    updateTable()
};

function updateTable(){
    fetch('/get_inventory')
             .then(function (response) {
                return response.json();
            }).then(function (text) {
                var table = document.getElementById("inventory")
                var tableBody = document.getElementById("inventory_body")
                // somehow clear entire table except head
                inventory = text["inventory"]
                tableBody.innerHTML = ""
                console.log(inventory)
                for (let i = 0; i < inventory.length; i++){
                    var row = tableBody.insertRow(0)
                    for (let j = 0; j < inventory[i].length; j++){
                        var cell = row.insertCell(-1)
                        cell.innerHTML = inventory[i][j]
                    }
                }

            });
};
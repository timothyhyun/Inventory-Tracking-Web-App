// function to handle adding an item
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
// function to handle editing an item
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
// function to handle deleting an item
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


// gather inventory every 100 milliseconds
window.onload = function (){
    var update_loop = setInterval(updateTable, 100);
    updateTable()
};
// renders HTML table from json representation
function updateTable(){
    fetch('/get_inventory')
             .then(function (response) {
                return response.json();
            }).then(function (text) {
                var table = document.getElementById("inventory")
                var tableBody = document.getElementById("inventory_body")
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


// function to export data into a csv file
function download_to_csv() {
	var csv = [];
	var rows = document.getElementsByTagName('tr');
	for (var i = 0; i < rows.length; i++) {
		var cols = rows[i].querySelectorAll('td,th');
		var csvrow = [];
		for (var j = 0; j < cols.length; j++) {
			csvrow.push(cols[j].innerHTML);
		}

		csv.push(csvrow.join(","));
	}
	csv= csv.join('\n');
    CSVFile = new Blob([csv], { type: "text/csv" });
    var temp_link = document.createElement('a');

    temp_link.download = "inventory.csv";
    var url = window.URL.createObjectURL(CSVFile);
    temp_link.href = url;
 
    temp_link.style.display = "none";
    document.body.appendChild(temp_link);

    temp_link.click();
    document.body.removeChild(temp_link);
}



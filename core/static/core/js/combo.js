$(document).ready(function() {

    var cboRegion  = $("#cboRegion");

    cboRegion.change(function() {
        var regionId = cboRegion.val();

        if(regionId=="") {
            $("#cboComuna").prop("disabled", true);
            $("#cboComuna").val("");
            return;
        }

        //enviamos una peticion a combo.php
        //enviandole el id de la region
        $.get("combo.php", {id:regionId}, function(respuesta) {
            
            //dejamos los option dentro del cboComuna con la funcion .html
            $("#cboComuna").html(respuesta);
            //habilitamos el combobox de comuna
            $("#cboComuna").prop("disabled", false);

        });

    });

});
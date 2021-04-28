function modal(url){
        var $ = jQuery.noConflict();
        $('#mostrar_modal').load(url, function(){
            $(this).modal('show');
        });
    }
$(document).ready(function(){
    $(document).on("click", ".soft-reset-btn", function(){
        console.log('js');
        $.ajax({
            method: 'post',
            url: soft_reset_view,
            data: {'save_id': $(this)[0].dataset.saveId},
        });
    });
});

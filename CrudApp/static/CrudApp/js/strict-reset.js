$(document).ready(function(){
    $(document).on("click", ".strict-reset-btn", function(){
        $.ajax({
            method: 'post',
            url: strict_reset_view,
            data: {'save_id': $(this)[0].dataset.saveId},
        });
    });
});

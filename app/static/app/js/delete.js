$(document).ready(function() {
    $(document).on("click", ".delete", function () {
        let tr = $(this).parents("tr");
        `
        $.ajax({
            method: 'post',
            url: '{% url 'delete_product' %}',
            data: {'delete_id':tr.attr("id")},
        });
        `
        tr.remove();
        $(".create-new").removeAttr("disabled");
    });
});
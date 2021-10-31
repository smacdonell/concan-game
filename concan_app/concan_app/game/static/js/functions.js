$( document ).ready(function() {
    $('#name_field').on('change keyup', function() {
        $('.player_name_input').val($(this).val());
    });
});
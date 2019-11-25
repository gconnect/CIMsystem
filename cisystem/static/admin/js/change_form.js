
function print_certificate(){
    window.print()
}

    $(function() {
    $('input[name=".field-registered_late"]').on('click', function() {
        if ($(this).val() == '0') {
            $('.field-id_card').show();
            $('.field-amount_paid').show();
        }
        else {
            $('.field-id_card').show();
            $('.field-amount_paid').show();            }
    });
})


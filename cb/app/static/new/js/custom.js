$(document).ready(function() {
    var mdcFabStop = 1;
	
	// загрузочная панелька
	$(".mdc-linear-progress__bar").css('transform', 'scaleX(1)');
	setTimeout(function(){
       $(".mdc-linear-progress").addClass(" mdc-linear-progress--closed ");
    }, 1000);

	// если таблица отобразилась (есть результаты поиска) - убрать заглушку и запустить paging
    $("table").has("td").css("display", "table");
    if ($("table").is(":visible")) {
        $(".nothing-to-show").hide();
        $('.mdl-data-table').paging({
            limit: 20
        })
    }

	// динамичная кнопка возврата в начало страницы
    $(window).scroll(function() {
        if ($(this).scrollTop() > 300) {
            if (mdcFabStop > 0) {
                $('#toTop').addClass("mdc-fab--exited");
                $('#toTop').css('opacity', '100');
                mdcFabStop = 0;
            }
            $('#toTop').removeClass("mdc-fab--exited");
        } else {
            $('#toTop').addClass("mdc-fab--exited");
        }
    });

    $('#toTop').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
});

// поиск у нас только капсом, не допускаем строчные буквы на вводе
function convertToUppercase(el) {
    el.value = el.value.toUpperCase();
}
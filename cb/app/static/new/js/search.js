$(document).ready(function() {
	// переключатель выдачи
	var limitValue = initRadio();

	// отображение таблицы и всего, что с ней связано
    tableInit(limitValue);
	
	// возвращаемся в начало по нажатию кнопки
	$('#toTop').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
});

// вызываем два вида снэкбаров, если не нашли результатов или превысили порог
function callAlert(ind) {
	var snackbar = mdc.snackbar.MDCSnackbar.attachTo(document.getElementById('alert'));
	var data =  {
        message: "По Вашему запросу ничего не найдено",
        timeout: 2500,
		actionText: 'Ошибка',
		actionHandler: function () {
			console.log('[No results] alert is pressed');
		}
    };
	var data1 =  {
        message: "Слишком много эмитентов, уточните запрос",
        timeout: 2500,
		actionText: 'Ошибка',
		actionHandler: function () {
			console.log('[Too many] alert is pressed');
		}
    };
	var alert_opt = [data,data1];
	snackbar.show(alert_opt[ind])
}

function initRadio() {
	var form = document.getElementById("search_form");
	return(form.elements.values.value);
}

// лого меняется, если навигационная панель слишком узкая
function resizing() {
	var w = window.innerWidth;
	if (w<980) {
		$(".logo").html("<img src='/static/new/img/CB-logo-min.png'>");
	} else {
		$(".logo").html("<img src='/static/new/img/CB-logo.png'>");
	}
}

// динамичная кнопка возврата в начало страницы
$(window).scroll(function () {
	var mdcFabStop = 1;
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

// поиск у нас только капсом, не допускаем строчные буквы на вводе
function convertToUppercase(el) {
    el.value = el.value.toUpperCase();
}

function resultsQuantity(el) {
	var q = (el.length-1)%100;
	var Qlform = '';
	var Qlform2 = '';
	if (q > 10 && q < 15) {
		Qlform = 'тов';
		Qlform2 = "о"
	} else {
		switch (q%10) {
			case 1:
				Qlform = 'т';
				break;
			case 2: case 3: case 4:
				Qlform = 'та';
				Qlform2 = "о";
				break;
			case 5: case 6: case 7: case 8: case 9: case 0:
				Qlform = 'тов';
				Qlform2 = "о";
				break;
		}
	}
	$( ".resultsQl" ).prepend("эмитен"+Qlform+" ");
	$( ".resultsQl" ).append( Qlform2 );
	$('.resultsQ-cont').fadeIn(1000);
	$('.resultsQ').each(function () {
		$(this).prop('Counter',0).animate({
        Counter: el.length-1
		}, {
			duration: 2000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});
}

function tableInit(limitValue) {
	// если таблица отобразилась (есть результаты поиска) - убрать заглушку и запустить paging
	$("table").has("td").css("display", "table");
    if ($("table").is(":visible")) {
		$("table").paging({
			limit: limitValue
		});
		resultsQuantity($("tr"))
    }
}
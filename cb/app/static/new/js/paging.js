(function($) {
    $(function() {
        $.widget("zpd.paging", {
            options: {
                limit: 5,
                rowDisplayStyle: 'block',
                activePage: 0,
                rows: [],
                avialable: 0
            },
            _create: function() {
                // даём начальные установки и погнали
                var rows = $("tbody", this.element).children();
                this.options.rows = rows;
                this.options.rowDisplayStyle = rows.css('display');
                this.options.avialable = Math.ceil(rows.length/this.options.limit);
                this._on($('.view-more button'), {
                    click: "pageClickHandler"
                });

                // alert('Всего элементов - '+rows.length+' '+', на неполной странице - '+(rows.length % this.options.limit));
                // отладочный алёрт скрыт

                this.showPage(0);
            },
            showPage: function(pageNum) {
                // вспоминаем переменные
                var max = this.options.avialable;
                var rows = this.options.rows;
                var limit = this.options.limit;
				var few_on_last = (rows.length%limit < limit/2);
				var merge_pages = false;
				var more = $('.view-more');
				
                // в самом начале работы всё должно быть скрыто
                if (pageNum == 0) {
                    for (var j = 0; j < rows.length; j++) {
                        $(rows[j]).css('display', 'none');
                    }
                }
				
                // хотим исключить "маленькие" страницы, на которых количество элементов минимум в 2 раза меньше лимита
                if (few_on_last && (max - (this.options.activePage+1)) == 1) {
                    var next = pageNum + 2;
					merge_pages = true
                } else {
					var next = pageNum + 1
				}
				
				var check = (max!=1 && !merge_pages);

                // наконец основная работа - отображать скрытые ранее элементы
                for (var i = limit*pageNum; i < limit*next && i < rows.length; i++) {
                    $(rows[i]).css('display', this.options.rowDisplayStyle);
                }
				
				// адаптируем высоту кнопки под последние две строки
				if (check) {
					var all = $("tr");
					var mbh = $(all[i]).height()+$(all[i-1]).height()-60;
					var mbh_out = mbh/2+"px 0 "+mbh/2+"px";
					$(".view-more").css("padding",mbh_out)
				}
					
				if (check && !more.is(':visible')) more.show();

                // alert('Отображение страницы №'+this.options.activePage+', с номерами элементов '+limit * pageNum+'-'+i);
                // отладочный алёрт скрыт

                // не забываем переключить страничку или скрыть кнопку, если странички кончились
                this.options.activePage = next;
                if (next+1 > max && more.is(':visible')){
                    more.hide();
                }
            },
            pageClickHandler: function(event) {
                event.preventDefault();
                this.showPage(this.options.activePage);
            }
        });
    });
})(jQuery);
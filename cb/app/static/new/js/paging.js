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
                this.options.avialable = Math.ceil(rows.length / this.options.limit) - 1;
                this._on($('.view-more button'), {
                    click: "pageClickHandler"
                });

                // alert('Всего элементов - '+rows.length+' '+', на неполной странице - '+(rows.length % this.options.limit));
                // отладочный алёрт скрыт

                this.showPage(0);
                if (this.options.avialable > 1) {
                    $('.view-more').show()
                }
            },
            showPage: function(pageNum) {
                // вспоминаем переменные
                var max = this.options.avialable;
                var rows = this.options.rows;
                var limit = this.options.limit;

                // в самом начале работы всё должно быть скрыто
                if (pageNum == 0) {
                    for (var j = 0; j < rows.length; j++) {
                        $(rows[j]).css('display', 'none');
                    }
                }

                // хотим исключить "маленькие" страницы, на которых количество элементов минимум в 2 раза меньше лимита
                var next = pageNum + 1;
                if ((rows.length % limit) < (limit / 2) && (max - this.options.activePage) == 1) {
                    next = pageNum + 2;
                }

                // наконец основная работа - отображать скрытые ранее элементы
                for (var i = limit * pageNum; i < limit * next && i < rows.length; i++) {
                    $(rows[i]).css('display', this.options.rowDisplayStyle);
                }

                // alert('Отображение страницы №'+this.options.activePage+', с номерами элементов '+limit * pageNum+'-'+i);
                // отладочный алёрт скрыт

                // не забываем переключить страничку или скрыть кнопку, если странички кончились
                this.options.activePage = next;
                if (this.options.activePage > max) {
                    $('.view-more').hide();
                }
            },
            pageClickHandler: function(event) {
                event.preventDefault();
                this.showPage(this.options.activePage);
            }
        });
    });
})(jQuery);
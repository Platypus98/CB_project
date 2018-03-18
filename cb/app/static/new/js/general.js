var loginAlert, logoutAlert, u_info, l_p;
var show_k = 0;

$(document).ready(function() {
	window.mdc.autoInit();
	loginAlert = mdc.dialog.MDCDialog.attachTo(document.querySelector('.login-dialog'));
	logoutAlert = mdc.dialog.MDCDialog.attachTo(document.querySelector('.logout-dialog'));
	u_info = mdc.menu.MDCMenu.attachTo(document.querySelector('.mdc-menu'));
	// $('.mdc-menu').click(function(){return false});
	
	// устанавливаем активную кнопку в навигационной панели
	var t = $("title").text().toLowerCase();
	var tabs = $(".mdc-tab");
	switch (0) {
		case t.indexOf('главная'):
			$(tabs[0]).addClass("mdc-tab--active");
			break
		case t.indexOf('поиск'):
			$(tabs[1]).addClass("mdc-tab--active");
			break
		case t.indexOf('обновление'):
			$(tabs[3]).addClass("mdc-tab--active");
			break
	}
	
	mdc.iconToggle.MDCIconToggle.attachTo(document.querySelector("#user-tab"));
	$("#user-tab").focus(function(){$(this).blur()});
	
	$('.exit').click(function(){logoutAlert.show()});
	
	// загрузочная панелька
	l_p = mdc.linearProgress.MDCLinearProgress.attachTo(document.querySelector("#progress"));
	load()
});

// загрузочная панелька
function load() {
	l_p.open();
	l_p.progress = 1;
	setTimeout(function(){l_p.close()}, 1000);
	setTimeout(function(){l_p.progress = 0}, 2000);
}

// показываем меню с информаицей о пользователе по клику на кнопку
function userMenu() {
	u_info.open = !u_info.open;
	show_k++;
	if (show_k == 1) {
		show_k++;
		setTimeout(function(){
			mdc.ripple.MDCRipple.attachTo(document.querySelector('.user-settings'));
			mdc.ripple.MDCRipple.attachTo(document.querySelector('.exit'))
		},100)
	}
}

// показываем диалоговое окно для входа в аккаунт
function showLogin() {
	loginAlert.show();
	show_k++;
	if (show_k == 1) {
		setTimeout(function(){
			var tf = $(".mdc-text-field");
			for (var i=0;i<tf.length;i++) {
				mdc.textField.MDCTextField.attachTo(tf[i])
			}
		},100)
	}
}

// не даём пользователю отправлять форму входа пустой
function validateAuth() {
	var form = document.getElementById("auth");
	var fields = $(".login-field input");
	var help_t = $(".must-fill");
	var invalid = false;
	for (var x=0;x < fields.length;x++) {
		if (fields[x].value == "") {
			$(fields[x]).parent('div').addClass("mdc-text-field--invalid");
			help_t.text('Поля должны быть заполнены');
			invalid = true
		}
	}
	if (!invalid) {
		help_t.animate({opacity: '0'},200);
		var auth_data = new FormData($('#auth').get(0));
		$.ajax({
			url: '/auth/',
			method: 'POST',
			data: auth_data,
			cache: false,
			processData: false,
			contentType: false,
			dataType: 'json',
			success: function (data) {
				if (data.l_in) {
					loginAlert.close();
					$('.login-alert p:first-child').append(data.name);
					$('.us_inf-name span').text(data.nick);
					$('#user-tab').text('person').attr('onclick','userMenu();');
					show_k = 0;
					load();
					setTimeout(function(){
						$('#auth').trigger('reset');
						loginSuccess()
					},500)
				} else {
					help_t.text('Неверный логин/пароль');
					help_t.animate({opacity: '1'},200)
				}
			}
		});
	} else {
		help_t.animate({opacity: '1'},200)
	}
}

function authLogout() {
	var out = new FormData($('#logout').get(0));
	$.ajax({
		url: '/auth/',
		method: 'POST',
		data: out,
		cache: false,
		processData: false,
		contentType: false,
		dataType: 'json',
		success: function (data) {
			if (data.l_out) {
				$('.us_inf-name span').text('username');
				$('#user-tab').text('person_outline').attr('onclick','showLogin();');
				var l_a = $('.login-alert p:first-child');
				var str = l_a.text();
				l_a.text(str.replace(str.split(" ")[2],''));
				show_k = 0;
				load()
			}
		}
	});
}

//показываем приветствие после успешного входа в аккаунт
function loginSuccess() {
	var alerts =document.getElementsByClassName("login-text");
	$(".login-alert").css({'height': '100%', 'visibility': 'visible'});
	$(".login-alert").animate({opacity: '0.8'});
	setTimeout(function (){$(alerts[0]).animate({opacity: '1',top: '40%'});},500);
	setTimeout(function (){$(alerts[1]).animate({opacity: '1'});},1000);
	setTimeout(function (){$(".login-alert").animate({opacity: '0'},200)},2800);
	setTimeout(function (){$(".login-alert").css({'height': '0', 'visibility': 'hidden'})},3000);
}


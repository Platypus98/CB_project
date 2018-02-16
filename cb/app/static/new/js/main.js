$(document).ready(function() {
	window.mdc.autoInit()
	
	var linearProgress = mdc.linearProgress.MDCLinearProgress.attachTo(document.querySelector("#progress"));
	
	// зажигаем часики
	startTime();
	// устанавливаем картиночку на фон
	var time_points = setPicture(false,0);
	
	// запускаем дэмку спустя 3 секунды
	setTimeout(function(){
		checkCookie(time_points)
    }, 3000);
	
	// загрузочная панелька
	linearProgress.progress = 1;
	setTimeout(function(){
		linearProgress.close()
    }, 1000);
});

function callAlert(ind) {
	var snackbar = mdc.snackbar.MDCSnackbar.attachTo(document.getElementById('alert'));
	var data =  {
        message: "Неверный логин/пароль",
        timeout: 2500,
		actionText: 'Ошибка',
		actionHandler: function () {
			console.log('[Wrong login] alert is pressed');
		}
    };
	var data1 =  {
        message: "Вы вышли из системы",
        timeout: 2500,
		actionText: 'Уведомление',
		actionHandler: function () {
			console.log('');
		}
    };
	var alert_opt = [data,data1];
	snackbar.show(alert_opt[ind])
}
//показываем приветствие после успешного входа в аккаунт
function loginSuccess() {
	var alerts =document.getElementsByClassName("login-text");
	$(".login-alert").css('height','100%');
	$(".login-alert").animate({opacity: '0.7'});
	setTimeout(function (){$(alerts[0]).animate({opacity: '1',top: '40%'});},500);
	setTimeout(function (){$(alerts[1]).animate({opacity: '1'});},1000);
	setTimeout(function (){$(".login-alert").animate({opacity: '0'},200)},2300);
	setTimeout(function (){$(".login-alert").css('height','0')},2500);
}

function setPicture(demo,demo_value) {
	var now = new Date();
	var times = seasonTime(now);
	if (demo) {
		now = demo_value;
	} else {
		now = now.getTime();
	}
	
	// для начала проверяем на исключения, когда начало/конец того, что
	// мы считаем "днём" не совпадает с началом процессов рассвета/заката
	if (times[8]<times[0]) var late_sunr = true;
	if (times[7]<times[9]) var early_suns = true;
	
	// теперь прописываем все возможные сценарии
	switch (true) {
		case (now<times[0]&&(!(late_sunr) || now<times[8])
			  || now>=times[7]&&(!(early_suns) || now>=times[9])):
			$("body").css("background-image", "url('/static/new/img/night.jpg')");
			break
		case (now<times[1]&&(now>=times[0] || now>=times[8]&&late_sunr)
			  || now>=times[6]&&(now<times[7] || now<times[9]&&early_suns)):
			$("body").css("background-image", "url('/static/new/img/night2.jpg')");
			break
		case (now<times[2]&&now>=times[1]):
			$("body").css("background-image", "url('/static/new/img/twilight1.jpg')");
			break
		case (now<times[3]&&now>=times[2]):
			$("body").css("background-image", "url('/static/new/img/sunrise.jpg')");
			break
		case (now<times[4]&&now>=times[3]):
			$("body").css("background-image", "url('/static/new/img/day.jpg')");
			break
		case (now<times[5]&&now>=times[4]):
			$("body").css("background-image", "url('/static/new/img/sunset.jpg')");
			break
		case (now<times[6]&&now>=times[5]):
			$("body").css("background-image", "url('/static/new/img/twilight2.jpg')");
			break
	}
	
	// отдельно - для надписи, так как там есть небольшие отличия
	switch (true) {
		case (now<times[8] || now>=times[9]):
			$(".welcome").html("Доброй ночи!");
			break
		case (now>=times[8]&&now<times[10]):
			$(".welcome").html("Доброе утро!");
			break
		case (now>=times[10]&&now<times[11]):
			$(".welcome").html("Добрый день!");
			break
		case (now>=times[11]&&now<times[9]):
			$(".welcome").html("Добрый вечер!");
			break
	}
	
	setTimeout(function(){setPicture()},900000);
	return(times)
}

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
	$("#clock").html(h+':'+m+':'+s);
	if (h < 10) $("#clock").css("margin-right","-30px");
	if (h > 9 & h<20) $("#clock").css("margin-right","-10px");
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // добавить ноль перед числами < 10
    return i;
}

// показываем диалоговое окно для входа в аккаунт
function showLogin() {
	var loginAlert = mdc.dialog.MDCDialog.attachTo(document.querySelector('.mdc-dialog'));
	loginAlert.show();
	setTimeout(function(){initLogin()},100)
}
// делаем так, чтобы ripple к полям входа
// прикреплялся только после нажатия кнопки
function initLogin() {
	var tf = $(".mdc-text-field");
	for (var i=0;i<tf.length;i++) {
		mdc.textField.MDCTextField.attachTo(tf[i])
	}
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

// дополнительная функция для удобного округления
function precisionRound(number, precision) {
  var factor = Math.pow(10, precision);
  return Math.round(number * factor) / factor;
}

// тут долго и нудно находим нужные контрольные
// временные точки для отображения фона
function seasonTime(now) {
	// этот кусок кода позволяет вычислить, какой
	// сегодня по счёту день в году
	var start = new Date(now.getFullYear(), 0, 0);
	var diff = (now - start) + ((start.getTimezoneOffset() - now.getTimezoneOffset()) * 60 * 1000);
	var oneDay = 1000 * 60 * 60 * 24;
	var day = Math.floor(diff / oneDay);
	
	// далее - коэффициенты для функций вычисления времени
	// восхода/заката, получены через Excel
	const sunr_par1 = [0.00000184763949328257,
					 -0.000459377203073874,
					 -0.00647695197872622,
					 9.03347216036568];
	const sunr_par2 = [-0.000000000118550432046054,
					 0.0000000563258816456847,
					 -0.0000101635843282044,
					 0.000881315775444591,
					 -0.00481943454667544,
					 3.77338232491456];
	const suns_par1 = [-0.00000000378951205766594,
					 0.000000732687323853898,
					 -0.000028296409412043,
					 0.0335632446096383,
					 16.0124308318809];
	const suns_par2 = [0.00000189380220801181,
					 -0.000495105027354448,
					 -0.00207881725347647,
					 21.3410361959413];
					 
	// здесь обозначаем дельты времени для начала
	// показа того или иного сценария фона
	var add_sunr = [-120,-60,0,90];
	var add_suns = [-90,0,60,120];
	
	// чтобы было дальше удобно создавать контрольную
	// точку - сегодняшняя дата готовится заранее
	var str_default = now.getFullYear()+" "+(now.getMonth()+1)+" "+now.getDate()+" ";
	
	// в этом массиве будут собраны, собственно, сами контрольные точки
	var result = [];
	result.length = 12;
	
	// поскольку области определения функций пересекаются,
	// прописываем как их комбинировать
	switch (true) {
        case (day<170):
			var pars = [sunr_par1,suns_par1];
			break;
        case (day>169 && day<178):
			var pars = [sunr_par2,suns_par1];
			break;
        case (day>177):
			var pars = [sunr_par2,suns_par2];
			break;
    }
	
	// рабочая лошадка, забирает каждую контрольную
	// точку из функции-обработчика
	for (var j=0;j<pars.length;j++) {
		for (var z=0;z<4;z++) {
			if (j==1) add_sunr = add_suns;
			result[4*j+z] = getSunTime(str_default,day,pars[j],add_sunr[z])
		}
	}
	
	// ах да, у нас же есть ещё точки, которые задают промежуток
	// того, что мы считаем "днём", добавим их ручками
	result[8] = (new Date(str_default+"5:00")).getTime();
	result[9] = (new Date(str_default+"23:00")).getTime();
	result[10] = (new Date(str_default+"10:00")).getTime();
	result[11] = (new Date(str_default+"16:00")).getTime();
	
	return(result)
}
function getSunTime(str_default,day,coefs,add) {
	var k = 0;
	
	// используя принятый набор коэффициентов,
	// находим таки нужное время для данного дня
	for (var i=0;i<coefs.length;i++) {
		k+=coefs[i]*Math.pow(day, coefs.length-i-1);
	}
	
	// на предыдущем шаге получили число с дробной частью -
	// избавляемся от неё и собираем контрольную точку
	k*=60;
	
	var str = Math.floor((k+add)/60)+":"+precisionRound((k+add)%60,0);
	var out = (new Date(str_default+str)).getTime();
	// alert(out);
	return(out)
}


// ЗДЕСЬ БОЛЬШАЯ ШТУКА С DEMO ДЛЯ РАЗРАБОВ
function setCookie(cname,cvalue,exdays) {
	var d = new Date();
	d.setTime(d.getTime() + (exdays*24*60*60*1000));
	var expires = "expires=" + d.toGMTString();
	document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
	var name = cname + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for(var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}
function checkCookie(times) {
	var demo_weather=getCookie("visited");
	var prompts = ["Вот так фон будет выглядеть глубокой ночью:",
				   "А так незадолго до утренних сумерек:",
				   "Утренние сумерки:",
				   "На рассвете:",
				   "Днём:",
				   "На закате:"];
	var values = [times[8],times[1],times[2],times[3],times[4],times[5]];
	if (demo_weather == "") {
		alert("Приветствую! Сейчас - небольшая демонстрация работы алгоритма смены фона\n\nКаждый день система вычисляет новые промежутки времени, в которые на фоне должен быть тот или иной пейзаж. Сейчас увидите!");
		function display(j,p,v) {
			if (j == v.length) {
				alert("И так далее. Можете заходить в течении дня, наблюдать за этим довольно забавно. Немного природы в компьютере каждого работника :)");
				setCookie("visited", "true", 30);
				setTimeout(function(){location.reload()},1000);
				return
			} else {
				setPicture(true,v[j]-300000);
				setTimeout(function(){alert(p[j]);display(j+1,p,v);}, 1000);
			}
		}
		display(0,prompts,values);
	}
}
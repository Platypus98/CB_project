$(document).ready(function() {
	$(".file-btn").click(function() {
		if ($('#user-tab').text().indexOf('person_outline') >= 0) {
			showLogin();
			return
		}
		document.getElementById("id_docfile").click()
	});
});

// в кнопочку запихиваем название выбранного файла из input
function fileNameUpd(value) {
	if (value == "") {
		$(".file-btn span").fadeOut(200,function() {
			$(this).text('Выберите новый файл')
		}).fadeIn();
		$(".file-btn i").delay(200).fadeIn();	
	} else {
		$(".file-btn i").fadeOut(200);
		$(".file-btn span").fadeOut(200,function() {
			$(this).text(value.replace(/C:\\fakepath\\/i, ''))
		}).fadeIn();
	}
}

// лого меняется, если навигационная панель слишком узкая
function resizing() {
	setTimeout(function(){refreshTiles(false);},1000);
	var w = window.innerWidth;
	if (w<980) {
		$(".logo").html("<img src='/static/new/img/CB-logo-min.png'>");
	} else {
		$(".logo").html("<img src='/static/new/img/CB-logo.png'>");
	}
}

var cl1 = "flash-tile";
var cl2 = "stable";
var step = 0.05;
var basis;
var global = 0;
var grid = $("#tiles-cont");
var lines = $("#tiles-back");

function refreshTiles(step_only) {
	if (!step_only) {
		basis = initGrid();
		progressHandler(basis[0],basis[1],global,false)
	}
	progressHandler(basis[0],basis[1],step,true)
}

function launchTiles() {
	if ($('#user-tab').text().indexOf('person_outline') >= 0) {
		showLogin();
		return
	}
	basis = initGrid();
	var head = $(".form-heading");
	var temp = $("#upd").width();
	$("#upd").css('width',temp+'px');
	head.animate({opacity: 0},250);
	setTimeout(function(){
		head.append('<span class="mdc-typography--display1">.....</span><span>0%</span>');
		head.removeClass("mdc-typography--display3");
		head.addClass("mdc-typography--display2");
		$(".info").slideUp(300);
	},300);
	setTimeout(function(){
		$("#upd").animate({padding: '30px 0'},250);
		head.animate({opacity: 1},1000)
	},700);
	setTimeout(function(){
		grid.css("height", "100%");
		lines.css("height","100%");
		grid.animate({opacity: '1'},250);
	},1000);
	setTimeout(function(){lines.animate({backgroundColor: '#000'},500)},1250);
	// function tester(b) {
		// refreshTiles(true);
		// global=precisionRound(global+b,2);
		// if (global > 1) return('')
		// setTimeout(function(){tester(b)},4000)
	// }
	// setTimeout(function(){tester(0.05)},3000);
	// setTimeout(function(){progressHandler(basis[0],basis[1],0.3,false)},1500);
	setTimeout(function(){
		refreshTiles(true);
		uploadFile()
	},3000);
}

function initGrid() {
	grid.empty();
	
	// инициализация - расчитываем кол-во столбцов и строчек
	var w = document.body.offsetWidth;
	var h = document.body.offsetHeight;
	var ht_val = Math.ceil(w/40);
	var vt_val = Math.ceil(h/40);
	var ht = "repeat("+ht_val+", 1fr [col-start])";
	var vt = "repeat("+vt_val+", 1fr [row-start])";
	grid.css("grid-template-rows", vt);
	grid.css("grid-template-columns", ht);
	
	console.log("Сетка "+ht_val+" на "+vt_val);
	console.log('')

	// рождаем нужное нам количество секторов
	var tiles_len = ht_val*vt_val;
	for (var i=0;i<tiles_len;i++) {
		$(grid).append('<div class="tile"></div>')
	}
	
	// так-с, теперь хотим перейти к двумерному массиву
	// для более простого доступа к какому-либо сектору
	var tiles = $(".tile");
	var main = [];
	for (i=0; i < ht_val; i++) {
		main[i] = [];
		for (var z=0;z < vt_val; z++) {
			main[i][z] = tiles[z*ht_val+i];
		}
	}
	
	// цикл для составления колец
	var rings_num = Math.ceil(vt_val/2);
	var rings = new Array(rings_num);
	// var color = "";
	for (i=0;i < rings_num;i++) {
		rings[i] = [];
		// добавляем горизонтальные составляющие
		for (z=0+i;z<ht_val-i;z++) {
			rings[i].push([z,i]);
			if (vt_val-1-i != i) rings[i].push([z,vt_val-1-i])
		}
		// а теперь вертикальные
		for (z=1+i;z<vt_val-i-1;z++) {
			rings[i].push([i,z]);
			rings[i].push([ht_val-i-1,z])
		}
		
		// это просто отладка для проверки целостности колец
		
		// color = '#'+Math.floor(Math.random()*16777215).toString(16);
		// for (z=0;z<rings[i].length;z++) {
			// var inds = rings[i][z];
			// $(main[inds[0]][inds[1]]).css("background-color",color)
		// }
	}
	
	return([main,rings])
}
	
function progressHandler(main,rings,val,buffer) {
	for (i=0;i < rings.length;i++) {
		var k = 0;
		var ring_small = [];
		var len = rings[i].length;
		console.log("В кольце №"+i+" "+len+" элементов");
		
		// когда запускается очередной раз - все секторы,
		// которые до этого мигали, должны окрасится
		for (z=0;z < len;z++) {
			var crd = rings[i][z];
			var tile = $(main[crd[0]][crd[1]]);
			if (tile.hasClass(cl1) && buffer)
				tile.removeClass(cl1).addClass(cl2)
			else if (buffer && !tile.hasClass(cl2))
				ring_small.push(rings[i][z])
			else if (!buffer) ring_small = rings[i];
		}
		console.log('GLOBAL:  '+global)
		if (global != 1) setTiles(main,ring_small,val,k,len,0,buffer);
		console.log('')
	}
}

function setTiles(main,ring,val,k,len,x,buffer) {
	var rep = Math.floor(val*len);
	if (rep == 0) {
		console.log("Кольцу не нужно было искать секторы");
		return
	}
	var left_over = len-rep*(1/step);
	if (global == 1-2*step) rep+=Math.floor(left_over/2);
	if (global == 1-step) rep+=left_over-Math.floor(left_over/2);
	var got = false;
	
	// получаем рандомный элемент из кольца
	var crd = ring[Math.floor(Math.random() * ring.length)];
	var tile = $(main[crd[0]][crd[1]]);
	
	// когда элементов уже слишком много, нет смысла заполнять "по-умному"
	if (!tile.hasClass(cl1) && !tile.hasClass(cl2)) {
		if (global < 0.3) got = checkAround(main,crd)
		else got = true
	}
	
	// после успешной проверки на соседей и состояние преобразуем элемент
	if (got) {
		k++;
		// console.log("Я элемент ["+crd[0]+","+crd[1]+"] проверился нахой");
		if (buffer) tile.addClass(cl1)
		else tile.addClass(cl2)
	}
	x++;
	if (x<rep*100) {
		if (k != rep) setTiles(main,ring,val,k,len,x,buffer)
		else {
			console.log("Кольцо искало подходящие секторы "+x+" раз. Найти нужно было "+rep);
		}
	} else console.log("Кольцо искало подходящие секторы и объебалось. Найти нужно было "+rep);
}

function checkAround(main,xy) {
	var x_ok,y_ok,y1,y2,x1,x2;
	x_ok = y_ok = y1 = y2 = x1 = false;
	
	
	// проверяем соседей по вертикали
	if (xy[1]!=(main[xy[0]].length-1)) {
		var down = main[xy[0]][xy[1]+1];
		y1 = no_cl(down)
	} else y1 = true;
	if (xy[1]!=0) {
		var up = main[xy[0]][xy[1]-1];
		y2 = no_cl(up)
	} else y2 = true;
	if (y1 && y2) y_ok = true;
	
	// теперь по горизонтали
	if (xy[0]!=0) {
		var left = main[xy[0]-1][xy[1]];
		x1 = no_cl(left)
	} else x1 = true;
	if (xy[0]!=(main.length-1)) {
		var right = main[xy[0]+1][xy[1]];
		x2 = no_cl(right)
	} else x2 = true;
	if (x1 && x2) x_ok = true;
	
	if (y_ok && x_ok) return(true)
	else return(false)
}

function no_cl(el) {
	if ($(el).hasClass(cl1) || $(el).hasClass(cl2)) return(false)
	else return(true)
}


// дополнительная функция для удобного округления
function precisionRound(number, precision) {
	var factor = Math.pow(10, precision);
	return Math.round(number * factor) / factor;
}

// загружаем файлик в систему
function uploadFile() {
	var db = new FormData($('#upd').get(0));

	$.ajax({
		url: '/db_update/',
		type: 'POST',
		data: db,
		cache: false,
		processData: false,
		contentType: false,
		dataType: 'json',
		success: function(data) {
			if (data.parse_ok) requestProgress(0)
			else alert("F")
		}
	});
	return false;
}

// кольца для рандомной раскраски готовы, начинаем запросы
function requestProgress(ind) {
	$.ajax({
		url: '/db_update/',
		data: {k: ind},
		dataType: 'json',
		success: function (data) {
			if (data.update_ok) {
				console.log("Преодолён столбец №"+(ind+2));
				var raw = precisionRound((ind+1)/96,2);
				$(".form-heading span:last-child").text(precisionRound(raw*100,0)+'%');
				var percent = precisionRound(Math.floor(raw/step)*step,2);
				if (percent > global) {
					global = percent;
					refreshTiles(true)
				}
				if (ind != 95) requestProgress(ind+1)
				else setTimeout(function(){location.reload()},1000)
			}
		}
	});
}
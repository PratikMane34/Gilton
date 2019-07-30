frappe.pages['dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Generic Dashboard',
		single_column: true
	});

	doctype_list=get_doc_list()
	doc_list_length = doctype_list.length
	$(frappe.render_template('sidebar',{"doctype_list":doctype_list,"length":doc_list_length})).appendTo(page.body);

	$("input[id='customer_name']").change(function(){
		alert("first alert")
		})
	datacall(subscription_data[0])
	sidebarClick()
}

function get_doc_list(){
	frappe.call({
		method:"gilton.gilton.page.dashboard.dashboard.get_doc_list",
		async: false,
		callback:function(r){
			subscription_data = r.message
			console.log("b",subscription_data)
			}
	});
	console.log(subscription_data)
	return subscription_data
}



function sidebarClick(){
	console.log("sidebarClick ...")
	$('.subscription_activation').click(function(){
		var doc = ($('#subscription_activation').text())
		$('li.active').removeClass('active');
		$(this).addClass('active');
		data=datacall(doc)

		subscription_update_generic(data)
		console.log("generic update in sidebar click")
	})
	$('.option1').click(function(){
		$('li.active').removeClass('active');
		$(this).addClass('active');
		var doc = ($('#option1').text())
		datacall(doc)
	})
	$('.option2').click(function(){
		$('li.active').removeClass('active');
		$(this).addClass('active');
		var doc = ($('#option2').text())
		datacall(doc)
	})
	$('.option3').click(function(){
		alert($('#option3').text())
		$('li.active').removeClass('active');
		//get_opportunity_details()
		$(this).addClass('active');
		var doc = ($('#option3').text())
		datacall(doc)

	})
	$('.option4').click(function(){
		alert($('#option4').text())
		var doc = ($('#option4').text())

		frappe.call({
			method:"gilton.gilton.page.dashboard.dashboard.get_doc_filter",
			args: {"doctype":doc},
			callback:function(r){
				if(r.message){
					console.log("got doc filterszzzzzzzzzzzzzzzzzz")
					console.log(r.message)
					$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filter":['asd','qwe','zxcv']})))
					//$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
				}
			}

		})
	})
	$('.option5').click(function(){
		alert($('#option5').text())
		var doc = ($('#option5').text())

		frappe.call({
			method:"gilton.gilton.page.dashboard.dashboard.get_doc_filter",
			args: {"doctype":doc},
			callback:function(r){
				if(r.message){
					console.log("got doc filterszzzzzzzzzzzzzzzzzz")
					console.log(r.message)
					$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filter":['asd','qwe','zxcv']})))
					//$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
				}
			}

		})
	})
	$('.option6').click(function(){
		alert($('#option6').text())
		var doc = ($('#option6').text())

		frappe.call({
			method:"gilton.gilton.page.dashboard.dashboard.get_doc_filter",
			args: {"doctype":doc},
			callback:function(r){
				if(r.message){
					console.log("got doc filterszzzzzzzzzzzzzzzzzz")
					console.log(r.message)
					$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filter":['asd','qwe','zxcv']})))
					//$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
				}
			}

		})
	})
	$('.option7').click(function(){
		alert($('#option7').text())
		var doc = ($('#option7').text())

		frappe.call({
			method:"gilton.gilton.page.dashboard.dashboard.get_doc_filter",
			args: {"doctype":doc},
			callback:function(r){
				if(r.message){
					console.log("got doc filterszzzzzzzzzzzzzzzzzz")
					console.log(r.message)
					$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filter":['asd','qwe','zxcv']})))
					//$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
				}
			}

		})
	})
	$('.option8').click(function(){
		alert($('#option8').text())
		var doc = ($('#option8').text())

		frappe.call({
			method:"gilton.gilton.page.dashboard.dashboard.get_doc_filter",
			args: {"doctype":doc},
			callback:function(r){
				if(r.message){
					console.log("got doc filterszzzzzzzzzzzzzzzzzz")
					console.log(r.message)
					$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filter":['asd','qwe','zxcv']})))
					//$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
				}
			}

		})
	})
	$('.option9').click(function(){
		alert($('#option9').text())
		var doc = ($('#option9').text())

		frappe.call({
			method:"gilton.gilton.page.dashboard.dashboard.get_doc_filter",
			args: {"doctype":doc},
			callback:function(r){
				if(r.message){
					console.log("got doc filterszzzzzzzzzzzzzzzzzz")
					console.log(r.message)
					$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filter":['asd','qwe','zxcv']})))
					//$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
				}
			}

		})
	})

}
function datacall(doc){
	console.log("?///////// inside datacall")
	//filter_search()

	var subscription_data=''
	frappe.call({
		method:"gilton.gilton.page.dashboard.dashboard.get_data",
		args: {"doctype":doc},
		async: false,
		callback:function(r){
			if(r.message){
				console.log
				data=r.message
				subscription_data =r.message.record
				$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filters":r.message.filter})))
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"records":r.message})))
				//subscription_update(r.message)

			}
		}
	});
	subscription_update_generic(data)
	console.log("datacall resp",data.filter)
	filter_call(doc)
	return data
//filter_call(doc)
}
function get_data(doc,filters){
	console.log(filters)
	frappe.call({
		method:"gilton.gilton.page.dashboard.dashboard.get_data",
		args: {"doctype":doc,
						"filters":filters
						},
		callback:function(r){
			if(r.message){
				var subscription_data =r.message.record
				$('.main_page').html($(frappe.render_template('filters',{"doctype":doc,"filters":r.message.filter})))
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"records":r.message})))
				//subscription_update(r.message)
				subscription_update_generic(r.message)
				filter_call(doc)

}
}
});
}

function filter_call(doc){
	//alert("filter call")
	$("input[id='customer_name']").change(function(){
		filters=get_filters()
		get_data(doc,filters)
		})
	$("input[id='email_address']").change(function(){
		console.log("email filter is working outside the for loop")
		filters=get_filters()
		get_data(doc,filters)
	})
	$("input[id='mobile']").change(function(){
		console.log("mobile filter is working outside the for loop")
		filters=get_filters()
		get_data(doc,filters)
	})
}
function get_filters(){
		return filters={
		"customer_name": is_null($("input[id='customer_name']").val()) ? null : $("input[id='customer_name']").val(),
		"creation": is_null($("input[id='creation']").val()) ? null : $("input[id='creation']").val(),
		"email_address": is_null($("input[id='email_address']").val()) ? null : $("input[id='email_address']").val(),
		"mobile": is_null($("input[id='mobile").val()) ? null : $("input[id='mobile']").val()
		}
}


function subscription_update_generic(records){
	$.getScript("https://www.gstatic.com/charts/loader.js",function(){
		google.charts.load('current', {packages: ['bar','corechart']});
			google.charts.setOnLoadCallback(drawChart);
		// Subscription Bar chart
		function drawChart() {
			 // Party Status Pie Chart
			google.charts.setOnLoadCallback(function(){

				var data = google.visualization.arrayToDataTable([
					["Status","Count"],
					["Active",5],
					["InActive",1]
				]);
						var options = {
							title: 'Status',
							chartArea: {left:20,top:20,width:'100%',height:'75%'}
						};
						var chart = new google.visualization.PieChart(document.getElementById('status'));
						chart.draw(data, options);
			});
			};

	})
	const assets = [
		"/assets/gilton/datatable/clusterize.min.js",
		"/assets/gilton/datatable/Sortable.min.js",
		"/assets/gilton/datatable/frappe-datatable.min.js",
		"/assets/gilton/datatable/frappe-datatable.min.css",
	]
	frappe.require(assets, () => {
		var datatable = new DataTable('#datatable', {
			// columns: ['Lead Id','Lead Name','Comapny Name','Status',
			// 	'Address','State','Pincode','Country',
			// 	'Phone','Mobile No','Email id',
			// 	'Lead Owner','Source','Territory','Owner'],
			columns:records.columns,
			data: records.record
		 });
	})
}

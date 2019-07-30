frappe.pages['dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'DashBoard',
		single_column: true
	});
	$(frappe.render_template('sidebar')).appendTo(page.body);
	//$(frappe.render_template('menubar')).appendTo(page.body);

	//get_lead_details()
	get_sales_invoice_details()

	$('.subscription_activation_SI').click(function(){
		console.log("subscription_activation_SI called")
		frappe.call({
		method: "gilton.gilton.page.dashboard.dashboard.get_sales_invoice_details",
		async: false,
		callback: function(r){
			console.log(r.message)
			subscription_data = r.message
			console.log("rendering template to filters")
			$('.main_page').html($(frappe.render_template('filters_SI')))
			console.log("rendering template to dashboard")
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
			console.log("rendering template to filters")
			}
		});
		$('li.active').removeClass('active');
		//get_lead_details()
		get_sales_invoice_details()
		$(this).addClass('active');
	})
	$('.payment_receivable').click(function(){
		$('li.active').removeClass('active');
		get_opportunity_details()
		$(this).addClass('active');
	})
	$('.trusted_driver').click(function(){
		$('li.active').removeClass('active');
		// trusted_driver()
		$(this).addClass('active');
	})

}
function get_sales_invoice_details(){
	frappe.call({
		method:"gilton.gilton.page.dashboard.dashboard.get_sales_invoice_details",
		async:false,
		callback:function(r){
			subscription_data=r.message
			$('.main_page').html($(frappe.render_template('filters',{"doctype":'Sales Invoice'})))
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
		}
	});
	subscription_update()
	$("select[name='status']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("input[type='date'][name='from_date']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("input[type='date'][name='to_date']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})

	function get_filters() {
		return filters={
			"from_date": is_null($("input[type='date'][name='from_date']").val()) ? "" : $("input[type='date'][name='from_date']").val(),
			"to_date": is_null($("input[type='date'][name='to_date']").val()) ? "" : $("input[type='date'][name='to_date']").val(),
			"status": is_null($("select[name='status']").val()) ? "" : $("select[name='status']").val(),
		}
	}
	function fetch_data(filters){
		frappe.call({
			method: "gilton.gilton.page.dashboard.dashboard.get_sales_invoice_details",
			async: false,
			args: {"filters":filters},
			callback: function(r){
				subscription_data = r.message
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
			}
		})
		subscription_update()

	}
	function subscription_update(){
			$.getScript("https://www.gstatic.com/charts/loader.js",function(){
				google.charts.load('current', {packages: ['bar','corechart']});
			  	google.charts.setOnLoadCallback(drawChart);
				// Subscription Bar chart
				function drawChart() {
					 // Party Status Pie Chart
					google.charts.setOnLoadCallback(function(){
						var data = google.visualization.arrayToDataTable(subscription_data.status);
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
					columns: ['Lead Id','Lead Name','Comapny Name','Status',
						'Address','State','Pincode','Country',
						'Phone','Mobile No','Email id',
						'Lead Owner','Source','Territory','Owner'],
					data: subscription_data.subscription_table });
			})
		}

}
function get_lead_details(){
	frappe.call({
		method: "gilton.gilton.page.dashboard.dashboard.get_lead_details",
		async: false,
		callback: function(r){
			subscription_data = r.message
			$('.main_page').html($(frappe.render_template('filters',{"doctype":'Lead'})))
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
		}
	});
	subscription_update()

	$("select[name='lead_status']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("input[type='date'][name='from_date']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("input[type='date'][name='to_date']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})

	function get_filters() {
		return filters={
			"from_date": is_null($("input[type='date'][name='from_date']").val()) ? "" : $("input[type='date'][name='from_date']").val(),
			"to_date": is_null($("input[type='date'][name='to_date']").val()) ? "" : $("input[type='date'][name='to_date']").val(),
			"lead_status": is_null($("select[name='lead_status']").val()) ? "" : $("select[name='lead_status']").val(),
		}
	}

	function fetch_data(filters){
		frappe.call({
			method: "gilton.gilton.page.dashboard.dashboard.get_lead_details",
			async: false,
			args: {"filters":filters},
			callback: function(r){
				subscription_data = r.message
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"subscription_data":subscription_data})))
			}
		})
		subscription_update()

	}

function subscription_update(){
		$.getScript("https://www.gstatic.com/charts/loader.js",function(){
			google.charts.load('current', {packages: ['bar','corechart']});
		  	google.charts.setOnLoadCallback(drawChart);
			// Subscription Bar chart
			function drawChart() {
				 // Party Status Pie Chart
				google.charts.setOnLoadCallback(function(){
					var data = google.visualization.arrayToDataTable(subscription_data.status);
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
				columns: ['Lead Id','Lead Name','Comapny Name','Status',
					'Address','State','Pincode','Country',
					'Phone','Mobile No','Email id',
					'Lead Owner','Source','Territory','Owner'],
				data: subscription_data.subscription_table });
		})
	}
}

function get_opportunity_details(){
	frappe.call({
		method: "gilton.gilton.page.dashboard.dashboard.get_opportunity_details",
		async: false,
		callback: function(r){
			opportunity_data = r.message
			$('.main_page').html($(frappe.render_template('filters',{"doctype":'Opportunity'})))
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"opportunity_data":opportunity_data})))
		}
	});
	opportunity_update()

	$("select[name='opportunity_status']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("input[type='date'][name='from_date']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("input[type='date'][name='to_date']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})

	function get_filters() {
		return filters={
			"from_date": is_null($("input[type='date'][name='from_date']").val()) ? "" : $("input[type='date'][name='from_date']").val(),
			"to_date": is_null($("input[type='date'][name='to_date']").val()) ? "" : $("input[type='date'][name='to_date']").val(),
			"opportunity_status": is_null($("select[name='opportunity_status']").val()) ? "" : $("select[name='opportunity_status']").val(),
		}
	}

	function fetch_data(filters){
		frappe.call({
			method: "gilton.gilton.page.dashboard.dashboard.get_opportunity_details",
			async: false,
			args: {"filters":filters},
			callback: function(r){
				opportunity_data = r.message
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"opportunity_data":opportunity_data})))
			}
		})
		opportunity_update()

	}

	function opportunity_update(){
		$.getScript("https://www.gstatic.com/charts/loader.js",function(){
			google.charts.load('current', {packages: ['bar','corechart']});
		  	google.charts.setOnLoadCallback(drawChart);
			// Subscription Bar chart
			function drawChart() {
				 // Party Status Pie Chart
				google.charts.setOnLoadCallback(function(){
					var data = google.visualization.arrayToDataTable(opportunity_data.status);
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
				columns: ['Enquiry From','Opportunity Type','Lead','Status',
					'Customer Name','Mins To First Response','Customer Type','Contact By',
					'To Discuss','Contact Date','Reminder Date',
					'Customer Address','Contact Person','Territory','Contact Display',
					'Customer Group','Contact Email','Contact Mobile','Source','Company','City',
					'Transaction Date','Enquiry id','Name Of Competitor','Enquiry Category',
					'Expected Purchase Rate','Enquiry Closure Date','Sales Stage',
					'SIC Code Type','Channel','SIC Code','Reason For Enquiry Lost','Sales Partner',
					'Sales Won Reason','Item Code','Quantity','Item Name'],
				data: opportunity_data.opportunity_table });
		})
	}
}

frappe.pages['testdash'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'TestDash',
		single_column: true
	});



	$(frappe.render_template('sidebar')).appendTo(page.body);

	get_lead_details()

	$('.lead').click(function(){
		frappe.call({
		method: "gilton.gilton.page.testdash.testdash.get_lead_details",
		async: false,
		callback: function(r){
			lead_data = r.message
			$('.main_page').html($(frappe.render_template('filters',{"doctype":'Lead'})))
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"lead_data":lead_data})))
			}
		});
		$('li.active').removeClass('active');
		get_lead_details()
		$(this).addClass('active');
	})
	$('.opportunity').click(function(){
		$('li.active').removeClass('active');
		get_opportunity_details()
		$(this).addClass('active');
	})
	$('.quotation').click(function(){
		$('li.active').removeClass('active');
		get_quotation_details()
		$(this).addClass('active');
	})

}

function get_lead_details(){
	frappe.call({
		method: "gilton.gilton.page.testdash.testdash.get_lead_details",
		async: false,

		callback: function(r){
			lead_data = r.message
			$('.main_page').html($(frappe.render_template('filters',{"doctype":'Lead'})))
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"lead_data":lead_data})))
		}
	});
	lead_update()

	$("select[name='lead_status']").change(function(){
		console.log("lead_status called ")
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
	$("select[name='lead_id']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("select[name='company_name']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})

	function get_filters() {
		return filters={
			"from_date": is_null($("input[type='date'][name='from_date']").val()) ? "" : $("input[type='date'][name='from_date']").val(),
			"to_date": is_null($("input[type='date'][name='to_date']").val()) ? "" : $("input[type='date'][name='to_date']").val(),
			"lead_status": is_null($("select[name='lead_status']").val()) ? "" : $("select[name='lead_status']").val(),
			"lead_id": is_null($("select[name='lead_id']").val()) ? "" : $("select[name='lead_id']").val(),
			"company_name": is_null($("select[name='company_name']").val()) ? "" : $("select[name='company_name']").val(),
		}
	}

	function fetch_data(filters){
		frappe.call({
			method: "gilton.gilton.page.testdash.testdash.get_lead_details",
			async: false,
			args: {"filters":filters},
			callback: function(r){
				lead_data = r.message
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"lead_data":lead_data})))
			}
		})
		lead_update()
	}

function lead_update(){
		$.getScript("https://www.gstatic.com/charts/loader.js",function(){
			google.charts.load('current', {packages: ['bar','corechart']});
		  	google.charts.setOnLoadCallback(drawChart);
			// Subscription Bar chart
			function drawChart() {
				 // Party Status Pie Chart
				google.charts.setOnLoadCallback(function(){
					var data = google.visualization.arrayToDataTable(lead_data.status);
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
					'Lead Owner','Source','Territory','account_status',
					'verified_account_id','kv_rating','contact_date', 'contact_by',
					'market_segment','industry','lob','sic_code','sic_code_type'
					],
				data: lead_data.subscription_table });
		})
	}
}

function get_opportunity_details(){
	frappe.call({
		method: "gilton.gilton.page.testdash.testdash.get_lead_details",
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
	$("select[name='opportunity_name']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("select[name='customer_name']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})

	function get_filters() {
		return filters={
			"from_date": is_null($("input[type='date'][name='from_date']").val()) ? "" : $("input[type='date'][name='from_date']").val(),
			"to_date": is_null($("input[type='date'][name='to_date']").val()) ? "" : $("input[type='date'][name='to_date']").val(),
			"opportunity_status": is_null($("select[name='opportunity_status']").val()) ? "" : $("select[name='opportunity_status']").val(),
			"opportunity_name": is_null($("select[name='opportunity_name']").val()) ? "" : $("select[name='opportunity_name']").val(),
			"customer_name": is_null($("select[name='customer_name']").val()) ? "" : $("select[name='customer_name']").val(),
		}
	}

	function fetch_data(filters){
		frappe.call({
			method: "gilton.gilton.page.testdash.testdash.get_lead_details",
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
					console.log("???????????????")
					console.log(opportunity_data.status)
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
				columns: ['Name','Status',
					'Customer Name','Contact By',
					'Contact Date','Reminder Date',
					'Customer Address','Contact Person','Territory','Contact Display',
					'Contact Email','Contact Mobile','Source',
					'Enquiry id','Name Of Competitor','Enquiry Category',
					'Expected Purchase Rate','Enquiry Closure Date','Sales Stage',
					'SIC Code Type','Channel','SIC Code','Reason For Enquiry Lost','Sales Partner',
					'Sales Won Reason','Item Code','Quantity','Item Name'],
				data: opportunity_data.opportunity_table });
		})
	}
}

function get_quotation_details(){
	frappe.call({
		method: "gilton.gilton.page.testdash.testdash.get_quotation_details",
		async: false,
		callback: function(r){
			quotation_data = r.message
			$('.main_page').html($(frappe.render_template('filters',{"doctype":'Quotation', "quotation_data": quotation_data})))
			$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"quotation_data":quotation_data})))
		}
	});
	quotation_update()

	$("select[name='quotation_status']").change(function(){
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
	$("select[name='customer_name']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("select[name='item_name']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})
	$("select[name='quotation_name']").change(function(){
		filters = get_filters()
		fetch_data(filters)
	})

	function get_filters() {
		return filters={
			"from_date": is_null($("input[type='date'][name='from_date']").val()) ? "" : $("input[type='date'][name='from_date']").val(),
			"to_date": is_null($("input[type='date'][name='to_date']").val()) ? "" : $("input[type='date'][name='to_date']").val(),
			"quotation_status": is_null($("select[name='quotation_status']").val()) ? "" : $("select[name='quotation_status']").val(),
			"customer_name": is_null($("select[name='customer_name']").val()) ? "" : $("select[name='customer_name']").val(),
			"item_name": is_null($("select[name='item_name']").val()) ? "" : $("select[name='item_name']").val(),
			"quotation_name": is_null($("select[name='quotation_name']").val()) ? "" : $("select[name='quotation_name']").val(),
		}
	}

	function fetch_data(filters){
		frappe.call({
			method: "gilton.gilton.page.testdash.testdash.get_quotation_details",
			async: false,
			args: {"filters":filters},
			callback: function(r){
				quotation_data = r.message
				$('.subscription_activation_main').html($(frappe.render_template('dashboard',{"quotation_data":quotation_data})))
			}
		})
		quotation_update()

	}


	function quotation_update(){
		$.getScript("https://www.gstatic.com/charts/loader.js",function(){
			google.charts.load('current', {packages: ['bar','corechart']});
		  	google.charts.setOnLoadCallback(drawChart);
			// Subscription Bar chart
			function drawChart() {
				 // Party Status Pie Chart
				google.charts.setOnLoadCallback(function(){
					var data = google.visualization.arrayToDataTable(quotation_data.status);
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
				columns: ['Quotation No.','Quotation Date',
				'Quotation Status', 'Customer Name', 'Follow Up By','Follow Up Date',
				'Source','Expected Purchase Date','Item Code','Item Name','Quantity','Rate','Amount'],
				data: quotation_data.quotation_table });
		})
	}

}

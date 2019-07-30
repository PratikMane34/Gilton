
frappe.pages['demo'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Trying',
		single_column: true
	});
// 	var txt = <nav class="navbar navbar-inverse">
//   <div class="container-fluid">
//     <div class="navbar-header">
//       <a class="navbar-brand" href="#">WebSiteName</a>
//     </div>
//     <ul class="nav navbar-nav">
//       <li class="active"><a href="#">Home</a></li>
//       <li><a href="#">Page 1</a></li>
//       <li><a href="#">Page 2</a></li>
//       <li><a href="#">Page 3</a></li>
//     </ul>
//   </div>
// </nav>
	$(frappe.render_template('template')).appendTo(page.body);
	//page.main.html()
}

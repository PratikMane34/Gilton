console.log("HIIIIIIII")
frappe.ui.form.on('Salary Slip', {
	onload: function(frm) {
    frappe.msgprint("Hiii")
    // frappe.db.getAll({
    //   doctype:'Customer'
    // })
}
});

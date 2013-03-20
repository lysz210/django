$(document).ready(function() {
	$('.modifica-titolo').css("margin", "0");
	$('.modifica-titolo').change(function(){
		var input = $(this);
		$.ajax({
			url: "./"+ input.attr('name') +"/titolo/",
			data: "titolo="+input.attr('value'),
			type: "POST",
			complete: function(xmlHttpRequest, message){
				if (message == 'success') {
				input.css("border", "1px solid green");
				} else {
				input.css("border", "1px solid red");
				}
			},
		});
	});
});
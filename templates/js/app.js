$('#flashMessage').hide().slideDown(1000).delay(3000).slideUp();



$('#submit_button').click(function(){
	console.log('hello');

	const template_type = $('#template_type').val();

	$('#templateTypePreview').text(template_type);
});
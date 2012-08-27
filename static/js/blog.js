$(function(){
	
	$('#content').val($('#contentValue').val())

	$('.previewContent').click(function(){
		$.post('/mdtohtml', { data: $('#content').val() },
		  function(data){
		  	$('.modal-body').html(data.result);
		  	$('#markdownPreview').modal('show');
		  });
	});

	$('a.closeDialog').click(function(){
		$('#markdownPreview').modal('hide')
	});

})
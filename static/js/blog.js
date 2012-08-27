$(function(){
	
	$('#wmd-input').val($('#contentValue').val())

	(function(){
		var converter = new Markdown.Converter();
		var editor = new Markdown.Editor(converter);
		editor.run();
	})()

})
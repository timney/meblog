$(function(){
	
	/* This a fix for templating, puttting an if block in textarea adds unecassary white space */
	$('#wmd-input').val($('#contentValue').val());

	(function(){
		if($('#wmd-input').length  > 0){
			var converter = new Markdown.Converter();
			var editor = new Markdown.Editor(converter);
			editor.run();
		}
	})();

	(function(){
		$('pre').addClass('prettyprint');
		prettyPrint();
	})();


})
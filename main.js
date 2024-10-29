/* Код для замены подряд идущих пробелов любых видов на один пробел
*/

function replaceText(node)
{
  var current = node.nodeValue;
  var replaced = current.replace(/ +/, " ");
  node.nodeValue = replaced;
}
function traverse(node)
{
  var children = node.childNodes;
  var childLen = children.length;
  for(var i = 0; i < childLen; i++)
  {
    var child = children.item(i);
    if(child.nodeType == 3)//or if(child instanceof Text)
      replaceText(child);
    else
      traverse(child);
  }
}
function replaceAll()
{
  traverse(document.body);
}


window.onload = function(e){
	// replaceAll();
}


/* Код для выделения жирным объедененных колонок в таблицах. Чистый js но querySelectorAll() не работает в старых IE
window.onload = function(e){ 
	var td_colspans = document.querySelectorAll("[colspan]");
	for (var i = 0; i < td_colspans.length; i++) {
		td_colspans[i].setAttribute("style", "font-weight:bold; text-align:center;");
	}
    // console.log(td_colspans);
}


var jsTag;
jsTag = document.createElement('script');
jsTag.setAttribute('type', 'text/javascript');
jsTag.setAttribute('src', 'https://code.jquery.com/jquery-1.12.4.min.js');
document.getElementsByTagName('head')[0].appendChild(jsTag);
// Здесь можно выполнить код когда загрузится вставка
jsTag.onload = function() {
	$(document).ready(function() {
		$("td[colspan]").addClass("colspan");
	});
}
*/

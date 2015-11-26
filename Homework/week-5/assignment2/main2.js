/* use this to test out your function */
window.onload = function() {
 	changeColor('path6484','orange'); // Netherlands
 	changeColor('is','orange'); // Iceland
 	changeColor('path2924','orange'); // Russia
 	changeColor('ua','orange'); // Ukraine
}

/* changeColor takes a path ID and a color (hex value)
   and changes that path's fill color */
function changeColor(id, color) {
	document.getElementById(id).style.fill = color;        
}

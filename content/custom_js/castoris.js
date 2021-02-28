// script for email
var m;
m = 'r';
m+= 'aym';
m+= 'u';
m+= 'ndo.c';
m+= 'as';
m+= 'san';
m+= 'i@g';
m+= 'mai';
m+= 'l.c';
m+= 'om';
$x = document.getElementsByClassName("fas fa-envelope fa-lg")[0].parentNode;
$x.href = 'mailto:' + m;

function pdf_link(url) {
  var r = confirm("Proceed as human?");
  if (r == true) {
    window.open(url, '_blank');  // open in a new tab
    }
}

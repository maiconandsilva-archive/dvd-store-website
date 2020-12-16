var alertElementReference = document.getElementById('cookie-alert');
var cookieAlreadyAccepted = localStorage.getItem('cookie-permition');
var tabs = document.getElementById('tabs')

if (alertElementReference !== null) {
    if (localStorage.getItem('cookie-permition') === null) {
        alertElementReference.classList.remove("hidden")
    } else {
        alertElementReference.classList.add("hidden")
    }
}

if (alertElementReference)
alertElementReference.onclick = function saveInCook() {
    return localStorage.setItem('cookie-permition', 1);
}


if (tabs)
tabs.onclick = function (e) {
    e=window.event? event.srcElement: e.target
    if(e.className && e.className.indexOf('linktab')!=-1) {
        openLink(e.getAttribute("for"))
    }
 }
 
function openLink(tab) {
    var el = document.getElementsByClassName("tab");
    for (var i = 0; i < el.length; i++) {
      el[i].style.display = "none";
    }
    document.getElementById(tab).style.display = "block";
}
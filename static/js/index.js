var alertElementReference = document.getElementById('alert');

var cookieAlreadyAccepted = localStorage.getItem('cookie-permition');


localStorage.getItem('cookie-permition') === null?  alertElementReference.classList.remove("hidden") : alertElementReference.classList.add("hidden")

function saveInCook() {
    return localStorage.setItem('cookie-permition', 1);
}
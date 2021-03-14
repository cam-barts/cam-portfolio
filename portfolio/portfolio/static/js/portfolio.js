const observer = lozad('.lazy');
observer.observe();

var neon = document.querySelectorAll('.left, .right')

function setProperty(element, duration) {
    element.style.setProperty('--animation-time', duration + 's');
}

function changeAnimationTime() {
    for (i = 0; i < neon.length; i++) {
        var animationDuration = Math.random() * 10;
        setProperty(neon[i], animationDuration);
    }
}

setInterval(changeAnimationTime, 1000);

var x = document.getElementById("snackbar");
x.className = "show";
setTimeout(function() { x.className = x.className.replace("show", ""); }, 2900);
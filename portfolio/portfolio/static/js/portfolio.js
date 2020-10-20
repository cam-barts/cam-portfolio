const observer = lozad('.lazy');
observer.observe();

/* init Jarallax */
jarallax(document.querySelectorAll(".jarallax"));

jarallax(document.querySelectorAll(".jarallax-keep-img"), {
    keepImg: true,
});
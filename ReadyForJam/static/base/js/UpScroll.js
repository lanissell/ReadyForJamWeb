document.addEventListener('DOMContentLoaded', function () {
    const goTopBtn = document.querySelector(".go-top");

    window.addEventListener("scroll", trackScroll);
    goTopBtn.addEventListener("click", goTop);

    function trackScroll() {
        const scrolled = window.pageYOffset;
        const coords = document.documentElement.clientHeight;
        if (scrolled > coords/1.2) {
            goTopBtn.classList.add("go-top--show");
        } else {
            goTopBtn.classList.remove("go-top--show");
        }
    }

    function goTop() {
        if (window.pageYOffset > 0) {
            window.scrollBy(0, -75);
            setTimeout(goTop, 0);
        }
    }
})
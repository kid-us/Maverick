// Swiper
var swiper;
swiper = new Swiper(".swiper", {
    breakpoints: {
        "@0.00": {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        "@0.75": {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        "@1.00": {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        "@1.50": {
            slidesPerView: 3,
            spaceBetween: 15,
        },
    },


    pagination: {
        el: ".swiper-pagination",
        type: "bullets",
        clickable: true,
    },
});
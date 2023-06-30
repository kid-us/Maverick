// Sticky navbar 
window.onscroll = function () { myFunction() };

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
}

// Small device navbar 
const menuBtn = document.getElementById("menu-btn");
if (menuBtn) {

    const menuPage = document.getElementById("menu-page");
    const closeMenuBtn = document.getElementById("close-menu");

    menuBtn.addEventListener("click", () => {
        if (menuPage.classList.contains("hidden")) {
            menuPage.classList.remove("hidden");
        } else {
            menuPage.classList.add("hidden");
        }
    });

    closeMenuBtn.addEventListener("click", () => {
        menuPage.classList.add("hidden");
    });

}

// Header
const openHeader = document.getElementById("open-header");
if (openHeader) {
    const headerModalPage = document.getElementById("header-modal-page");

    const closeHeader = document.getElementById("close-header");
    openHeader.addEventListener("click", () => {
        headerModalPage.classList.remove("hidden");
    });

    closeHeader.addEventListener("click", () => {
        headerModalPage.classList.add("hidden");
    });
}

// Dashboard username Link script
const usernameLink = document.getElementById("username-link");
const dashboardLinksPage = document.getElementById("dashboard-links");
const iconLink = document.getElementById("icon-link");
usernameLink.addEventListener("click", () => {
    if (dashboardLinksPage.classList.contains('hidden')) {
        dashboardLinksPage.classList.remove("hidden");
        iconLink.classList.remove("bi-caret-down-fill");
        iconLink.classList.add("bi-caret-up-fill");
    } else {
        dashboardLinksPage.classList.add("hidden");
        iconLink.classList.remove("bi-caret-up-fill");
        iconLink.classList.add("bi-caret-down-fill");
    }
});


//
const balance = document.getElementById("balance");
if (balance) {
    const withdrawBtn = document.getElementById("withdraw-btn");
    const errorMessage = document.getElementById("error-msg");
    if (balance.textContent < 1) {
        withdrawBtn.addEventListener("mouseenter", () => {
            withdrawBtn.setAttribute("disabled", true)
            errorMessage.classList.remove("hidden");
        })
    }
}

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
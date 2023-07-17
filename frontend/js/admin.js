const sidebarBtn = document.getElementById("sm-menu-bar");
const xsSidebarBtn = document.getElementById("sm-menu-bar-sm");
const sidebarPage = document.getElementById("small-sidebar");
const sidebarClose = document.getElementById("sidebar-close");
const sidebarOverlay = document.getElementById("sidebar-overlay");

sidebarBtn.addEventListener("click", () => {
    if (sidebarPage.classList.contains("hidden")) {
        sidebarPage.classList.remove("hidden");
        sidebarOverlay.classList.remove("hidden");
    }
})
sidebarClose.addEventListener("click", () => {
    sidebarPage.classList.add("hidden");
    sidebarOverlay.classList.add("hidden");
})

sidebarOverlay.addEventListener("click", function () {
    sidebarPage.classList.add("hidden");
    sidebarOverlay.classList.add("hidden");
})

const changeLink = document.getElementById("changeLink");
const passPage = document.getElementById("password-page");

if (changeLink) {
    changeLink.addEventListener("click", function () {
        if (passPage.classList.contains("hidden")) {
            passPage.classList.remove("hidden");
        } else {
            passPage.classList.add("hidden");
        }
    });
}

Notification
const notificationLink = document.getElementById("notification-link");
const notificationContainer = document.getElementById("notification-container");
if (notificationLink) {
    notificationLink.addEventListener("click", () => {
        if (notificationContainer.classList.contains("hidden")) {
            notificationContainer.classList.remove("hidden");
        } else {
            notificationContainer.classList.add("hidden");
        }
    })
}


// Large device Account dropdown
// const adminLink = document.getElementById("admin-link");
// if (adminLink) {
//     const accountDropdown = document.getElementById("admin-dropdown");
//     const caretIcon = document.getElementById("caret");
//     adminLink.addEventListener("click", () => {
//         if (accountDropdown.classList.contains("hidden")) {
//             accountDropdown.classList.remove("hidden");
//             caretIcon.classList.remove("bi-caret-down-fill")
//             caretIcon.classList.add("bi-caret-up-fill")
//         } else {
//             accountDropdown.classList.add("hidden");
//             caretIcon.classList.remove("bi-caret-up-fill")
//             caretIcon.classList.add("bi-caret-down-fill")
//         }
//     })
// }

// Small device dropdown 
// const mdAccountsLink = document.getElementById("md-accounts-link");
// if (mdAccountsLink) {
//     const mdAccountDropdown = document.getElementById("md-account-dropdown");
//     const mdCaretIcon = document.getElementById("md-caret");

//     mdAccountsLink.addEventListener("click", () => {
//         if (mdAccountDropdown.classList.contains("hidden")) {
//             mdAccountDropdown.classList.remove("hidden");
//             mdCaretIcon.classList.remove("bi-caret-down-fill")
//             mdCaretIcon.classList.add("bi-caret-up-fill")
//         } else {
//             mdAccountDropdown.classList.add("hidden");
//             mdCaretIcon.classList.remove("bi-caret-up-fill")
//             mdCaretIcon.classList.add("bi-caret-down-fill")
//         }
//     })
// }

// Small device dropdown 
// const smAccountsLink = document.getElementById("sm-accounts-link");
// if (smAccountsLink) {
//     const smAccountDropdown = document.getElementById("sm-account-dropdown");
//     const smCaretIcon = document.getElementById("sm-caret");

//     smAccountsLink.addEventListener("click", () => {
//         if (smAccountDropdown.classList.contains("hidden")) {
//             smAccountDropdown.classList.remove("hidden");
//             smCaretIcon.classList.remove("bi-caret-down-fill")
//             smCaretIcon.classList.add("bi-caret-up-fill")
//         } else {
//             smAccountDropdown.classList.add("hidden");
//             smCaretIcon.classList.remove("bi-caret-up-fill")
//             smCaretIcon.classList.add("bi-caret-down-fill")
//         }
//     })
// }

// Search accounts 
// let searchKey = document.getElementById("searchInput");
// if (searchKey) {
//     searchKey.addEventListener("keyup", function () {
//         let filter = searchKey.value.toUpperCase();
//         let tr = document.getElementsByTagName("tr");
//         for (let i = 0; i < tr.length; i++) {
//             let td = tr[i].getElementsByTagName("td");
//             let text = "";
//             for (let j = 0; j < td.length; j++) {
//                 text += td[j].textContent.toUpperCase();
//             }
//             if (text.indexOf(filter) > -1) {
//                 tr[i].style.display = "";
//             } else {
//                 tr[i].style.display = "none";
//             }
//         }
//     });
// }

// small device search account
// let smSearchKey = document.getElementById("searchSmInput");
// if (smSearchKey) {
//     smSearchKey.addEventListener("keyup", function () {
//         let filter = smSearchKey.value.toUpperCase();
//         let tr = document.getElementsByTagName("tr");
//         for (let i = 0; i < tr.length; i++) {
//             let td = tr[i].getElementsByTagName("td");
//             let text = "";
//             for (let j = 0; j < td.length; j++) {
//                 text += td[j].textContent.toUpperCase();
//             }
//             if (text.indexOf(filter) > -1) {
//                 tr[i].style.display = "";
//             } else {
//                 tr[i].style.display = "none";
//             }
//         }
//     });
// }

// let searchKey = document.getElementById("searchInput");
// searchKey.addEventListener("keyup", function () {
//     // input = document.getElementById("myInput");
//     let filter = searchKey.value.toUpperCase();
//     let container = document.getElementById("updateContainer");
//     let form = container.getElementsByTagName("form");
//     for (let i = 0; i < form.length; i++) {
//         let searchPlace = form[i].getElementsByTagName("input")[1];
//         let searchKey = searchPlace.value;
//         if (searchKey.toUpperCase().indexOf(filter) > -1) {
//             form[i].style.display = "";
//         } else {
//             form[i].style.display = "none";
//         }
//     }
// });


let editBtn = document.querySelectorAll(".edit-btn");
editBtn.forEach(function (edit) {
    edit.addEventListener("click", function () {
        let num = edit.getAttribute("data-num");
        let fieldset = document.querySelectorAll(".fieldset" + num);
        edit.classList.add("hidden");
        fieldset.forEach(function (f) {
            f.removeAttribute("disabled");
        });

        let cancel = document.querySelectorAll(".discard-btn" + num);
        let submit = document.querySelectorAll(".update-btn" + num);

        cancel.forEach(function (d) {
            d.classList.remove("hidden");
        });
        submit.forEach(function (s) {
            s.classList.remove("hidden");
        });
    });
});

let cancelBtn = document.querySelectorAll(".discard");
cancelBtn.forEach(function (close) {
    close.addEventListener("click", function () {
        close.classList.add('hidden');
        let num = close.getAttribute("data-num");
        let fieldset = document.querySelectorAll(".fieldset" + num);
        fieldset.forEach(function (f) {
            f.setAttribute("disabled", true);
        });

        let del = document.querySelectorAll(".delete-btn" + num);
        let update = document.querySelectorAll(".update-btn" + num);
        del.forEach(function (d) {
            d.classList.remove("hidden");
        });

        update.forEach(function (s) {
            s.classList.add("hidden");
        });

        let edit = document.querySelectorAll(".edit-btn");
        edit.forEach(function (e) {
            e.classList.remove("hidden");
        });
    });
});

let deleteBtn = document.querySelectorAll(".delete-tournament");
deleteBtn.forEach(function (del) {
    del.addEventListener("click", function () {
        let num = del.getAttribute("data-num");
        let fieldset = document.querySelectorAll(".fieldset" + num);
        fieldset.forEach(function (f) {
            f.removeAttribute("disabled");
        });
    });
});
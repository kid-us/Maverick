const showPasswordBtn = document.getElementById("password-eye");
const passwordInput = document.getElementById("password");
showPasswordBtn.addEventListener("click", () => {
    // console.log("clicked");
    if (showPasswordBtn.classList.contains("bi-eye-slash-fill")) {
        showPasswordBtn.classList.remove("bi-eye-slash-fill");
        showPasswordBtn.classList.add("bi-eye-fill");
        passwordInput.setAttribute("type", "text");
    } else {
        showPasswordBtn.classList.remove("bi-eye-fill");
        showPasswordBtn.classList.add("bi-eye-slash-fill");
        passwordInput.setAttribute("type", "password");
    }
});

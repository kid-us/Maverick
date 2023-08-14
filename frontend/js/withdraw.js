// Withdraw
const balance = parseInt(document.getElementById("balance").textContent);
const withdrawThrough = document.getElementById("withdraw-type");
if (balance > 0) {
    document.getElementById("error-msg").classList.add("hidden");
    withdrawThrough.addEventListener("change", () => {
        if (withdrawThrough.value === "tele") {
            document.getElementById("phone").classList.remove("hidden")
            document.getElementById("account-number").classList.add("hidden")
        } else {
            document.getElementById("phone").classList.add("hidden")
            document.getElementById("account-number").classList.remove("hidden")
        }
    });
} else {
    document.getElementById("withdraw-form").classList.add("hidden");
}

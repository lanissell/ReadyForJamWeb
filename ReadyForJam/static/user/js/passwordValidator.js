document.addEventListener("DOMContentLoaded", function () {

    const errorColor = "#ff6363"
    const successColor = "#1f9127"

    //errors text
    const passwordSizeError = document.querySelector("#password_size")
    const passwordNumError = document.querySelector("#password_num")
    const passwordRepeatError = document.querySelector("#password_repeat")

    //fields
    const passwordField = document.querySelector("#id_password1")
    const passwordRepeatField = document.querySelector("#id_password2")

    const btn = document.querySelector("#register_btn")

    passwordSizeError.style.color = errorColor
    passwordNumError.style.color = errorColor
    passwordRepeatError.style.color = errorColor

    DeactivateRegistrationBtn()

    passwordField.addEventListener("input", function () {
        ShowRegisterBtn()
    })
    passwordRepeatField.addEventListener("input", function () {
        ShowRegisterBtn()
    })

    function ShowRegisterBtn() {
        if ((PasswordSizeValid() & PasswordNumValid()) && PasswordRepeatValid()) {
            btn.type = "submit"
            btn.style.background = errorColor;
            btn.style.color = "rgb(255,255,255)";
        } else {
           DeactivateRegistrationBtn()
        }
    }
    function DeactivateRegistrationBtn() {
        btn.type = "button"
        btn.style.background = "rgba(0,0,0,0)";
        btn.style.color = "rgba(0,0,0,0.5)";
    }
    function PasswordSizeValid() {
        if (passwordField.value.length >= 8) {
            passwordSizeError.style.color = successColor
            return true
        } else {
            passwordSizeError.style.color = errorColor
            return false
        }
    }

    function PasswordNumValid() {
        let value = passwordField.value.replace(/[^0-9, ]/g, "")
        if (value.length > 0) {
            passwordNumError.style.color = successColor
            return true
        } else {
            passwordNumError.style.color = errorColor
            return false
        }
    }

    function PasswordRepeatValid() {
        if (passwordField.value === passwordRepeatField.value) {
            passwordRepeatError.style.color = successColor
            return true
        } else {
            passwordRepeatError.style.color = errorColor
            return false
        }
    }
})
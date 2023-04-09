document.addEventListener("DOMContentLoaded", function () {
    let lastFromIndex = 0

    const button = document.querySelector("#criteria_add_btn")
    button.addEventListener("click", AddForm)

    function AddForm() {
        const lastForm = document.querySelector(
            GetFormId(lastFromIndex));
        const newForm = lastForm.cloneNode(true);
        newForm.id = newForm.id.replaceAll(lastFromIndex, lastFromIndex + 1)
        newForm.name = newForm.name.replaceAll(lastFromIndex, lastFromIndex + 1)
        lastForm.parentNode.insertBefore(newForm, lastForm)
        lastFromIndex++
    }

    function GetFormId(index) {
        return "#id_form-" + index + "-name";
    }
});
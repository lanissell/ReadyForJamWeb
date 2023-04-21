document.addEventListener("DOMContentLoaded", function () {

    const maxCriteriaCount = 5
    let lastFromIndex = 0

    const addButton = document.querySelector("#criteria_add_btn")
    addButton.addEventListener("click", AddForm)

    function AddForm() {
        if (lastFromIndex === maxCriteriaCount) return
        let lastForm = document.querySelector(
            GetFormId(lastFromIndex))
        console.log(lastForm)
        let newForm = lastForm.cloneNode(true);
        newForm.id = newForm.id.replaceAll(lastFromIndex, lastFromIndex + 1)
        newForm.name = newForm.name.replaceAll(lastFromIndex, lastFromIndex + 1)
        InsertAfter(lastForm, newForm)
        lastFromIndex++
    }

    const removeButton = document.querySelector("#criteria_remove_btn")
    removeButton.addEventListener("click", RemoveForm)

    function RemoveForm()
    {
        if (lastFromIndex === 0) return
        let lastForm = document.querySelector(
            GetFormId(lastFromIndex))
        lastForm.remove()
        lastFromIndex--
    }

    function GetFormId(index) {
        return "#id_form-" + index + "-name"
    }

    function InsertAfter(referenceNode, newNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling)
}
});
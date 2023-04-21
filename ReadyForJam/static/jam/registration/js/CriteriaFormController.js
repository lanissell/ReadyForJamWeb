document.addEventListener("DOMContentLoaded", function () {

    const maxCriteriaCount = 5
    let lastFromIndex = 0

    const addButton = document.querySelector("#criteria_add_btn")
    addButton.addEventListener("click", AddForm)

    function AddForm() {
        if (lastFromIndex === maxCriteriaCount) return
        let lastForm = document.querySelector(
            GetFormId(lastFromIndex)).parentElement
        let newForm = lastForm.cloneNode(true);
        let child = newForm.children[0]
        child.id = child.id.replaceAll(lastFromIndex, lastFromIndex + 1)
        child.name = child.name.replaceAll(lastFromIndex, lastFromIndex + 1)
        InsertAfter(lastForm, newForm)
        lastFromIndex++
    }

    const removeButton = document.querySelector("#criteria_remove_btn")
    removeButton.addEventListener("click", RemoveForm)

    function RemoveForm()
    {
        if (lastFromIndex === 0) return
        let lastForm = document.querySelector(
            GetFormId(lastFromIndex)).parentElement
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
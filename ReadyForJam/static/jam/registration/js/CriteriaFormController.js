document.addEventListener("DOMContentLoaded", function () {

    const maxCriteriaCount = 5

    const addButton = document.querySelector("#criteria_add_btn")
    addButton.addEventListener("click", AddForm)

    const removeButton = document.querySelector("#criteria_remove_btn")
    removeButton.addEventListener("click", RemoveForm)

    const totalFormCounter = document.querySelector("#id_form-TOTAL_FORMS")
    let lastFromIndex = totalFormCounter.value - 1

    function AddForm() {
        if (lastFromIndex === maxCriteriaCount) return
        let formPattern = document.querySelector(GetFormId(lastFromIndex)).parentElement
        let newForm = formPattern.cloneNode(true);
        for (let child of newForm.children){
            child.id = child.id.replaceAll(lastFromIndex, lastFromIndex + 1)
            child.name = child.name.replaceAll(lastFromIndex, lastFromIndex + 1)
            child.value = ""
        }
        formPattern.parentElement.appendChild(newForm)
        lastFromIndex++
        totalFormCounter.value++
    }

    function RemoveForm()
    {
        if (lastFromIndex === 0) return
        let lastForm = document.querySelector(
            GetFormId(lastFromIndex)).parentElement
        lastForm.remove()
        lastFromIndex--
        totalFormCounter.value--
    }

    function GetFormId(index) {
        return "#id_form-" + index + "-name"
    }

});
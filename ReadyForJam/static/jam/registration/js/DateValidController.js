document.addEventListener("DOMContentLoaded", function () {
    const dateStart = document.querySelector("#id_startDate")
    const votingStartDate = document.querySelector("#id_votingStartDate")
    const votingEndDate = document.querySelector("#id_votingEndDate")

    const votingStartDateParent = votingStartDate.parentElement
    const votingEndDateParent = votingEndDate.parentElement

    dateStart.addEventListener("change", function () {
        votingStartDateParent.style.visibility = "visible"
        votingStartDate.setAttribute("min", dateStart.value)
    })
    votingStartDate.addEventListener("change", function () {
        votingEndDateParent.style.visibility = "visible"
        votingEndDate.setAttribute("min", votingStartDate.value)
    })

    if (dateStart.value === "") {
        votingStartDateParent.style.visibility = "hidden"
        votingEndDateParent.style.visibility = "hidden"
    }else {
        votingStartDate.setAttribute("min", dateStart.value)
        votingEndDate.setAttribute("min", votingStartDate.value)
    }


})


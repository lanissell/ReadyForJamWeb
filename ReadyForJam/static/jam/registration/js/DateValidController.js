document.addEventListener("DOMContentLoaded", function (){
    const dateStart = document.querySelector("#id_startDate")
    const votingStartDate = document.querySelector("#id_votingStartDate")
    const votingEndDate = document.querySelector("#id_votingEndDate")

    const votingStartDateParent = votingStartDate.parentElement
    votingStartDateParent.style.visibility = "hidden"

    const votingEndDateParent = votingEndDate.parentElement
    votingEndDateParent.style.visibility = "hidden"

    dateStart.addEventListener("change", function (){
        votingStartDateParent.style.visibility = "visible"
        votingStartDate.setAttribute("min", dateStart.value)
    })
    votingStartDate.addEventListener("change", function (){
        votingEndDateParent.style.visibility = "visible"
        votingEndDate.setAttribute("min", dateStart.value)
    })

})


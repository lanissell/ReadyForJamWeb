document.addEventListener("DOMContentLoaded", function () {
    const dateStart = document.querySelector("#id_startDate")
    const votingStartDate = document.querySelector("#id_votingStartDate")
    const votingEndDate = document.querySelector("#id_votingEndDate")

    dateStart.addEventListener("change", function () {
        votingStartDate.removeAttribute('disabled')
        votingStartDate.setAttribute("min", dateStart.value)
    })
    votingStartDate.addEventListener("change", function () {
        votingEndDate.removeAttribute('disabled')
        votingEndDate.setAttribute("min", votingStartDate.value)
    })

    if (dateStart.value === "") {
        votingStartDate.setAttribute('disabled', 'disabled')
        votingEndDate.setAttribute('disabled', 'disabled')
    }else {
        votingStartDate.setAttribute("min", dateStart.value)
        votingEndDate.setAttribute("min", votingStartDate.value)
    }


})


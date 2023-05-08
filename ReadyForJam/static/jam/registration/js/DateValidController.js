document.addEventListener("DOMContentLoaded", function () {
    const dateStart = document.querySelector("#id_start_date")
    const votingStartDate = document.querySelector("#id_voting_start_date")
    const votingEndDate = document.querySelector("#id_voting_end_date")

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


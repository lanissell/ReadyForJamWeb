let iframe

document.addEventListener("DOMContentLoaded", function () {
                        const input = document.querySelector("#formColor")
                        input.addEventListener("change", function () {
                            GetIFrame().contentDocument.body.style.backgroundColor = input.value
                        })
                    })

function GetIFrame(){
    if (iframe == null){
        iframe = document.querySelector("#cke_1_contents").childNodes[1]
    }
    return iframe
}

let inputFormColor;
let inputTextColor;

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('#deleting_form').remove();

    inputFormColor = document.querySelector("#formColor")
    inputTextColor = document.querySelector("#id_main_text_color")


    SetColorToContent();
    inputFormColor.addEventListener("change", function () {
        SetColorToContent();
    })
    inputTextColor.addEventListener("change", function () {
        SetColorToContent();
    })
})

function SetColorToContent(){
    RemoveContentStyle();
    const style = document.createElement('style');
    style.id = '#content-style';
    style.innerHTML = `
    .content-color {
        background-color: ${inputFormColor.value};
        color: ${inputTextColor.value};
    }`
    document.head.appendChild(style);
}

function RemoveContentStyle(){
    let style = document.querySelector('#content-style');
    if (style) style.remove();
}
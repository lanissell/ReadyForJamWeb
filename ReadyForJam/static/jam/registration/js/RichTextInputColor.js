let iframe

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('#deleting_form').remove();

    const input = document.querySelector("#formColor")
    const contentBlock = document.querySelector(".ck-editor__main").children[0];


    SetColorToContent(input.value);
    input.addEventListener("change", function () {
        SetColorToContent(input.value);
    })


})

function SetColorToContent(color){
    RemoveContentStyle();
    const style = document.createElement('style');
    style.id = '#content-style';
    style.innerHTML = `
    .content-color {
        background-color: ${color};
    }`
    document.head.appendChild(style);
}

function RemoveContentStyle(){
    let style = document.querySelector('#content-style');
    if (style) style.remove();
}
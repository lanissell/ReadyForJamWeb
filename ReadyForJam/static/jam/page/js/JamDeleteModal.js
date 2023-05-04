let modal = document.querySelector('.modal');
let parent = modal.parentElement;

modal.querySelector('.modal-no-btn').addEventListener('click', DeactivateModal);
modal.querySelector('.modal-yes-btn').addEventListener('click', function (){
    window.location = window.location.pathname + 'delete/';
})

DeactivateModal();
AddEventToActivateModalBtn();

function ActivateModal() {
    parent.append(modal);
}

function DeactivateModal() {
    modal.remove();
}

function AddEventToActivateModalBtn() {
    const activateModalBtn = document.querySelector('#delete_button');
    if (activateModalBtn === null)
        setTimeout(AddEventToActivateModalBtn, 100);
    else
        activateModalBtn.addEventListener('click', function () {
            ActivateModal();
        })
}

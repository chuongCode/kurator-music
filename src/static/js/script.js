let content = document.querySelector('#content');
let searchForm = document.querySelector('#search-form');
let addButton = document.querySelector('#add-button');
let addPopup = document.querySelector('#add-popup');
let closeAddPopupButton = document.querySelector('#close-add-popup');
// Edit button and popup
let editButtons = document.querySelectorAll('.edit-button');
let editPopup = document.querySelector('#edit-popup');
let closeEditPopupButton = document.querySelector('#close-edit-popup');

addButton.addEventListener('click', function(event) {
    event.preventDefault();
    addPopup.classList.add('popup-visible');
    content.classList.add('blur');
});

closeAddPopupButton.addEventListener('click', function(event) {
    event.preventDefault();
    addPopup.classList.remove('popup-visible');
    content.classList.remove('blur');
});

// Edit button event listeners
editButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        editPopup.classList.add('popup-visible');
        console.log('edit button clicked');
        content.classList.add('blur');
    });
});

closeEditPopupButton.addEventListener('click', function(event) {
    event.preventDefault();
    editPopup.classList.remove('popup-visible');
    content.classList.remove('blur');
});

editButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        let result = button.parentElement.parentElement;
        let song = result.querySelector('.song-name').textContent;
        let artist = result.querySelector('.artist').textContent;
        let album = result.querySelector('.album').textContent;
        let file = result.querySelector('.file-name').textContent;

        document.getElementById('edit-song').value = song;
        document.getElementById('edit-artist').value = artist;
        document.getElementById('edit-album').value = album;
        document.getElementById('edit-file').value = file;
    });
});
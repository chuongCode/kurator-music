let content = document.querySelector('#content');
let searchForm = document.querySelector('#search-form');
let addButton = document.querySelector('#add-button');
let addPopup = document.querySelector('#add-popup');
let closeAddPopupButton = document.querySelector('#close-add-popup');
// Edit button and popup
let editButton = document.querySelector('#edit-button');
let editButtons = document.querySelectorAll('.edit-button');
let editPopup = document.querySelector('#edit-popup');
let closeEditPopupButton = document.querySelector('#close-edit-popup');

searchForm.addEventListener('submit', function(event) {
    // prevent the default form submission
    event.preventDefault();

    // get the search query
    let searchQuery = document.querySelector('#search-query').value;

    // validate the search query
    if (!searchQuery.trim()) {
        alert('Please enter a search query.');
        return;
    }

    // make an AJAX request to the search API
    fetch(`/api/search?query=${encodeURIComponent(searchQuery)}`)
        .then(response => response.json())
        .then(results => {
            // handle the search results
            let resultsArea = document.querySelector('#results-area');
            resultsArea.innerHTML = ''; // clear the current results
            results.forEach(result => {
                let resultElement = document.querySelector('#result-template').content.cloneNode(true);
                resultElement.querySelector('.song-name').textContent = result.songName;
                resultElement.querySelector('.artist').textContent = result.artist;
                resultElement.querySelector('.album').textContent = result.album;
                resultElement.querySelector('.file-name').textContent = result.fileName;
                resultsArea.appendChild(resultElement);
            });
        });
});

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
editButton.addEventListener('click', function(event) {
    event.preventDefault();
    editPopup.classList.add('popup-visible');
    content.classList.add('blur');
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

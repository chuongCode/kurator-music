let content = document.querySelector('#content');
let searchForm = document.querySelector('#search-form');
let addButton = document.querySelector('#add-button');
let popup = document.querySelector('#popup');
let closePopupButton = document.querySelector('#close-popup');

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
    popup.classList.add('popup-visible');
    content.classList.add('blur');
});

closePopupButton.addEventListener('click', function(event) {
    event.preventDefault();
    popup.classList.remove('popup-visible');
    content.classList.remove('blur');
});
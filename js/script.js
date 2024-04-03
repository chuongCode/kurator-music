let searchForm = document.querySelector('#search-form');

searchForm.addEventListener('submit', function(event) {
    // prevent the default form submission
    event.preventDefault();

    // get the search query
    let searchQuery = document.querySelector('#search-query').value;

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
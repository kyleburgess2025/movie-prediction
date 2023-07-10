// ==UserScript==
// @name         LetterboxdScraper
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Predict what movies a user will like based on Letterboxd profile
// @author       Kyle Burgess
// @match        https://letterboxd.com/*/films/
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    addButton("see recommended movie", helper);

    function helper() {
        const username = document.querySelector("body").getAttribute("data-owner");
        const allMoviesWatched = document.querySelectorAll(".poster-container");
        let reviewedMovies = {};
        for (let i = 0; i < allMoviesWatched.length; i++) {
            const movieRating = allMoviesWatched[i].querySelector("p").querySelector(".rating")?.className;
            if (movieRating) {
                const rating = movieRating.match(/(\d+)/)[0]/10;
                const name = allMoviesWatched[i].querySelector("div").getAttribute('data-film-name')
                console.log(name);
                reviewedMovies[name] = rating
            }
        }
        console.log(reviewedMovies);
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:3000/predict", true);
        xhr.send(JSON.stringify(reviewedMovies));
        xhr.onreadystatechange = function() {addResults(JSON.parse(this.responseText))};
        return reviewedMovies;
    }

    function addButton(text, onclick, cssObj) {
        cssObj = cssObj || {position: 'absolute', bottom: '7%', left:'4%', 'z-index': 3}
        let button = document.createElement('button'), btnStyle = button.style
        button.className = "childButton"
        document.body.appendChild(button)
        button.innerHTML = text
        button.onclick = onclick
        btnStyle.position = 'absolute'
        Object.keys(cssObj).forEach(key => btnStyle[key] = cssObj[key])
        return button
    }


    function addResults(text_arr, cssObj) {
        cssObj = {position: 'absolute', bottom: '7%', left:'4%', 'z-index': 3, "background-color": 'white', "color": 'black'}
        let div = document.createElement('div'), divStyle = div.style
        div.className = "results"
        document.body.appendChild(div)
        Object.keys(cssObj).forEach(key => divStyle[key] = cssObj[key])
        let button = document.querySelector(".childButton")
        button.style.display = "none"
        for (let i = 0; i < text_arr.length; i++) {
            let current = document.createElement('p')
            document.querySelector(".results").appendChild(current)
            current.innerHTML = text_arr[i]
        }
        return div
    }

})();

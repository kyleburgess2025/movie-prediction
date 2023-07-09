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
        const allMoviesWatched = document.querySelectorAll(".poster-container");
        let reviewedMovieObjs = [];
        for (let i = 0; i < allMoviesWatched.length; i++) {
            const movieRating = allMoviesWatched[i].querySelector("p").querySelector(".rating")?.className;
            if (movieRating) {
                const rating = movieRating.match(/(\d+)/)[0];
                const name = allMoviesWatched[i].querySelector("div").getAttribute("data-film-link")?.replace("/film", "").replaceAll("/", "");
                console.log(`${name}: ${rating}`);
                reviewedMovieObjs.push({"rating": rating, "name": name});
            }
        }
        console.log(reviewedMovieObjs);
        return reviewedMovieObjs;
    }

    function addButton(text, onclick, cssObj) {
        cssObj = cssObj || {position: 'absolute', bottom: '7%', left:'4%', 'z-index': 3}
        let button = document.createElement('button'), btnStyle = button.style
        document.body.appendChild(button)
        button.innerHTML = text
        button.onclick = onclick
        btnStyle.position = 'absolute'
        Object.keys(cssObj).forEach(key => btnStyle[key] = cssObj[key])
        return button
    }


    function addResults(text_arr) {
        cssObj = {position: 'absolute', bottom: '7%', left:'4%', 'z-index': 3}
        let button = document.querySelector(button)
        button.style.display("none")
    }

})();

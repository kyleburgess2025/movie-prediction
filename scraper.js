// ==UserScript==
// @name         LetterboxsScraper
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

    const allMoviesWatched = document.querySelectorAll(".poster-container");
    let reviewedMovieObjs = [];
    for (let i = 0; i < allMoviesWatched.length; i++) {
        const movieRating = allMoviesWatched[i].querySelector("p").querySelector(".rating")?.className;
        if (movieRating) {
            const rating = movieRating.match(/(\d+)/)[0];
            const name = allMoviesWatched[i].querySelector("div").getAttribute("data-target-link").replace("/film", "").replaceAll("/", "");
            console.log(`${name}: ${rating}`);
            reviewedMovieObjs.push({"rating":rating, "name": name});
        }
    }
    console.log(reviewedMovieObjs);
})();
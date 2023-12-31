# FlickPicks - Collaborative Filtering Movie Recommendation Extension

## Project Description
FlickPicks is a browser extension that addresses the pain point of finding movies to watch, which can be time-consuming and frustrating. The extension uses collaborative filtering to generate personalized movie suggestions for users based on their preferences and the preferences of similar users.

## Project Components
FlickPicks consists of the following components:

1. Collaborative Filtering: FlickPicks utilizes collaborative filtering to recommend movies to users. By finding users with similar tastes and preferences, FlickPicks suggests movies that those users have enjoyed but the current user hasn't watched yet.

2. Jaccard Similarity: Jaccard similarity is used to measure the similarity between users. It compares the set of movies that users have rated, identifying the overlap and determining the similarity based on the ratio of shared movies to the total number of movies rated. 

## Promoting Wellness
FlickPicks promotes wellness by offering movie suggestions that cater to different needs and moods. It enhances the movie-watching experience by recommending films that fall into the following categories:

1. Relaxing: FlickPicks suggests movies that are calming, soothing, and provide a sense of relaxation. These movies can help users unwind and reduce stress.

2. Enjoyable: The extension recommends movies that are entertaining, funny, and engaging. These movies can provide an enjoyable and uplifting experience.

3. Educational: FlickPicks can recommend movies that are informative, thought-provoking, and inspiring.
   
## Innovation
FlickPicks brings innovation to the movie recommendation landscape by providing a seamless browsing experience. Unlike traditional movie recommendation apps, FlickPicks operates as a browser extension, integrating with popular movie websites and platforms. By leveraging existing sites, FlickPicks eliminates the need for users to switch between different applications, making movie discovery and selection more convenient and efficient.

Through its collaborative filtering approach and focus on wellness, FlickPicks revolutionizes the way users find movies to watch, ensuring a personalized and enjoyable movie-watching experience.

## Demo

Watch our demo here: https://youtu.be/36JUCBAaVP8

## FAQ

#### Q: Can FlickPicks recommend movies from different genres?
A: Yes, FlickPicks can recommend movies from a wide range of genres. Our dataset includes over 40,000!

#### Q: How accurate are the predictions made by FlickPicks?
A: To evaluate the accuracy of predictions, we used a test dataset (test.csv) containing actual movie ratings. The model achieved an RMSE (Root Mean Squared Error) score of 0.1606 when comparing the predicted ratings against the actual ratings. This indicates a reasonably accurate prediction performance.

#### Q: Where does the dataset used by FlickPicks originate from?
A: The dataset used by FlickPicks is sourced from open-source datasets that were recycled from a past project. These datasets contain over 40,000 examples and provide a diverse range of movie ratings and information.

## Future Plans

If we had more time, we would like to enhance FlickPicks with the following features:

1. Incorporating Movie Metadata: Integrate movie metadata such as revenue and synopsis into FlickPicks. By leveraging movie characteristics, we can create a hybrid model that combines collaborative filtering with content-based filtering. This hybrid approach will provide even better movie recommendations by taking into account both user preferences and movie attributes.
  
2. Natural Language Processing (NLP) Analysis of User Reviews: Analyze user comments using NLP techniques to identify common themes or tropes in user reviews. The extension would analyze frequently used words and phrases in positive or negative reviews, gaining insights into user sentiment and preferences. 

## How to Run
Download the TamperMonkey Chromium extension. Copy the contents of `scraper.js` into a new TamperMonkey script and enable the script for your browser. This will allow the script to scrape the contents of your Letterboxd when you are on your Watched Films page.

Run the server in `server.py` by running `python3 server.py`. The server uses Flask to create a simple API with a single POST endpoint where the results of the model will be posted. This API is accessed in the scraper, and the results are displayed to your page using DOM manipulation. The model itself is defined in `move_predict.py` and uses Jaccard similarity to find the movies you are most likely to rate highest.

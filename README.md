# FlickPicks - Collaborative Filtering Movie Recommendation Extension

## Project Description
FlickPicks is a browser extension that addresses the pain point of finding movies to watch, which can be time-consuming and frustrating. The extension uses collaborative filtering to generate personalized movie suggestions for users based on their preferences and the preferences of similar users.

## Project Components
FlickPicks consists of the following components:

1. Collaborative Filtering: FlickPicks utilizes collaborative filtering to recommend movies to users. It leverages the Jaccard similarity measure to identify similar users based on their movie ratings. By finding users with similar tastes and preferences, FlickPicks suggests movies that those users have enjoyed but the current user hasn't watched yet.

2. Jaccard Similarity: Jaccard similarity is used to measure the similarity between users. It compares the set of movies that users have rated, identifying the overlap and determining the similarity based on the ratio of shared movies to the total number of movies rated. This collaborative filtering approach is advantageous over content-based filtering as it relies on the collective wisdom of multiple users, allowing for serendipitous discoveries and recommendations beyond the limitations of content-based approaches.

## Promoting Wellness
FlickPicks promotes wellness by offering movie suggestions that cater to different needs and moods. It enhances the movie-watching experience by recommending films that fall into the following categories:

1. Relaxing: FlickPicks suggests movies that are calming, soothing, and provide a sense of relaxation. These movies can help users unwind and reduce stress.

2. Enjoyable: The extension recommends movies that are entertaining, funny, and engaging. These movies can bring joy and laughter to users' lives, providing an enjoyable and uplifting experience.

3. Educational: FlickPicks can recommend movies that are informative, thought-provoking, and inspiring. These movies offer an opportunity for users to expand their knowledge, learn new perspectives, and gain valuable insights.

## Innovation
FlickPicks brings innovation to the movie recommendation landscape by providing a seamless browsing experience. Unlike traditional movie recommendation apps, FlickPicks operates as a browser extension, integrating with popular movie websites and platforms. By leveraging existing sites, FlickPicks eliminates the need for users to switch between different applications, making movie discovery and selection more convenient and efficient.

Through its collaborative filtering approach and focus on wellness, FlickPicks revolutionizes the way users find movies to watch, ensuring a personalized and enjoyable movie-watching experience.

## FAQ

#### Q: How accurate are the predictions made by FlickPicks?
A: To evaluate the accuracy of predictions, we used a test dataset (test.csv) containing actual movie ratings. The model achieved an RMSE (Root Mean Squared Error) score of 0.1606 when comparing the predicted ratings against the actual ratings. This indicates a reasonably accurate prediction performance.

## Future Plans
If we had more time, we would like to enhance FlickPicks by incorporating movie metadata such as revenue and synopsis. By integrating movie metadata, we can create a hybrid model that combines collaborative filtering with content-based filtering. This hybrid approach would provide even better movie recommendations by taking into account both user preferences and movie characteristics. 

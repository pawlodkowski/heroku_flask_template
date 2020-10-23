import random
from movie_rec_app.movies import MOVIES


def random_recommender(num, user_input):

    """Here is where we take the user input from Flask
    and use it as an input to our NMF model.

    Note: user_input argument is currently not used."""

    ### NOTE: the following is complete pseudocode
    ### (we haven't built the functions yet)
    """user_vector = process_user_input(movie_list, ratings_list)
    nmf_model = load_trained_model('nmf_model.bin')
    user_profile = nmf_model.transform(user_vector)
    user_results = np.dot(user_profile, nmf_model.components_)
    user_results_final = convert_to_names(user_results)"""

    user_results_final = random.sample(MOVIES, k=num)
    return user_results_final

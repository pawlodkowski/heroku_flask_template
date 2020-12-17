import random
from movie_rec_app.movies import MOVIES


def random_recommender(num, user_input):

    """
    Note
    -----
    At the moment this is just a dummy function for demonstration
    purposes. The "user_input" argument is currently not used.

    Here is where we would eventually take the user input
    from the form and eventually use it as an input to our NMF model.
    """

    user_results_final = random.sample(MOVIES, k=num)
    return user_results_final

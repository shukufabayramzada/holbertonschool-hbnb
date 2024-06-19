from Model.baseclass import BaseClass


class Reviews(BaseClass):
    """
    Represents a review for a place.
    """

    def __init__(self, id, created_at, updated_at, place, rating, comment):
        """
        Initializes a new instance of the Reviews class.
        """
        super().__init__()
        self.place = place
        self.rating = rating
        self.comment = comment

    def add_rating(self, rating):
        """
        Adds a rating to the review.
        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Ratings must be from 1 to 5")
from reviews.repository import ReviewRepository


class ReviewService:

    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        return self.review_repository.get_reviews()

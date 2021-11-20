from .models import Merch_Rating


# Calculates an average rating from user ratings
# Adds ratings to model input
def add_rating(merch):
    for item in merch:
        avg_rating = 0
        merch_rating_list = []
        all_ratings = Merch_Rating.objects.all().filter(merchandise_id=item.id)
        for rating in all_ratings:
            merch_rating_list.append(rating.rating)

        number_of_ratings = len(merch_rating_list)
        if number_of_ratings != 0:
            total_rating = sum(merch_rating_list)
            avg_rating = round(total_rating / number_of_ratings, 2)
        item.avg_rating = avg_rating
        item.number_of_ratings = number_of_ratings
    return merch

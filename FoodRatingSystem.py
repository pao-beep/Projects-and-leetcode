#solution 73/78
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.num_foods = len(foods)
        self.num_cuisines = self.num_foods
        self.num_ratings = self.num_foods
        # print(self.num_foods)
        self.f_rating_dict = {}
        # self.f_rating_dict = {cuisine:{} for cuisine in cuisines}
        self.food_to_cuisine_dict = {}
        # for food in foods:
        #     self.food_to_cuisine_dict[food] = ""

        for i in range(self.num_foods):
            if self.f_rating_dict.get(cuisines[i]) is None:
                self.f_rating_dict[cuisines[i]] = {}
            self.f_rating_dict[cuisines[i]][foods[i]] = ratings[i]
            self.food_to_cuisine_dict[foods[i]] = cuisines[i]
        # for i in range(self.num_foods):
        #     self.food_to_cuisine_dict[foods[i]]=cuisines[i]
        # print(self.food_to_cuisine_dict)
        # print(self.f_rating_dict)
        # for i in range(self.num_foods):
        #     tmp ={foods[i]:0}
        #     self.f_rating_dict[cuisines[i]] = tmp
        # #print(self.f_rating_dict)
        # for i in range (self.num_foods):
        #     self.f_rating_dict[cuisines[i]][foods[i]] = ratings[i]

        # print(self.f_rating_dict)

    def changeRating(self, food: str, newRating: int) -> None:
        # print("in change rating")
        # print(f"args: food={food},newrate={newRating}")
        # print(self.f_rating_dict)
        food_cuisine = self.food_to_cuisine_dict[food]
        if self.f_rating_dict[food_cuisine].get(food) is not None:
            self.f_rating_dict[food_cuisine][food] = newRating
        # for i in self.f_rating_dict.keys():
        #     if self.f_rating_dict[i].get(food) is not None:
        #         self.f_rating_dict[i][food] = newRating
        # print("after finge change")
        # print(self.f_rating_dict)

    def highestRated(self, cuisine: str) -> str:
        # print("in highest ratings")
        # print(self.f_rating_dict[cuisine].items())
        tmp = sorted(self.f_rating_dict[cuisine].items(), key=lambda food: (-food[1], food[0]))
        # print(tmp)
        # print(tmp[0][0])

        return tmp[0][0]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
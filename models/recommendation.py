def recommend(category):

    recommendations = {

        "Electronics": [
            "Smart Phone",
            "Laptop",
            "Smart Watch"
        ],

        "Fashion": [
            "Shirts",
            "Shoes",
            "Jackets"
        ],

        "Books": [
            "AI Book",
            "Python Book",
            "Data Science"
        ],

        "Sports": [
            "Cricket Bat",
            "Football",
            "Gym Kit"
        ],

        "Home": [
            "Chair",
            "Table",
            "Lamp"
        ]
    }

    return recommendations.get(category, [])
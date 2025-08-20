# Product Recommendation System with Ethical Guidelines

def collect_user_history():
    print("To recommend products, we need to collect your product usage or purchase history.")
    print("We value your privacy and will use your data only for providing recommendations.")
    history = []
    while True:
        product = input("Enter a product you have used or purchased (or type 'done' to finish): ")
        if product.lower() == 'done':
            break
        history.append(product.strip().lower())
    return history

def recommend_products(user_history, product_catalog):
    # Simple recommendation: recommend products from the same category as user's history
    recommendations = set()
    for product in user_history:
        category = product_catalog.get(product)
        if category:
            for prod, cat in product_catalog.items():
                if cat == category and prod != product:
                    recommendations.add(prod)
    # Remove already used products
    recommendations = recommendations - set(user_history)
    return list(recommendations)

def main():
    print("Welcome to the Ethical Product Recommendation System!")
    print("Transparency: We will explain how recommendations are made.")
    print("Fairness: Recommendations are based on your input, not on any personal attributes.")
    print("You can opt out at any time by typing 'done'.\n")

    # Example product catalog: product -> category
    product_catalog = {
        "laptop": "electronics",
        "smartphone": "electronics",
        "headphones": "electronics",
        "novel": "books",
        "cookbook": "books",
        "running shoes": "sportswear",
        "yoga mat": "sportswear",
        "basketball": "sportswear",
        "blender": "kitchen",
        "toaster": "kitchen"
    }

    user_history = collect_user_history()
    if not user_history:
        print("No history provided. Unable to make recommendations.")
        return

    recommendations = recommend_products(user_history, product_catalog)
    print("\nHow recommendations are made: We look for products in the same categories as those you've used or purchased.")
    if recommendations:
        print("Recommended products for you (based on your history):")
        for rec in recommendations:
            print(f"- {rec.title()}")
    else:
        print("No new recommendations found based on your history.")

    print("\nThank you for using our system. Your data was used only for this session and not stored.")

if __name__ == "__main__":
    main()

import streamlit as st

# Function to compare two houses
def compare_houses():
    st.title("House Comparison Tool")

    # User input for house 1
    st.header("House 1 Details")
    house1_name = st.text_input("Enter the name of House 1", key="house1_name")
    house1_location = st.text_input(f"Location of {house1_name}", key="house1_location")
    house1_cost = st.number_input(f"Total cost of {house1_name} (in SGD)", min_value=0, key="house1_cost")
    house1_room_size = st.number_input(f"Room size of {house1_name} (in square meters)", min_value=0, key="house1_room_size")
    
    house1_amenities = {
        "coffeeshop": st.number_input(f"Distance to nearest coffeeshop from {house1_name} (in km)", min_value=0.0, key="house1_coffeeshop"),
        "supermarket": st.number_input(f"Distance to nearest supermarket from {house1_name} (in km)", min_value=0.0, key="house1_supermarket"),
        "school": st.number_input(f"Distance to nearest school from {house1_name} (in km)", min_value=0.0, key="house1_school"),
        "mall": st.number_input(f"Distance to nearest shopping mall from {house1_name} (in km)", min_value=0.0, key="house1_mall"),
        "gym": st.number_input(f"Distance to nearest gym from {house1_name} (in km)", min_value=0.0, key="house1_gym"),
        "mrt": st.number_input(f"Distance to nearest MRT station from {house1_name} (in km)", min_value=0.0, key="house1_mrt")
    }
    
    # User input for house 2
    st.header("House 2 Details")
    house2_name = st.text_input("Enter the name of House 2", key="house2_name")
    house2_location = st.text_input(f"Location of {house2_name}", key="house2_location")
    house2_cost = st.number_input(f"Total cost of {house2_name} (in SGD)", min_value=0, key="house2_cost")
    house2_room_size = st.number_input(f"Room size of {house2_name} (in square meters)", min_value=0, key="house2_room_size")
    
    house2_amenities = {
        "coffeeshop": st.number_input(f"Distance to nearest coffeeshop from {house2_name} (in km)", min_value=0.0, key="house2_coffeeshop"),
        "supermarket": st.number_input(f"Distance to nearest supermarket from {house2_name} (in km)", min_value=0.0, key="house2_supermarket"),
        "school": st.number_input(f"Distance to nearest school from {house2_name} (in km)", min_value=0.0, key="house2_school"),
        "mall": st.number_input(f"Distance to nearest shopping mall from {house2_name} (in km)", min_value=0.0, key="house2_mall"),
        "gym": st.number_input(f"Distance to nearest gym from {house2_name} (in km)", min_value=0.0, key="house2_gym"),
        "mrt": st.number_input(f"Distance to nearest MRT station from {house2_name} (in km)", min_value=0.0, key="house2_mrt")
    }
    
    # Calculate price per square meter
    if house1_room_size != 0 and house2_room_size != 0:
        house1_price_per_sqm = house1_cost / house1_room_size
        house2_price_per_sqm = house2_cost / house2_room_size
    else:
        st.error("Room size cannot be zero.")
        return
    
    # Initialize scores for each house
    house1_score = 0
    house2_score = 0
    
    # Compare price per square meter (lower price gets 1 point)
    if house1_price_per_sqm < house2_price_per_sqm:
        house1_score += 1
        house1_score += 1  # Additional point for lower price per square meter
    elif house2_price_per_sqm < house1_price_per_sqm:
        house2_score += 1
        house2_score += 1  # Additional point for lower price per square meter
    
    # Compare amenities (shorter distance gets 1 point)
    for amenity in house1_amenities:
        if house1_amenities[amenity] < house2_amenities[amenity]:
            house1_score += 1
        elif house2_amenities[amenity] < house1_amenities[amenity]:
            house2_score += 1
    
    # Display results
    if st.button("Compare Houses"):
        st.subheader("Comparison Results")
        st.write(f"House 1: {house1_name}, located at {house1_location}, has a price per square meter of SGD {house1_price_per_sqm:.2f}")
        st.write(f"House 2: {house2_name}, located at {house2_location}, has a price per square meter of SGD {house2_price_per_sqm:.2f}")
        
        if house1_price_per_sqm < house2_price_per_sqm:
            price_diff = house2_price_per_sqm - house1_price_per_sqm
            st.write(f"{house1_name} is cheaper by SGD {price_diff:.2f} per square meter.")
        elif house2_price_per_sqm < house1_price_per_sqm:
            price_diff = house1_price_per_sqm - house2_price_per_sqm
            st.write(f"{house2_name} is cheaper by SGD {price_diff:.2f} per square meter.")
        
        st.write(f"\nHouse 1 Score: {house1_score}")
        st.write(f"House 2 Score: {house2_score}")
        
        if house1_score > house2_score:
            st.success(f"{house1_name} is a better choice based on your preferences.")
        elif house2_score > house1_score:
            st.success(f"{house2_name} is a better choice based on your preferences.")
        else:
            st.warning("Both houses are equally good based on your preferences.")

# Run the app
if __name__ == "__main__":
    compare_houses()

from data_package import  remove_duplicates, strip_whitespaces
from data_package import calculate_mean, find_maximum, find_minimum
    
def main():
    
    user_input= input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")
    
    string_list= user_input.split(",")
    stripped_strings= strip_whitespaces(string_list)
    
    float_list=[]
    
    try:
        for item in stripped_strings:
            if item != "": 
                float_list.append(float(item))
    
        unique_data = remove_duplicates(float_list)
        
        print(f"Cleaned and unique data: {unique_data}")
        print("-" * 20)
        
    
        mean_val = calculate_mean(unique_data)
        max_val = find_maximum(unique_data)
        min_val = find_minimum(unique_data)
        
        print(f"Mean: {mean_val:.2f}")
        print(f"Maximum: {max_val:.1f}")
        print(f"Minimum: {min_val:.1f}")
        
    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")


if __name__ == "__main__":
    main()
        

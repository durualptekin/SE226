import geometry_utils

def main():
    
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")
    
    operations = { 
        "circle_area": geometry_utils.circle_area, 
        "circle_perimeter": geometry_utils.circle_perimeter, 
        "rectangle_area": geometry_utils.rectangle_area, 
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area,
    }
    
    operaiton_name = input("Enter the operation you want to perform: ")
    
    if operaiton_name not in operations:
        print("Invalid operaiton!")
        return
    
    try:
        if "circle" in operaiton_name:
            
            radius =float(input("Enter radius: "))
            result= operations[operaiton_name](radius)
            
        elif "rectangle" in operation_name:
            
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = operations[operation_name](width, height)
            
        elif "triangle" in operation_name:
            
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = operations[operation_name](base, height)
            
        print(f"Result: {result:.2f}")


    except ValueError as e:
    
        if str(e) == "Dimensions must be strictly positive.":
            print(f"Input Error: {e}")
            
        else:
            print("Input Error: Please enter valid numbers.")
            
        

if __name__ == "__main__":
    main()
    
    


import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height


def main():
    print("\n===== AREA CALCULATOR =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-4): "))

            if choice == 1:
                radius = float(input("Enter radius: "))
                print(f"Area of Circle: {area_circle(radius):.2f}")

            elif choice == 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print(f"Area of Rectangle: {area_rectangle(length, width):.2f}")

            elif choice == 3:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"Area of Triangle: {area_triangle(base, height):.2f}")

            elif choice == 4:
                print("Exiting program...")
                break

            else:
                print("Invalid choice! Please select between 1 and 4.")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()
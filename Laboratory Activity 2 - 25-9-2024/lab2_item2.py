while True:
    total_amount = float(input("Enter the total purchase amount: "))
    
    if total_amount > 5000:
        discount = total_amount * 0.10
    else:
        discount = total_amount * 0.05

    final_amount = total_amount - discount
    
    print(f"Initial Purchase Amount: {total_amount:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_amount:.2f}")
    
    if input("Do you want to try again? (yes/no): ").strip().lower() != 'yes':
        print("Thank you!")
        break

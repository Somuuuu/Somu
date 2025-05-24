categories = {
   "clothes": ["shirt", "jeans"],
   "electronics": ["phone", "charger"]
}
a = input("Enter category(cloths/ electronics):").strip()
if a == "clothes":
   print("List of products:", categories["clothes"])
elif a =="electronics":
   print("List of products:", categories["electronics"])
else:
      print("Invalid category")


import os

png_images = [file for file in os.listdir() if file.endswith('.png')]

if png_images:
    print("PNG image(s) available. Select which one to convert:")
    
    for index, file_name in enumerate(png_images, start=1):
        print(f"{index}. {file_name}")

    choice = input(f"Enter your choice (1 to {len(png_images)}): ")
    
    try:
        choice_index=int(choice)-1
        selected_file=png_images[choice_index]
        print(f"PNG image: {selected_file} is selected!")

        from PIL import Image
        png_image = Image.open(selected_file)
        png_image.save("icon.ico", format='ICO', sizes=[(32, 32)])
        print("Done; converted to icon.ico and saved in the same directory.")

    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number.")
else:
    print("No PNG images are available in the current directory.")

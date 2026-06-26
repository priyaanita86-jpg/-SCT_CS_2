from PIL import Image

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y][:3]

                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

                pixels[x, y] = (r, g, b)

        encrypted_path = "encrypted_image.png"
        img.save(encrypted_path)

        print(f"Image encrypted successfully!")
        print(f"Saved as: {encrypted_path}")

    except Exception as e:
        print("Error:", e)


def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y][:3]

                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

                pixels[x, y] = (r, g, b)

        decrypted_path = "decrypted_image.png"
        img.save(decrypted_path)

        print(f"Image decrypted successfully!")
        print(f"Saved as: {decrypted_path}")

    except Exception as e:
        print("Error:", e)


def main():
    print("\n===== Image Encryption Tool =====")

    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            image_path = input("Enter image path: ")
            key = int(input("Enter encryption key: "))
            encrypt_image(image_path, key)

        elif choice == "2":
            image_path = input("Enter encrypted image path: ")
            key = int(input("Enter decryption key: "))
            decrypt_image(image_path, key)

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()





Output -

===== Image Encryption Tool =====

1. Encrypt Image
2. Decrypt Image
3. Exit

Enter your choice: 1
Enter image path: photo.jpg
Enter encryption key: 50

Image encrypted successfully!
Saved as: encrypted_image.png

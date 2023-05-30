from PIL import Image, ImageDraw, ImageFont, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

def generate_badges(template_path, image_directory, output_directory):

    # Get info from user
    print('What font should the program use? Example: Poppins-Bold.ttf')
    whatfont = input()
    print('Specify starting tag, the program will count up by 1 for each badge.')
    tag = input()
    tag = int(tag)

    # Iterate through the image files in the directory
    for filename in os.listdir(image_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_directory, filename)

            # Load the template image
            template_image = Image.open(template_path)
            template_copy = template_image.copy()

            # Load the photo
            photo = Image.open(image_path)
            nickname = os.path.splitext(filename)[0]

            # Position the photo
            photo_x = 45
            photo_y = 190
            template_copy.paste(photo, (photo_x, photo_y))
            template_copy.paste(template_image, (0, 0), mask=template_image)

            # Add the nickname
            nickname_x = 400
            nickname_y = 1180
            font = ImageFont.truetype(whatfont, 130)
            draw = ImageDraw.Draw(template_copy)
            draw.text((nickname_x, nickname_y), nickname, fill=(255, 255, 255), font=font)

            # Add the tag
            tag_x = 945
            tag_y = 1320
            font = ImageFont.truetype(whatfont, 50)
            draw = ImageDraw.Draw(template_copy)
            draw.text((tag_x, tag_y), '#'+str(tag), fill=(255, 255, 255), font=font)
            tag = tag+1

            # Generate the output
            output_path = os.path.join(output_directory, f"{nickname}_badge.png")
            template_copy.save(output_path)

            photo.close()
            del draw

        template_image.close()

# Specify folders
template_path = "badgetemplate/badgetemplate.png"
image_directory = "badgeimages/"
output_directory = "badgeoutput/"

generate_badges(template_path, image_directory, output_directory)

print('The program has finished. Press enter to continue.')
x = input()
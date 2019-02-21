import os
import urllib.parse as urlparse
import urllib.request


def image_downloader(file):
    """
    This Function Downloads all images from a Text File including urls.

    Args:
        file: the path of the text file.

    On Execution:
        Downloads the images from URLs provided on the text file
        and saves them in the images Directory.

    Raises:
        ValueError or URLError if url is incorrect or unknown url type.
    """
    directory = './images'

    if not os.path.exists(directory):
        # if directory Doesnt Exist Create it.
        os.makedirs(directory)

    with open(file, "r") as text_file:
        image_count = 0

        for line in text_file:
            name_from_url = urlparse.urlsplit(line)[2].split('/')[-1]

            try:
                image = name_from_url.split('.')[0]
                # Try to get Image Extention.
                image_ext = name_from_url.split('.')[1]
                image_name = '{}-{}.{}'.format(
                    image, image_count, image_ext)
            except IndexError:
                # As Some URLs Don't Include Extentions use .jpg format.
                image_name = '{}-{}.jpg'.format(
                    name_from_url, image_count)

            file_path = directory + '/' + image_name

            # Download The image
            urllib.request.urlretrieve(line, file_path)
            # increase count for name uniqueness.
            image_count += 1


if __name__ == '__main__':
    input_file = input("Provide The Text File Path Which Include Image URLs: ")
    image_downloader(input_file)

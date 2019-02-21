import os
import tempfile
import unittest
import urllib

from image_downloader.downloader import image_downloader


class TestImageDownloader(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(mode='w+t', suffix='.txt')

    def tearDown(self):
        self.test_file.close()

    @classmethod
    def tearDownClass(cls):
        super(TestImageDownloader, cls).tearDownClass()
        os.rmdir('images')

    def test_images_directory_created(self):
        image_downloader(self.test_file.name)

        self.assertTrue(os.path.exists('./images'))

    def test_invalid_image_url(self):
        self.test_file.writelines("hs://images.unsplash.com/test")
        self.test_file.seek(0)

        self.assertRaises(
            urllib.error.URLError, image_downloader, self.test_file.name)

    def test_not_found_image_url(self):
        self.test_file.writelines("https://images.unsplash.com/test")
        self.test_file.seek(0)

        self.assertRaises(
            urllib.error.HTTPError, image_downloader, self.test_file.name)


if __name__ == '__main__':
    unittest.main()

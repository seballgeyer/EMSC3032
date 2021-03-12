import unittest # import TestCase


class Test(unittest.TestCase):
    def test_read_sph(self):
        """
        Testing lab2.read_sph with a file without header
        """
        import tempfile
        temp_File = tempfile.TemporaryFile(mode='r+')
        temp_File.write("0 0 3.3 5.2\n")
        temp_File.write("1 0 3.5 3.1\n")
        temp_File.write("1 1 6.2 2.3\n")
        temp_File.seek(0)
        from emsc3032 import lab2
        c, s = lab2.read_sph(temp_File)
        self.assertEqual(c[0, 0], 3.3, "Should be 3.3")
        self.assertEqual(c[1, 0], 3.5, "Should be 3.5")
        temp_File.close()

    def test_read_sph_1(self):
        """
        Testing lab2.read_sph with a file with header starting with "#"
        """
        import tempfile
        temp_File = tempfile.TemporaryFile(mode='r+')
        temp_File.write("# line of header\n")
        temp_File.write("0 0 3.3 5.2\n")
        temp_File.write("1 0 3.5 3.1\n")
        temp_File.write("1 1 6.2 2.3\n")
        temp_File.seek(0)
        from emsc3032 import lab2
        c, s = lab2.read_sph(temp_File)
        self.assertEqual(c[0, 0], 3.3, "Should be 3.3")
        self.assertEqual(c[1, 0], 3.5, "Should be 3.5")
        temp_File.close()


    def test_read_sph_2(self):
        """
        Testing lab2.read_sph with a file with header which doesn't start with "#"
        """
        import tempfile
        temp_File = tempfile.TemporaryFile(mode='r+')
        temp_File.write("line of header\n")
        temp_File.write("0 0 3.3 5.2\n")
        temp_File.write("1 0 3.5 3.1\n")
        temp_File.write("1 1 6.2 2.3\n")
        temp_File.seek(0)
        from emsc3032 import lab2
        c, s = lab2.read_sph(temp_File, skiprows=1)
        self.assertEqual(c[0, 0], 3.3, "Should be 3.3")
        self.assertEqual(c[1, 0], 3.5, "Should be 3.5")
        temp_File.close()

    def test_read_sph_3(self):
        """
        Testing lab2.read_sph with a file with header starting with "#"
        """
        import tempfile
        temp_File = tempfile.TemporaryFile(mode='r+')
        temp_File.write("# line of header\n")
        temp_File.write("0 0 3.3 5.2\n")
        temp_File.write("1 0 3.5 3.1\n")
        temp_File.write("1 1 6.2 2.3\n")
        temp_File.seek(0)
        from emsc3032 import lab2
        c, s = lab2.read_sph(temp_File, skiprows=1)
        self.assertEqual(c[0, 0], 3.3, "Should be 3.3")
        self.assertEqual(c[1, 0], 3.5, "Should be 3.5")
        temp_File.close()


if __name__ == '__main__':
    unittest.main()

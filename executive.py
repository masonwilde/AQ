from lers_reader import Lers_Reader

class Executive(object):

    def run(self):

        # Get and open file from the user
        file_open = False
        while not file_open:
            filename = raw_input("Please enter a filename: ")
            try:
                file_test = open(filename, 'r')
                file_open = True
            except IOError:
                print "File could not be opened"
                file_open = False
        # End file name retrieval

        # Get maxstar value from the user
        maxstar_obtained = False
        maxstar = None
        while not maxstar_obtained:
            maxstar = raw_input("Please enter an integer value for MAXSTAR: ")
            try:
                maxstar = int(maxstar)
                if maxstar > 0:
                    maxstar_obtained = True
                else:
                    print "Invalid Maxstar value. Please enter an integer larger than 0."
            except ValueError:
                print "Invalid Maxstar value. Please enter an integer larger than 0."
        # End maxstar retrieval

        reader = Lers_Reader(filename)
        dataset = reader.read()
        #dataset.display()
        if not dataset.is_consistent():
            with open(filename, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write("! Dataset is inconsistent".rstrip('\r\n') + '\n' + content)
            print "Dataset is inconsistent"
            print "No rules induced"
            return
        else:
            print "Come on then"

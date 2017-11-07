class Executive(object):

    def run(self):

        # Get and open file from the user
        file_open = False
        while not file_open:
            file_name = raw_input("Please enter a filename: ")
            try:
                file_test = open(file_name, 'r')
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

        print file_name
        print maxstar

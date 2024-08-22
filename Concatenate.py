OVERLAP_LENGTH = 5

while True:
    fragments = [] #initialise fragments as a list

    # To collect 10 nucleotide base pair fragments from user as a input (prototyping)
    print("Enter 10 nucleotide base pair fragments (500 bases each): ")

    for i in range(10):
        while True:
            try:
                fragment = input("Entire Fragment " + str(i + 1) + ": ").replace(' ', '')  # Remove spaces
                
                # Validate fragment length and content
                if len(fragment) != 500:
                    raise ValueError("Fragment length is not 500 bases.")
                if not all(n in "ATGC" for n in fragment):
                    raise ValueError("Fragment contains invalid characters.")
                
                
                fragments.append(fragment)  # Add valid fragment to the list
                break  # Break the loop if input is valid
            
            #Error Handling
            except ValueError as ve:
                print("Error with fragment input: " + str(ve) + ". Please ensure the fragment is exactly 500 bases long and contains only 'A', 'T', 'G', and 'C'.")
                print(" ")
            except TypeError as te:
                print("Type error with fragment input: " + str(te) + ". This might occur if the input type is not as expected.")
                print(" ")
            except Exception as err:
                print("An unexpected error occurred while collecting fragment " + str(i + 1) + ": " + str(err))
                print(" ")




    # To initialise the complete sequence with our first fragment
    complete_sequence = fragments[0]  #Initializes the complete sequence with the first fragment (0 index = 1)
    used_fragments = [False] * len(fragments)  # Creates a list to track which fragments have been used, initialized as "False".
    used_fragments[0] = True # Marks the first fragment as used in the sequence.
    



    # For assemblng the sequence:
    try: 
        for j in range(len(fragments) - 1):
            added = False      #to track whether a fragment was successfully added in this iteration.
            for i, fragment in enumerate(fragments):   #
                if not used_fragments[i]:

                    # For checking if our current fragment is overlapping with the end of complete sequence:
                    if complete_sequence[-OVERLAP_LENGTH:] == fragment[:OVERLAP_LENGTH]:
                        complete_sequence += fragment[OVERLAP_LENGTH:]
                        used_fragments[i] = True
                        added = True
                        break

                    # For checking if the current fragment is overlaping with the beginning of complete sequence:
                    elif fragment[-OVERLAP_LENGTH:] == complete_sequence[:OVERLAP_LENGTH]:
                        complete_sequence = fragment[:OVERLAP_LENGTH] + complete_sequence
                        used_fragments[i] = True
                        added = True
                        break
            if not added:
                print("Unable to create a complete sequence. Fragments do not overlap correctly or cannot be assembled.")
                break

    #Error handling
    except TypeError as te:
        print("Type error during sequence assembly: " + str(te) + ". This might happen if a non-string type is used in string operations.")
    except Exception as err:
        print("An unexpected error occurred during sequence assembly: " + str(err))




    # Result output
    if all(used_fragments):
        print("Complete sequence constructed: ")
        print(complete_sequence)
        print(" ")
        print("Length of complete sequence: ", len(complete_sequence))
        print("Programme executed successfully...")
        print(" ")
    else:
        print("Not all fragments could be used to construct a complete sequence!!")
        print(" ")



    # Prompt user to overlap another batch of fragments or exit
    while True:
        try:
            user_choice = int(input("Do you want to concatenate next batch of 10 fragments? "))
            print("Enter 1 for Yes: ")
            print("Enter 0 for No: ")
            if user_choice == 1:
                print(" ")
                break
            elif user_choice == 0:
                print("Programme exited!")
                exit()
            else:
                print("Invalid input! Please enter 1 for Yes or 0 for No")

        #Error Handling
        except ValueError as ve:
            print("Invalid input: " + str(ve) + ". Please enter a number.")
        except Exception as err:
            print("An error has occurred while processing user choice: " + str(err))


#Programme still under works

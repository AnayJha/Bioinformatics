OVERLAP_LENGTH = 5    #Defines the length of the overlap between consecutive fragments

while True:
    fragments = [] #initialise fragments as a list to hold the valid nucleotide fragments entered. 
    existing_fragments = []  #Ensure no fragment is duplicate or contained within another fragment, for uniqueness.

    # To collect 10 nucleotide base pair fragments from user as a input (prototyping)
    print("Enter 10 nucleotide base pair fragments (500 bases each): ")

    for i in range(10):    # Loops 10 times to collect 10 fragments.
        while True:
            try:
                fragment = input("Entire Fragment " + str(i + 1) + ": ").replace(' ', '')  # Remove spaces if any
                
                # Validate fragment length and content
                if len(fragment) != 500:
                    raise ValueError("Fragment length is not 500 bases.")

                # Validate fragment content
                if not all(n in "ATGC" for n in fragment):
                    raise ValueError("Fragment contains invalid characters!")

                # Check for uniqueness
                if fragment in existing_fragments:
                    raise ValueError("Fragment is a duplicate.")

                # Check if the Fragment is contained within another fragment
                if any(fragment in f for f in existing_fragments):  #Check if fragment is contained within any of previously collected existing_fragments.
                    raise ValueError("Fragment is contained within another fragment.")

                # Add valid fragment to the list
                fragments.append(fragment)  # Add valid fragment to the list
                break  # Break the loop if user input is valid

            
            #Error Handling
            except ValueError as ve:
                print("Error with fragment input: " + str(ve) + ". Please ensure the fragment is exactly 500 bases long and contains only 'A', 'T', 'G', and 'C'.")
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
        for j in range(len(fragments) - 1):       #The first fragment is already part of complete_sequence
            added = False      #To track whether a fragment was successfully added in this iteration, initially no fragments are used.
            for i, fragment in enumerate(fragments):   #Used to loop through the fragments list & access both, index and fragment.
                if not used_fragments[i]:

                    # For checking if our current fragment is overlapping with the end of complete sequence:
                    if complete_sequence[-OVERLAP_LENGTH:] == fragment[:OVERLAP_LENGTH]:   #Using slicing and negative indexing
                        complete_sequence += fragment[OVERLAP_LENGTH:]   #Concatenated strings using inplace operator
                        used_fragments[i] = True   #Updated value at i-index
                        added = True
                        break

                    # For checking if the current fragment is overlaping with the beginning of complete sequence:
                    elif fragment[-OVERLAP_LENGTH:] == complete_sequence[:OVERLAP_LENGTH]:   #Checks if start overlaps with end 
                        complete_sequence = fragment[:OVERLAP_LENGTH] + complete_sequence
                        used_fragments[i] = True  #Updated value at i-index
                        added = True
                        break
                        
            if not added:    #If no fragment was added
                print("Unable to create a complete sequence. Fragments do not overlap correctly or cannot be assembled.")
                print(" ")
                break

    #Error handling
    except Exception as err:
        print("An unexpected error occurred during sequence assembly: " + str(err))
        print(" ")



    # Result output
    if all(used_fragments):   #Checks if all fragments have been used.
        print("Complete sequence constructed: ", complete_sequence)
        print(" ")
        print("Length of complete sequence: ", len(complete_sequence))
        print(" ")
        print("Programme executed successfully...")
        
    else:
        print("Not all fragments could be used to construct a complete sequence!!")
        print(" ")


    # Prompt user to overlap another batch of fragments or exit
    while True:
        # Display the prompt and instructions to the user
        print("Do you want to concatenate the next batch of 10 fragments?")
        print("Enter 1 for Yes")
        print("Enter 0 for No")
        print(" ")
    
        try:
            # Read user input
            user_choice = int(input("Your choice: "))
    
            # Check user's choice and act accordingly
            if user_choice == 1:
                print(" ")
                break  # Exit the loop and continue 
            elif user_choice == 0:
                print("Programme exited!")
                exit()  # Used for exiting our program
            else:
                print("Invalid input! Please enter 1 for Yes or 0 for No")
                print(" ")

        #Error Handling
        except ValueError as ve:
            print("Invalid input: " + str(ve) + ". Please enter a number.")
            print(" ")
        except Exception as err:
            print("An error has occurred while processing user choice: " + str(err))
            print(" ")


#Programme still under works

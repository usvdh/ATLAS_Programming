# Read README before running for pre-requisites.

# Import libraries. customtkinter is used for the graphical user interface. os is used to detect the textfiles we want to search.
# customtkinter was chosen over tkinter because tkinter gave me so many headaches. I promise I tried ;-;
import customtkinter
import os

# We establish the root widget, which is a window with a title bar and other decoration provided by the window manager. This way, we initialize the customtkinter.
# We give the root a size (this case 1000x500 pixels)
root = customtkinter.CTk()
root.geometry("1000x500")

def search():
    '''
    This function loops through all the files given by detectFiles() and finds the query input into the searchbox. 
    
    :param query: This is the query that was input into the searchbox in the GUI. 
    :param lines: This stores all the lines seperately in an array. 
    :return: Returns nothing, but inserts the search results to GUI textbox. 
    '''
    
    # Gets query from searchquery entry box
    query = queryEntry.get()
    
    # Clears textbox
    resultsTextbox.delete('1.0', customtkinter.END)

    # Open all files and read all lines in the file
    for i in detectFiles(): 
        lines = open("textfiles/" + i, "r").readlines()
        for line in lines: 
            # Check if the search query is present on a line
            # if find() finds no match, it returns -1, which is why "!= -1"
            if line.find(query) != -1:
                resultsTextbox.insert("0.0", str(i) + ", Line " + str(lines.index(line)) + ": " + "'" + line + "'" + "\n\n")
    return 

def detectFiles():
    '''
    This function detects all .txt files in the folder 'textfiles'
    
    :param fileList: Array to store each text file name in.
    :return: Returns complete array with all .txt files in the 'textfiles' folder. 
    '''
    
    fileList = []
    
    # For some reason it won't work when removing root and dirs, so still left in there.
    for root, dirs, files in os.walk("textfiles"):
        for file in files:
            if file.endswith('.txt'):
                fileList.append(file)
    return fileList

# GUI derived from https://www.youtube.com/watch?v=iM3kjbbKHQU

# Establish how the interface will look like
# Create frame, define what it looks like
frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both")

# Create text "Soogle", define what it looks like
soogle = customtkinter.CTkLabel(master=frame, text="Soogle")
soogle.pack(padx=10, pady=12)

# Create the query entry, define what it looks like
queryEntry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Search query")
queryEntry.pack(padx=10, pady=12)

# Create the button, define what it looks like
button = customtkinter.CTkButton(master=frame, text="Search", command=search)
button.pack(padx=10, pady=12)

# Create text "results", define what it looks like
resultsLabel = customtkinter.CTkLabel(master=frame, text="Results")
resultsLabel.pack(padx=10, pady=12)

# Create textbox (where findings will be displayed), define what it looks like
resultsTextbox = customtkinter.CTkTextbox(master=frame, width=700)
resultsTextbox.pack(padx=10, pady=12)

root.mainloop()
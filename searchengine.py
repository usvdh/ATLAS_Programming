# Import some programs (customtkinter is needed for the interface, os is needed to let the operating system run smoothly)
import customtkinter
import os

# We establish the root widget, which is a window with a title bar and other decoration provided by the window manager. This way, we initialize the customtkinter.
# We give the root a size (this case 500x500 pixels)
root = customtkinter.CTk()
root.geometry("1000x500")

def search():
    print("Test")
    # print query, so it says "Search query"
    query = queryEntry.get()
    print(query)
    # insert at line 0 character 0, plus the text you will see
    resultsTextbox.insert("0.0", "testfile.txt: " + "...Hello, this is a test.")
    # print the number of files there has been searched in
    print(countFiles()[1])
    # fileList = countFiles().fileList

    # Open all files and read all lines in the file
    for i in countFiles()[0]: 
        lines = open("textfiles/" + i, "r").readlines()
        for line in lines: 
            # Check if the search query is present on a line
            if line.find(query) != -1:
                print(query, 'is found in ' + i)
                print('Line Number:', lines.index(line))
                print('Line:', line) 
                resultsTextbox.insert("0.0", str(i) + ", Line " + str(lines.index(line)) + ": " + "'" + line + "' " + "\n\n")

#define number of files searched in
def countFiles():
    fileList = []
    fileCounter = -1 #to match index of array
    
    #For everything found in the system (this case only files), if it ends with '.txt', count it as 1 file
    for root, dirs, files in os.walk("textfiles"):
        for file in files:
            if file.endswith('.txt'):
                fileCounter += 1
                fileList.append(file)
                # print(fileCounter)
                # print(fileList)
    return fileList, fileCounter

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


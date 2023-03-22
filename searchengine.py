import customtkinter

root = customtkinter.CTk()
root.geometry("500x500")


def search():
    print("Test")
    query = queryEntry.get()
    print(query)
    # insert at line 0 character 0
    resultsTextbox.insert("0.0", "testfile.txt: " +
                          "...Hello, this is a test...")


frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both")

soogle = customtkinter.CTkLabel(master=frame, text="Soogle")
soogle.pack(padx=10, pady=12)

queryEntry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Search query")
queryEntry.pack(padx=10, pady=12)

button = customtkinter.CTkButton(master=frame, text="Search", command=search)
button.pack(padx=10, pady=12)

resultsLabel = customtkinter.CTkLabel(master=frame, text="Results")
resultsLabel.pack(padx=10, pady=12)

resultsTextbox = customtkinter.CTkTextbox(master=frame)
resultsTextbox.pack(padx=10, pady=12)

root.mainloop()

from pyscript import document, display

grade7_members = {"Angela Lee", "Nicole Semana"}
grade8_members = {"Rhyzza Fallore", "Allen Camitan"}
grade9_members = {"Miel Adriano", "Frenccy Lerona", "Miguel Mundo"}
grade10_members = {"Chelsey Porcalla", "Gab Vital", "Ehlia Orio"}


all_members = grade7_members | grade8_members | grade9_members | grade10_members


# Display the updated member list and total
def update_results():
    # Sort the set alphabetically and separate names with HTML line breaks
    members_list = "<br>".join(sorted(all_members))

    # Display the names and the total number of unique members
    document.getElementById("member-list").innerHTML = f"{members_list}"
    document.getElementById("member-count").innerHTML = f"{len(all_members)}"


# Add a new member using the names entered by the user
def add_member(event):
    global all_members

    # Get and format the user's input
    first_name = document.getElementById("first-name").value.strip().title()
    last_name = document.getElementById("last-name").value.strip().title()

    # Combine the first and last names into one string
    new_member = f"{first_name} {last_name}"

    # Use the union operator to add the new member to the master set
    all_members = all_members | {new_member}

    # Update the results on the webpage
    update_results()

    # Clear the input boxes after adding the member
    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""


# Import the webpage elements and show the initial results
from js import document

update_results()

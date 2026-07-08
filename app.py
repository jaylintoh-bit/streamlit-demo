import streamlit as st
from PIL import Image

# --- Add these functions after the import lines ---

def generate_greeting(name, gender):
    """Return a personalised greeting based on name and gender."""
    title = "Mr." if gender == "Male" else "Ms."
    greeting = f"Welcome {title} {name.title()}!"
    return greeting

def get_level_description(level):
    """Return a word description for the numeric level."""
    descriptions = {
        1: "Beginner",
        2: "Elementary",
        3: "Intermediate",
        4: "Advanced",
        5: "Expert"
    }
    return descriptions[level]

# App title
st.title("Jaylin's Streamlit Demo")

# Header and subheader
st.header("Welcome to My App")
st.subheader("An interactive Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is bold markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
img = Image.open("dog.jpg")
st.image(img, width=200)

# Dynamic checkboxes generated from a list
st.subheader("Select your skills")

skills = ["Python", "HTML", "Data Analysis", "AI", "Robotics"]
selected_skills = []  # empty list to collect selected skills

# Loop through the list to create one checkbox per skill
for skill in skills:
    if st.checkbox(skill):            # creates a checkbox with the skill name
        selected_skills.append(skill)  # add to selected list if ticked

# Display results based on what was selected
if len(selected_skills) > 0:
    st.success(f"You selected {len(selected_skills)} skill(s):")
    for s in selected_skills:
        st.write(f"  - {s}")

    # Calculate and display a percentage
    percentage = round(len(selected_skills) / len(skills) * 100)
    st.metric("Skills coverage", f"{percentage}%")
else:
    st.warning("Please select at least one skill.")

   
# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])

# Use the generate_greeting function instead of if/else
# (We need the name variable too, so this will work with the text input below)


# Selectbox - using a list variable instead of hardcoded values
hobbies = ["Dancing", "Reading", "Sports", "Gaming",
           "Cooking", "Music", "Photography", "Gardening"]

hobby = st.selectbox("Select your main hobby:", hobbies)
st.write("Your main hobby is:", hobby)

# Multiselect - lets the user pick more than one hobby
selected = st.multiselect("Pick all your hobbies:", hobbies)

# Loop through the selected hobbies and display each one
if selected:
    st.write(f"You selected {len(selected)} hobbies:")
    for h in selected:
        st.write(f"  - {h}")
else:
    st.info("No hobbies selected yet.")

# Slider
# Slider - original
level = st.slider("Choose a level", 1, 5)
st.write(f"Selected level: {level}")

# New slider for practice hours
hours = st.slider("Hours of practice per week", 1, 20, 5)

# Calculate totals using arithmetic operators
monthly = hours * 4          # multiplication
yearly = hours * 52          # multiplication
daily = round(hours / 7, 1)  # division and rounding
remaining = 500 - yearly     # subtraction

# Display the yearly total as a prominent metric
st.metric("Yearly Practice Hours", yearly)
st.write(f"That is about {daily} hours per day")
st.write(f"And about {monthly} hours per month")

# Conditional feedback based on the calculation
if yearly > 500:
    st.success(f"You are on track to mastery with {yearly} hours per year!")
elif yearly > 250:
    st.info(f"Good progress! {remaining} more hours to reach 500.")
else:
    st.warning(f"Keep going! You need {remaining} more hours to reach 500.")


# Text input with string processing
name = st.text_input("Enter your name", "Type here...")

if st.button("Submit"):
    # Check if the user has typed a real name
    if name == "Type here..." or name == "":
        st.warning("Please enter your name first.")
    else:
        # Validate: check if name contains only letters and spaces
        name_letters = name.replace(" ", "")
        if not name_letters.isalpha():
            st.error("Name should contain letters only!")
        else:
            # Display string method results
            st.success(generate_greeting(name, gender))
            st.write(f"Uppercase: {name.upper()}")
            st.write(f"Lowercase: {name.lower()}")
            st.write(f"Number of characters: {len(name)}")
            st.write(f"Your name reversed: {name[::-1]}")
            st.write(f"Starts with 'A': {name.upper().startswith('A')}")

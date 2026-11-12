import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="TripMate AI",
    page_icon="✈️",
    layout="wide"
)

# Connect Gemini AI
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Application title
st.title("✈️ TripMate AI")
st.subheader("Your Personal AI Travel Planner")

st.write(
    "Plan your dream trip with the help of Artificial Intelligence!"
)

st.divider()

# Travel information
st.header("🌍 Plan Your Journey")

destination = st.text_input(
    "Where do you want to travel?",
    placeholder="Example: Goa"
)

budget = st.number_input(
    "Your total budget (₹)",
    min_value=1000,
    value=10000,
    step=1000
)

days = st.number_input(
    "Number of travel days",
    min_value=1,
    max_value=30,
    value=3
)

travel_type = st.selectbox(
    "Choose your travel style",
    ["Adventure", "Family", "Romantic", "Solo", "Relaxation"]
)

people = st.number_input(
    "Number of travellers",
    min_value=1,
    max_value=20,
    value=2
)

# Generate travel plan
if st.button("Generate My Travel Plan 🚀"):

    if not destination.strip():
        st.warning("Please enter your destination.")

    else:
        prompt = f"""
        Act as an expert travel planner.

        Create a detailed travel plan.

        Destination: {destination}
        Budget: ₹{budget}
        Number of days: {days}
        Travel style: {travel_type}
        Number of travellers: {people}

        Include:
        1. Introduction to destination
        2. Day-wise itinerary
        3. Estimated budget breakdown
        4. Food recommendations
        5. Accommodation suggestions
        6. Travel tips
        7. Packing checklist

        Keep the plan practical and organized.
        Mention that prices are estimates and need verification.
        """

        try:
            with st.spinner("Creating your travel plan..."):

                response = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=prompt
                )

            st.success("Your travel plan is ready!")

            st.markdown(response.text)

            st.download_button(
                label="Download Travel Plan",
                data=response.text,
                file_name="TripMate_Travel_Plan.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()

st.caption("TripMate AI | Powered by Google Gemini")
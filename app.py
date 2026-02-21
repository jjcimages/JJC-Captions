import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- UI Configuration (Premium Blue Aesthetic) ---
st.set_page_config(page_title="JJC Images | Caption Engine", page_icon="📸", layout="centered")

# Custom CSS for the blue branding
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0047AB;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
    }
    div.stButton > button:first-child:hover {
        background-color: #003380;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📸 JJC Images Caption Engine")
st.markdown("Generate bespoke, modern, and punchy captions for your media.")

# --- API Key Setup ---
api_key = st.text_input("Enter your Gemini API Key to start:", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # --- Layout & Inputs ---
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Upload Media")
        uploaded_file = st.file_uploader("Upload Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Reference Media", use_container_width=True)

    with col2:
        st.subheader("2. Post Settings")
        
        target_audience = st.selectbox("Target Audience", [
            "Realtors & Brokers", 
            "Home Builders & Developers", 
            "STR & Property Management"
        ])
        
        model_type = st.selectbox("Media Model", [
            "Interior", "Exterior", "Drone / Aerial", "Twilight", 
            "Virtual Staging", "Behind-the-Scenes"
        ])
        
        location = st.selectbox("Location", [
            "Marble Falls", "Horseshoe Bay", "Kingsland", "Burnet", "Spicewood", 
            "Granite Shoals", "Buchanan Dam", "Sunrise Beach Village", "Llano",
            "Austin", "Bee Cave", "Lakeway", "Dripping Springs", "West Lake Hills"
        ])
        
        property_size = st.selectbox("Property Size", [
            "Under 2500 sqft", 
            "Over 2500 sqft"
        ])
        
        platform = st.selectbox("Platform", ["Instagram", "TikTok", "LinkedIn", "Facebook"])

    # --- Generation Logic ---
    if st.button("Generate Caption") and uploaded_file is not None:
        with st.spinner("Analyzing image and writing caption..."):
            try:
                # Build the dynamic prompt
                prompt = f"""
                You are the lead social media copywriter for JJC Images, a premium real estate media company. 
                Your tone is professional, laid-back, and friendly.

                CRITICAL RULE: The caption must be extremely short, punchy, and concise—about a quarter of the length of a typical real estate post. Do not write long paragraphs.

                Context for this post:
                - Target Audience: {target_audience}
                - Media Type: {model_type}
                - Location: {location}, Texas
                - Property Size: {property_size}
                - Platform: {platform}

                Instructions:
                1. Write a scroll-stopping hook.
                2. Add 1-2 short sentences of value/story based on the image and context. If 'Under 2500 sqft', emphasize efficient/inviting layouts. If 'Over 2500 sqft', emphasize expansive/grand scale.
                3. Include a Call to Action (CTA) tailored to the target audience (e.g., booking a shoot, upgrading their listing, etc.).
                4. Output exactly 3 to 5 highly relevant hashtags at the bottom. Use #JJCImages and a location tag.

                Adapt the tone slightly for {platform}. If TikTok, make it hyper-casual and extremely brief. If LinkedIn, lean into the B2B professional value of high-quality media.
                """
                
                # Call Gemini Vision Model
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content([prompt, image])
                
                st.success("Caption Generated!")
                st.markdown("### Your Custom Caption:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
elif not api_key:
    st.info("Please enter your Gemini API key to unlock the app.")

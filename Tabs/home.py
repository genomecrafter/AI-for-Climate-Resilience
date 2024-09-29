import streamlit as st

def app():
    # Set the page layout to wide for better appearance
    #st.set_page_config(layout="wide")

    
    # Adding CSS for improved styling, hover effect, and compartmentalization
    st.markdown("""
        <style>
            .main {
                background-color: #f7fbfc;
            }
            .header-title {
                font-family: 'Helvetica', sans-serif;
                color: #4CAF50;
                font-size: 48px;
                margin-bottom: 0px;
            }
            .sub-title {
                font-family: 'Arial', sans-serif';
                color: #2E8B57;
                font-size: 24px;
                margin-bottom: 40px;
            }
            .section {
                background-color: #e0f7fa;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
            }
            .center-image {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 70%;
                transition: transform 0.3s ease;  /* Smooth hover effect */
            }
            .center-image:hover {
                transform: scale(1.2);  /* Enlarges the image by 20% on hover */
            }
            .sdg-info {
                background-color: #e0ffe8;
                padding: 15px;
                border-radius: 10px;
                font-family: 'Georgia', sans-serif;
                color: #00695c;
                line-height: 1.5;
            }
            footer {
                background-color: #f1f8e9;
                padding: 15px;
                font-size: 14px;
                text-align: center;
                color: #555;
            }
            .contact {
                font-family: 'Arial', sans-serif;
                color: #FF5722;
                text-align: center;
                font-size: 18px;
                margin-top: 20px;
            }
            .sdg-button {
                display: block;
                text-align: center;
                margin-top: 20px;
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main header section with event title and subtitle
    st.markdown(
        """
        <div class="section" style="background-color:#c8e6c9;">
            <h2 class="header-title" style="text-align:center;">
                IEEE Sustain Fiesta 2024
            </h2>
            <h4 class="sub-title" style="text-align:center;">
                Young Pros Unite for Green Vibes
            </h4>
        </div>
        """, unsafe_allow_html=True
    )

    # Project title
    st.markdown(
        """
        <div class="section">
            <h1 style="text-align: center; color:#2E7D32;">
                TECH TITANS present: AI for Climate Resilience
            </h1>
        </div>
        """, unsafe_allow_html=True
    )

    # Earth image section with hover effect
    st.markdown(
        """
        <div class="section" style="background-color:#e8f5e9;">
            <img src="https://wmo.int/sites/default/files/styles/featured_image_x1_768x512/public/2023-09/AdobeStock_543104806.jpeg?h=8aa5fa2d&itok=LNk-h0Ct" class="center-image">
        </div>
        """, unsafe_allow_html=True
    )

    # Add SDG and Project Details with the second image hover effect
    st.markdown(
        """
        <div class="sdg-info section" style="background-color: #e0ffe8;">
            <h3 style='text-align:center;'>Sustainable Development Goal (SDG) Related to Climate</h3>
            <p>
                Our project focuses on <strong>SDG 13: Climate Action</strong> - taking urgent action to combat climate change and its impacts. 
                By leveraging artificial intelligence (AI) for climate forecasting, we aim to predict and mitigate the effects of climate change 
                through better data and insights.
            </p>
            <p>
                <strong>Prophet Algorithm:</strong> We use the Prophet algorithm, a time series forecasting model, to analyze climate data and 
                make future predictions, helping communities prepare for and adapt to climate changes.
            </p>
        </div>
        """, unsafe_allow_html=True
    )

    # Button to link to SDG 13 webpage
    st.markdown(
        """
        <div class="sdg-button">
            <a href="https://sdgs.un.org/goals/goal13" target="_blank">
                <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px;">
                    Learn More About SDG 13
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True
    )

    # Second image with hover effect below the button
    st.markdown(
        """
        <div class="section" style="background-color:#e0f7fa;">
            <img src="https://www.canterbury.ac.nz/content/dam/uoc-main-site/images/6-graphics/c-sdg-graphics/sdg-rectangle-graphics-2024/sdg-13-rectangle.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg" class="center-image">
        </div>
        """, unsafe_allow_html=True
    )

    # Call to action/participation section
    st.markdown(
        """
        <div class="section" style="background-color:#ffe0b2;">
            <h2 style='text-align:center;'>Join the Mission</h2>
            <p style='text-align:center; font-size:18px;'>
                Together, we can build a sustainable future through AI and innovation.<br> 
                Get involved and be part of the solution!
            </p>
            <p class="contact">Contact Us: <strong>dhu0918@gmail.com</strong></p>
        </div>
        """, unsafe_allow_html=True
    )

    # Footer section
    st.markdown(
        """
        <footer>
            <small>© 2024 IEEE Sustain Fiesta - AI for Climate Resilience by TECH TITANS</small>
        </footer>
        """, unsafe_allow_html=True
    )

# Call the app function
if __name__ == "__main__":
    app()



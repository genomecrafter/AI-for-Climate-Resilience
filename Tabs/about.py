
import streamlit as st

def app():
    # Set the page layout to wide
    #st.set_page_config(layout="wide")

    # Title of the page
    st.title("TECH TITANS")

    # Add CSS for table styling
    st.markdown("""
        <style>
        .team-table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }
        .team-table th, .team-table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        .team-table th {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
        }

        .team-table tr:hover {
            background-color: #ddd;
        }
        .team-table td {
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display the table using HTML for flexibility
    st.markdown("""
        <table class="team-table">
            <thead>
                <tr>
                    <th>Sl. No.</th>
                    <th>Name</th>
                    <th>Branch</th>
                    <th>Institution</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Dhruthi Rudrangi</td>
                    <td>ISE</td>
                    <td>RVCE</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Nikita S Raj Kapini</td>
                    <td>CSE</td>
                    <td>RVCE</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Tulya Reddy Y</td>
                    <td>CSE</td>
                    <td>RVCE</td>
                </tr>
            </tbody>
        </table>
    """, unsafe_allow_html=True)

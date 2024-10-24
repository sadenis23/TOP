import streamlit as st
import json

# Sample report data (fictional)
report_data = [
    {
        "title": "2024 Sales Report",
        "author": "Alice Johnson",
        "date": "2024-10-01",
        "description": "A comprehensive analysis of the sales performance for 2024.",
        "link": "https://example.com/reports/2024-sales",
        "image": "https://via.placeholder.com/150"  # Placeholder image
    },
    {
        "title": "2023 Marketing Overview",
        "author": "Bob Smith",
        "date": "2023-12-20",
        "description": "Detailed insights into the marketing campaigns of 2023.",
        "link": "https://example.com/reports/2023-marketing",
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "Customer Satisfaction Survey 2024",
        "author": "Clara Davis",
        "date": "2024-09-15",
        "description": "Findings from the customer satisfaction survey conducted in Q3 2024.",
        "link": "https://example.com/reports/customer-satisfaction-2024",
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "Product Development Report",
        "author": "Daniel Lee",
        "date": "2024-08-30",
        "description": "An in-depth review of the product development efforts for the year.",
        "link": "https://example.com/reports/product-development-2024",
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "New Product Launch 2024",
        "author": "Emma Wilson",
        "date": "2024-07-15",
        "description": "The official report of the launch of the new product line for 2024.",
        "link": "https://example.com/reports/product-launch-2024",
        "image": "https://via.placeholder.com/150"
    }
]

# Function to load report data (since it's already embedded here, no file read)
def load_report_data():
    """
    Returns a list of report data.
    """
    return report_data

# Reusable function to render report card in a column
def report_list_item(report):
    """
    Renders a horizontally aligned report item.
    """
    # Use a horizontal container (columns) for a list-like appearance
    col1, col2 = st.columns([1, 4])  # Adjust the ratio between image and text

    # Column for the image
    with col1:
        st.image(report['image'], width=120)

    # Column for the report information
    with col2:
        # Title with larger font size and bold
        st.markdown(f"<h3 style='margin-bottom: 5px;'>{report['title']}</h3>", unsafe_allow_html=True)
        # Display metadata: author and date
        st.markdown(f"<p style='color: #555; font-size: 14px;'>Author: {report['author']} | Date: {report['date']}</p>", unsafe_allow_html=True)
        # Short description of the report
        st.markdown(f"<p style='font-size: 16px; line-height: 1.6;'>{report['description']}</p>", unsafe_allow_html=True)
        # Link to view the full report, styled as a button
        st.markdown(f"<a href='{report['link']}' target='_blank' style='text-decoration: none;'>"
                    f"<button style='background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; border-radius: 5px; cursor: pointer;'>📄 View Full Report</button>"
                    f"</a>", unsafe_allow_html=True)
    
    # Add a horizontal divider between items
    st.markdown("<hr style='border: none; height: 1px; background-color: #ddd;'>", unsafe_allow_html=True)


# Main Streamlit app
st.set_page_config(layout="wide")  # Set Streamlit to use the full page width

st.title("Top Reports in the Organization")

# Load report metadata (using the embedded report data)
reports = load_report_data()

# Sidebar for filtering and sorting
st.sidebar.header("Filter & Sort Options")
filter_author = st.sidebar.selectbox("Filter by Author", ["All"] + list(set(report['author'] for report in reports)))
sort_by = st.sidebar.selectbox("Sort by", ["Date", "Title"])

# Filter reports by selected author
if filter_author != "All":
    reports = [r for r in reports if r['author'] == filter_author]

# Sort reports based on user selection
if sort_by == "Date":
    reports = sorted(reports, key=lambda x: x['date'], reverse=True)
elif sort_by == "Title":
    reports = sorted(reports, key=lambda x: x['title'])

# Display report count
st.markdown(f"### Showing {len(reports)} reports", unsafe_allow_html=True)

# Display the reports in a horizontal list style
for report in reports:
    report_list_item(report)

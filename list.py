import streamlit as st
from urllib.parse import urlencode, quote
import re

# Helper function to generate a custom URL from the report's title and date
def generate_custom_url(report):
    """Generates a URL using the report title and date."""
    title_sanitized = re.sub(r'\W+', '-', report['title'].lower()).strip('-')
    return f"https://example.com/reports/{title_sanitized}-{report['date']}"

# Sample report data (fictional) with custom URLs
report_data = [
    {
        "title": "2024 Sales Report",
        "author": "Alice Johnson",
        "date": "2024-10-01",
        "description": (
            "This comprehensive report covers the sales performance for the year 2024, highlighting "
            "key trends, regional performance, and product line analysis. The report includes detailed "
            "metrics on revenue growth, market share, and sales targets for the year."
        ),
        "details": {
            "Revenue Growth": "15% year-over-year increase in total revenue.",
            "Top Performing Regions": "North America (30% growth), Europe (25% growth), APAC (20% growth).",
            "Product Line Breakdown": "Electronics (50% of sales), Clothing (30%), Home Appliances (20%).",
            "Key Metrics": "Total Sales: $12.5M | New Customers: 8,000+ | Repeat Purchase Rate: 45%"
        },
        "link": generate_custom_url({"title": "2024 Sales Report", "date": "2024-10-01"}),
        "image": "https://via.placeholder.com/150"  # Placeholder image
    },
    {
        "title": "2023 Marketing Overview",
        "author": "Bob Smith",
        "date": "2023-12-20",
        "description": (
            "This report offers a detailed overview of the marketing campaigns executed in 2023. "
            "It includes performance metrics from key campaigns, return on investment (ROI), and "
            "the strategies used to grow brand awareness and customer engagement."
        ),
        "details": {
            "Top Campaigns": "Summer Product Launch Campaign, Holiday Discount Campaign, Influencer Marketing Campaign.",
            "ROI Metrics": "Average ROI across campaigns: 350%. Influencer marketing contributed 40% to overall sales.",
            "Customer Engagement": "Social media engagement grew by 25%, email open rates increased by 12%.",
            "Advertising Spend": "Total advertising spend: $1.2M | Customer acquisition cost: $45"
        },
        "link": generate_custom_url({"title": "2023 Marketing Overview", "date": "2023-12-20"}),
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "Customer Satisfaction Survey 2024",
        "author": "Clara Davis",
        "date": "2024-09-15",
        "description": "Findings from the customer satisfaction survey conducted in Q3 2024.",
        "link": generate_custom_url({"title": "Customer Satisfaction Survey 2024", "date": "2024-09-15"}),
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "Product Development Report",
        "author": "Daniel Lee",
        "date": "2024-08-30",
        "description": "An in-depth review of the product development efforts for the year.",
        "link": generate_custom_url({"title": "Product Development Report", "date": "2024-08-30"}),
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "New Product Launch 2024",
        "author": "Emma Wilson",
        "date": "2024-07-15",
        "description": "The official report of the launch of the new product line for 2024.",
        "link": generate_custom_url({"title": "New Product Launch 2024", "date": "2024-07-15"}),
        "image": "https://via.placeholder.com/150"
    }
]

# Function to load report data (since it's already embedded here, no file read)
def load_report_data():
    """
    Returns a list of report data.
    """
    return report_data

# Reusable function to render a single report item in the list
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
        
        # Add link to view the full report (using query parameters for routing)
        params = urlencode({"report": report['title']})
        view_link = f"?{params}"
        st.markdown(f"<a href='{view_link}' style='text-decoration: none;'>"
                    f"<button style='background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; border-radius: 5px; cursor: pointer;'>📄 View Full Report</button>"
                    f"</a>", unsafe_allow_html=True)

    # Add a horizontal divider between items
    st.markdown("<hr style='border: none; height: 1px; background-color: #ddd;'>", unsafe_allow_html=True)


# Function to show full details of a single report
def show_report_details(report):
    """
    Displays full details of a single report.
    """
    st.image(report['image'], width=300)
    st.markdown(f"## {report['title']}")
    st.markdown(f"**Author:** {report['author']}  |  **Date:** {report['date']}")
    st.write(report['description'])

    # Show additional detailed information if available
    if 'details' in report:
        st.markdown("### Key Highlights:")
        for key, value in report['details'].items():
            st.markdown(f"**{key}:** {value}")
    
    st.markdown(f"[📄 View Full Report External Link]({report['link']})")

    # Back button to go back to the list
    st.markdown("<a href='/' style='text-decoration: none;'>"
                f"<button style='background-color: #4CAF50; color: white; border: none; padding: 10px 20px; text-align: center; border-radius: 5px; cursor: pointer;'>🔙 Back to Reports</button>"
                f"</a>", unsafe_allow_html=True)


# Main Streamlit app
st.set_page_config(layout="wide")

# Load report metadata
reports = load_report_data()

# Parse the query parameters to check if a report is selected
query_params = st.query_params
selected_report_title = query_params.get('report', [None])[0]

# Check if a specific report is selected for viewing full details
if selected_report_title:
    # Find the selected report by title
    selected_report = next((r for r in reports if r['title'] == selected_report_title), None)
    
    if selected_report:
        show_report_details(selected_report)
    else:
        st.write("Report not found.")
else:
    # If no report is selected, show the list of reports
    st.title("📊 Top Reports in the Organization")

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

    # Display the list of reports
    for report in reports:
        report_list_item(report)

import streamlit as st


def generate_blog(title, sections, points, style, industry, terminologies, sentiment):
    # Simulated blog content generation
    blog_content = f"Generated Blog Content:\n\nTitle: {title}\n\n"
    for section, point in zip(sections, points):
        blog_content += f"## {section}\n- {point}\n\n"
    blog_content += f"\nWriting Style: {style}, Industry: {industry}, Sentiment: {sentiment}\n"
    return blog_content


def generate_seo_metadata(title, blog_content):
    # Simulated SEO metadata and title tags generation
    seo_metadata = {
        "SEO Title": f"{title} - Optimized for Search",
        "SEO Description": f"A brief overview of the content related to {title}.",
        "SEO Keywords": "blog, AI, generation, content, SEO"
    }
    return seo_metadata

st.title("AI-Powered Blog Generation System")

st.header("Blog Outline")
title = st.text_input("Blog Title", value="Enter your blog title")
sections = st.text_area("Sections (comma-separated)", value="Introduction, Main Body, Conclusion").split(',')
points = st.text_area("Points under each section (comma-separated for each section)", value="Point1, Point2").split(',')

# Writing style, industry, and terminologies input
st.header("Customization Options")
style = st.selectbox("Select Writing Style", ["Formal", "Academic", "Research", "Casual", "Marketing"])
industry = st.text_input("Industry Input", value="Enter industry (e.g., Technology, Healthcare)")
terminologies = st.text_area("Custom Terminologies (comma-separated)", value="AI, Machine Learning, Data Science")
sentiment = st.selectbox("Select Sentiment", ["Positive", "Negative", "Neutral"])


if st.button("Generate Blog"):
    if title and sections and points:
       
        blog_content = generate_blog(title, sections, points, style, industry, terminologies, sentiment)
        
        st.subheader("Generated Blog Content")
        st.write(blog_content)
        
        seo_metadata = generate_seo_metadata(title, blog_content)

        st.subheader("Generated SEO Metadata")
        st.write(seo_metadata)
    else:
        st.error("Please fill in all the required fields.")

st.markdown("---")
st.caption("Developed with ❤️ by Sanchit Baweja")

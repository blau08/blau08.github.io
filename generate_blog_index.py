import os
import yaml
from datetime import datetime

# Directory containing blog posts
blog_dir = 'docs'
# Output file for blog index
output_file = os.path.join(blog_dir, 'blog-index.md')

# Function to read metadata from a markdown file
def read_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                metadata = yaml.safe_load(content[3:end])
                return metadata
    return {}

# Collect metadata from all blog posts
posts = []
for filename in os.listdir(blog_dir):
    if filename.endswith('.md') and filename != 'blog-index.md':
        file_path = os.path.join(blog_dir, filename)
        metadata = read_metadata(file_path)
        if 'date' in metadata:
            metadata['filename'] = filename
            posts.append(metadata)

# Sort posts by date
posts.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)

# Generate blog index content
index_content = "# Blog Index\n\nWelcome to the Blog Index page. Here you can find all the blog posts in one place.\n\n## All Blog Posts\n\n"
for post in posts:
    index_content += f"- [{post.get('title', 'Untitled')}]({post['filename']}) - Posted on: {post['date']}\n"

# Write to blog index file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(index_content)

print(f"Blog index generated at {output_file}")

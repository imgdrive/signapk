import os
import requests

def markdown_to_html_via_github_api(markdown):
    headers = {"Content-Type": "text/plain", "charset": "utf-8"}
    return str(
        requests.post("https://api.github.com/markdown/raw", headers=headers, data=markdown.encode("utf-8")).content,
        encoding="utf-8"
    )

def markdown_to_html(intput_md_file, output_html_file):
    with open(intput_md_file, "r") as f:
        # Converts markdown to html, using the github api
        md_content = f.read()
        html_content = markdown_to_html_via_github_api(md_content)

        # Write html file
        with open(output_html_file, "w") as f:
            f.write("<!DOCTYPE html><html lang=\"en\"><head>\n")
            f.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n")
            f.write("<title>")
            f.write(intput_md_file.replace(".md", ""))
            f.write("</title>\n")
            f.write("<link href=\"github-markdown.css\" rel=\"stylesheet\" type=\"text/css\">\n")
            f.write("</head><body><div class=\"markdown-body\">\n")
            f.write(html_content)
            f.write("</div></body></html>")

# Convert all .md files to .html in current directory
files = os.listdir(".")
for name in files:
    if name.endswith(".md"):
        print("markdown_to_html "+name)
        markdown_to_html(name, name.replace(".md", ".html"))
print("Finish!")

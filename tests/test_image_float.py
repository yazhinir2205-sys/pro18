import os
import sys
from bs4 import BeautifulSoup


FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "starter",
    "index.html"
)

TOTAL_MARKS = 50
score = 0


def passed(message, marks):
    global score
    score += marks
    print(f"PASS: {message} [{marks} marks]")


def failed(message):
    print(f"FAIL: {message} [0 marks]")


# =========================================================
# File check
# =========================================================

if not os.path.exists(FILE):
    print("ERROR: starter/index.html was not found.")
    sys.exit(1)


with open(FILE, "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

style = soup.find("style")
css = style.get_text(" ", strip=True) if style else ""


# =========================================================
# 1. HTML DOCUMENT STRUCTURE - 5 MARKS
# =========================================================

print("\n1. HTML DOCUMENT STRUCTURE")

if soup.find("html"):
    passed("<html> exists", 1)
else:
    failed("<html> is missing")

if soup.find("head"):
    passed("<head> exists", 1)
else:
    failed("<head> is missing")

if soup.find("body"):
    passed("<body> exists", 1)
else:
    failed("<body> is missing")

title = soup.find("title")

if title and title.get_text(strip=True) == "Image float":
    passed("Correct page title", 2)
else:
    failed("Page title must be 'Image float'")


# =========================================================
# 2. HEADING - 5 MARKS
# =========================================================

print("\n2. HEADING")

h2 = soup.find("h2")

expected_heading = (
    "Teach your students using the books the professionals use"
)

if h2:
    passed("<h2> exists", 2)
else:
    failed("<h2> is missing")

if h2 and h2.get_text(" ", strip=True) == expected_heading:
    passed("Correct heading text", 3)
else:
    failed("Heading text is incorrect")


# =========================================================
# 3. BODY STYLING - 7 MARKS
# =========================================================

print("\n3. BODY STYLING")

body_requirements = [
    ("font-family", 1, "Font family is specified"),
    ("font-size: 85%", 1, "Font size is 85%"),
    ("width: 650px", 2, "Body width is 650px"),
    ("margin: 0 auto", 1, "Body is centered"),
    ("padding: 1em", 1, "Body padding is 1em"),
]

for css_value, marks, message in body_requirements:
    if css_value in css:
        passed(message, marks)
    else:
        failed(f"Missing CSS: {css_value}")


# =========================================================
# 4. IMAGE AND ACCESSIBILITY - 8 MARKS
# =========================================================

print("\n4. IMAGE AND ACCESSIBILITY")

img = soup.find("img")

if img:
    passed("Image exists", 2)
else:
    failed("Image is missing")

if img and img.get("alt") == "teacher and students":
    passed("Correct alt text", 2)
else:
    failed("Incorrect or missing alt text")

if img and img.get("width") == "192":
    passed("Image width is 192", 1)
else:
    failed("Image width must be 192")

if img and img.get("height") == "128":
    passed("Image height is 128", 1)
else:
    failed("Image height must be 128")

if img and img.get("longdesc"):
    passed("Long description exists", 2)
else:
    failed("Long description is missing")


# =========================================================
# 5. IMAGE FLOAT - 10 MARKS
# =========================================================

print("\n5. IMAGE FLOAT")

if "float: left" in css:
    passed("Image floats left", 6)
else:
    failed("Image must use float: left")

if "margin-top: 10px" in css:
    passed("Image has 10px top margin", 1)
else:
    failed("Image top margin must be 10px")

if "margin-bottom: 10px" in css:
    passed("Image has 10px bottom margin", 1)
else:
    failed("Image bottom margin must be 10px")

if "img" in css:
    passed("Image has a CSS rule", 2)
else:
    failed("Image CSS rule is missing")


# =========================================================
# 6. UNORDERED LIST - 7 MARKS
# =========================================================

print("\n6. UNORDERED LIST")

ul = soup.find("ul")

if ul:
    passed("<ul> exists", 2)
else:
    failed("<ul> is missing")

items = ul.find_all("li") if ul else []

if len(items) == 3:
    passed("Exactly three list items", 3)
else:
    failed("There must be exactly three list items")

if "margin-left: 210px" in css:
    passed("List has 210px left margin", 2)
else:
    failed("List must have margin-left: 210px")


# =========================================================
# 7. CLEAR PROPERTY - 5 MARKS
# =========================================================

print("\n7. CLEAR PROPERTY")

last = soup.find(id="last")

if last:
    passed("Final paragraph has id='last'", 2)
else:
    failed("Final paragraph must have id='last'")

if "#last" in css:
    passed("#last CSS selector exists", 1)
else:
    failed("#last CSS selector is missing")

if "clear: left" in css:
    passed("Left float is cleared", 2)
else:
    failed("The final paragraph must use clear: left")


# =========================================================
# 8. SPACING AND TYPOGRAPHY - 3 MARKS
# =========================================================

print("\n8. SPACING AND TYPOGRAPHY")

if "line-height: 1.3" in css:
    passed("Line height is 1.3", 1)
else:
    failed("Line height must be 1.3")

if "margin: 0" in css:
    passed("Paragraph margin is zero", 1)
else:
    failed("Paragraph margin must be zero")

if "padding-left: 1em" in css:
    passed("List padding-left is 1em", 1)
else:
    failed("List padding-left must be 1em")


# =========================================================
# FINAL RESULT
# =========================================================

score = min(score, TOTAL_MARKS)

print("\n" + "=" * 60)
print("IMAGE FLOAT ASSIGNMENT")
print("=" * 60)
print(f"FINAL SCORE: {score}/{TOTAL_MARKS}")

if score == TOTAL_MARKS:
    print("RESULT: PASS")
else:
    print("RESULT: REVIEW REQUIRED")

print("=" * 60)

sys.exit(0)

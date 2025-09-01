from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER

# Output path for PDF
pdf_path = "D:/COLLAGE/7TH SEM/SEMINAR 2025/Micro_Robotics_Report.pdf"

# Create document
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(name="CenterTitle", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, spaceAfter=20))
styles.add(ParagraphStyle(name="HeadingCustom", parent=styles["Heading2"], fontSize=14, spaceAfter=10))
styles.add(ParagraphStyle(name="NormalCustom", parent=styles["Normal"], fontSize=11, spaceAfter=6))

story = []

# Title Page
story.append(Paragraph("Micro-Robotics: The Tiny Revolution in Technology", styles["CenterTitle"]))
story.append(Paragraph("By Arjun Murmu", styles["HeadingCustom"]))
story.append(Spacer(1, 40))

# Content sections
sections = {
    "Introduction": [
        "Micro-robots are extremely small robots designed to perform tasks at the micrometer or millimeter scale. "
        "Their importance lies in their ability to work in environments where traditional robots cannot operate."
    ],
    "Key Characteristics": [
        "Size: Micrometer to a few millimeters",
        "Lightweight but functional",
        "Often bio-inspired designs",
        "High precision and efficiency"
    ],
    "Types of Micro-Robots": [
        "Medical: drug delivery, minimally invasive surgery, diagnostics",
        "Industrial: micro-assembly, electronics manufacturing, maintenance in tight spaces",
        "Environmental: pollution cleanup, water quality monitoring, underwater exploration",
        "Military: surveillance, reconnaissance, disarming explosives",
        "Research: biological studies, materials science"
    ],
    "How Micro-Robots Work": [
        "Powered by magnetic, chemical, acoustic, or optical energy",
        "Movement via micro-actuators or bio-inspired propulsion",
        "Controlled externally or autonomously",
        "Swarm behavior for collective tasks",
        "Example: Clearing blocked blood vessels or manipulating liquid metals"
    ],
    "Applications - Medical": [
        "Targeted drug delivery",
        "Non-invasive surgery",
        "Cancer therapy",
        "Tissue regeneration"
    ],
    "Applications - Industrial": [
        "Micro-assembly of electronics",
        "Inspection and maintenance of machines",
        "Micro-scale 3D printing"
    ],
    "Applications - Environmental": [
        "Water purification",
        "Oil spill cleanup",
        "Microplastic removal"
    ],
    "Applications - Military": [
        "Surveillance in hostile environments",
        "Explosive disposal",
        "Reconnaissance missions"
    ],
    "Advantages": [
        "High precision",
        "Minimal invasiveness",
        "Access to confined or dangerous spaces",
        "Efficiency in micro-scale tasks"
    ],
    "Challenges & Limitations": [
        "Limited power sources",
        "Complex control and navigation",
        "Safety and ethical concerns",
        "Short operational lifetime",
        "Complex fabrication techniques",
        "High cost of fabrication",
        "Risk of malfunction inside the human body",
        "Dependence on external control systems"
    ],
    "Recent Innovations": [
        "Swarm robots inspired by ants and bees",
        "Medical bots for clearing blocked vessels",
        "Self-assembling and shape-changing robots",
        "Space microbots under NASA research",
        "Research from Drexel University and Korean scientists"
    ],
    "Case Studies": [
        "Medical nanobots for cancer treatment delivering drugs directly to tumors",
        "Screw-shaped millirobots controlled by magnets to move against blood flow",
        "Environmental microbots for removing microplastics from water"
    ],
    "Future Scope": [
        "AI integration for autonomous navigation",
        "Personalized medicine using patient-specific bots",
        "Large-scale industrial automation",
        "Environmental sustainability (climate monitoring, microplastic cleanup)",
        "Military and defense applications"
    ],
    "Conclusion": [
        "Micro-robots represent a revolutionary step in robotics.",
        "They hold immense potential in medicine, environment, and industry.",
        "Despite challenges, ongoing research is promising.",
        "“Small robots, big impact.”"
    ]
}

# Build story
for section, content in sections.items():
    story.append(Paragraph(section, styles["HeadingCustom"]))
    for item in content:
        story.append(Paragraph(f"- {item}", styles["NormalCustom"]))
    story.append(Spacer(1, 15))

# Build PDF
doc.build(story)

pdf_path

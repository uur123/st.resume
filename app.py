from pathlib import Path

import streamlit as st

from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir/ "assets" / "CV.pdf"
profile_pic = current_dir/ "assets" / "profile.jpeg"




#--- General Setting ---

PAGE_TITLE = "DIGITAL CV | Yasin Ugur Kayran"
PAGE_ICON = ":wave:"
NAME = "Ugur Kayran"
DESCRIPTION = """
I am a results-driven chemist with a strong foundation in analytical techniques. 
 I bring technical expertise to every project. """
EMAIL = "kayran.ugur@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/ugurkayran/",
    "Google Scholar" : "https://scholar.google.com/citations?user=rC0kXIYAAAAJ&hl=en",
    "ResearchGate": "https://www.researchgate.net/profile/Ugur-Kayran"
}

PROJECTS = {
    "*A Ready-to-Use Electrochemical Kit Design for the Diagnosis of Single Nucleotide Polymorphisms": "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/elan.201300386",
    "A Pencil Graphite Electrode In Situ Modified by Monovalent Copper: a Promising Tool for the Determination of Methylxanthines" : "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/elan.201400017",
    "*Selection of Highly SERS-Active Nanostructures from a Size Gradient of Au Nanovoids on a Single Bipolar Electrode" : "https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/celc.201500423",
    "Differentiation between single‐ and double‐stranded DNA by local capacitance measurements": "https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/celc.201600075",
    "Traditional earth-abundant coal as new energy materials to catalyze the oxygen reduction reaction in alkaline solution":"http://dx.doi.org/10.1016/j.electacta.2016.05.137",
    "Few-layer graphene modified with nitrogen-rich metallomacrocyclic complexes as precursor for bifunctional oxygen electrocatalysts":"https://www.sciencedirect.com/science/article/abs/pii/S0013468616324239?via%3Dihub",
    "*Cystic Fibrosis Mutation Detection with SPR Biosensor in Real Samples via Multiple Surfaces Binding Method":"https://www.eurekaselect.com/article/80776",
    "DNA-wrapped multi-walled carbon nanotube modified electrochemical biosensor for the detection of Escherichia coli from real samples":"https://www.sciencedirect.com/science/article/abs/pii/S0039914017300048?via%3Dihub",
    "Unraveling compositional effects on the light-induced oxygen evolution in Bi(V-Mo-X)O4 material libraries":"https://pubs.rsc.org/en/content/articlelanding/2017/EE/C7EE00287D",
    "Cobalt boride modified with N-doped carbon nanotubes as high-performance bifunctional oxygen electrocatalyst":"https://pubs.rsc.org/en/content/articlelanding/2017/TA/C7TA06995B",
    "*Monitoring potential-induced DNA dehybridization kinetics for SNP detection using in-situ surface enhanced Raman scattering":"https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/celc.201701220",
    "Local Surface Modifications Investigated by Combining Scanning Electrochemical Microscopy and Surface-Enhanced Raman Scattering":"https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cplu.201800031",
    "*Nanostructured DNA Microarrays for Dual SERS and Electrochemical Read-out":"https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/elan.201800579",
    "Optimized Ag Nanovoid Structures for Probing Electrocatalytic Carbon Dioxide Reduction Using Operando Surface-Enhanced Raman Spectroscopy":"https://pubs.acs.org/doi/10.1021/acs.langmuir.8b02501",
    "Controlling DNA/Surface Interactions for Potential Pulse‐Assisted Preparation of Multi‐Probe DNA Microarrays":"https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/elan.201900233",
    "CoFe–OH Double Hydroxide Films Electrodeposited on Ni-Foam as Electrocatalyst for the Oxygen Evolution Reaction":"https://www.degruyter.com/document/doi/10.1515/zpch-2019-1466/html",

}


st.set_page_config(page_title= PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF  & Profil pic ----

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Hero Section ---
col1, col2 = st.columns(2,gap= "small")
with col1:
    st.image(profile_pic, width=270)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label =":clipboard: Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    st.write(":mailbox:" , EMAIL)


 # --- Social links ---   

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# -- Experience and qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- :white_check_mark: Experienced Analytical chemist, hands on chemical and physical material characterization
- :white_check_mark: 3 years lab management experience, team of 6 researchers
- :white_check_mark: Health and safety coordinator, detail oriented 
- :white_check_mark: Team player, consistently collaborating with colleagues to drive shared goals in multicultural work environment

"""
)

# --- Skills ---

st.write("#")
st.subheader("Hard Skills")
st.write(
    """

- :microscope:  Surface characterization , SEM, EDX, optical microscopy
- :sunrise: Chemical analysis, ICP_OES, XRF, XRD
- :thermometer: Thermal gravimetric analysis, STA, dilatometer
- :bar_chart:  Data Analysis, Python programing, Pandas
- :jigsaw:  Management, Analytical service lab management
"""
)


# --- Work Histroy ---
st.write("#")
st.subheader("🧰" "Work Experience")
st.write("---")

# --- Job 1
st.write("#")
st.subheader("📊" "**Analytical Lab Manager | Foseco Nederland BV**")
st.write("01/2020 - Present")

st.write(
    """

- Overseeing and guiding team members for higher performance
- Develop methods for requested analysis
- Organize the training sessions for the researchers in the Analytical team
- Audit the concluded reports, and ensure data integrity
- Ensure a well-organized and safe working environment

"""
)

# --- Job 2
st.write("#")
st.subheader("🔍"  "**HSE Officer | Foseco Nederland BV**")
st.write("01/2019 - Present")

st.write(
    """

- Regulate and monitor the monthly safety audits
- Organize safety training sessions
- Inform colleagues about the safety standards and policies 
- Support the HSE manager

"""
)

# --- Job 3
st.write("#")
st.subheader("🔬"  "**Analytical Chemist | Foseco Nederland BV**")
st.write("07/2018 - 01/2020")

st.write(
    """

- Perform chemical analysis for ongoing investigations in the research center.
- Report the analysis results with high accurracy and realiability
- Organize the training sessions for the researchers in the Analytical team
- Organize the maintenance and calibration services of the instruments in the analytical lab

"""
)


# --- Educational Background ---
st.write("#")
st.subheader("🎓" "Educational Background")
st.write("---")

# --- PhD 1
st.write("#")
st.subheader("**PhD | Ruhr University Bochum, Germany**")
st.write("04/2014 - 12/2017")

st.write(
    """

- Faculty of Chemistry and Biochemistry
- “Fabrication and characterization of tunable plasmonic nanovoid structures and their application in DNA/RNA hybridization assays”

"""
)

# --- Master 2
st.write("#")
st.subheader("**Master in Science | Ege University Izmir, Turkey**")
st.write("09/2009 - 02/2012")

st.write(
    """

- Analytical Chemistry Department, Institute of Health Sciences
- “The design and applications of optical (SPR Based) and electrochemical biosensors for genetic diseases and microorganism detection”

"""
)

# --- Bachelor 1
st.write("#")
st.subheader( "**Bachelor's Degree | Ege University Izmir, Turkey**")
st.write("09/2005 - 07/2009")

st.write(
    """

- Biochemistry Department, Faculty of Science 

"""
)


# --- Publications ---

st.write("#")
st.subheader("Publications")
st.write("---")
st.write("*" "first author")

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
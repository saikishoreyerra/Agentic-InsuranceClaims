"""Generate localized Indian insurance sample PDFs for RAG ingestion."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from config.settings import PROJECT_ROOT

ROOT_DIR = str(PROJECT_ROOT)

def create_pdf(filename, title, content_paragraphs):
    """Utility function to compile structured sample PDFs using ReportLab"""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'], spaceAfter=12, fontSize=14, leading=18
    )
    body_style = ParagraphStyle(
        'DocBody', parent=styles['BodyText'], spaceAfter=10, fontSize=10, leading=14
    )

    story = [Paragraph(f"<b>{title}</b>", title_style), Spacer(1, 10)]
    for paragraph_text in content_paragraphs:
        story.append(Paragraph(paragraph_text, body_style))

    doc.build(story)
    print(f"  Successfully generated: {filename}")

# Target folders
POLICY_DIR = os.path.join(ROOT_DIR, "data/policies")
ENDORSEMENT_DIR = os.path.join(ROOT_DIR, "data/endorsements")
REGULATION_DIR = os.path.join(ROOT_DIR, "data/regulations")

os.makedirs(POLICY_DIR, exist_ok=True)
os.makedirs(ENDORSEMENT_DIR, exist_ok=True)
os.makedirs(REGULATION_DIR, exist_ok=True)



def generate_all_sample_pdfs():
    """Generate all localized Indian insurance sample PDFs into data/."""
    print("\nGenerating PDFs for Policies, Endorsements, and Regulations...")
    # --- 1. HOME INSURANCE PORTFOLIO ---
    home_policy = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0001V2026 | <b>Insurer:</b> Bharat General Insurance Ltd.",
        "<b>SECTION I: STANDARD FIRE & SPECIAL PERILS (BUILDING)</b><br/>This policy covers physical loss or damage to the insured building structure directly caused by natural perils including Fire, Lightning, Earthquake, Storm, Cyclone, Flood, and Inundation (STFI) as per standard Indian residential clauses.",
        "<b>SECTION II: GENERAL EXCLUSIONS</b><br/>The company shall not be liable for any loss, damage, or structural failure caused directly or indirectly by: (a) Normal wear and tear, gradual depreciation, or atmospheric conditions. (b) Loss due to Burglary or Theft if the residential premises are left unoccupied for more than 30 consecutive days. (c) Short-circuiting or electrical breakdown of home appliances unless causing an actual fire spread.",
        "<b>SECTION III: CONDITIONS PRECEDENT TO LIABILITY</b><br/>The insured must notify the company immediately upon the occurrence of a peril and submit a fully executed internal survey request along with a detailed list of damages within 15 days from the date of the incident."
    ]
    create_pdf(os.path.join(POLICY_DIR, "home_base_policy.pdf"), "Bharat Griha Raksha - Home Insurance Policy", home_policy)

    home_endorsement = [
        "<b>Endorsement Add-on Wordings:</b> BGI-ADD-ELEC-2026 | <b>Attachment to UIN:</b> IRDAN123P0001V2026",
        "<b>ADD-ON COVER: MECHANICAL & ELECTRICAL BREAKDOWN RIDER</b><br/>In consideration of the payment of an additional premium, it is hereby agreed that this policy is extended to cover sudden and accidental internal mechanical or electrical breakdown of home appliances (specifically Air Conditioners and Television sets) up to a maximum Sum Insured of Rs. 50,000.",
        "<b>SPECIFIC EXCLUSIONS TO THIS RIDER</b><br/>This add-on explicitly excludes depreciation, standard wear and tear, or defects covered under a manufacturer's warranty."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "home_electrical_rider.pdf"), "Add-on Endorsement: Electrical Breakdown Cover", home_endorsement)

    home_regulation = [
        "<b>Regulatory Notification:</b> IRDAI/NL/REG/2026 | <b>Effective Date:</b> February 2026",
        "<b>IRDAI PROTECTION OF POLICYHOLDERS' INTERESTS REGULATIONS (HOME)</b><br/>Pursuant to updated statutory guidelines, every general insurance company operating in India must appoint an independent surveyor within 72 hours of receiving a home property damage claim notification.",
        "The surveyor must submit their final report to the insurer within 30 days of appointment. Upon receipt of the surveyor's report, the insurer is legally mandated to either offer a claim settlement or issue a formal rejection notice within 30 days."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_home_claims_regulation.pdf"), "IRDAI (Property Settlement Timelines) Regulations", home_regulation)

    # --- EXPANDED HOME SCENARIOS (1 to 5) ---
    home_renter = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0005V2026 | <b>Product:</b> Bharat Griha Renters Shield",
        "<b>SECTION I: CONTENTS COVERAGE</b><br/>Covers physical loss or damage to household contents, furniture, and personal electronics within rented premises caused by Fire, Flood, or Explosion up to Rs. 5,00,000."
    ]
    create_pdf(os.path.join(POLICY_DIR, "home_renter_policy.pdf"), "Bharat Griha Renters Policy", home_renter)

    home_burglary_rider = [
        "<b>Endorsement UIN:</b> BGI-ADD-BURG-2026 | <b>Attachment to UIN:</b> IRDAN123P0005V2026",
        "<b>ADD-ON COVER: BURGLARY & THEFT</b><br/>Extends coverage to loss of contents resulting from burglary, housebreaking, or theft without requiring forcible physical entry up to Rs. 2,00,000."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "home_burglary_rider.pdf"), "Add-on Endorsement: Burglary & Theft", home_burglary_rider)

    home_renter_reg = [
        "<b>Regulatory Notification:</b> IRDAI/NL/RENT/2026",
        "<b>IRDAI TENANT RELOCATION DIRECTIVE</b><br/>Insurers must disburse a emergency relocation allowance within 48 hours for verified uninhabitable residential tenant claims."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_tenant_relocation_reg.pdf"), "IRDAI Tenant Relocation Guidelines", home_renter_reg)

    home_villa = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0006V2026 | <b>Product:</b> Villa Structural Supreme",
        "<b>SECTION I: LANDSLIDE & SUBSIDENCE COVER</b><br/>Provides structural protection for standalone villas, perimeter walls, and outdoor fixtures against rockslides, landslides, and land subsidence."
    ]
    create_pdf(os.path.join(POLICY_DIR, "home_villa_policy.pdf"), "Villa Structural Supreme Policy", home_villa)

    home_debris_rider = [
        "<b>Endorsement UIN:</b> BGI-ADD-DEBRIS-2026 | <b>Attachment to UIN:</b> IRDAN123P0006V2026",
        "<b>ADD-ON COVER: DEBRIS REMOVAL & ARCHITECT FEES</b><br/>Increases total claim limit by 10% to cover costs incurred for site clearance, debris removal, and professional architect survey fees."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "home_debris_rider.pdf"), "Add-on Endorsement: Debris Removal & Architect Fees", home_debris_rider)

    home_villa_reg = [
        "<b>Regulatory Notification:</b> IRDAI/GEO/2026",
        "<b>IRDAI HILLY AREA UNDERWRITING MANDATE</b><br/>Mandates geo-tagging and aerial drone inspections prior to claim disbursement in declared high-risk landslide zones."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_hilly_underwriting_reg.pdf"), "IRDAI Hilly Area Claims Directive", home_villa_reg)

    home_coliving = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0007V2026 | <b>Product:</b> Multi-Tenant PG & Co-Living Policy",
        "<b>SECTION I: HYBRID COMMERCIAL-RESIDENTIAL COVER</b><br/>Covers structural and fixture damages in residential Paying Guest (PG) facilities resulting from short-circuits, pipe bursts, and fire."
    ]
    create_pdf(os.path.join(POLICY_DIR, "home_coliving_policy.pdf"), "Multi-Tenant PG & Co-Living Policy", home_coliving)

    home_rent_loss_rider = [
        "<b>Endorsement UIN:</b> BGI-ADD-RENT-2026 | <b>Attachment to UIN:</b> IRDAN123P0007V2026",
        "<b>ADD-ON COVER: LOSS OF RENTAL INCOME</b><br/>Reimburses verified rental loss up to Rs. 50,000 per month for up to 6 months while the insured co-living building is uninhabitable."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "home_rent_loss_rider.pdf"), "Add-on Endorsement: Loss of Rent Cover", home_rent_loss_rider)

    home_coliving_reg = [
        "<b>Regulatory Notification:</b> IRDAI/HYB/2026",
        "<b>IRDAI CO-LIVING AUDIT GUIDELINES</b><br/>Insurers must verify commercial fire safety NOC certificates before underwriting hybrid co-living multi-tenant premises."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_coliving_audit_reg.pdf"), "IRDAI Co-Living Safety Standards", home_coliving_reg)

    home_solar = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0008V2026 | <b>Product:</b> Eco-Home Solar Shield Policy",
        "<b>SECTION I: RENEWABLE ENERGY FIXTURES</b><br/>Covers roof-mounted photovoltaic solar panels, inverters, and battery storage units against hail, storm, and accidental impact."
    ]
    create_pdf(os.path.join(POLICY_DIR, "home_solar_policy.pdf"), "Eco-Home Solar Shield Policy", home_solar)

    home_solar_rider = [
        "<b>Endorsement UIN:</b> BGI-ADD-GRID-2026 | <b>Attachment to UIN:</b> IRDAN123P0008V2026",
        "<b>ADD-ON COVER: NET-METERING LOSS COVER</b><br/>Compensates for lost feed-in tariff power revenue during period of grid disconnection due to insured physical panel damage."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "home_solar_rider.pdf"), "Add-on Endorsement: Net-Metering Revenue Loss", home_solar_rider)

    home_solar_reg = [
        "<b>Regulatory Notification:</b> CEA-IRDAI/SOLAR/2026",
        "<b>CEA & IRDAI SAFETY DISCONNECTION REGULATION</b><br/>Requires immediate physical isolating disconnections of damaged grid-tied solar assets before survey process execution."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "cea_irdai_solar_reg.pdf"), "CEA-IRDAI Grid Safety Circular", home_solar_reg)

    home_seismic = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0009V2026 | <b>Product:</b> Metro Apartment Seismic Guard",
        "<b>SECTION I: EARTHQUAKE & SEISMIC STRUCTURAL RISK</b><br/>Provides indemnification for structural column, beam, and wall cracking in Zone IV and Zone V seismic metro residential apartments."
    ]
    create_pdf(os.path.join(POLICY_DIR, "home_seismic_policy.pdf"), "Metro Apartment Seismic Guard Policy", home_seismic)

    home_escalation_rider = [
        "<b>Endorsement UIN:</b> BGI-ADD-ESCAL-2026 | <b>Attachment to UIN:</b> IRDAN123P0009V2026",
        "<b>ADD-ON COVER: INFLATION & ESCALATION RIDER</b><br/>Automatically increases Sum Insured by 10% annually to offset rising raw construction material costs like steel and cement."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "home_escalation_rider.pdf"), "Add-on Endorsement: Inflation Escalation Rider", home_escalation_rider)

    home_seismic_reg = [
        "<b>Regulatory Notification:</b> IRDAI/EQ/ZONE/2026",
        "<b>IRDAI MANDATORY SEISMIC DEDUCTIBLE DISCLOSURE</b><br/>Insurers must state seismic deductibles in prominent bold font on the first page of all residential schedules."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_seismic_disclosure_reg.pdf"), "IRDAI Seismic Deductible Disclosure Rules", home_seismic_reg)


    # --- 2. PERSONAL ACCIDENT INSURANCE PORTFOLIO ---
    accident_policy = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0002V2026 | <b>Product:</b> Personal Accident Suraksha",
        "<b>SECTION I: COVERAGE BENEFITS</b><br/>This policy provides 100% payout of the Sum Insured in the event of accidental death or Permanent Total Disablement (PTD) resulting solely and directly from an accident caused by external, violent, and visible means.",
        "<b>SECTION II: EXCLUSIONS</b><br/>No indemnity will be paid for claims arising out of: (a) Intentional self-injury, suicide, or attempted suicide. (b) Accidents occurring while the insured person is under the influence of intoxicating liquor or drugs. (c) Participation in hazardous sports or aviation activities unless specifically endorsed."
    ]
    create_pdf(os.path.join(POLICY_DIR, "personal_accident_policy.pdf"), "Personal Accident Insurance Policy", accident_policy)

    accident_endorsement = [
        "<b>Endorsement Add-on Wordings:</b> ACC-ADVENTURE-2026 | <b>Attachment to UIN:</b> IRDAN123P0002V2026",
        "<b>ADD-ON COVER: HAZARDOUS & ADVENTURE SPORTS RIDER</b><br/>This policy is amended to extend accidental death and disablement benefits to incidents occurring while the insured is engaged in amateur adventure sports, including trekking, river rafting, and competitive cycling.",
        "<b>CONDITIONS</b><br/>All activities must be conducted under the supervision of a certified institutional guide. Payout limits are capped at 50% of the base Sum Insured."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "accident_adventure_rider.pdf"), "Add-on Endorsement: Adventure Sports Rider", accident_endorsement)

    accident_regulation = [
        "<b>Regulatory Notification:</b> IRDAI/PA/REG/2026",
        "<b>IRDAI PERSONAL ACCIDENT CLAIMS PROCESSING GUIDELINES</b><br/>Insurers must prioritize personal accident claims involving permanent disablement. Medical board evaluation certifications issued by Indian Government public hospitals must be accepted as conclusive proof of disablement percentages without mandatory redundant corporate re-examinations."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_accident_regulation.pdf"), "IRDAI Personal Accident Settlement Guidelines", accident_regulation)

    # --- EXPANDED ACCIDENT SCENARIOS (6 to 10) ---
    accident_driver = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0010V2026 | <b>Product:</b> Commercial Driver Fleet PA",
        "<b>SECTION I: OCCUPATIONAL ROAD ACCIDENT COVER</b><br/>Provides payout for fatal accidents or permanent dismemberment suffered by long-haul commercial motor vehicle drivers during transit operations."
    ]
    create_pdf(os.path.join(POLICY_DIR, "accident_driver_policy.pdf"), "Commercial Driver Fleet PA Policy", accident_driver)

    accident_ttd_rider = [
        "<b>Endorsement UIN:</b> ACC-ADD-TTD-2026 | <b>Attachment to UIN:</b> IRDAN123P0010V2026",
        "<b>ADD-ON COVER: TEMPORARY TOTAL DISABLEMENT (TTD)</b><br/>Provides weekly allowance of Rs. 5,000 for up to 104 weeks during medically ordered continuous confinement due to accidental injury."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "accident_ttd_rider.pdf"), "Add-on Endorsement: Weekly TTD Income Benefit", accident_ttd_rider)

    accident_driver_reg = [
        "<b>Regulatory Notification:</b> MORTH-IRDAI/PA/2026",
        "<b>MORTH & IRDAI MANDATORY COMMERCIAL PA MANDATE</b><br/>Renders statutory Personal Accident cover compulsory for all valid commercial transport driving license holders."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "morth_irdai_driver_reg.pdf"), "MoRTH-IRDAI Commercial Driver Mandatory PA Circular", accident_driver_reg)

    accident_gig = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0011V2026 | <b>Product:</b> Gig Delivery Partner Micro-PA",
        "<b>SECTION I: ON-DUTY ACCIDENTAL COVERAGE</b><br/>Protects quick-commerce and delivery partners against accidental injuries occurring during active order delivery cycles."
    ]
    create_pdf(os.path.join(POLICY_DIR, "accident_gig_policy.pdf"), "Gig Delivery Partner Micro-PA Policy", accident_gig)

    accident_fracture_rider = [
        "<b>Endorsement UIN:</b> ACC-ADD-FRAC-2026 | <b>Attachment to UIN:</b> IRDAN123P0011V2026",
        "<b>ADD-ON COVER: FRACTURE & TRAUMA ALLOWANCE</b><br/>Provides lump-sum benefit between Rs. 10,000 and Rs. 50,000 for verified bone fractures, independent of hospital stay duration."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "accident_fracture_rider.pdf"), "Add-on Endorsement: Fracture & Trauma Benefit", accident_fracture_rider)

    accident_gig_reg = [
        "<b>Regulatory Notification:</b> IRDAI/GIG/SOC/2026",
        "<b>IRDAI GIG WORKER DIGITIZATION REGULATION</b><br/>Mandates paperless, fully API-driven claims processing for gig economy accident claims within 24 hours."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_gig_worker_reg.pdf"), "IRDAI Gig Worker Fast-Track Settlement Circular", accident_gig_reg)

    accident_gpa = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0012V2026 | <b>Product:</b> Corporate Group Personal Accident",
        "<b>SECTION I: 24/7 WORLDWIDE EMPLOYEE PROTECTION</b><br/>Offers 24/7 global accidental death and permanent total disability cover for corporate employees on and off duty."
    ]
    create_pdf(os.path.join(POLICY_DIR, "accident_gpa_policy.pdf"), "Corporate Group Personal Accident Policy", accident_gpa)

    accident_child_rider = [
        "<b>Endorsement UIN:</b> ACC-ADD-EDUC-2026 | <b>Attachment to UIN:</b> IRDAN123P0012V2026",
        "<b>ADD-ON COVER: CHILD EDUCATION BENEFIT</b><br/>Reimburses documented higher education tuition expenses up to Rs. 2,00,000 per dependent child upon fatal accident of employee."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "accident_child_rider.pdf"), "Add-on Endorsement: Child Education Benefit", accident_child_rider)

    accident_gpa_reg = [
        "<b>Regulatory Notification:</b> IRDAI/GPA/DIS/2026",
        "<b>IRDAI GROUP ACCIDENT EQUALITY CIRCULAR</b><br/>Prohibits insurers from applying non-disclosure exclusions for pre-existing physical disabilities in corporate group PA plans."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_gpa_disability_reg.pdf"), "IRDAI Group PA Non-Discrimination Rules", accident_gpa_reg)

    accident_aviation = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0013V2026 | <b>Product:</b> Executive Flight & Transit PA Cover",
        "<b>SECTION I: AVIATION & TRANSIT HAZARDS</b><br/>Covers accidental injuries, dismemberment, or demise occurring during commercial or non-scheduled charter flight transits."
    ]
    create_pdf(os.path.join(POLICY_DIR, "accident_aviation_policy.pdf"), "Executive Flight & Transit PA Policy", accident_aviation)

    accident_air_rider = [
        "<b>Endorsement UIN:</b> ACC-ADD-AIR-2026 | <b>Attachment to UIN:</b> IRDAN123P0013V2026",
        "<b>ADD-ON COVER: AIR AMBULANCE EVACUATION</b><br/>Covers emergency air evacuation expenses up to Rs. 10,00,000 to transport critical accident victims to tertiary trauma centers."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "accident_air_rider.pdf"), "Add-on Endorsement: Air Ambulance Evacuation Cover", accident_air_rider)

    accident_aviation_reg = [
        "<b>Regulatory Notification:</b> IRDAI/INT/FOREX/2026",
        "<b>IRDAI CROSS-BORDER PA CLAIMS GUIDELINES</b><br/>Sets standard foreign exchange conversion rules for settling emergency overseas accidental trauma medical costs."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_crossborder_forex_reg.pdf"), "IRDAI Cross-Border Claim Forex Rules", accident_aviation_reg)

    accident_student = [
        "<b>Policy Schedule UIN:</b> IRDAN123P0014V2026 | <b>Product:</b> Student Overseas Personal Accident Plan",
        "<b>SECTION I: INTERNATIONAL ACCIDENTAL EMERGENCY</b><br/>Provides global emergency room and accidental disability cover for Indian students enrolled in foreign educational institutes."
    ]
    create_pdf(os.path.join(POLICY_DIR, "accident_student_policy.pdf"), "Student Overseas PA Policy", accident_student)

    accident_sponsor_rider = [
        "<b>Endorsement UIN:</b> ACC-ADD-SPON-2026 | <b>Attachment to UIN:</b> IRDAN123P0014V2026",
        "<b>ADD-ON COVER: SPONSOR PROTECTION RIDER</b><br/>Pays balance university tuition fees if sponsoring parent suffers accidental demise or permanent total disability."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "accident_sponsor_rider.pdf"), "Add-on Endorsement: Sponsor Protection Benefit", accident_sponsor_rider)

    accident_student_reg = [
        "<b>Regulatory Notification:</b> IRDAI/EDU/ABROAD/2026",
        "<b>IRDAI DIRECT UNIVERSITY WIRE DIRECTIVE</b><br/>Requires direct wire transfers to university bursar accounts for validated student sponsor loss claims."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_student_wire_reg.pdf"), "IRDAI Overseas Tuition Remittance Rules", accident_student_reg)


    # --- 3. TERM LIFE INSURANCE PORTFOLIO ---
    life_policy = [
        "<b>Policy Schedule UIN:</b> IRDAN123L0003V2026 | <b>Product:</b> Bharat Jeevan Term Plan",
        "<b>SECTION I: DEATH BENEFIT</b><br/>The insurer guarantees to pay the specified Sum Assured to the designated nominee upon the unfortunate demise of the life assured during the policy term, provided the policy is active and all premiums are fully paid.",
        "<b>SECTION II: CRITICAL EXCLUSIONS</b><br/>Suicide Exclusion: If the life assured commits suicide within 12 months from the date of inception of the policy, the nominee shall only be entitled to 80% of the premiums paid. No full death benefit is payable under fraud or material non-disclosure of health conditions."
    ]
    create_pdf(os.path.join(POLICY_DIR, "term_life_policy.pdf"), "Term Life Insurance Policy", life_policy)

    life_endorsement = [
        "<b>Endorsement Add-on Wordings:</b> LIFE-CI-RIDER-2026 | <b>Attachment to UIN:</b> IRDAN123L0003V2026",
        "<b>ADD-ON COVER: CRITICAL ILLNESS RIDER</b><br/>This policy is extended to provide a lump-sum accelerated advance payout of 25% of the basic Sum Assured immediately upon the first diagnosis of any of the 10 specified critical illnesses, including stroke, open-chest CABG, and major organ transplant.",
        "<b>SURVIVAL PERIOD</b><br/>A mandatory survival period of 30 days from the date of diagnosis is strictly required before the rider benefit can be disbursed."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "life_critical_illness_rider.pdf"), "Add-on Endorsement: Critical Illness Accelerated Rider", life_endorsement)

    life_regulation = [
        "<b>Insurance Act Section 45 Mandate:</b> IND-LIFE-SEC45",
        "<b>STATUTORY THREE-YEAR MORATORIUM ON LIFE INSURANCE CLAIMS</b><br/>As per Section 45 of the Indian Insurance Act, no policy of life insurance shall be called in question on any ground whatsoever, including misstatement or non-disclosure of facts, after the expiry of three years from the date of issuance or reinstatement of the policy."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "insurance_act_section45_life.pdf"), "Section 45 Indian Insurance Act Regulation", life_regulation)

    # --- EXPANDED TERM LIFE SCENARIOS (11 to 15) ---
    life_keyman = [
        "<b>Policy Schedule UIN:</b> IRDAN123L0015V2026 | <b>Product:</b> Keyman Life Protection Plan",
        "<b>SECTION I: CORPORATE KEYMAN INDEMNITY</b><br/>Disburses Sum Assured directly to the employer firm upon premature death of designated key corporate executive."
    ]
    create_pdf(os.path.join(POLICY_DIR, "life_keyman_policy.pdf"), "Keyman Corporate Life Protection Policy", life_keyman)

    life_buyout_rider = [
        "<b>Endorsement UIN:</b> LIFE-ADD-BUYOUT-2026 | <b>Attachment to UIN:</b> IRDAN123L0015V2026",
        "<b>ADD-ON COVER: PARTNERSHIP BUYOUT RIDER</b><br/>Earmarks funds specifically to facilitate equity buyout from legal heirs of deceased key partners."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "life_buyout_rider.pdf"), "Add-on Endorsement: Partnership Buyout Rider", life_buyout_rider)

    life_keyman_reg = [
        "<b>Regulatory Notification:</b> IT-IRDAI/KEYMAN/2026",
        "<b>INCOME TAX & IRDAI KEYMAN TAX CIRCULAR</b><br/>Establishes strict tax deduction and maturity taxation rules under Section 10(10D) for corporate keyman policies."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "it_irdai_keyman_tax_reg.pdf"), "IT-IRDAI Keyman Policy Taxation Circular", life_keyman_reg)

    life_mortgage = [
        "<b>Policy Schedule UIN:</b> IRDAN123L0016V2026 | <b>Product:</b> Decreasing Term Mortgage Protect",
        "<b>SECTION I: DECREASING SUM ASSURED</b><br/>Sum Assured automatically decreases monthly matching the amortized balance of policyholder's approved home loan."
    ]
    create_pdf(os.path.join(POLICY_DIR, "life_mortgage_policy.pdf"), "Decreasing Term Mortgage Protect Policy", life_mortgage)

    life_terminal_rider = [
        "<b>Endorsement UIN:</b> LIFE-ADD-TERM-2026 | <b>Attachment to UIN:</b> IRDAN123L0016V2026",
        "<b>ADD-ON COVER: TERMINAL ILLNESS ACCELERATED PAYOUT</b><br/>Disburses 100% sum assured prior to demise upon certified medical diagnosis of terminal illness with life expectancy under 6 months."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "life_terminal_rider.pdf"), "Add-on Endorsement: Terminal Illness Payout", life_terminal_rider)

    life_mortgage_reg = [
        "<b>Regulatory Notification:</b> RBI-IRDAI/BUNDLING/2026",
        "<b>RBI & IRDAI ANTI-BUNDLING MANDATE</b><br/>Strictly bans banks from making life insurance purchase a forced pre-condition for loan sanctioning."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "rbi_irdai_antibundling_reg.pdf"), "RBI-IRDAI Anti-Bundling Directives", life_mortgage_reg)

    life_joint = [
        "<b>Policy Schedule UIN:</b> IRDAN123L0017V2026 | <b>Product:</b> Dual Jeevan Joint Life Plan",
        "<b>SECTION I: SPOUSAL DUAL COVER</b><br/>Provides joint life coverage for both spouses under a single policy schedule; pays benefit upon first demise."
    ]
    create_pdf(os.path.join(POLICY_DIR, "life_joint_policy.pdf"), "Dual Jeevan Joint Life Policy", life_joint)

    life_wop_rider = [
        "<b>Endorsement UIN:</b> LIFE-ADD-WOP-2026 | <b>Attachment to UIN:</b> IRDAN123L0017V2026",
        "<b>ADD-ON COVER: WAIVER OF PREMIUM (WoP) RIDER</b><br/>Waives all remaining future premiums for the surviving spouse following the death of the primary insured."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "life_wop_rider.pdf"), "Add-on Endorsement: Waiver of Premium", life_wop_rider)

    life_joint_reg = [
        "<b>Regulatory Notification:</b> IRDAI/JOINT/EQUITY/2026",
        "<b>IRDAI JOINT POLICY RIGHTS CIRCULAR</b><br/>Protects non-working spouse claims and guarantees equal nominee rights under joint life contracts."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_joint_equity_reg.pdf"), "IRDAI Joint Life Contract Guidelines", life_joint_reg)

    life_trop = [
        "<b>Policy Schedule UIN:</b> IRDAN123L0018V2026 | <b>Product:</b> Term Return of Premium (TROP) Plan",
        "<b>SECTION I: MATURITY REFUND COVER</b><br/>Guarantees 100% refund of total basic premiums paid if the life assured survives to the end of policy term."
    ]
    create_pdf(os.path.join(POLICY_DIR, "life_trop_policy.pdf"), "Term Return of Premium Policy", life_trop)

    life_adb_rider = [
        "<b>Endorsement UIN:</b> LIFE-ADD-ADB-2026 | <b>Attachment to UIN:</b> IRDAN123L0018V2026",
        "<b>ADD-ON COVER: ACCIDENTAL DEATH DOUBLE BENEFIT</b><br/>Doubles sum assured payout if death occurs directly as a result of a road accident."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "life_adb_rider.pdf"), "Add-on Endorsement: Double Accidental Benefit", life_adb_rider)

    life_trop_reg = [
        "<b>Regulatory Notification:</b> IRDAI/TROP/DISC/2026",
        "<b>IRDAI TROP DISCLOSURE CIRCULAR</b><br/>Requires full disclosure of gross vs. net interest earnings on returned premium calculations in TROP plans."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_trop_disclosure_reg.pdf"), "IRDAI TROP Return Disclosures", life_trop_reg)

    life_senior = [
        "<b>Policy Schedule UIN:</b> IRDAN123L0019V2026 | <b>Product:</b> Senior Protection Life Plan",
        "<b>SECTION I: SENIOR GUARANTEED ISSUE COVER</b><br/>Guaranteed issue life protection tailored for individuals entering aged brackets 55 to 70 with simplified health questions."
    ]
    create_pdf(os.path.join(POLICY_DIR, "life_senior_policy.pdf"), "Senior Protection Life Policy", life_senior)

    life_palliative_rider = [
        "<b>Endorsement UIN:</b> LIFE-ADD-PAL-2026 | <b>Attachment to UIN:</b> IRDAN123L0019V2026",
        "<b>ADD-ON COVER: PALLIATIVE CARE STIPEND</b><br/>Provides monthly benefit of Rs. 15,000 for verified end-of-life nursing and home palliative care."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "life_palliative_rider.pdf"), "Add-on Endorsement: Palliative Care Benefit", life_palliative_rider)

    life_senior_reg = [
        "<b>Regulatory Notification:</b> IRDAI/SR/LIFE/2026",
        "<b>IRDAI SENIOR CITIZEN CANCELLATION PROHIBITION</b><br/>Prohibits insurers from arbitrarily cancelling senior life contracts due to post-issue health updates."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_senior_life_reg.pdf"), "IRDAI Senior Citizen Protection Directive", life_senior_reg)


    # --- 4. HEALTH (MEDICAL) INSURANCE PORTFOLIO ---
    medical_policy = [
        "<b>Policy Schedule UIN:</b> IRDAN123H0004V2026 | <b>Product:</b> Arogya Sanjeevani Health Policy",
        "<b>SECTION I: HOSPITALISATION COVER</b><br/>This policy covers reasonable and customary medical expenses incurred during inpatient hospitalisation for a minimum period of 24 consecutive hours due to illness, disease, or accidental injury sustained during the policy period.",
        "<b>SECTION II: WAITING PERIODS & EXCLUSIONS</b><br/>(a) Pre-Existing Diseases (PED) are excluded for a continuous period of 36 months from policy inception. (b) A general waiting period of 30 days applies to all diseases contracted except accidental emergency hospitalisation. (c) Outpatient treatment (OPD) and cosmetic surgeries are strictly excluded."
    ]
    create_pdf(os.path.join(POLICY_DIR, "health_medical_policy.pdf"), "Arogya Sanjeevani Medical Insurance Policy", medical_policy)

    medical_endorsement = [
        "<b>Endorsement Add-on Wordings:</b> AROGYA-OPD-2026 | <b>Attachment to UIN:</b> IRDAN123H0004V2026",
        "<b>ADD-ON COVER: OUT-PATIENT DEPARTMENT (OPD) CARE</b><br/>It is hereby agreed and declared that in consideration of an additional premium, this policy is extended to cover reasonable Out-Patient Expenses (consultation fees, diagnostic tests, and pharmacy bills) up to a maximum limit of Rs. 10,000 per policy year.",
        "<b>EXCLUSIONS</b><br/>This rider explicitly excludes any cosmetic treatments or dental procedures unless necessitated by an acute accidental injury."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "health_opd_rider.pdf"), "Add-on Endorsement: OPD Expenses Rider", medical_endorsement)

    medical_regulation = [
        "<b>Regulatory Circular:</b> IRDAI/HLT/REG/2026/V1",
        "<b>IRDAI STANDARDIZATION OF PRE-EXISTING DISEASES (PED)</b><br/>As per the 2026 master guidelines, no general or health insurer can classify a disease or ailment as 'Pre-Existing' if it was diagnosed or treated less than 36 months prior to the inception of the policy.",
        "Furthermore, any claim filed for a condition that occurs after a continuous renewal period of 8 years (Moratorium Period) cannot be contested by the insurer on grounds of non-disclosure, except in proven instances of deliberate cross-border financial fraud."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_health_regulations.pdf"), "IRDAI Master Circular on Health Insurance Metrics", medical_regulation)

    # --- EXPANDED HEALTH SCENARIOS (16 to 20) ---
    medical_floater = [
        "<b>Policy Schedule UIN:</b> IRDAN123H0020V2026 | <b>Product:</b> Parivar Swasthya Floater Plan",
        "<b>SECTION I: SHARED FAMILY SUM INSURED</b><br/>Provides floating inpatient cover up to Rs. 10,00,000 shared among self, spouse, and up to two dependent children."
    ]
    create_pdf(os.path.join(POLICY_DIR, "health_floater_policy.pdf"), "Parivar Swasthya Floater Policy", medical_floater)

    medical_maternity_rider = [
        "<b>Endorsement UIN:</b> AROGYA-ADD-MAT-2026 | <b>Attachment to UIN:</b> IRDAN123H0020V2026",
        "<b>ADD-ON COVER: MATERNITY & NEWBORN CARE</b><br/>Extends cover for delivery expenses and newborn medical care including first-year routine vaccinations up to Rs. 50,000."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "health_maternity_rider.pdf"), "Add-on Endorsement: Maternity & Newborn Cover", medical_maternity_rider)

    medical_floater_reg = [
        "<b>Regulatory Notification:</b> IRDAI/FLT/PORT/2026",
        "<b>IRDAI FLOATER PORTABILITY MANDATE</b><br/>Guarantees dependent children aging out at 25 years full credit transfer for waiting periods when moving to individual policies."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_floater_portability_reg.pdf"), "IRDAI Family Floater Portability Directive", medical_floater_reg)

    medical_super_topup = [
        "<b>Policy Schedule UIN:</b> IRDAN123H0021V2026 | <b>Product:</b> Super Top-Up Shield",
        "<b>SECTION I: HIGH-DEDUCTIBLE COVERAGE</b><br/>Activates medical payouts after cumulative annual inpatient bills cross base deductible threshold of Rs. 5,00,000."
    ]
    create_pdf(os.path.join(POLICY_DIR, "health_super_topup_policy.pdf"), "Super Top-Up Shield Policy", medical_super_topup)

    medical_deductible_rider = [
        "<b>Endorsement UIN:</b> AROGYA-ADD-DED-2026 | <b>Attachment to UIN:</b> IRDAN123H0021V2026",
        "<b>ADD-ON COVER: DEDUCTIBLE RESTORATION RIDER</b><br/>Restores deductible threshold limit once per year in case of multiple unrelated catastrophic hospitalizations."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "health_deductible_rider.pdf"), "Add-on Endorsement: Deductible Restoration", medical_deductible_rider)

    medical_topup_reg = [
        "<b>Regulatory Notification:</b> IRDAI/TOP/INTEG/2026",
        "<b>IRDAI CASHLESS INTEGRATION REGULATION</b><br/>Requires primary insurers and top-up underwriters to execute joint cashless claim authorizations directly with hospitals."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_topup_integration_reg.pdf"), "IRDAI Cashless Top-Up Rules", medical_topup_reg)

    medical_chronic = [
        "<b>Policy Schedule UIN:</b> IRDAN123H0022V2026 | <b>Product:</b> Diabetes & Hypertension Care Plan",
        "<b>SECTION I: CHRONIC CONDITION DAY-1 COVER</b><br/>Immediate coverage for complications arising from Type-2 Diabetes and Hypertension without applying standard pre-existing waiting periods."
    ]
    create_pdf(os.path.join(POLICY_DIR, "health_chronic_policy.pdf"), "Diabetes & Hypertension Care Policy", medical_chronic)

    medical_wellness_rider = [
        "<b>Endorsement UIN:</b> AROGYA-ADD-WELL-2026 | <b>Attachment to UIN:</b> IRDAN123H0022V2026",
        "<b>ADD-ON COVER: WELLNESS & HBA1C REWARD RIDER</b><br/>Grants up to 25% premium discount at renewal upon achieving target HbA1c and blood pressure health metrics."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "health_wellness_rider.pdf"), "Add-on Endorsement: Wellness Reward Benefit", medical_wellness_rider)

    medical_chronic_reg = [
        "<b>Regulatory Notification:</b> IRDAI/WELL/LOAD/2026",
        "<b>IRDAI NON-LOADING WELLNESS DIRECTIVE</b><br/>Bans underwriters from increasing renewal premiums solely based on regular chronic condition checkup updates."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_wellness_loading_reg.pdf"), "IRDAI Anti-Premium Loading Directive", medical_chronic_reg)

    medical_ayush = [
        "<b>Policy Schedule UIN:</b> IRDAN123H0023V2026 | <b>Product:</b> AYUSH Comprehensive Health Plan",
        "<b>SECTION I: AYURVEDA & ALTERNATIVE CARE</b><br/>100% sum insured coverage for inpatient hospitalization expenses under Ayurveda, Yoga, Unani, Siddha, and Homeopathy systems."
    ]
    create_pdf(os.path.join(POLICY_DIR, "health_ayush_policy.pdf"), "AYUSH Comprehensive Health Policy", medical_ayush)

    medical_panchakarma_rider = [
        "<b>Endorsement UIN:</b> AROGYA-ADD-PANCH-2026 | <b>Attachment to UIN:</b> IRDAN123H0023V2026",
        "<b>ADD-ON COVER: PANCHAKARMA OUTPATIENT RIDER</b><br/>Covers certified residential Panchakarma detox therapies and procedures up to Rs. 25,000 annually."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "health_panchakarma_rider.pdf"), "Add-on Endorsement: Panchakarma Care Benefit", medical_panchakarma_rider)

    medical_ayush_reg = [
        "<b>Regulatory Notification:</b> AYUSH-IRDAI/PARITY/2026",
        "<b>AYUSH-IRDAI EQUALITY REGULATION</b><br/>Mandates equal cashless hospital network facilities for NABH-accredited AYUSH institutions on par with allopathic hospitals."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "ayush_irdai_parity_reg.pdf"), "AYUSH-IRDAI Network Cashless Directives", medical_ayush_reg)

    medical_senior_care = [
        "<b>Policy Schedule UIN:</b> IRDAN123H0024V2026 | <b>Product:</b> Senior Citizen Domiciliary Care Policy",
        "<b>SECTION I: ICU & HOME HOSPITALISATION</b><br/>Covers ICU expenses and home hospitalisation (domiciliary care) when hospital bed availability is limited or transport is medically unsafe."
    ]
    create_pdf(os.path.join(POLICY_DIR, "health_senior_care_policy.pdf"), "Senior Citizen Domiciliary Care Policy", medical_senior_care)

    medical_attendant_rider = [
        "<b>Endorsement UIN:</b> AROGYA-ADD-ATTEND-2026 | <b>Attachment to UIN:</b> IRDAN123H0024V2026",
        "<b>ADD-ON COVER: HOME ATTENDANT & EQUIPMENT RENTAL</b><br/>Reimburses oxygen concentrator, hospital bed rentals, and certified nurse charges up to Rs. 30,000 post-discharge."
    ]
    create_pdf(os.path.join(ENDORSEMENT_DIR, "health_attendant_rider.pdf"), "Add-on Endorsement: Home Attendant & Equipment Rental", medical_attendant_rider)

    medical_senior_reg = [
        "<b>Regulatory Notification:</b> IRDAI/SR/REJECT/2026",
        "<b>IRDAI EXECUTIVE BOARD REJECTION MANDATE</b><br/>Requires all senior citizen health claim rejections to be personally reviewed and countersigned by a board director."
    ]
    create_pdf(os.path.join(REGULATION_DIR, "irdai_senior_rejection_reg.pdf"), "IRDAI Senior Claims Board Review Circular", medical_senior_reg)

    print("✅ All Indian policy documents generated successfully!")


if __name__ == "__main__":
    generate_all_sample_pdfs()

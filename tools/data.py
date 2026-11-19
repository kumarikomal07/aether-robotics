"""Aether Robotics - site content (single source of truth).

Placeholders that must be confirmed before launch are listed in README.md.
Products, projects, statistics and research areas are ILLUSTRATIVE and labelled as such on the site.
"""

SITE = {
    "name": "Aether Robotics",
    "domain": "https://www.aetherrobotics.sg",   # placeholder
    "email": "hello@aetherrobotics.sg",          # placeholder
    "partner_email": "partners@aetherrobotics.sg",  # placeholder
    "whatsapp": "",                              # empty = WhatsApp hidden until a verified number is provided
    "city": "Singapore",
    "founded": "2020",
}

AI_SERVICES = [
    {"slug": "ai-development", "name": "Artificial Intelligence Development", "short": "Custom AI systems that turn data into decisions and automate complex work.", "icon": "brain", "img": "ae-cubes",
     "overview": "We design and build AI systems tailored to your operations, from decision-support models to AI-powered applications embedded in your existing software. Every system is engineered for reliability, transparency and measurable value.",
     "problems": ["Decisions rely on manual analysis of large volumes of data", "Repetitive expert tasks slow teams down", "Off-the-shelf AI tools do not fit specialised workflows", "Pilot projects never reach production"],
     "capabilities": ["AI strategy and use-case discovery", "Custom model design and training", "AI-powered application development", "Model deployment, APIs and integration", "Monitoring, evaluation and retraining", "Responsible AI and governance"],
     "tech": ["Python", "PyTorch", "TensorFlow", "FastAPI", "Docker", "Kubernetes"],
     "benefits": [("Faster decisions", "Models surface insights in seconds rather than days."), ("Scalable expertise", "Capture expert knowledge in systems that work around the clock."), ("Production-ready", "Engineered for reliability, monitoring and safe updates."), ("Transparent", "Explainability and audit trails built in from the start.")],
     "usecases": ["Decision support for operations teams", "Intelligent assistants for technical documentation", "Automated triage of service requests"]},
    {"slug": "machine-learning", "name": "Machine Learning Solutions", "short": "Predictive models that learn from your data to forecast, classify and optimise.", "icon": "chart", "img": "ae-wave",
     "overview": "Our machine learning solutions turn historical and real-time data into predictions you can act on, from forecasting demand to detecting anomalies in equipment, with robust pipelines that keep models accurate over time.",
     "problems": ["Unplanned downtime and reactive maintenance", "Inaccurate forecasts leading to waste or shortages", "Anomalies discovered too late", "Data spread across disconnected systems"],
     "capabilities": ["Predictive analytics and forecasting", "Classification and anomaly detection", "Recommendation and optimisation models", "Feature engineering and data pipelines", "MLOps: versioning, CI/CD and monitoring", "Model evaluation and drift detection"],
     "tech": ["Python", "scikit-learn", "PyTorch", "NumPy", "Pandas", "Jupyter"],
     "benefits": [("Anticipate change", "Act on predictions before problems occur."), ("Reduce waste", "Better forecasts mean leaner inventory and planning."), ("Always learning", "Pipelines retrain models as conditions change."), ("Measurable", "Clear metrics tied to business outcomes.")],
     "usecases": ["Predictive maintenance for machinery", "Demand and capacity forecasting", "Quality anomaly detection"]},
    {"slug": "computer-vision", "name": "Computer Vision & Image Recognition", "short": "Vision systems that see, inspect and understand the physical world.", "icon": "eye", "img": "robot-face",
     "overview": "We build computer vision systems that detect objects, inspect quality, read documents and guide robots, running on edge devices or in the cloud depending on speed, privacy and cost requirements.",
     "problems": ["Manual visual inspection is slow and inconsistent", "Robots need to perceive changing environments", "Safety monitoring depends on human attention", "Visual data is collected but never analysed"],
     "capabilities": ["Object detection and tracking", "Defect detection and visual inspection", "Image classification and segmentation", "Optical character recognition (OCR)", "Edge deployment on embedded hardware", "Vision guidance for robotics"],
     "tech": ["OpenCV", "PyTorch", "TensorFlow", "C++", "ROS", "Python"],
     "benefits": [("Consistent quality", "Every item inspected to the same standard."), ("Real-time", "Edge inference for low-latency decisions."), ("Safer sites", "Automated monitoring of hazardous zones."), ("Robot-ready", "Perception that lets robots adapt to their surroundings.")],
     "usecases": ["Automated surface-defect inspection", "Pick-and-place guidance for robotic arms", "PPE and safety-zone monitoring"]},
    {"slug": "nlp", "name": "Natural Language Processing", "short": "Language AI that understands, summarises and generates text and speech.", "icon": "chat", "img": "ai-chip",
     "overview": "Our NLP solutions help organisations understand and act on unstructured language, from technical manuals and support tickets to voice commands for machines, using modern language models with appropriate safeguards.",
     "problems": ["Knowledge is locked in documents and manuals", "Support teams answer the same questions repeatedly", "Reports and logs are too long to review manually", "Operators need hands-free interaction with systems"],
     "capabilities": ["Document understanding and extraction", "Semantic search and knowledge assistants", "Summarisation and report generation", "Classification and sentiment analysis", "Speech recognition and voice interfaces", "Multilingual language processing"],
     "tech": ["Python", "PyTorch", "Transformers", "FastAPI", "PostgreSQL", "Vector search"],
     "benefits": [("Instant answers", "Teams find information in seconds."), ("Less admin", "Automated extraction and summaries reduce manual work."), ("Hands-free", "Voice interfaces for operators and technicians."), ("Grounded", "Answers linked back to trusted sources.")],
     "usecases": ["Maintenance manual assistant for technicians", "Automated incident report summaries", "Voice commands for collaborative robots"]},
    {"slug": "process-automation", "name": "Intelligent Process Automation", "short": "Automation that combines AI, rules and integrations to streamline operations.", "icon": "flow", "img": "ae-status",
     "overview": "We combine AI, business rules and system integrations to automate end-to-end processes, keeping people in the loop for exceptions and decisions that need judgement.",
     "problems": ["Data re-keyed between systems", "Approvals and handovers create delays", "Processes vary between teams and sites", "Little visibility of where work is stuck"],
     "capabilities": ["Process discovery and mapping", "AI-driven document and data processing", "Workflow orchestration and integrations", "Human-in-the-loop review queues", "Monitoring dashboards and alerts", "Continuous improvement analytics"],
     "tech": ["Python", "Node.js", "FastAPI", "PostgreSQL", "Docker", "Grafana"],
     "benefits": [("Throughput", "Routine work completed automatically."), ("Accuracy", "Fewer manual errors and rework."), ("Visibility", "Live view of every process and exception."), ("Control", "People approve what matters.")],
     "usecases": ["Automated order and invoice processing", "Maintenance work-order orchestration", "Supplier onboarding workflows"]},
    {"slug": "ai-research", "name": "AI Research & Development", "short": "Applied research that explores new AI methods and turns them into prototypes.", "icon": "flask", "img": "students-lab",
     "overview": "Our applied R&D work explores emerging methods in machine learning, perception and autonomy, and evaluates whether they are ready for real-world use through prototypes and structured experiments.",
     "problems": ["Uncertainty about which AI methods are mature enough", "No internal capacity for experimentation", "Need for proof-of-concept before investment", "Complex problems without established solutions"],
     "capabilities": ["Technology scouting and feasibility studies", "Rapid prototyping and proof-of-concepts", "Experiment design and benchmarking", "Simulation and synthetic data", "Research collaboration support", "Technical reports and recommendations"],
     "tech": ["Python", "PyTorch", "Jupyter", "ROS", "MATLAB", "Simulation"],
     "benefits": [("De-risk innovation", "Test ideas before committing major budgets."), ("Evidence-based", "Decisions backed by experiments, not hype."), ("Speed", "Prototypes in weeks rather than months."), ("Knowledge transfer", "Findings documented for your teams.")],
     "usecases": ["Feasibility study for autonomous inspection", "Benchmarking vision models for a new product line", "Simulation-based robot path planning prototype"]},
]

ROBOTICS = [
    {"id": "industrial-arms", "name": "Industrial Robotics & Robotic Arms", "icon": "arm", "img": "ae-arm-weld",
     "text": "Design, programming and integration of robotic arms for welding, assembly, material handling and machine tending, with safety systems engineered to applicable standards.",
     "points": ["Robot cell design and simulation", "Path planning and motion programming", "End-of-arm tooling selection", "Safety zones and interlocks"]},
    {"id": "assistance", "name": "Robotic Assistance Systems", "icon": "robot", "img": "robot-white",
     "text": "Collaborative and assistive robots that work alongside people, taking on repetitive, strenuous or precise tasks while operators stay in control.",
     "points": ["Collaborative robot (cobot) deployment", "Operator-guided task teaching", "Voice and gesture interaction", "Ergonomic task analysis"]},
    {"id": "autonomous", "name": "Autonomous Systems Development", "icon": "drone", "img": "drone",
     "text": "Perception, localisation and navigation for mobile robots and drones that move safely through dynamic environments such as warehouses and industrial sites.",
     "points": ["SLAM and localisation", "Obstacle detection and avoidance", "Fleet coordination", "Simulation-first testing"]},
    {"id": "integration", "name": "Intelligent Robotics Integration", "icon": "chip", "img": "ae-arm-close",
     "text": "Connecting robots to AI, vision and enterprise systems so they can adapt to variation, report their status and improve over time.",
     "points": ["Vision-guided robotics", "PLC, MES and ERP integration", "Remote monitoring dashboards", "Predictive maintenance for robots"]},
]

PRODUCTS = [
    {"slug": "aether-ai-core", "name": "Aether AI Core", "tag": "AI Platform", "icon": "brain", "img": "ae-cubes",
     "short": "Intelligent AI platform for business automation and data-driven decisions.",
     "intro": "Aether AI Core is an illustrative concept for a central AI platform that connects data sources, hosts machine learning models and delivers decisions and automations to the systems people already use.",
     "purpose": "It is designed to give organisations one governed place to build, deploy and monitor AI capabilities instead of scattering models across teams and tools.",
     "features": [("Unified data connectors", "Connect databases, sensors and business applications."), ("Model hub", "Deploy, version and roll back models safely."), ("Decision APIs", "Serve predictions to any application in real time."), ("Monitoring", "Track accuracy, drift and usage on live dashboards."), ("Access control", "Role-based permissions and audit logging."), ("Workflow triggers", "Turn model outputs into automated actions.")],
     "applications": ["Operational decision support", "Enterprise AI governance", "Real-time scoring for business systems", "Central hub for AI initiatives"]},
    {"slug": "roboassist", "name": "RoboAssist", "tag": "Robotics", "icon": "arm", "img": "ae-arm-weld",
     "short": "Robotic assistance system for industrial and operational environments.",
     "intro": "RoboAssist is an illustrative concept for a collaborative robotic assistance system that supports operators with repetitive, precise or physically demanding tasks.",
     "purpose": "It is designed to combine a collaborative arm, vision guidance and a simple teaching interface so that new tasks can be set up without specialist programming.",
     "features": [("Collaborative operation", "Designed to work alongside people with safety monitoring."), ("Vision guidance", "Locates parts and adapts to variation."), ("Teach by demonstration", "Operators show tasks through a guided interface."), ("Task library", "Reusable routines for common operations."), ("Status reporting", "Live health and utilisation data."), ("Integration ready", "Connects to PLC and MES systems.")],
     "applications": ["Assembly assistance", "Machine tending", "Kitting and packing", "Laboratory sample handling"]},
    {"slug": "visionx", "name": "VisionX", "tag": "Computer Vision", "icon": "eye", "img": "robot-face",
     "short": "AI-powered image recognition and visual analysis solution.",
     "intro": "VisionX is an illustrative concept for a computer vision solution that detects, classifies and measures objects in images and video streams.",
     "purpose": "It is designed to bring consistent visual inspection and monitoring to production lines, warehouses and facilities, running at the edge or in the cloud.",
     "features": [("Object detection", "Identify and locate items in real time."), ("Defect inspection", "Flag surface and assembly defects."), ("Edge deployment", "Run on embedded devices near cameras."), ("Custom training", "Adapt models to your products with labelled examples."), ("Analytics dashboard", "Trends, alerts and image evidence."), ("Privacy controls", "Blurring and retention settings.")],
     "applications": ["Quality inspection", "Inventory and pallet counting", "Safety-zone monitoring", "Robot vision guidance"]},
    {"slug": "autoflow", "name": "AutoFlow", "tag": "Automation", "icon": "flow", "img": "ae-status",
     "short": "Intelligent business process automation platform.",
     "intro": "AutoFlow is an illustrative concept for an intelligent automation platform that orchestrates multi-step business processes across people, systems and AI services.",
     "purpose": "It is designed to replace manual handovers and re-keying with visual workflows, AI document processing and clear exception handling.",
     "features": [("Visual workflow builder", "Design processes with drag-and-drop steps."), ("AI document processing", "Extract data from forms, invoices and reports."), ("System connectors", "Integrate ERP, CRM and messaging tools."), ("Human-in-the-loop", "Route exceptions to the right reviewer."), ("SLA tracking", "Monitor timings and bottlenecks."), ("Audit trail", "Full history of every automated decision.")],
     "applications": ["Order-to-cash automation", "Maintenance work orders", "Supplier onboarding", "Compliance reporting"]},
    {"slug": "neurasense", "name": "NeuraSense", "tag": "Machine Learning", "icon": "pulse", "img": "ae-wave",
     "short": "Machine learning solution for predictive insights and data analysis.",
     "intro": "NeuraSense is an illustrative concept for a machine learning solution that analyses sensor and operational data to predict outcomes and detect anomalies.",
     "purpose": "It is designed to help teams move from reactive to predictive operations by forecasting failures, demand and performance.",
     "features": [("Time-series forecasting", "Predict demand, load and performance."), ("Anomaly detection", "Spot unusual patterns in sensor streams."), ("Root-cause hints", "Highlight the signals behind each alert."), ("Automated retraining", "Models update as data changes."), ("Alerting", "Notifications to email, chat or work-order systems."), ("Explainable insights", "Readable explanations for each prediction.")],
     "applications": ["Predictive maintenance", "Energy optimisation", "Demand forecasting", "Process quality monitoring"]},
]

INDUSTRIES = [
    {"id": "manufacturing", "name": "Manufacturing & Industrial Automation", "short": "Manufacturing", "icon": "factory", "img": "factory-robots",
     "overview": "Manufacturers are under pressure to raise quality and throughput while coping with labour shortages and product variation.",
     "challenges": ["Labour-intensive repetitive tasks", "Inconsistent manual inspection", "Unplanned machine downtime"],
     "applications": ["Robotic welding, assembly and handling", "Vision-based quality inspection", "Predictive maintenance"],
     "solutions": ["RoboAssist-style collaborative cells", "VisionX-style inspection stations", "NeuraSense-style machine analytics"]},
    {"id": "healthcare", "name": "Healthcare & Medical Technology", "short": "Healthcare", "icon": "health", "img": "med-tech",
     "overview": "Healthcare organisations want to reduce administrative load and support clinicians with technology that is safe and privacy-conscious.",
     "challenges": ["High administrative workload", "Manual handling of samples and supplies", "Large volumes of medical images and records"],
     "applications": ["Laboratory and logistics robotics", "AI-assisted image analysis (decision support)", "Document and records automation"],
     "solutions": ["Assistive robotics for routine tasks", "Vision models with clinical oversight", "NLP for documentation workflows"]},
    {"id": "logistics", "name": "Logistics & Supply Chain", "short": "Logistics", "icon": "truck", "img": "warehouse",
     "overview": "Logistics operators need faster fulfilment, accurate inventory and resilient operations across warehouses and networks.",
     "challenges": ["Picking and sorting labour demand", "Inventory inaccuracy", "Volatile demand and capacity planning"],
     "applications": ["Autonomous mobile robots", "Vision-based counting and tracking", "Demand forecasting"],
     "solutions": ["AMR fleet integration", "VisionX-style pallet and parcel recognition", "ML forecasting pipelines"]},
    {"id": "research-education", "name": "Research & Education", "short": "Research", "icon": "flask", "img": "lab-research",
     "overview": "Universities, labs and training providers need platforms to explore AI and robotics and to train the next generation of engineers.",
     "challenges": ["Building research platforms from scratch", "Limited robotics expertise", "Bridging research and real-world deployment"],
     "applications": ["Robotics research platforms", "AI experimentation environments", "Simulation and digital twins"],
     "solutions": ["Configurable robot test beds", "Curated ML tooling and datasets", "Collaborative R&D projects"]},
    {"id": "industrial-enterprises", "name": "Industrial Enterprises", "short": "Industrial Enterprises", "icon": "building", "img": "engineer-2",
     "overview": "Energy, utilities, construction and heavy-industry organisations operate complex assets where safety and uptime are critical.",
     "challenges": ["Inspection of hazardous or remote assets", "Ageing equipment and knowledge loss", "Fragmented operational data"],
     "applications": ["Drone and robot-based inspection", "Asset health analytics", "Knowledge assistants for field teams"],
     "solutions": ["Autonomous inspection workflows", "Predictive asset models", "NLP assistants over technical manuals"]},
    {"id": "technology", "name": "Technology Companies", "short": "Technology", "icon": "chip", "img": "servers",
     "overview": "Technology companies want to embed AI and robotics capabilities into their own products without building every component in-house.",
     "challenges": ["Scarce AI and robotics talent", "Moving prototypes to production", "Scaling and monitoring models"],
     "applications": ["Embedded AI features", "Perception modules for devices", "MLOps and model platforms"],
     "solutions": ["Dedicated AI engineering teams", "Edge-optimised vision models", "Aether AI Core-style platforms"]},
]
HOME_INDUSTRIES = INDUSTRIES[:5]

RESEARCH = [
    ("ml-dl", "Machine Learning & Deep Learning", "brain", "Exploring efficient training, small-data learning and model compression so advanced models can run reliably on industrial hardware.", ["Data-efficient learning", "Model compression for edge devices", "Uncertainty estimation"]),
    ("neural", "Neural Networks & Intelligent Systems", "network", "Studying architectures that combine learned models with rules and planning to make systems more dependable and explainable.", ["Hybrid neuro-symbolic approaches", "Explainability methods", "Robustness testing"]),
    ("autonomous", "Autonomous Robotics", "drone", "Investigating perception, planning and control methods that let robots operate safely in changing, human-shared environments.", ["Navigation in dynamic spaces", "Sim-to-real transfer", "Multi-robot coordination"]),
    ("vision", "Computer Vision Research", "eye", "Evaluating detection, segmentation and 3D perception methods for inspection and manipulation tasks.", ["3D perception and depth", "Few-shot defect detection", "Vision for grasping"]),
    ("hmi", "Human-Machine Interaction", "hand", "Exploring how people and robots communicate and collaborate safely, through voice, gesture and intuitive interfaces.", ["Natural language robot control", "Gesture and intent recognition", "Trust and usability studies"]),
    ("emerging", "Emerging Technology Exploration", "spark", "Tracking and testing emerging technologies such as foundation models for robotics, digital twins and edge AI accelerators.", ["Foundation models for robotics", "Digital twins and simulation", "Edge AI hardware"]),
]

PROJECT_CATS = ["AI", "Robotics", "Automation", "Computer Vision"]
PROJECTS = [
    {"slug": "smart-assembly-assistant", "title": "Smart Assembly Assistant", "cat": "Robotics", "img": "ae-arm-weld", "industry": "Manufacturing",
     "summary": "A collaborative robotic cell that supports operators during repetitive assembly steps.",
     "background": "An electronics assembler (fictional scenario) relied on manual fastening and part placement, leading to fatigue and variation between shifts.",
     "challenge": "Introduce automation without redesigning the whole line, while keeping operators in control of complex steps.",
     "solution": "A collaborative arm with vision-guided part location, a tablet interface for task selection and safety monitoring zones around the shared workspace.",
     "tech": ["ROS", "C++", "OpenCV", "Python", "PLC integration"],
     "approach": ["Time-and-motion study of current tasks", "Simulation of robot reach and cycle time", "Pilot cell with operator feedback", "Phased roll-out with training"],
     "outcomes": ["Repetitive steps handled by the robot", "Operators focus on inspection and complex work", "Consistent fastening sequence across shifts"],
     "learnings": "Involving operators in task teaching built confidence and surfaced edge cases early."},
    {"slug": "visual-quality-inspection", "title": "Visual Quality Inspection", "cat": "Computer Vision", "img": "factory-robots", "industry": "Automotive components",
     "summary": "Camera-based inspection that flags surface defects on moving production lines.",
     "background": "A component supplier (fictional scenario) inspected parts by eye at the end of the line.",
     "challenge": "Detect small, rare defects reliably under varying lighting at line speed.",
     "solution": "Controlled lighting, high-resolution cameras and a defect-detection model running on an edge device, with images of rejected parts stored for review.",
     "tech": ["PyTorch", "OpenCV", "Edge GPU", "Python", "Grafana"],
     "approach": ["Defect taxonomy workshop", "Image collection and labelling", "Model training with augmentation", "Shadow-mode trial before go-live"],
     "outcomes": ["Every part inspected to the same standard", "Image evidence for each rejection", "Trend dashboards for quality teams"],
     "learnings": "Lighting design mattered as much as the model architecture."},
    {"slug": "warehouse-amr-fleet", "title": "Warehouse Autonomous Mobile Robots", "cat": "Robotics", "img": "warehouse", "industry": "Logistics",
     "summary": "Autonomous mobile robots that move goods between storage and packing zones.",
     "background": "A distribution centre (fictional scenario) spent significant staff time walking between aisles.",
     "challenge": "Navigate safely among people and forklifts, and integrate with the warehouse management system.",
     "solution": "A fleet of mobile robots with SLAM navigation, a traffic-management layer and integration with order-picking workflows.",
     "tech": ["ROS 2", "C++", "Python", "Kubernetes", "PostgreSQL"],
     "approach": ["Site mapping and traffic analysis", "Simulation of fleet size and routes", "Pilot in one zone", "Expansion with fleet monitoring"],
     "outcomes": ["Less walking for pickers", "Live view of robot locations and tasks", "Flexible routes as layouts change"],
     "learnings": "Clear floor markings and staff briefings were essential for smooth human-robot traffic."},
    {"slug": "predictive-maintenance", "title": "Predictive Maintenance Intelligence", "cat": "AI", "img": "ae-status", "industry": "Industrial enterprises",
     "summary": "Machine learning models that forecast equipment issues from sensor data.",
     "background": "A processing plant (fictional scenario) maintained equipment on fixed schedules and still suffered surprise failures.",
     "challenge": "Combine vibration, temperature and maintenance history into early, trustworthy warnings.",
     "solution": "A data pipeline from plant sensors, anomaly-detection and remaining-useful-life models, and alerts that create work orders automatically.",
     "tech": ["Python", "TensorFlow", "Pandas", "Grafana", "Azure"],
     "approach": ["Asset criticality review", "Sensor data audit and cleaning", "Model development with engineers", "Alert tuning in production"],
     "outcomes": ["Earlier visibility of degrading equipment", "Maintenance planned around production", "Explainable alerts for engineers"],
     "learnings": "Pairing data scientists with maintenance engineers improved model usefulness."},
    {"slug": "demand-forecasting", "title": "Demand Forecasting Engine", "cat": "AI", "img": "ae-wave", "industry": "Retail & distribution",
     "summary": "Forecasting models that improve inventory and capacity planning.",
     "background": "A distributor (fictional scenario) planned stock with spreadsheets and intuition.",
     "challenge": "Forecast thousands of products with seasonality, promotions and supply delays.",
     "solution": "A forecasting pipeline with hierarchical models, scenario planning and a planner-friendly dashboard.",
     "tech": ["Python", "PyTorch", "NumPy", "PostgreSQL", "React"],
     "approach": ["Historical data consolidation", "Baseline and ML model comparison", "Planner workshops", "Automated weekly forecasts"],
     "outcomes": ["Consistent, data-driven forecasts", "Scenario planning for promotions", "Less manual spreadsheet work"],
     "learnings": "Showing planners why a forecast changed was key to adoption."},
    {"slug": "document-intelligence", "title": "Document Intelligence Automation", "cat": "Automation", "img": "ai-chip", "industry": "Enterprise operations",
     "summary": "AI document processing that removes manual re-keying from back-office workflows.",
     "background": "An operations team (fictional scenario) re-typed data from supplier documents into several systems.",
     "challenge": "Handle many document layouts while keeping accuracy high and humans in control.",
     "solution": "Document classification and extraction models, validation rules, a review queue and integrations with ERP systems.",
     "tech": ["Python", "Transformers", "FastAPI", "Node.js", "PostgreSQL"],
     "approach": ["Process mapping", "Document sampling and labelling", "Extraction model and rules", "Review queue and integrations"],
     "outcomes": ["Routine documents processed automatically", "Exceptions routed to reviewers", "Complete audit trail"],
     "learnings": "Confidence thresholds made it easy to balance automation and oversight."},
    {"slug": "clinical-assistance-robot", "title": "Clinical Logistics Robot Concept", "cat": "Robotics", "img": "robot-white", "industry": "Healthcare",
     "summary": "An assistive robot concept for transporting supplies within healthcare facilities.",
     "background": "A hospital (fictional scenario) found nurses spending time fetching supplies and samples.",
     "challenge": "Move safely through corridors and lifts while respecting privacy and infection control.",
     "solution": "A mobile service robot concept with secure compartments, autonomous navigation and a request app for staff.",
     "tech": ["ROS 2", "Python", "OpenCV", "React Native", "AWS"],
     "approach": ["Workflow observation with staff", "Route and lift integration study", "Prototype trials after hours", "Staff feedback iterations"],
     "outcomes": ["Staff request deliveries from an app", "Secure, tracked transport of supplies", "More clinician time for patients"],
     "learnings": "Designing for crowded corridors required conservative speed and clear signalling."},
]

TECH = [
    ("AI & Machine Learning", "brain", [("PyTorch", "pytorch"), ("TensorFlow", "tensorflow"), ("NumPy", "numpy"), ("Pandas", "pandas"), ("Jupyter", "jupyter")]),
    ("Robotics & Vision", "arm", [("ROS", "ros"), ("OpenCV", "opencv"), ("MATLAB", "matlab"), ("Arduino", "arduino"), ("Raspberry Pi", "raspberrypi")]),
    ("Languages", "code", [("Python", "python"), ("C++", "cplusplus"), ("Rust", "rust"), ("Go", "go"), ("TypeScript", "typescript")]),
    ("Platforms & DevOps", "cloud", [("Docker", "docker"), ("Kubernetes", "kubernetes"), ("Linux", "linux"), ("AWS", "amazonwebservices"), ("Azure", "azure"), ("Google Cloud", "googlecloud")]),
    ("Applications & Data", "layers", [("FastAPI", "fastapi"), ("React", "react"), ("Node.js", "nodejs"), ("PostgreSQL", "postgresql"), ("Grafana", "grafana")]),
]

INSIGHT_CATS = ["Artificial Intelligence", "Robotics Engineering", "Machine Learning", "Intelligent Automation", "Computer Vision", "Emerging Technologies"]

ARTICLES = [
    {"slug": "future-of-ai-in-industrial-automation", "title": "The Future of AI in Industrial Automation", "cat": "Intelligent Automation", "img": "ae-arm-weld", "date": "2026-11-12", "date_h": "12 Nov 2026", "read": 7,
     "summary": "AI is changing industrial automation from fixed, pre-programmed routines to adaptive systems that perceive, learn and improve.",
     "body": """<p class="lead-p">For decades, industrial automation meant machines repeating the same programmed motion. Artificial intelligence is shifting automation towards systems that can perceive their environment and adapt.</p>
<h2>From fixed automation to adaptive systems</h2>
<p>Traditional automation works well when parts, positions and processes never change. Modern production is different: smaller batches, more product variants and frequent changes. AI-enabled perception and decision-making allow automated systems to cope with this variation.</p>
<h2>Key technologies driving the shift</h2>
<ul><li><strong>Computer vision</strong> lets robots locate parts and inspect quality.</li><li><strong>Machine learning</strong> predicts equipment issues and optimises settings.</li><li><strong>Collaborative robotics</strong> allows people and robots to share workspaces safely.</li><li><strong>Edge computing</strong> runs AI close to machines for fast responses.</li></ul>
<blockquote>The goal is not lights-out factories, but systems where people and intelligent machines each do what they do best.</blockquote>
<h2>Challenges to plan for</h2>
<p>Data quality, integration with legacy equipment, cybersecurity and workforce skills are the most common obstacles. Projects succeed when they start with a clear operational problem and involve operators from the beginning.</p>
<h2>Getting started</h2>
<ol><li>Identify a repetitive or quality-critical process.</li><li>Assess the data and sensors already available.</li><li>Run a contained pilot with clear success measures.</li><li>Scale what works and build internal skills.</li></ol>"""},
    {"slug": "how-machine-learning-improves-business-decisions", "title": "How Machine Learning Improves Business Decisions", "cat": "Machine Learning", "img": "ae-wave", "date": "2026-10-28", "date_h": "28 Oct 2026", "read": 6,
     "summary": "Machine learning helps organisations move from hindsight to foresight by turning data into predictions that support better decisions.",
     "body": """<p class="lead-p">Most organisations collect more data than they can analyse. Machine learning turns that data into predictions and recommendations that support everyday decisions.</p>
<h2>What machine learning does well</h2>
<ul><li><strong>Forecasting</strong> demand, capacity or energy use.</li><li><strong>Classifying</strong> items, documents or events.</li><li><strong>Detecting anomalies</strong> in transactions or sensor data.</li><li><strong>Recommending</strong> next best actions.</li></ul>
<h2>Decisions, not just models</h2>
<p>A model only creates value when its output changes a decision. Successful projects define the decision first, then design the model, interface and workflow around it.</p>
<blockquote>Ask "what will we do differently with this prediction?" before asking "which algorithm should we use?"</blockquote>
<h2>Building trust</h2>
<p>Explainable outputs, honest accuracy reporting and human oversight help teams trust and adopt machine learning. Monitoring for data drift keeps models reliable as conditions change.</p>
<h2>A practical roadmap</h2>
<ol><li>Select a decision with measurable impact.</li><li>Check data availability and quality.</li><li>Build a simple baseline before complex models.</li><li>Deploy with monitoring and feedback loops.</li></ol>"""},
    {"slug": "understanding-computer-vision-technology", "title": "Understanding Computer Vision Technology", "cat": "Computer Vision", "img": "robot-face", "date": "2026-10-09", "date_h": "09 Oct 2026", "read": 6,
     "summary": "Computer vision enables machines to interpret images and video. Here is how it works and where it creates value.",
     "body": """<p class="lead-p">Computer vision gives machines the ability to interpret images and video: detecting objects, reading text, measuring dimensions and spotting defects.</p>
<h2>How it works</h2>
<p>Modern computer vision relies on deep neural networks trained on labelled examples. The network learns visual patterns, such as edges, textures and shapes, that distinguish one object or condition from another.</p>
<h2>Common tasks</h2>
<ul><li><strong>Classification:</strong> what is in this image?</li><li><strong>Detection:</strong> where are the objects?</li><li><strong>Segmentation:</strong> which pixels belong to which object?</li><li><strong>OCR:</strong> what text appears in the image?</li></ul>
<blockquote>In vision projects, good lighting and good data often matter more than the newest model.</blockquote>
<h2>Edge or cloud?</h2>
<p>Edge deployment processes images on devices near the camera for low latency and privacy. Cloud deployment suits heavier analysis and centralised management. Many systems combine both.</p>
<h2>Applications</h2>
<p>Quality inspection, robot guidance, inventory counting, safety monitoring and document processing are among the most mature uses today.</p>"""},
    {"slug": "role-of-robotics-in-modern-manufacturing", "title": "The Role of Robotics in Modern Manufacturing", "cat": "Robotics Engineering", "img": "factory-robots", "date": "2026-09-22", "date_h": "22 Sep 2026", "read": 7,
     "summary": "Robots are becoming more flexible, collaborative and intelligent, changing how manufacturers approach productivity and quality.",
     "body": """<p class="lead-p">Robots have long been part of high-volume manufacturing. Today, smaller, smarter and collaborative robots are making automation accessible to a much wider range of manufacturers.</p>
<h2>Types of industrial robots</h2>
<ul><li><strong>Articulated arms</strong> for welding, painting and assembly.</li><li><strong>Collaborative robots</strong> that work safely near people.</li><li><strong>Autonomous mobile robots</strong> for moving materials.</li><li><strong>Gantry and SCARA robots</strong> for fast pick-and-place.</li></ul>
<h2>Where robots add value</h2>
<p>Robots excel at repetitive, precise or physically demanding tasks. They improve consistency and free people for problem-solving, quality and supervision.</p>
<blockquote>The most successful robot deployments are designed around people, not in spite of them.</blockquote>
<h2>Safety and standards</h2>
<p>Risk assessments, safety-rated controls and compliance with applicable standards are essential parts of every robotics project.</p>
<h2>Planning a robotics project</h2>
<ol><li>Choose a well-defined, repeatable task.</li><li>Simulate the cell before buying hardware.</li><li>Plan integration with existing systems.</li><li>Train staff and plan for maintenance.</li></ol>"""},
    {"slug": "autonomous-systems-and-their-applications", "title": "Autonomous Systems and Their Applications", "cat": "Emerging Technologies", "img": "drone", "date": "2026-09-03", "date_h": "03 Sep 2026", "read": 6,
     "summary": "From warehouse robots to inspection drones, autonomous systems are moving from research labs into real operations.",
     "body": """<p class="lead-p">Autonomous systems sense their environment, make decisions and act without continuous human control. They are increasingly found in warehouses, farms, ports and industrial sites.</p>
<h2>Core building blocks</h2>
<ul><li><strong>Perception:</strong> cameras, LiDAR and sensors interpret surroundings.</li><li><strong>Localisation:</strong> the system knows where it is.</li><li><strong>Planning:</strong> it decides how to reach its goal safely.</li><li><strong>Control:</strong> it executes movements precisely.</li></ul>
<h2>Applications today</h2>
<p>Autonomous mobile robots move goods in warehouses, drones inspect infrastructure, and autonomous machines support agriculture and mining. Most operate in structured or semi-structured environments.</p>
<blockquote>Autonomy is a spectrum: many valuable systems combine automated operation with human supervision.</blockquote>
<h2>Testing and safety</h2>
<p>Simulation, staged trials and clear operating boundaries are essential before autonomous systems work around people.</p>
<h2>What comes next</h2>
<p>Advances in AI foundation models, sensor costs and edge computing are expanding where autonomy is practical.</p>"""},
]

CAREER_AREAS = [
    ("AI Engineering", "brain", "Machine Learning Engineering", "Build, train and deploy models that solve real operational problems."),
    ("AI Engineering", "eye", "Computer Vision Engineering", "Develop perception systems for inspection and robot guidance."),
    ("Robotics", "arm", "Robotics Engineering", "Design, program and integrate robotic arms and mobile robots."),
    ("Robotics", "chip", "Embedded & Controls Engineering", "Work on sensors, controllers and real-time robot software."),
    ("Software Development", "code", "Software & Platform Engineering", "Create the platforms, APIs and interfaces that connect intelligent systems."),
    ("Research", "flask", "Applied Research", "Explore emerging methods and turn them into prototypes."),
]

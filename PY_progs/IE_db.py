import pandas as pd

# Data compiled from the previous message (selected structured rows)
data = [
    ["Skye Air Mobility", "Drone logistics startup enabling rapid deliveries of medical supplies across India.", "info@skyeair.tech"],
    ["TSAW Drones", "Drone logistics company focused on healthcare deliveries, connecting distribution centers to rural health centers.", "business@tsaw.tech"],
    ["TechEagle", "Autonomous drone solutions provider for medical logistics, enabling liquid biopsy and medicine transport.", "info@techeagle.in"],
    ["Redwing Labs", "Autonomous delivery drones and flight management software, specializing in healthcare deliveries.", "founders@redwinglabs.in"],
    ["Garuda Aerospace", "Drone manufacturer/operator with delivery drones for medicines and vaccines.", "business@garudaaerospace.com"],
    ["Amber Wings", "Cargo drone startup building hybrid VTOL drones for last-mile medical and e-commerce logistics.", "fly@amberwings.co"],
    ["Aero360", "Full-stack drone manufacturer serving enterprise and defense, producing surveillance and cargo UAVs.", "marketing@aero360.co.in"],
    ["EndureAir", "Deep-tech UAV startup building high-endurance drones for logistics and healthcare delivery.", "rama@endureair.tech"],
    ["Tsalla Aerospace", "IISc Bangalore aerospace venture developing UAVs for industrial and medical delivery.", "info@tsallaaerospace.com"],
    ["Haveli UAVs", "Custom drone manufacturer focusing on agriculture, defense, surveillance, and logistics applications.", "info@haveliuavs.com"],
    ["UrbanMatrix", "Aerial robotics startup providing autonomous drones and cloud management for logistics.", "contact@urbanmatrix.co.in"],
    ["Indrones", "Drone integrator providing UAV mapping and logistics solutions.", "info@indrones.com"],
    ["DTown Robotics", "Drone and robotics R&D company building UAVs for agriculture, surveillance, and material transport.", "contact@dtownrobotics.com"],
    ["Skylark Drones", "Drone-based logistics and mapping solutions provider with AI-powered data platforms.", "info@skylarkdrones.com"],
    ["Aereo (Aarav Unmanned Systems)", "Developer of long-range, high-endurance drones for commercial and defense use, including pharma logistics.", "vipul@aus.co.in"],
    ["DroneAcharya", "Drone solutions provider offering UAV fleet management and logistics testing.", "info@droneacharya.com"],
    ["IG Drones", "UAV company focusing on defense drones and training simulators.", "sales@igdrones.com"],
    ["ideaForge", "Veteran drone manufacturer exploring logistics use cases alongside defense UAVs.", "business@ideaforgetech.com"],
    ["Paras Aerospace", "Drone manufacturer specializing in agricultural and logistics UAVs.", "info@parasaerospace.com"],
    ["Hubblefly Technologies", "DGCA-authorized UAV manufacturer producing agricultural spray drones and VTOL platforms.", "sales@hubblefly.com"],
    ["Drona Aviation", "Developer of mini-programmable drones for education and medical delivery pilots.", "support@dronaaviation.com"],
    ["Endeavour Control", "Manufacturer of rotary-wing and hybrid UAVs for surveying and industrial inspection.", "support@endeavourcontrol.com"],
    ["Endeavour Airworks", "Drone logistics and fleet management service provider.", "admin@endeavourairworks.in"],
    ["Vyomik Drones", "UAV solutions provider for corporate logistics.", "info@vyomikdrones.com"],
    ["DronaMaps", "Drone-based surveying and mapping platform provider.", "info@dronamaps.com"],
    ["Marut Drones", "Developer of agricultural multi-utility drones with DGCA certification.", "salesteam@marutdrones.com"],
    ["Skyeagle", "Drone R&D firm for defense and logistics.", "info@skyeagle.in"],
    ["Edall Systems", "Drone integrator and retailer for hobbyist and professional UAVs.", "contact@edallsystems.com"],
    ["Ayecka", "Drone testbed and training startup incubated at IISc.", "contact@ayecka.io"],
    ["DronaSpect", "UAV service provider for industry inspection and logistics.", "sales@dronaspect.com"],
    ["C-DAC – CDOT Drone", "Government R&D body spin-offs building UAV communication/drone networks.", "contact@cdac.in"],
    ["Advik Multicopter", "Manufacturer of multi-rotor UAVs for surveillance.", "sales@advikmulticopter.com"],
    ["BotsEye", "Drone-based inspection services for infrastructure projects.", "info@botseye.in"],
    ["BeyondSky", "Drone operator offering video and survey solutions.", "support@beyondsksy.com"],
    ["Empyrean Robotics", "Developer of structural health monitoring robots and UAV components.", "info@empyrotech.com"],
    ["Samhams Technologies", "Drone IT solutions provider for enterprise UAV software and services.", "info@samhamstechnologies.com"],
    ["Alpha Entropies", "Drone testbeds and trials company for agriculture and infrastructure.", "contact@alphaentropies.com"],
    ["Synergy Aerospace", "UAV consultancy and manufacturing company.", "info@synergyaerospace.in"],
    ["HST (Hoscom)", "Drone R&D firm focusing on robotics and UAV development.", "support@hoscom.co.in"],
    ["EagleView India", "Drone imagery and analytics services provider.", "india@eagleview.com"],
    ["SICA", "Provider of drone ID tagging services for regulatory compliance.", "info@sicaaero.com"],
    ["Spur Drones", "UAV software platform developer.", "sales@spurdrones.com"],
    ["UVC", "Drone service startup focused on UAV deliveries.", "info@uvc.in"],
    ["EMBRAIR", "Drone startup focusing on UAV delivery R&D.", "contact@embrare.com"],
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["Startup Name", "Description", "Email"])

# Save to Excel
excel_path = "/mnt/data/indian_medical_drone_startups.xlsx"
df.to_excel(excel_path, index=False)

excel_path

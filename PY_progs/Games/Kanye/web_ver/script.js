// --- Module Aliases ---
// These are shortcuts to make the code easier to read
let Engine = Matter.Engine,
    Render = Matter.Render,
    Runner = Matter.Runner,
    Bodies = Matter.Bodies,
    Composite = Matter.Composite;

// --- 1. Create the Engine & World ---
// The 'engine' runs the physics simulation
let engine = Engine.create();
// The 'world' is the container for all your objects
let world = engine.world;

// --- 2. Create the Renderer ---
// The 'render' is what draws the physics world onto the HTML page
let render = Render.create({
    element: document.body, // Draw into the <body>
    engine: engine,
    options: {
        width: window.innerWidth,
        height: window.innerHeight,
        wireframes: false, // Set to 'false' to see the textures
        background: '#f0f0f0' // A light gray background
    }
});

// --- 3. Create Static Bodies (Ground & Walls) ---
// 'isStatic: true' means the object will not move
let ground = Bodies.rectangle(window.innerWidth / 2, window.innerHeight, window.innerWidth, 60, { isStatic: true });
let leftWall = Bodies.rectangle(0, window.innerHeight / 2, 60, window.innerHeight, { isStatic: true });
let rightWall = Bodies.rectangle(window.innerWidth, window.innerHeight / 2, 60, window.innerHeight, { isStatic: true });

// Add these static bodies to the world
Composite.add(world, [ground, leftWall, rightWall]);

// --- 4. Add Mouse Click (or press) Event ---
// We use 'mousedown' so you can click and hold to spawn many
document.addEventListener('mousedown', function(event) {
    // This is the function that runs on every click
    spawnFace(event.clientX, event.clientY);
});

// --- 5. The Spawning Function ---
function spawnFace(x, y) {
    // Create a new circle (the 'face')
    let face = Bodies.circle(
        x, // X-position from the mouse
        y, // Y-position from the mouse
        40, // Radius of the circle (play with this value)
        {
            // --- Physics Properties ---
            friction: 0.1,       // How much it grips other surfaces
            restitution: 0.6,    // Bounciness (0 = no bounce, 1 = perfect bounce)
            
            // --- Render Properties (The Fun Part) ---
            render: {
                sprite: {
                    // This is where you put your image!
                    // Find any image URL online to test.
                    texture: 'https://i.imgur.com/CgbQB1j.png', // A simple smiley face
                    xScale: 0.5, // Scale the image to fit the circle
                    yScale: 0.5
                }
            }
        }
    );

    // Add the newly created 'face' to the physics world
    Composite.add(world, face);
}

// --- 6. Run the Engine & Renderer ---
// 'Runner' keeps the simulation updated (i.e., makes it run)
let runner = Runner.create();
Runner.run(runner, engine);

// 'Render.run' starts the drawing loop
Render.run(render);
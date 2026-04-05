import * as THREE from 'three';
import * as dat from 'dat.gui';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { OutlinePass } from 'three/addons/postprocessing/OutlinePass.js';

console.log("Create the scene");
const scene = new THREE.Scene();

console.log("Create a perspective projection camera");
var camera = new THREE.PerspectiveCamera( 45, window.innerWidth/window.innerHeight, 0.1, 1000 );
camera.position.set(-175, 115, 5);

console.log("Create the renderer");
const renderer = new THREE.WebGL1Renderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
renderer.toneMapping = THREE.ACESFilmicToneMapping;

console.log("Create an orbit control");
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.75;
controls.screenSpacePanning = false;

scene.background = new THREE.Color(0x000000);

// ******  Сонце  ******
const sunSize = 697/40; 
const sunGeom = new THREE.SphereGeometry(sunSize, 32, 20);
const sunMat = new THREE.MeshStandardMaterial({
    color: 0xffcc00,
    emissive: 0xFFF88F,
    emissiveIntensity: 2
});
const sun = new THREE.Mesh(sunGeom, sunMat);
scene.add(sun);
const sunLight = new THREE.PointLight(0xffffff, 2, 500); 
sunLight.position.set(0, 0, 0);
scene.add(sunLight); // сонце світиться
const ambientLight = new THREE.AmbientLight(0x404040, 1.5); 
scene.add(ambientLight); // загальне світло

// ****** Функція для планет ******
function createPlanet(planetName, size, position, tilt, color) {
    const material = new THREE.MeshPhongMaterial({
    color: color,
    });
    const name = planetName;
    const geometry = new THREE.SphereGeometry(size, 32, 20);
    const planet = new THREE.Mesh(geometry, material);
    const planetSystem = new THREE.Group();
    let Ring;
    const orbitGroup = new THREE.Object3D();
    planetSystem.add(planet);
    planet.position.x = position;
    planet.rotation.z = tilt * Math.PI / 180;
    // orbit
     const orbitPath = new THREE.EllipseCurve(
    0, 0,           
    position, position, 
    0, 2 * Math.PI,   
    false,            
    0                 
);
const pathPoints = orbitPath.getPoints(100);
const orbitGeometry = new THREE.BufferGeometry().setFromPoints(pathPoints);
const orbitMaterial = new THREE.LineBasicMaterial({ color: 0xFFFFFF, transparent: true, opacity: 0.03 });
const orbit = new THREE.LineLoop(orbitGeometry, orbitMaterial);
orbit.rotation.x = Math.PI / 2;
planetSystem.add(orbit);

if(ring)
  {
    const RingGeo = new THREE.RingGeometry(ring.innerRadius, ring.outerRadius,30);
    const RingMat = new THREE.MeshStandardMaterial({
      side: THREE.DoubleSide
    });
    Ring = new THREE.Mesh(RingGeo, RingMat);
    planetSystem.add(Ring);
    Ring.position.x = position;
    Ring.rotation.x = -0.5 *Math.PI;
    Ring.rotation.y = -tilt * Math.PI / 180;
  }

// ****** Створення планет ******
const planetObjects = [];
const mercury = createPlanet('Mercury', 2.4, 40, 0, 0xaaaaaa);
const venus = createPlanet('Venus', 6.1, 65, 177, 0xe3bb76);
const earth = createPlanet('Earth', 6.4, 90, 23.5, 0x2233ff);
const mars = createPlanet('Mars', 3.4, 115, 25, 0xff3300);
const jupiter = createPlanet('Jupiter', 69/4, 200, 3, 0xd39c7e);
const saturn = createPlanet('Saturn', 58/4, 270, 26, 0xf4d4ad, {
    innerRadius: 18, 
    outerRadius: 29
});
const uranus = createPlanet('Uranus', 25/4, 320, 97, 0x66ffff, {
    innerRadius: 10, 
    outerRadius: 12
});
const neptune = createPlanet('Neptune', 24/4, 350, 28, 0x3366ff);
const pluto = createPlanet('Pluto', 1.2, 380, 122, 0x96847a);
const planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto];
const distances = [40, 65, 90, 115, 200, 270, 320, 350, 380];
};

// Інформація про планети, що з'являється, при їх натисканні
const planetsData = {
    'Mercury': {
        radius: '2,439.7 km',
        tilt: '0.034°',
        rotation: '58.6 Earth days',
        orbit: '88 Earth days',
        distance: '57.9 million km',
        moons: '0',
        info: 'The smallest planet in our solar system and nearest to the Sun.'
    },
    'Venus': {
        radius: '6,051.8 km',
        tilt: '177.4°',
        rotation: '243 Earth days',
        orbit: '225 Earth days',
        distance: '108.2 million km',
        moons: '0',
        info: 'Second planet from the Sun, known for its extreme temperatures and thick atmosphere.'
    },
    'Earth': {
        radius: '6,371 km',
        tilt: '23.5°',
        rotation: '24 hours',
        orbit: '365 days',
        distance: '150 million km',
        moons: '1 (Moon)',
        info: 'Third planet from the Sun and the only known planet to harbor life.'
    },
    'Mars': {
        radius: '3,389.5 km',
        tilt: '25.19°',
        rotation: '1.03 Earth days',
        orbit: '687 Earth days',
        distance: '227.9 million km',
        moons: '2 (Phobos and Deimos)',
        info: 'Known as the Red Planet, famous for its reddish appearance and potential for human colonization.'
    },
    'Jupiter': {
        radius: '69,911 km',
        tilt: '3.13°',
        rotation: '9.9 hours',
        orbit: '12 Earth years',
        distance: '778.5 million km',
        moons: '95 known moons (Ganymede, Callisto, Europa, Io are the 4 largest)',
        info: 'The largest planet in our solar system, known for its Great Red Spot.'
    },
    'Saturn': {
        radius: '58,232 km',
        tilt: '26.73°',
        rotation: '10.7 hours',
        orbit: '29.5 Earth years',
        distance: '1.4 billion km',
        moons: '146 known moons',
        info: 'Distinguished by its extensive ring system, the second-largest planet in our solar system.'
    },
    'Uranus': {
        radius: '25,362 km',
        tilt: '97.77°',
        rotation: '17.2 hours',
        orbit: '84 Earth years',
        distance: '2.9 billion km',
        moons: '27 known moons',
        info: 'Known for its unique sideways rotation and pale blue color.'
    },
    'Neptune': {
        radius: '24,622 km',
        tilt: '28.32°',
        rotation: '16.1 hours',
        orbit: '165 Earth years',
        distance: '4.5 billion km',
        moons: '14 known moons',
        info: 'The most distant planet from the Sun in our solar system, known for its deep blue color.'
    },
    'Pluto': {
        radius: '1,188.3 km',
        tilt: '122.53°',
        rotation: '6.4 Earth days',
        orbit: '248 Earth years',
        distance: '5.9 billion km',
        moons: '5 (Charon, Styx, Nix, Kerberos, Hydra)',
        info: 'Originally classified as the ninth planet, Pluto is now considered a dwarf planet.'
    }
};
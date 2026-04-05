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
    const orbitGroup = new THREE.Object3D();
    planetSystem.add(planet);
    planet.position.x = position;
    planet.rotation.z = tilt * Math.PI / 180;
}

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

/**
// Масив планет
const planetObjects = [];
// сцена/місце, де буде анімація
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight, 
    0.1,
    1000
);
camera.position.set(0, 20, 100);

const renderer = new THREE.WebGLRenderer({
  antialias: true
});
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
// renderer.render(scene, camera);

const controls = new OrbitControls(camera, renderer.domElement);

// Сонце
const sunGeometry = new THREE.SphereGeometry(10, 32, 32);
const sunMaterial = new THREE.MeshBasicMaterial({ color: 0xffff00 });
const sun = new THREE.Mesh(sunGeometry, sunMaterial);
scene.add(sun);

const sunLight = new THREE.PointLight(0xffffff, 2, 500); 
sunLight.position.set(0, 0, 0);
scene.add(sunLight); // сонце світиться
const ambientLight = new THREE.AmbientLight(0xffffff, 0.2); 
scene.add(ambientLight); // загальне світло

// Анімація планет
function initPlanets() {
    Object.keys(planetsData).forEach((name) => {
        const data = planetsData[name];
        // Орбіти
        const orbitGeometry = new THREE.RingGeometry(data.distance, data.distance + 0.1, 64);
        const orbitMaterial = new THREE.MeshBasicMaterial({ 
            color: 0xffffff, 
            side: THREE.DoubleSide,
            transparent: true,
            opacity: 0.5
        });
        const orbit = new THREE.Mesh(orbitGeometry, orbitMaterial);
        orbit.rotation.x = Math.PI / 2; 
        scene.add(orbit);
        // Планети
        const geometry = new THREE.SphereGeometry(data.size, 32, 32);
        const material = new THREE.MeshStandardMaterial({ color: data.color });
        const planetMesh = new THREE.Mesh(geometry, material);
        // Позиція Планет
        planetMesh.position.x = data.distance;
        planetMesh.name = name;
        scene.add(planetMesh); // Сцена
        // Швидкість обертання
        planetObjects.push({
            mesh: planetMesh,
            distance: data.distance,
            angle: Math.random() * Math.PI * 2,
            speed: 0.5 / Math.pow(data.distance, 1.5), // обертання навколо сонця
            rotationSpeed: 0.01 // Навколо власної осі 
        });
    });
}
initPlanets();

// Анімація
function animate() {
    requestAnimationFrame(animate);
    sun.rotation.y += 0.005;
    planetObjects.forEach((obj) => {
        obj.angle += obj.speed;
        obj.mesh.position.x = Math.cos(obj.angle) * obj.distance;
        obj.mesh.position.z = Math.sin(obj.angle) * obj.distance;
        obj.mesh.rotation.y += obj.rotationSpeed;
    });
    controls.update();
    renderer.render(scene, camera);
}
animate(); */
